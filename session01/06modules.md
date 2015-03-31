---
title: Modules
---

## Modules

### File modules
Each python file defines a module:

{{ notebookfile('01','pretty.py') }}

Modules can be imported to another file with `import`:

{{ pyfrag('01','modules','FileImport') }}

### Module variables

Modules can contain variables as well as functions, and these can be changed.

{{ pyfrag('01','modules','ModuleVariable') }}

### Importing from modules

Things can be imported from modules to become part of the current module

{{ pyfrag('01','modules','ImportFrom') }}

### Import and rename

You can rename things as you import them for convenience, or to avoid clashes:

{{ pyfrag('01','modules','ImportAlias') }}

### Packages (folders as modules)

If we create an empty file called `__init__.py` and place it in a folder, the *folder* becomes a module. We call this a package:

``` tree
module1
|-- __init__.py
|-- module2.py
`-- module3
    `-- __init__.py
```

{{ notebookfile('01','module1/__init__.py')}}

{{ notebookfile('01','module1/module2.py') }}

{{ pyfrag('01','modules','FolderModules') }}

### Relative import

Inside packages, you can use `..` to refer to the parent module

{{ notebookfile('01','module1/module3/__init__.py')}}

{{ pyfrag('01','modules','RelativeImport') }}

