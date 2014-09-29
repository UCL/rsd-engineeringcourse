---
title: Functions and modules
---

# Functions 

## Definition

We use `def` to define a function, and `return` to pass back a value:

``` python
{{d['session01/python/functions.py|idio|pycon']['Function']}}
```

## Side effects

Functions can do things to change their **mutable** arguments,
so `return` is optional.

``` python
{{d['session01/python/functions.py|idio|pycon']['SideEffect']}}
```

## Early Return

Return without arguments can be used to exit early from a function

``` python
{{d['session01/python/functions.py|idio|pycon']['EarlyReturn']}}
```

## Unpacking arguments

If a vector is supplied to a function with a '*', its elements
are used to fill each of a function's arguments. 

``` python
{{d['session01/python/functions.py|idio|pycon']['UnpackingArguments']}}
```

This can be quite powerful:

``` python
{{d['session01/python/functions.py|idio|pycon']['UnpackingPower']}}
```

## Sequence Arguments

Similiarly, if a `*` is used in the definition of a function, multiple
arguments are absorbed into a tuple:

``` python
{{d['session01/python/functions.py|idio|pycon']['SequenceArguments']}}
```

## Keyword Arguments

If two asterisks are used, named arguments are supplied as a dictionary:

``` python
{{d['session01/python/functions.py|idio|pycon']['KeywordArguments']}}
```

# Modules

## File Modules
Each python file defines a module, which can be imported from with import:

File pretty.py:

``` python
{{d['session01/python/pretty.py|idio|t']['Arrow']}}
```

Another file:

``` python
{{d['session01/python/modules.py|idio|pycon']['FileImport']}}
```

## Module Variables

Modules can contain variables as well as functions, and these can be changed.

``` python
{{d['session01/python/modules.py|idio|pycon']['ModuleVariable']}}
```

## Importing from modules

Things can be imported from modules to become part of the current module

``` python
{{d['session01/python/modules.py|idio|pycon']['ImportFrom']}}
```

## Import and rename

You can rename things as you import them to avoid clashes or for convenience

``` python
{{d['session01/python/modules.py|idio|pycon']['ImportAlias']}}
```

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

```python
{{d['session01/python/modules.py|idio|pycon']['FolderModules']}}
```

`module1/__init__.py`:

```python
{{d['session01/python/module1/__init__.py|idio|t']}}
```

`module1/module2.py`:

```python
{{d['session01/python/module1/module2.py|idio|t']}}
```

## Relative Import

Inside packages, you can use `..` to refer to the parent module

`module1/module3/__init__.py`:

```python
{{d['session01/python/module1/module3/__init__.py|idio|t']}}
```

```python
{{d['session01/python/modules.py|idio|pycon']['RelativeImport']}}
```
