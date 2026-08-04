"""
Turns the extraction produced by the reader script (dict of file_name -> class/method
definitions) into the `hive/cookbook/*.py` source files, and splices the resulting
class list into `hive/api.py`.

Two implementation details are load-bearing and easy to "clean up" by mistake:

1. `ast.arguments.args`, `ast.arguments.kwarg` and `ast.FunctionDef.returns` are populated
   here with *raw source-text strings* (e.g. "uuid: str", "params", " list") instead of
   proper `ast.arg` / expression nodes. astor's unparser is duck-typed: when a field holds
   something that is not an `ast.AST` instance it writes it out verbatim instead of
   dispatching a node visitor. This is intentional: it lets the reader hand over a fully
   formatted parameter (name + type hint + default value) as a single string without having
   to build the equivalent annotation/default expression AST by hand. Do NOT wrap these
   strings in `ast.arg(...)` "to do it properly" - that changes what gets rendered (and,
   for `kwarg`/`returns`, doesn't apply at all since those aren't lists of ast.arg).
2. Every statement in a function body IS parsed for real (`ast.parse(...).body[0]`), so
   those must be syntactically valid Python source - unlike the signature pieces above.
"""
import ast
from pathlib import Path
from typing import List, Optional

import astor

REPO_ROOT = Path(__file__).resolve().parent
COOKBOOK_DIR = REPO_ROOT / 'hive' / 'cookbook'
COOKBOOK_DIR_MOCK = REPO_ROOT / 'test' / 'cookbook'
API_FILE = REPO_ROOT / 'hive' / 'api.py'

IMPORTS_START_MARKER = '# hive imports start'
IMPORTS_STOP_MARKER = '# hive imports stop'
CLASS_DECLARATION_PREFIX = 'class XautomataApi('


def function_gen(function_name: str, funcion_body: list, function_docstring: str, returns: str, arg: list, kwarg: str) -> ast.FunctionDef:
    """Assemble a single method. `arg`/`kwarg`/`returns` are raw strings, see module docstring."""

    body = [ast.parse(operation).body[0] for operation in funcion_body if operation != '']
    docstring = ast.Expr(ast.Constant(value=function_docstring))
    body.insert(0, docstring)

    args_node = ast.arguments(posonlyargs=[], args=arg, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=kwarg, defaults=[])

    return ast.FunctionDef(name=function_name,
                           args=args_node,
                           decorator_list=[],
                           body=body,
                           returns=returns)


def function_assembler(function_names: list, funcion_bodys: List[list], function_docstrings: list, returnss: list, args: List[list], kwarg: list) -> List[ast.FunctionDef]:
    return [function_gen(function_name, funcion_body, function_docstring, returns, arg, kw)
           for function_name, funcion_body, function_docstring, returns, arg, kw
           in zip(function_names, funcion_bodys, function_docstrings, returnss, args, kwarg)]


def class_gen(class_name: str, class_parent: list, class_docstring: str, functions: Optional[list] = None) -> ast.ClassDef:
    if functions is None:
        functions = []

    class_body = [ast.Expr(value=ast.Constant(value=class_docstring))]
    class_body += functions

    parent = [ast.Name(id=par, ctx=ast.Load()) for par in class_parent] if len(class_parent) > 0 else []

    return ast.ClassDef(name=class_name, bases=parent, keywords=[], body=class_body, decorator_list=[])


def module_gen(filename: str, imports: Optional[list] = None, from_imports: Optional[list] = None, classes: Optional[list] = None, functions: Optional[list] = None, **kwargs) -> None:
    """Render a full module (imports + class) to disk under hive/cookbook, or test/cookbook when kwargs['mock']."""
    if imports is None: imports = []
    if from_imports is None: from_imports = []
    if functions is None: functions = []
    if classes is None: classes = []

    import_nodes = [ast.Import(names=[ast.alias(name=import_name, asname=None)]) for import_name in imports]
    from_import_nodes = [ast.ImportFrom(module=module_name, names=[ast.alias(name=name, asname=None)], level=0) for
                         module_name, name in from_imports]
    all_imports = import_nodes + from_import_nodes

    module = ast.Module(body=all_imports + functions + classes, type_ignores=[])

    source_code = astor.to_source(module)

    target_dir = COOKBOOK_DIR_MOCK if kwargs.get('mock') else COOKBOOK_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / f'{filename}.py').write_text(source_code)


