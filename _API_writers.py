import ast
import astor
from typing import List


def function_gen(function_name: str, funcion_body: list, function_docstring: str, returns: str, arg: list, kwarg: str):

    body = [ast.parse(operation).body[0] for operation in funcion_body if operation != '']
    docstring = ast.Expr(ast.Str(s=function_docstring))
    body.insert(0, docstring)

    return ast.FunctionDef(name=function_name,
                           args=ast.arguments(args=arg, kwarg=kwarg, defaults=[]),
                           decorator_list=[],
                           body=body,
                           returns=returns)


def function_assembler(function_names: list, funcion_bodys: List[list], function_docstrings: list, returnss: list, args: List[list], kwarg: list):
    functions = []
    for function_name, funcion_body, function_docstring, returns, arg, kwarg in zip(function_names, funcion_bodys, function_docstrings, returnss, args, kwarg):
        functions.append(function_gen(function_name, funcion_body, function_docstring, returns, arg, kwarg))
    return functions


def class_gen(class_name: str, class_parent: list, class_docstring: str, functions: list = None):
    if functions is None: functions = []

    class_body = [ast.Expr(value=ast.Str(s=class_docstring))]
    class_body += functions

    parent = [ast.Name(id=par, ctx=ast.Load()) for par in class_parent] if len(class_parent) > 0 else []

    # Creiamo un oggetto ClassDef che rappresenta la definizione della classe
    return ast.ClassDef(name=class_name, bases=parent, keywords=[], body=class_body, decorator_list=[])


def module_gen(filename: str, imports: list = None, from_imports: list = None, classes: list = None, functions: list = None, **kwargs):
    if imports is None: imports = []
    if from_imports is None: from_imports = []
    if functions is None: functions = []
    if classes is None: classes = []

    # Creiamo oggetti Import che rappresentano gli import normali
    import_nodes = [ast.Import(names=[ast.alias(name=import_name, asname=None)]) for import_name in imports]
    # Creiamo oggetti ImportFrom che rappresentano gli import del tipo "from"
    from_import_nodes = [ast.ImportFrom(module=module_name, names=[ast.alias(name=name, asname=None)], level=0) for
                         module_name, name in from_imports]
    # Uniamo entrambe le liste di import
    all_imports = import_nodes + from_import_nodes

    # Creiamo un modulo che contiene la funzione principale
    module = ast.Module(body=all_imports + functions + classes)

    # Generiamo il codice sorgente astratto in una stringa
    source_code = astor.to_source(module)
    # print(source_code)

    if kwargs['mock']:
        # Scriviamo il codice sorgente nel file specificato
        with open(f'./test/cookbook/{filename}.py', 'w') as file:
            file.write(source_code)
    else:
        # Scriviamo il codice sorgente nel file specificato
        with open(f'./hive/cookbook/{filename}.py', 'w') as file:
            file.write(source_code)


def generate_python_code(file_name: str, imports: List[str], from_imports: List[tuple], class_name: str, class_parent: list, docstring_class: str,
                         function_names: List[str], funcion_bodys: List[list], function_docstrings: List[str], function_returns: List[str],
                         function_args: List[list], function_kwargs: List[str], **kwargs):
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


def underscore_to_camelcase(name):
    words = name.split('_')
    camelcase_name = ''.join(word.capitalize() for word in words)
    return camelcase_name


def lib_import_set(import_link, class_list, **kwargs):

    classes = ", ".join(class_list).lstrip(', ')
    classes = f'class XautomataApi({classes}):'

    with open("./hive/api.py", "r") as f:
        contents = f.readlines()

    for i in range(len(contents)):
        contents[i] = contents[i].rstrip('\n')

    vers_start = contents.index('# hive imports start') + 1
    vers_stop = contents.index('# hive imports stop')

    # venogono aggiunte le nuove librerie alla lista da scrivere sul file
    contents[vers_start:vers_stop] = import_link

    start, stop = 0, 0
    for i, line in enumerate(contents):
        if 'class XautomataApi(' in line:
            start = i
        if start > 0 and '):' in line:
            stop = i
            break

    del contents[start:stop+1]
    contents[start:start] = [classes]

    if not kwargs['mock']:
        with open("./hive/api.py", "w") as f:
            for s in contents:
                f.write(str(s) + "\n")