"""
Reads the openapi schema exposed by a running Xautomata instance and (re)generates every
file under hive/cookbook/, plus the `hive.infrastrucure_keys.Keys.*` field-length hints and
the import/base-class list in hive/api.py.

This script does not know anything about REST semantics beyond what the schema tells it -
whether an endpoint is "bulk", paginable, a "query" style POST, etc. is inferred from
substrings of the URL/operation name, because the FastAPI backend does not expose a
dedicated flag for any of that. That inference lives in `api_interpreter`/`name_gen` and is
inherently a best-effort heuristic: the `hidden_*` lists right below are the escape hatch for
the handful of endpoints that don't follow the naming convention. If a newly added endpoint
comes out of the generator with the wrong shape (not paginable when it should be, wrongly
tagged as bulk, wrong method name), the fix is almost always adding it to one of those lists,
not changing the heuristic itself.
"""
import argparse
import logging
import re
from typing import Optional

from _API_writers_V3 import generate_python_code, underscore_to_camelcase, lib_import_set
from hive.infrastrucure_keys import Keys
from utilities.dictionary import DeepDict
import requests
import json

logger = logging.getLogger('hive')

FORCE_STATUS = [429, 500, 502, 503, 504]
METHODS = ["HEAD", "GET", "OPTIONS", "POST"]

# endpoints whose POST body carries the varchar-length constraints mirrored in infrastrucure_keys.py
ENTITY_ENDPOINTS = {
    'customer_keys': '/customers/',
    'virtual_domain_keys': '/virtual_domains/',
    'site_keys': '/sites/',
    'group_keys': '/groups/',
    'object_keys': '/objects/',
    'metric_type_keys': '/metric_types/',
    'metric_keys': '/metrics/',
    'service_keys': '/services/',
}

# endpoints whose path looks like a normal single-item GET/POST but are actually a bulk
# "query" style call (function name gets a "_bulk" suffix, pagination enabled)
HIDDEN_QUERY = ['services_last_status_query', 'last_status']
HIDDEN_QUERY_EXACT_NAME = []
# endpoints whose path doesn't contain "bulk" but behave like a bulk write (no single-item pagination)
HIDDEN_BULK_POST = ['metric_ingest', 'probes_log_ingest', 'ts_cost_management']
HIDDEN_BULK_POST_EXACT_NAME = ['/webhooks/{webhook_type}']


def _resolve_schema_ref(schema_node: dict) -> Optional[str]:
    """$ref -> schema name, or items.$ref -> schema name. None if neither is present."""
    if '$ref' in schema_node:
        return schema_node['$ref'].split('/')[-1]
    if 'items' in schema_node and '$ref' in schema_node['items']:
        return schema_node['items']['$ref'].split('/')[-1]
    return None


def extract_max_lengths_from_post(apis: dict, schemas: dict, endpoint: str) -> dict:
    """maxLength per field declared on the POST body schema of `endpoint`, {} if not applicable."""
    if endpoint not in apis or 'post' not in apis[endpoint]:
        return {}
    mode_data = apis[endpoint]['post']
    if 'requestBody' not in mode_data:
        return {}
    content = mode_data['requestBody']['content']

    schema_body = None
    for app_type in ['application/json', 'application/x-www-form-urlencoded']:
        if app_type in content:
            schema_body = content[app_type]['schema']
            break
    if schema_body is None:
        return {}

    schema_ref = _resolve_schema_ref(schema_body)
    if schema_ref is None or schema_ref not in schemas or 'properties' not in schemas[schema_ref]:
        return {}

    lengths = {}
    for key, value in schemas[schema_ref]['properties'].items():
        if 'maxLength' in value:
            lengths[key] = value['maxLength']
        elif 'anyOf' in value:
            # nullable field: maxLength can be nested inside one of the anyOf branches
            for t in value['anyOf']:
                if isinstance(t, dict) and 'maxLength' in t:
                    lengths[key] = t['maxLength']
                    break
    return lengths


