---
title: Functions
---

## Functions 

### Definition

We use `def` to define a function, and `return` to return a value from the function:

{{ pyfrag('01','functions','Function') }}

### Side effects

Functions can do things to change **mutable** arguments,
so `return` is optional:

{{ pyfrag('01','functions','SideEffect') }}

### Early return

We can exit early from a function with `return`:

{{ pyfrag('01','functions','EarlyReturn') }}

### Unpacking arguments

If a vector is supplied to a function with a '*', its elements
are used to fill each of a function's arguments:

{{ pyfrag('01','functions','UnpackingArguments') }}

This can be quite powerful:

{{ pyfrag('01','functions','UnpackingPower') }}

### Sequence arguments

Similarly, if a `*` is used in the definition of a function, multiple
arguments are absorbed into a tuple:

{{ pyfrag('01','functions','SequenceArguments') }}

### Keyword arguments

If two asterisks are used, named arguments are supplied as a dictionary:

{{ pyfrag('01','functions','KeywordArguments') }}
