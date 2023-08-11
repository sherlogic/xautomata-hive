from utilities.args.parser import ArgumentParser
from utilities.io.services_job_util import Invoker, get_config
from _API_writers import generate_python_code, underscore_to_camelcase, lib_import_set
from utilities.dictionary import DeepDict


FORCE_STATUS = [429, 500, 502, 503, 504]
METHODS = ["HEAD", "GET", "OPTIONS", "POST"]

single_page_doc = "            single_page (bool, optional): se False la risposta viene ottenuta a step per non appesantire le API. Default to False."
page_size_doc = "            page_size (int, optional): Numero di oggetti per pagina se single_page == False. Default to 5000."
kwargs_doc = "            kwargs (dict, optional): additional parameters for execute. Default to None."
warm_start_doc = "            warm_start (bool, optional): salva la risposta in un file e se viene richiamata la stessa funzione con gli stessi argomenti restituisce il contenuto del file. Default to False."
params_doc = "            **params: additional parameters for the API."
params_doc2 = "            params (dict, optional): additional parameters for the API."
payload_doc = "            **payload: additional parameters for the API."
payload_doc_bulk = "            payload (list[dict], optional): List dict to create."
payload_doc_query = "            payload (dict, optional): additional parameters for the API."

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


def find_ref(schemas, schema_ref, key, key_type, name):
    if 'anyOf' in schemas[schema_ref]['properties'][key]:
        for types in schemas[schema_ref]['properties'][key]['anyOf']:
            key_type.append(types['type'])
    elif 'type' in schemas[schema_ref]['properties'][key]:
        key_type.append(schemas[schema_ref]['properties'][key]['type'])
    # elif '$ref' in schemas[schema_ref]['properties'][key]:
    #     key_type = find_ref(schemas, schemas[schema_ref]['properties'][key]['$ref'].split('/')[-1], key, key_type)
    else:
        print(f'wrong requestBody type {name}')
        key_type = None
    return key_type


def main(**kwargs):

    spell = Invoker(get_config(**kwargs), **kwargs)
    data = spell.openapi()
    apis = data['paths']
    schemas = data['components']['schemas']
    # print(data)

    allowed = {
        # "/ts_cost_management/": ["GET", "POST", "PUT", "DELETE"],
        # "/ts_cost_management/{uuid_metric}": ["GET", "POST", "PUT", "DELETE"],
        # "/metrics/{uuid}": ["GET", "POST", "DELETE", "PUT"],
        # "/metrics/{uuid}/services": ["GET"],
        # "/metrics/{uuid}/services/{uuid_service}": ["POST", "DELETE"],
        # "/metrics/bulk/read/": ["POST"],
        # "/metrics/bulk/read_by/": ["POST"],
        # "/metrics/bulk/create/": ["POST"],
        # "/metrics/bulk/delete/": ["POST"],
        # "/metrics/bulk/create/services": ["POST"],
        # "/metrics/bulk/delete/services": ["POST"],
        # "/sites/": ["POST"],
        # "/sites/{uuid}": ["GET", "PUT"],
        # "/services/query/": ["GET", "POST"],
        # "/last_status/": ["GET", "POST"]
    }

    api_dict = DeepDict()

    for name in apis:
        if name != '/openapi.js':

            for mode in apis[name]:
                if (len(allowed) > 0 and name in allowed and mode.upper() in allowed[name]) or (len(allowed) == 0):
                    # if name == '/ts_cost_management/':
                    #     print(name)
                    description = apis[name][mode]['summary']

                    params = dict()
                    if 'parameters' in apis[name][mode]:
                        for param in apis[name][mode]['parameters']:
                            param_type = param['schema']['type'] if 'type' in param['schema'] else None
                            params[param['name']] = {'type': param_type, 'required': param['required']}

                    payload = dict()
                    if 'requestBody' in apis[name][mode]:
                        application = 'application/json' if 'application/json' in apis[name][mode]['requestBody']['content'] else 'application/x-www-form-urlencoded'
                        if '$ref' in apis[name][mode]['requestBody']['content'][application]['schema']:
                            schema_ref = apis[name][mode]['requestBody']['content'][application]['schema']['$ref'].split('/')[-1]

                        elif 'items' in apis[name][mode]['requestBody']['content'][application]['schema'] and \
                                '$ref' in apis[name][mode]['requestBody']['content'][application]['schema']['items']:
                            schema_ref = apis[name][mode]['requestBody']['content'][application]['schema']['items']['$ref'].split('/')[-1]

                        elif 'items' in apis[name][mode]['requestBody']['content'][application]['schema'] and \
                                'anyOf' in apis[name][mode]['requestBody']['content'][application]['schema']['items']:

                            schema_ref = []
                            for schemas_ref in apis[name][mode]['requestBody']['content'][application]['schema']['items']['anyOf']:
                                if '$ref' in schemas_ref: schema_ref.append(schemas_ref['$ref'].split('/')[-1])

                        elif 'items' in apis[name][mode]['requestBody']['content'][application]['schema'] and \
                                'required' in apis[name][mode]['requestBody']:
                            schema_ref = 'missing'

                        else:
                            print(f'missing the schema_ref for {name}')
                            schema_ref = None

                        schema_ref = [schema_ref] if not isinstance(schema_ref, list) else schema_ref

                        for ii, schema in enumerate(schema_ref):
                            if schema is not None and schema != 'missing':
                                for key in schemas[schema]['properties']:
                                    key_type = []
                                    key_type = find_ref(schemas, schema, key, key_type, name)

                                    key_required = False
                                    if 'required' in schemas[schema] and key in schemas[schema]['required']:
                                        key_required = True

                                    key_name = f'{key}_{ii}' if len(schema_ref) > 1 else key
                                    payload[key_name] = {'type': key_type,
                                                         'required': key_required}
                            elif schema == 'missing':
                                payload['uuid'] = {'type': 'str',
                                                   'required': True}
                            else:
                                payload = {}

                    api_dict = api_interpreter(mode.upper(), name, description, params, payload, api_dict)

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