def _patch_entity_lengths(source: str, entity_name: str, fields: dict) -> str:
    """
    Update the `"len": N` hints for `entity_name` inside infrastrucure_keys.py's source text.

    The substitution is scoped to this entity's own `entity_name = { ... }` block (found via
    brace counting) before the per-field regex runs, otherwise a field name shared by two
    entities with the same current length (e.g. "status": {"len": 1} appears in several
    entities) would get patched everywhere the text matches, not just in the intended block.
    """
    block_start = source.find(f'{entity_name} = {{')
    if block_start == -1:
        return source

    depth = 0
    block_end = None
    for i in range(block_start, len(source)):
        if source[i] == '{':
            depth += 1
        elif source[i] == '}':
            depth -= 1
            if depth == 0:
                block_end = i + 1
                break
    if block_end is None:
        return source

    block = source[block_start:block_end]
    modified_block = block

    current_entity = getattr(Keys, entity_name, None)
    if current_entity is None:
        return source

    for section in ('mandatory', 'optional'):
        section_dict = current_entity.get(section, {})
        for field, new_len in fields.items():
            if field not in section_dict:
                continue
            field_def = section_dict[field]
            current_len = field_def.get('len')
            if current_len == new_len:
                continue

            logger.info(f'Updating {entity_name}.{field}: len {current_len} -> {new_len}')

            pattern = (
                rf'("{re.escape(field)}"'
                rf'\s*:\s*\{{[^}}]*'
                rf'"len"\s*:\s*)'
                rf'{re.escape(str(current_len))}'
            )
            replacement = rf'\g<1>{new_len}'
            modified_block, count = re.subn(pattern, replacement, modified_block)
            if count == 0:
                logger.warning(f'pattern not found in source for {entity_name}.{field}')

    return source[:block_start] + modified_block + source[block_end:]


def update_infrastructure_keys(apis: dict, schemas: dict) -> None:
    """Keep hive/infrastrucure_keys.py's "len" hints in sync with the API's maxLength constraints."""
    entity_lengths = {}
    for key_name, endpoint in ENTITY_ENDPOINTS.items():
        lengths = extract_max_lengths_from_post(apis, schemas, endpoint)
        if lengths:
            entity_lengths[key_name] = lengths

    filepath = './hive/infrastrucure_keys.py'
    try:
        with open(filepath, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filepath} not found")

    modified = source
    for entity_name, fields in entity_lengths.items():
        modified = _patch_entity_lengths(modified, entity_name, fields)

    if modified != source:
        with open(filepath, 'w') as f:
            f.write(modified)
        logger.info('infrastrucure_keys.py updated successfully')
    else:
        logger.info('No changes needed in infrastrucure_keys.py')


single_page_doc = "            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False."
page_size_doc = "            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000."
page_size_doc_bulk = "            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 50."
kwargs_doc = "            kwargs (dict, optional): additional parameters for execute. Default to None."
warm_start_doc = "            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False."
params_doc = "            **params: additional parameters for the API."
params_doc2 = "            params (dict, optional): additional parameters for the API."
payload_doc = "            **payload: additional parameters for the API."
payload_doc_bulk = "            payload (list[dict], optional): List dict to create."
payload_doc_query = "            payload (dict, optional): additional parameters for the API."
headers_doc = "            headers (dict, optional): additional HTTP headers required by the API (see Keyword Args). Default to None."
headers_doc_kwarg = "            **headers: additional HTTP headers required by the API."

dict_doc = {
            "skip": "numero di oggetti che si vogliono saltare nella risposta. Default to 0.",
            "limit": "numero di oggetti massimi che si vogliono ottenere. Default to 1_000_000.",
            "count": "Se True nel header della risposta e' presente la dimensione massima a db della chiamata fatta, sconsigliabile perche raddoppia il tempo per chiamata. Default to False.",
            "like": "Se True, eventuali filtri richiesti dalla API vengono presi come porzioni di testo, se False il matching sul campo dei filtri deve essere esatto. Default to True.",
            "sort_by": 'Stringa separata da virgole di campi su cui ordinare. Si indica uno o piu campi della risposta e si puo chiedere di ottenere i valori di quei campi in ordine ascendente o discendente. Esempio "Customer:Desc". Default to "".',
            "null_fileds": 'Stringa separata da virgole di campi di cui si vuole rimuovere, o imporre, un valore nullo nel result set. Esempio "campo:nullable". Default to "".',
            "join": "Se join = true, ogni riga restituita conterra' chiavi aggiuntive che fanno riferimento ad altre entita', con cui la riga ha relazioni 1:1. Default to False",
            "extract_severity": "Se True nella risposta e' anche presente la severita, Default to False."
}


