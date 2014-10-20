---
title: Functions and modules
---

# Functions 

## Definition

We use `def` to define a function, and `return` to pass back a value:

{{ pyfrag('functions','Function') }}

## Side effects

Functions can do things to change their **mutable** arguments,
so `return` is optional.

{{ pyfrag('functions','SideEffect') }}

## Early Return

Return without arguments can be used to exit early from a function

{{ pyfrag('functions','EarlyReturn') }}

## Unpacking arguments

If a vector is supplied to a function with a '*', its elements
are used to fill each of a function's arguments. 

{{ pyfrag('functions','UnpackingArguments') }}

This can be quite powerful:

{{ pyfrag('functions','UnpackingPower') }}

## Sequence Arguments

Similiarly, if a `*` is used in the definition of a function, multiple
arguments are absorbed into a tuple:

{{ pyfrag('functions','SequenceArguments') }}

## Keyword Arguments

If two asterisks are used, named arguments are supplied as a dictionary:

{{ pyfrag('functions','KeywordArguments') }}

# Modules

## File Modules
Each python file defines a module, which can be imported from with import:

{{ notebookfile('pretty') }}

Another file:

{{ pyfrag('modules','FileImport') }}

## Module Variables

Modules can contain variables as well as functions, and these can be changed.

{{ pyfrag('modules','ModuleVariable') }}

## Importing from modules

Things can be imported from modules to become part of the current module

{{ pyfrag('modules','ImportFrom') }}

## Import and rename

You can rename things as you import them to avoid clashes or for convenience

{{ pyfrag('modules','ImportAlias') }}

## Folders as modules

If you make a folder with a special file called __init__.py in, the *folder* becomes
a module, and can contain other modules. It is referred to as a package:

``` tree
module1
|-- __init__.py
|-- module2.py
`-- module3
    `-- __init__.py
```

{{ notebookfile('module1/__init__')}}

{{ notebookfile('module1/module2') }}

{{ pyfrag('modules','FolderModules') }}

## Relative Import

Inside packages, you can use `..` to refer to the parent module

{{ notebookfile('module1/module3/__init__')}}

{{ pyfrag('modules','RelativeImport') }}