def generate_python_code(file_name: str, imports: List[str], from_imports: List[tuple], class_name: str, class_parent: list, docstring_class: str,
                         function_names: List[str], funcion_bodys: List[list], function_docstrings: List[str], function_returns: List[str],
                         function_args: List[list], function_kwargs: List[str], **kwargs) -> None:
    """
    generate python file with class and methods

    Args:
        file_name (str): file_name
        imports (list): imports
        from_imports (list[tuple]): imports derived from a "from" statement
        class_name (str): class name
        class_parent (list[str]): lista delle classi parent
        docstring_class (str): docstring class content
        function_names (list[str]): list of methods names
        funcion_bodys (list[str]): list of methods in the class
        function_docstrings (list[str]): list of docstring for each methods
        function_returns (list): list of return types for each methods
        function_args (list[str]): list of the methods keys
        function_kwargs (list[str]): name of the kwarg for each methods

    Examples:
        imports = ['os']
        from_imports = [('math', 'sqrt')]
        file_name = 'generated_code.py'

        class_name = 'NomeClasse'
        docstring_class = "Questa è la docstring della classe MyClass."

        function_names = ['foo1' 'foo2']
        funcion_body = [['pd.DataFrame(a)', 'b = a * 2', 'a = "ciso"', 'return [a, b]'], ['pd.DataFrame(a)', 'b = a * 2', 'a = "ciso"', 'return [a, b]']]
        docstring_foo = [["Questa è la docstring della funzione."], ["Questa è la docstring della funzione."]]
        function_returns = [' list', ' list']
        function_args = [['self', 'a', 'b'], ['self', 'a', 'b']]
        function_kwargs = ['params', 'payload']
    """

    functions = function_assembler(function_names, funcion_bodys, function_docstrings, function_returns, function_args, function_kwargs)
    classy = class_gen(class_name, class_parent, docstring_class, functions)
    module_gen(file_name, imports, from_imports, [classy], **kwargs)


def underscore_to_camelcase(name: str) -> str:
    words = name.split('_')
    camelcase_name = ''.join(word.capitalize() for word in words)
    return camelcase_name


def lib_import_set(import_link: List[str], class_list: List[str], **kwargs) -> None:
    """
    Splice the generated `from hive.cookbook.X import Y` lines and the `XautomataApi(...)`
    base-class list into hive/api.py, in place, between fixed markers.

    Skipped entirely when kwargs['mock'] is truthy (dry-run / test generation).
    """
    classes = ", ".join(class_list).lstrip(', ')
    classes = f'class XautomataApi({classes}):'

    contents = API_FILE.read_text().splitlines()

    try:
        vers_start = contents.index(IMPORTS_START_MARKER) + 1
        vers_stop = contents.index(IMPORTS_STOP_MARKER)
    except ValueError as e:
        raise RuntimeError(f'{API_FILE}: could not find the "{IMPORTS_START_MARKER}" / "{IMPORTS_STOP_MARKER}" markers') from e

    contents[vers_start:vers_stop] = import_link

    start_class, stop_class = None, None
    for i, line in enumerate(contents):
        if start_class is None and line.startswith(CLASS_DECLARATION_PREFIX):
            start_class = i
        if start_class is not None and '):' in line:
            stop_class = i
            break

    if start_class is None or stop_class is None:
        raise RuntimeError(f'{API_FILE}: could not find the "{CLASS_DECLARATION_PREFIX}...):" class declaration to replace - refusing to touch the file')

    del contents[start_class:stop_class + 1]
    contents[start_class:start_class] = [classes]

    if not kwargs.get('mock'):
        API_FILE.write_text(''.join(f'{line}\n' for line in contents))