def find_ref(schemas: dict, schema_ref: str, key: str, key_type: list, name: str) -> Optional[list]:
    """Resolve the python-ish type(s) of `schemas[schema_ref]['properties'][key]` for the docstring."""
    created = False
    if 'anyOf' in schemas[schema_ref]['properties'][key]:
        for types in schemas[schema_ref]['properties'][key]['anyOf']:
            if 'type' in types:
                key_type.append(types['type'])
                created = True
    elif 'type' in schemas[schema_ref]['properties'][key]:
        key_type.append(schemas[schema_ref]['properties'][key]['type'])
        created = True
    else:
        logger.warning(f'wrong requestBody type {name}')
        key_type = None
        created = True

    if not created:
        key_type = None

    return key_type


def openapi(root: str) -> dict:
    response = requests.get(f'{root}/openapi.js')
    data = json.loads(response.content[15:].decode('utf-8'))
    return data


def _resolve_param_type(param: dict, schemas: dict) -> str:
    """Type string for a `parameters[]` entry (query/path param), following $ref/anyOf."""
    schema = param['schema']
    if 'type' in schema:
        return schema['type']

    if 'anyOf' in schema:
        schema_ref, param_type = '', ''
        for ii in schema['anyOf']:
            if '$ref' in ii:
                schema_ref = ii['$ref'].split('/')[-1]
                param_type = schemas[schema_ref]['type']
            if 'type' in ii and ii['type'] is not None and ii['type'] != 'null':
                schema_ref = 'ok'
                param_type = ii['type']
        if schema_ref == '' or param_type == '':
            raise NotImplementedError
        return param_type

    if '$ref' in schema:
        schema_ref = schema['$ref'].split('/')[-1]
        return schemas[schema_ref]['type']

    raise NotImplementedError


def _resolve_request_body_schema_refs(request_body: dict, application: str, name: str):
    """
    Schema name(s) backing a requestBody, or a sentinel:
      - 'empty'   -> body is an inline anyOf with no $ref (nothing to document)
      - 'missing' -> body is a bare list with no discoverable schema (falls back to uuid)
      - None      -> genuinely couldn't figure it out (logged, payload becomes None)
    Always returned as a list (len > 1 only for the items->anyOf-of-$ref case).
    """
    schema = request_body['content'][application]['schema']

    if '$ref' in schema:
        schema_ref = schema['$ref'].split('/')[-1]
    elif 'items' in schema and '$ref' in schema['items']:
        schema_ref = schema['items']['$ref'].split('/')[-1]
    elif 'items' in schema and 'anyOf' in schema['items']:
        schema_ref = [s['$ref'].split('/')[-1] for s in schema['items']['anyOf'] if '$ref' in s]
    elif 'anyOf' in schema:
        schema_ref = 'empty'
    elif 'items' in schema and 'required' in request_body:
        schema_ref = 'missing'
    else:
        logger.warning(f'missing the schema_ref for {name}')
        schema_ref = None

    return [schema_ref] if not isinstance(schema_ref, list) else schema_ref


def _extract_params(operation: dict, schemas: dict):
    """
    Split `operation['parameters']` into query/path params and header params (`in: header`).

    Path params stay mixed into `params` here on purpose: api_interpreter/name_gen already
    pop them out by name once they've been turned into an explicit `{name}: str` argument, and
    duplicating that logic here would be redundant. Header params get their own dict because
    they must reach `self.execute(..., headers=...)`, not `params=...` - the API reads them
    off the HTTP header, not the query string.
    """
    params = dict()
    headers = dict()
    if 'parameters' in operation:
        for param in operation['parameters']:
            param_type = _resolve_param_type(param, schemas)
            entry = {'type': param_type, 'required': param['required']}
            if param.get('in') == 'header':
                headers[param['name']] = entry
            else:
                params[param['name']] = entry
    return params, headers


