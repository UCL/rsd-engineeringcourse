---
title: Functions and modules
---

## Functions 

### Definition

We use `def` to define a function, and `return` to pass back a value:

{{ pyfrag('01','functions','Function') }}

### Side effects

Functions can do things to change their **mutable** arguments,
so `return` is optional.

{{ pyfrag('01','functions','SideEffect') }}

### Early Return

Return without arguments can be used to exit early from a function

{{ pyfrag('01','functions','EarlyReturn') }}

### Unpacking arguments

If a vector is supplied to a function with a '*', its elements
are used to fill each of a function's arguments. 

{{ pyfrag('01','functions','UnpackingArguments') }}

This can be quite powerful:

{{ pyfrag('01','functions','UnpackingPower') }}

### Sequence Arguments

Similiarly, if a `*` is used in the definition of a function, multiple
arguments are absorbed into a tuple:

{{ pyfrag('01','functions','SequenceArguments') }}

### Keyword Arguments

If two asterisks are used, named arguments are supplied as a dictionary:

{{ pyfrag('01','functions','KeywordArguments') }}

## Modules

### File Modules
Each python file defines a module, which can be imported from with import:

{{ notebookfile('01','pretty.py') }}

Another file:

{{ pyfrag('01','modules','FileImport') }}

### Module Variables

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

### Relative Import

Inside packages, you can use `..` to refer to the parent module

{{ notebookfile('01','module1/module3/__init__.py')}}

{{ pyfrag('01','modules','RelativeImport') }}