def api_interpreter(mode, name, description, params, payload, api_dict):

    imports = []
    from_imports = [('hive.api', 'ApiManager, handling_single_page_methods')]

    file_name = name.split('/')[1]

    class_parent = ['ApiManager']
    class_name = underscore_to_camelcase(file_name)
    docstring_class = f'Class that handles all the XAutomata {file_name} APIs'

    #############################################################################################################

    # if name == '/ts_cost_management/' and mode == "GET":
    #     print(name)

    function_name, additional_param, uuid_counter = name_gen(name, mode)

    skip_limit = True if 'skip' in params else False  # se skip e' tra i parametri allora si puo paginare se no non si puo

    single_page, key_single_page = 'single_page: bool = False', ''
    page_size, key_page_size = 'page_size: int = 5000', ''
    warm_start, key_warm_start = 'warm_start: bool = False', ''
    params_body, key_params = 'params: dict = False', ''
    payload_body, payload_body_query, key_payload = 'payload: list', 'payload: dict = False', ''

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

    hidden_query = ['last_status']
    hidden_bulk_post = ['metric_ingest', 'probes_log_ingest']

    if mode == 'POST':
        for hidden in hidden_query:
            if hidden in function_name:
                query = True
                function_name = hidden+'_bulk'
                bulk, bulk_read = True, True
                break
        for hidden in hidden_bulk_post:
            if hidden in function_name:
                bulk, bulk_read = True, False
                break

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
            function_arg += [single_page, page_size]
            function_doc += [single_page_doc, page_size_doc]
            key_single_page = ' single_page=single_page, '
            key_page_size = ' page_size=page_size, '
        key_warm_start = '' if bulk and not bulk_read else ' warm_start=warm_start, '

    if mode in ['POST', 'PUT', 'DELETE']:
        if bulk:
            if len(payload) == 0 and len(params) > 0:
                function_kwarg = 'params'
                key_params = ' params=params, '
            elif len(payload) > 0 and len(params) == 0:
                function_arg = [payload_body_query if query else payload_body] + function_arg
                function_doc += [payload_doc_query if query else payload_doc_bulk] + function_doc
                key_payload = ' payload=payload, '
            elif len(payload) > 0 and len(params) > 0:
                function_arg = [payload_body_query if query else payload_body] + function_arg
                function_doc += [payload_doc_query if query else payload_doc_bulk] + function_doc
                function_kwarg = 'params'
                key_params = ' params=params, '
                key_payload = ' payload=payload, '
        else:
            if len(payload) == 0 and len(params) > 0:
                function_kwarg = 'params'
                key_params = ' params=params, '
            elif len(payload) > 0 and len(params) == 0:
                function_kwarg = 'payload'
                key_payload = ' payload=payload, '
            elif len(payload) > 0 and len(params) > 0:
                function_arg += [params_body]
                function_doc += [params_doc2] + function_doc
                function_kwarg = 'payload'
                key_params = ' params=params, '
                key_payload = ' payload=payload, '

    function_arg += ['kwargs: dict = None']
    function_arg = ['self'] + function_arg
    function_doc += [kwargs_doc]
    if function_kwarg == 'params':
        function_doc += [params_doc]
    elif function_kwarg == 'payload':
        function_doc += [payload_doc]
    else:
        pass

    # corpo della funzione
    kwargs_converter = 'if kwargs is None: kwargs = dict()'
    non_paginabili = ''
    if not skip_limit and mode == 'GET' and ('params' in function_kwarg or 'params' in function_arg):
        non_paginabili = 'kwargs, params = handling_single_page_methods(kwargs=kwargs, params=params)'
    execute = f"response = self.execute('{mode}', path=f'{name}',{key_single_page}{key_page_size}{key_warm_start}{key_params}{key_payload} **kwargs)"
    response = 'return response'

    #############################################################################################################

    required_dict = {True: 'required', False: 'optional'}
    full_params_doc = []
    example_doc = []

    for param in params:
        text_doc = dict_doc[param] if param in dict_doc else 'additional filter'
        full_params_doc.append(f"            {param} ({params[param]['type']} {required_dict[params[param]['required']]}): {text_doc} - parameter")

    if bulk:
        for param in payload:
            type_doc = " ".join(payload[param]['type']) if isinstance(payload[param]['type'], list) else payload[param]['type']
            example_doc.append(f'            "{param}": "{type_doc}", {required_dict[payload[param]["required"]]}')
    else:
        for param in payload:
            text_doc = dict_doc[param] if param in dict_doc else 'additional filter'
            type_doc = " ".join(payload[param]['type']) if isinstance(payload[param]['type'], list) else payload[param]['type']
            full_params_doc.append(f"            {param} ({type_doc} {required_dict[payload[param]['required']]}): {text_doc} - payload")

    args_doc = '        Args:'
    kwargs_title_doc = '        Keyword Args:'
    examples_doc = '        Examples:'
    return_doc = '        Returns: list'
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

    funcion_body = [kwargs_converter, non_paginabili, execute, response]  # list
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
                print('################# errore #######################')
                print('API overwriting another one')

    dict_content = {'function_name': function_name, 'funcion_body': funcion_body,
                    'function_docstring': function_docstring, 'function_return': function_return,
                    'function_arg': function_arg, 'function_kwarg': function_kwarg}

    api_dict.deep_update([file_name, 'function_names', function_name], dict_content)

    return api_dict