def _extract_payload(operation: dict, schemas: dict, name: str) -> Optional[dict]:
    if 'requestBody' not in operation:
        return None

    request_body = operation['requestBody']
    content = request_body['content']
    if 'application/json' in content:
        application = 'application/json'
    elif 'application/x-www-form-urlencoded' in content:
        application = 'application/x-www-form-urlencoded'
    elif 'multipart/form-data' in content:
        application = 'multipart/form-data'
    else:
        raise ValueError('new application insert here')  # a not-yet-seen content type needs to be added above

    schema_refs = _resolve_request_body_schema_refs(request_body, application, name)

    payload = dict()
    for ii, schema in enumerate(schema_refs):
        if schema is not None and schema not in ('missing', 'empty'):
            for key in schemas[schema]['properties']:
                key_type = find_ref(schemas, schema, key, [], name)
                if isinstance(key_type, list) and 'null' in key_type:
                    key_type = [x for x in key_type if x != 'null']

                key_required = 'required' in schemas[schema] and key in schemas[schema]['required']
                key_name = f'{key}_{ii}' if len(schema_refs) > 1 else key
                payload[key_name] = {'type': key_type, 'required': key_required}

        elif schema == 'empty':
            payload = {}

        elif schema == 'missing':
            payload['uuid'] = {'type': 'str', 'required': True}

        else:
            payload = None

    return payload


def main(**kwargs) -> None:

    data = openapi(kwargs['url'])
    apis = data['paths']
    schemas = data['components']['schemas']
    update_infrastructure_keys(apis, schemas)

    # populate to restrict generation to a subset of endpoints while iterating on the generator
    allowed = {}

    api_dict = DeepDict()

    for name in apis:
        if name == '/openapi.js':
            continue
        for mode in apis[name]:
            if len(allowed) > 0 and not (name in allowed and mode.upper() in allowed[name]):
                continue

            operation = apis[name][mode]
            description = operation['summary']
            params, headers = _extract_params(operation, schemas)
            payload = _extract_payload(operation, schemas, name)

            api_dict = api_interpreter(mode.upper(), name, description, params, payload, api_dict, headers=headers)

    link_imports = []
    class_list = []

    for file_name in api_dict:
        imports = api_dict[file_name]['imports']
        from_imports = api_dict[file_name]['from_imports']
        file_name = api_dict[file_name]['file_name']

        class_name = api_dict[file_name]['class_name']
        class_parent = api_dict[file_name]['class_parent']
        docstring_class = api_dict[file_name]['docstring_class']

        function_names = []
        funcion_bodys = []
        function_docstrings = []
        function_returns = []
        function_args = []
        function_kwargs = []

        for function_name in api_dict[file_name]['function_names']:
            function_names.append(api_dict[file_name]['function_names'][function_name]['function_name'])
            funcion_bodys.append(api_dict[file_name]['function_names'][function_name]['funcion_body'])
            function_docstrings.append(api_dict[file_name]['function_names'][function_name]['function_docstring'])
            function_returns.append(api_dict[file_name]['function_names'][function_name]['function_return'])
            function_args.append(api_dict[file_name]['function_names'][function_name]['function_arg'])
            function_kwargs.append(api_dict[file_name]['function_names'][function_name]['function_kwarg'])

        generate_python_code(file_name, imports, from_imports, class_name, class_parent, docstring_class, function_names, funcion_bodys,
                             function_docstrings, function_returns, function_args, function_kwargs, **kwargs)

        link_imports.append(f'from hive.cookbook.{file_name} import {class_name}')
        class_list.append(class_name)

    lib_import_set(link_imports, class_list, **kwargs)


def _apply_hidden_overrides(mode: str, name: str, function_name: str, bulk: bool, bulk_read: bool, query: bool):
    """
    Apply the HIDDEN_* escape hatches for endpoints whose path doesn't follow the
    bulk/query naming convention closely enough for api_interpreter to classify on its own.
    Only ever triggers on POST, matching the original behaviour.
    """
    if mode != 'POST':
        return function_name, bulk, bulk_read, query

    for hidden in HIDDEN_QUERY:
        if hidden in function_name:
            return hidden + '_bulk', True, True, True
    for hidden in HIDDEN_QUERY_EXACT_NAME:
        if hidden in name:
            return hidden + '_bulk', True, True, True
    for hidden in HIDDEN_BULK_POST:
        if hidden in function_name:
            return function_name, True, False, query
    for hidden in HIDDEN_BULK_POST_EXACT_NAME:
        if hidden in name:
            return function_name, True, False, query

    return function_name, bulk, bulk_read, query


