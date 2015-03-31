---
title: Modules
---

## Modules

### File modules
Each python file defines a module, which can be imported from with import:

{{ notebookfile('01','pretty.py') }}

Another file:

{{ pyfrag('01','modules','FileImport') }}

### Module variables

Modules can contain variables as well as functions, and these can be changed.

{{ pyfrag('01','modules','ModuleVariable') }}

### Importing from modules

Things can be imported from modules to become part of the current module

{{ pyfrag('01','modules','ImportFrom') }}

### Import and rename

You can rename things as you import them to avoid clashes or for convenience

{{ pyfrag('01','modules','ImportAlias') }}

### Folders as modules

If you make a folder with a special file called __init__.py in, the *folder* becomes
a module, and can contain other modules. It is referred to as a package:

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
