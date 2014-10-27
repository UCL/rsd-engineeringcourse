---
title: Structures and Types
---


## Data in Python

### Floats and integers

Python has two core numeric types:
{{ pyfrag('01','structures','Numerical') }}

### Strings

Python has a built in `string` type, supporting many
useful operations.

{{ pyfrag('01','structures','String') }}

### Coersion

The name of a type can be used to convert between types:

{{ pyfrag('01','structures','Coersion') }}

### Arrays

Python's basic **container** type is the `array`

{{ pyfrag('01','structures','Array') }}

### Sequences

Many things can be treated like arrays, supporting slicing,
a `len` operator and so on:

{{ pyfrag('01','structures','Sequence') }}

### Unpacking

Sequences can be **unpacked** from sequences:

{{ pyfrag('01','structures','Unpacking') }}

### Concepts and Duck Typing

We call the set of things that behave like arrays from the point of
view of slicing "sequences". 

This is an example of "Duck Typing": anything that behaves like a
sequence can be used as a sequence.

> If it looks like a duck, and it quacks like a duck, then
> it must be a duck

### Mutability

An array can be modified:

{{ pyfrag('01','structures','Mutable') }}

### Tuples
A `tuple` is an immutable sequence:

{{ pyfrag('01','structures','Tuple', check_errors=False) }}

`str`, `int` and `float` are all immutable too.

### Identity vs Equality

Having the same data is different from being the same actual object
in memory:

{{ pyfrag('01','structures','Equality') }}

### Memory and containers

The way memory works with containers can be important:

{{ pyfrag('01','structures','Memory') }}

### Dictionaries

Python supports an "associative array":

{{ pyfrag('01','structures','Sequence') }}

### Immutable Keys Only

The way in which dictionaries work is one of the coolest things in computer science:
the "hash table". We'll look more into this later, but the consequence of this is
that things would totally break of you changed a key in a dictionary.

So, you can only use **immutable** things as keys.

{{ pyfrag('01','structures','ImmutableKeys', check_errors=False) }}

### No guarantee of order

Another consequence of the way dictionaries work is that there's no guaranteed order among the
elements:

{{ pyfrag('01','structures','Unordered') }}

### Sets

A set works like a dictionary, but with just keys.

There's no guaranteed order, elements cannot occur twice.

{{ pyfrag('01','structures','Set') }}