def _official_list_block(kind: str, keys, function_name: str) -> str:
    """
    Build the `official_<kind>_list = [...]` line, the (intentionally unused) chained
    `<kind>.get(...)` expression, and the `warning_wrong_parameters(...)` call.

    The `.get(...)` expression is dead code by design: it exists purely so IDEs (PyCharm in
    particular) that infer dict-key completions from `.get()` call sites inside a function
    pick up the endpoint's known parameter names, so autocompleting `params['` / `payload['`
    inside a caller's usage of this method suggests the right keys. Do not remove it as
    "unused code" - that autocomplete hint is the entire point of the line existing.
    """
    keys = list(keys)
    list_line = "' ,'".join(keys)
    list_line = list_line.lstrip("' ,")
    list_line = f"official_{kind}_list = ['" + list_line + "']"

    suggestion_line = f"'), {kind}.get('".join(keys)
    suggestion_line = suggestion_line.lstrip("'), ")
    suggestion_line = f"{kind}.get('" + suggestion_line + "')"

    warning_line = f'if not self._silence_warning: warning_wrong_parameters(self.{function_name}.__name__, {kind}, official_{kind}_list)'

    return list_line, suggestion_line, warning_line


def api_interpreter(mode, name, description, params, payload, api_dict, headers=None):

    if headers is None: headers = {}

    imports = []
    from_imports = [('hive.api', 'ApiManager, handling_single_page_methods, warning_wrong_parameters')]

    file_name = name.split('/')[1]

    class_parent = ['ApiManager']
    class_name = underscore_to_camelcase(file_name)
    docstring_class = f'Class that handles all the XAutomata {file_name} APIs'

    #############################################################################################################
    # se dentro all'url si trova la dicitura v2 lo tengo a mente per usarlo dopo
    v2 = True if 'v2' in name else False

    function_name, additional_param, uuid_counter = name_gen(name, mode)

    # se l'url ha v2, controlle se e' rimasto nel nome della funzione e lo tolgo
    if v2: function_name = function_name.replace('_v2', '')

    skip_limit = True if 'skip' in params else False  # se skip e' tra i parametri allora si puo paginare se no non si puo

    single_page, key_single_page = 'single_page: bool = False', ''
    page_size, key_page_size = 'page_size: int = 5000', ''
    warm_start, key_warm_start = 'warm_start: bool = False', ''
    params_body, key_params = 'params: dict = False', ''
    payload_body, payload_body_query, key_payload = 'payload: list', 'payload: dict = False', ''
    # headers is never the **kwargs catch-all (params/payload already contend for that single
    # slot): it's always an explicit dict argument, added only for the handful of endpoints
    # that declare an `in: header` parameter in the schema.
    headers_body, key_headers = 'headers: dict = None', ''

    # chiavi della funzione
    function_arg = []  # parametri che finiscono dentro alle chiavi della funzioni
    function_doc = []
    function_kwarg = ''  # str, il kwarg che viene messo dentro alle chiavi delle funzioni (tipo **parmas)

    if uuid_counter > 0:
        for add_param in additional_param:
            if add_param in params: params.pop(add_param)
            function_arg += [f'{add_param}: str']
            function_doc += [f'            {add_param} (str, required): {add_param}']

    bulk = True if 'bulk' in name or 'query' in name else False
    bulk_read = True if 'bulk/read' in name or ('query' in name) else False
    query = True if 'query' in name else False

    function_name, bulk, bulk_read, query = _apply_hidden_overrides(mode, name, function_name, bulk, bulk_read, query)

    if mode == 'GET' or bulk:
        if bulk and not bulk_read:
            pass
        else:
            function_arg += [warm_start]
            function_doc += [warm_start_doc]

        if len(params) > 0:
            function_kwarg = 'params'
            key_params = ' params=params, '

        if skip_limit or bulk:
            if bulk and not query:
                function_arg += [single_page, 'page_size: int = 50']
                function_doc += [single_page_doc, page_size_doc_bulk]
            else:
                function_arg += [single_page, page_size]
                function_doc += [single_page_doc, page_size_doc]

            key_single_page = ' single_page=single_page, '
            key_page_size = ' page_size=page_size, '
        key_warm_start = '' if bulk and not bulk_read else ' warm_start=warm_start, '

    if mode in ['POST', 'PUT', 'DELETE']:
        if bulk:
            if payload is None and len(params) > 0:
                function_kwarg = 'params'
                key_params = ' params=params, '
            elif payload is not None and len(params) == 0:
                function_arg = [payload_body_query if query else payload_body] + function_arg
                function_doc = [payload_doc_query if query else payload_doc_bulk] + function_doc
                key_payload = ' payload=payload, '
            elif payload is not None and len(params) > 0:
                function_arg = [payload_body_query if query else payload_body] + function_arg
                function_doc = [payload_doc_query if query else payload_doc_bulk] + function_doc
                function_kwarg = 'params'
                key_params = ' params=params, '
                key_payload = ' payload=payload, '
        else:
            if payload is None and len(params) > 0:
                function_kwarg = 'params'
                key_params = ' params=params, '
            elif payload is not None and len(params) == 0:
                function_kwarg = 'payload'
                key_payload = ' payload=payload, '
            elif payload is not None and len(params) > 0:
                function_arg += [params_body]
                function_doc = [params_doc2] + function_doc
                function_kwarg = 'payload'
                key_params = ' params=params, '
                key_payload = ' payload=payload, '

    if len(headers) > 0:
        if function_kwarg == '':
            # nothing else claimed the **kwargs catch-all slot (params is empty, payload
            # isn't in play) - headers gets to be the friendly **headers form, same
            # official-list/IDE-hint treatment as params/payload get when they're the
            # catch-all.
            function_kwarg = 'headers'
        else:
            # the catch-all slot is already taken (by params or payload): headers falls
            # back to an explicit dict argument, same as params/payload do to each other
            # in that situation.
            function_arg += [headers_body]
            function_doc += [headers_doc]
        key_headers = ' headers=headers, '

    # riaggiungo il v2 tolto prima, sul fondo della funzione
    if v2: function_name += '_v2'

    function_arg += ['kwargs: dict = None']
    function_arg = ['self'] + function_arg
    function_doc += [kwargs_doc]
    if function_kwarg == 'params':
        function_doc += [params_doc]
    elif function_kwarg == 'payload':
        function_doc += [payload_doc]
    elif function_kwarg == 'headers':
        function_doc += [headers_doc_kwarg]
    else:
        pass

    # corpo della funzione
    kwargs_converter = 'if kwargs is None: kwargs = dict()'

    non_paginabili = ''
    if not skip_limit and mode == 'GET' and ('params' in function_kwarg or 'params' in function_arg):
        non_paginabili = 'kwargs, params = handling_single_page_methods(kwargs=kwargs.copy(), params=params.copy())'

    execute = f"response = self.execute('{mode}', path=f'{name}',{key_single_page}{key_page_size}{key_warm_start}{key_headers}{key_params}{key_payload} **kwargs)"
    response = 'return response'

    #############################################################################################################

    required_dict = {True: 'required', False: 'optional'}
    full_params_doc = []
    example_doc = []

    for param in params:
        text_doc = dict_doc[param] if param in dict_doc else 'additional filter'
        full_params_doc.append(f"            {param} ({params[param]['type']} {required_dict[params[param]['required']]}): {text_doc} - parameter")

    for header in headers:
        text_doc = dict_doc[header] if header in dict_doc else 'additional filter'
        full_params_doc.append(f"            {header} ({headers[header]['type']} {required_dict[headers[header]['required']]}): {text_doc} - header")

    if bulk and (payload is not None):
        for param in payload:
            type_doc = " ".join(payload[param]['type']) if isinstance(payload[param]['type'], list) else payload[param]['type']
            example_doc.append(f'            "{param}": "{type_doc}", {required_dict[payload[param]["required"]]}')
    elif payload is not None:
        for param in payload:
            text_doc = dict_doc[param] if param in dict_doc else 'additional filter'
            type_doc = " ".join(payload[param]['type']) if isinstance(payload[param]['type'], list) else payload[param]['type']
            full_params_doc.append(f"            {param} ({type_doc} {required_dict[payload[param]['required']]}): {text_doc} - payload")
    else:
        pass

    args_doc = '\n        Args:'
    kwargs_title_doc = '\n        Keyword Args:'
    examples_doc = '\n        Examples:'
    return_doc = '\n        Returns: list'
    description = [description, args_doc]
    description += function_doc

    if len(full_params_doc) > 0:
        description.append(kwargs_title_doc)
        description += full_params_doc

    if len(example_doc) > 0:
        description.append(examples_doc)
        description.append("            payload = ")
        if not query: description.append("          [")
        if len(example_doc) > 1:        description.append("           {")
        description += example_doc
        if len(example_doc) > 1:        description.append("           }")
        if not query: description.append("          ]")

    description.append(return_doc)

    description = "\n".join(description)

    if function_kwarg == 'params':
        params_list_line, params_suggestion_line, warning_wrong_parameters = _official_list_block('params', params, function_name)
    elif function_kwarg == 'payload':
        params_list_line, params_suggestion_line, warning_wrong_parameters = _official_list_block('payload', payload, function_name)
    elif function_kwarg == 'headers':
        params_list_line, params_suggestion_line, warning_wrong_parameters = _official_list_block('headers', headers, function_name)
    else:
        params_list_line, params_suggestion_line, warning_wrong_parameters = '', '', ''

    funcion_body = [kwargs_converter, non_paginabili, params_list_line, params_suggestion_line, warning_wrong_parameters, execute, response]  # list
    function_docstring = description  # str, docstring delle funzioni
    function_return = ' list'  # str

    api_dict.deep_update([file_name, 'imports'], imports)
    api_dict.deep_update([file_name, 'from_imports'], from_imports)
    api_dict.deep_update([file_name, 'file_name'], file_name)
    api_dict.deep_update([file_name, 'class_name'], class_name)
    api_dict.deep_update([file_name, 'class_parent'], class_parent)
    api_dict.deep_update([file_name, 'docstring_class'], docstring_class)

    function_kwarg = None if function_kwarg == '' else function_kwarg

    if file_name in api_dict:
        if 'function_names' in api_dict[file_name]:
            if function_name in api_dict[file_name]['function_names']:
                if len(additional_param) > 0:
                    for par in additional_param:
                        function_name = f'{function_name}_{par}'
                        if function_name not in api_dict[file_name]['function_names']:
                            break
            if function_name in api_dict[file_name]['function_names']:
                logger.error('API overwriting another one')

    dict_content = {'function_name': function_name, 'funcion_body': funcion_body,
                    'function_docstring': function_docstring, 'function_return': function_return,
                    'function_arg': function_arg, 'function_kwarg': function_kwarg}

    api_dict.deep_update([file_name, 'function_names', function_name], dict_content)

    return api_dict