def name_gen(url, mode):
    additional_param = []
    mode_converter = {'GET': '', 'POST': '_create', 'PUT': '_put', 'DELETE': '_delete'}
    converted_mode = mode_converter[mode]

    name_split = url.lstrip('/').rstrip('/')
    name_split = name_split.split('/')
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

    uuid_counter = 0
    i = 0
    for j in range(len(name_split)):

        break_cycle = False

        if i == (len(name_split) - 1):
            break_cycle = True

        if ('{' in name_split[i]) and ('}' in name_split[i]):
            uuid_counter += 1
            # if uuid_counter == 2:
            #     additional_param = name_split[i].lstrip('{').rstrip('}')
            additional_param.append(name_split[i].lstrip('{').rstrip('}'))
            name_split.pop(i)
            i -= 1

        if name_split[i] in ['read', 'read_by', 'create', 'update', 'delete', 'bulk']:
            name_split.pop(i)
            i -= 1

        if 'query' in name_split[i]:
            name_split.pop(i)
            i -= 1

        i += 1

        if break_cycle: break

    if mode == 'GET' and uuid_counter == 1 and len(name_split) == 1:
        name_split[-1] = name_split[-1].rstrip('s')

    function_name = '_'.join(name_split) + converted_mode + bulk
    function_name = function_name.replace('-', '_')
    return function_name, additional_param, uuid_counter


parser = ArgumentParser(job_use=True)
parser.add_param('-mk', '--mock', str, required=False, default=False)

if __name__ == '__main__':

    main(**vars(parser.parse_arguments()))