def name_gen(url: str, mode: str):
    """
    Derive the python method name from the URL, e.g. '/metrics/{uuid}' + GET -> 'metric'.

    Two things happen in one pass over the URL's path segments:
      1. any {placeholder} segment is pulled out into `additional_param` (it becomes a
         `param: str` argument of the generated method rather than part of its name);
      2. purely structural segments ('read', 'bulk', 'query', ...) are dropped, since they're
         already reflected in `converted_mode`/`bulk` below.
    What's left, joined with '_', is the function name (plus the mode/bulk suffix).
    """
    additional_param = []
    mode_converter = {'GET': '', 'POST': '_create', 'PUT': '_put', 'DELETE': '_delete'}
    converted_mode = mode_converter[mode]

    name_split = url.lstrip('/').rstrip('/').split('/')
    bulk = ''

    if 'bulk' in url:
        if 'read' in url: converted_mode = mode_converter['GET']
        if 'read_by' in url: converted_mode = '_read_by'
        if 'create' in url: converted_mode = mode_converter['POST']
        if 'update' in url: converted_mode = mode_converter['PUT']
        if 'delete' in url: converted_mode = mode_converter['DELETE']
        bulk = '_bulk'

    if 'query' in url:
        if mode == 'GET': converted_mode = '_query'
        if mode == 'POST': converted_mode = '_query_bulk'

    structural_segments = {'read', 'read_by', 'create', 'update', 'delete', 'bulk'}
    kept_segments = []
    for segment in name_split:
        if '{' in segment and '}' in segment:
            additional_param.append(segment.lstrip('{').rstrip('}'))
            continue
        if segment in structural_segments or 'query' in segment:
            continue
        kept_segments.append(segment)
    name_split = kept_segments

    uuid_counter = len(additional_param)

    if mode == 'GET' and uuid_counter == 1 and len(name_split) == 1:
        name_split[-1] = name_split[-1].rstrip('s')

    function_name = '_'.join(name_split) + converted_mode + bulk
    function_name = function_name.replace('-', '_')
    return function_name, additional_param, uuid_counter


parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, help="URL", required=True)
parser.add_argument('--mock', type=str, required=False, default=False)

if __name__ == '__main__':

    main(**vars(parser.parse_args()))
