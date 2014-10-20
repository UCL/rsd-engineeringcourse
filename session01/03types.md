---
title: Structures and Types
---

# Data in Python

## Floats and integers

Python has two core numeric types:

``` python
{{d['session01/python/structures.py|idio|pycon']["Numerical"]}}
```

## Strings

Python has a built in `string` type, supporting many
useful operations.

``` python
{{d['session01/python/structures.py|idio|pycon']["String"]}}
```

## Coersion

The name of a type can be used to convert between types:

``` python
{{d['session01/python/structures.py|idio|pycon']["Coersion"]}}
```

## Arrays

Python's basic **container** type is the `array`

``` python
{{d['session01/python/structures.py|idio|pycon']["Array"]}}
```

## Sequences

Many things can be treated like arrays, supporting slicing,
a `len` operator and so on:

``` python
{{d['session01/python/structures.py|idio|pycon']["Sequence"]}}
```

## Unpacking

Sequences can be **unpacked** from sequences:

``` python
{{d['session01/python/structures.py|idio|pycon']["Unpacking"]}}
```

## Concepts and Duck Typing

We call the set of things that behave like arrays from the point of
view of slicing "sequences". 

This is an example of "Duck Typing": anything that behaves like a
sequence can be used as a sequence.

> If it looks like a duck, and it quacks like a duck, then
> it must be a duck

## Mutability

An array can be modified:

``` python
{{d['session01/python/structures.py|idio|pycon']["Mutable"]}}
```

## Tuples

A `tuple` is an immutable sequence:

``` python
{{d['session01/python/structures.py|idio|pycon']["Tuple"]}}
```

`str`, `int` and `float` are all immutable too.

## Identity vs Equality

Having the same data is different from being the same actual object
in memory:

``` python
{{d['session01/python/structures.py|idio|pycon']["Equality"]}}
```

## Memory and containers

The way memory works with containers can be important:

``` python
{{d['session01/python/structures.py|idio|pycon']["Memory"]}}
```

## Dictionaries

Python supports an "associative array":

``` python
{{d['session01/python/structures.py|idio|pycon']["Dictionary"]}}
```

## Immutable Keys Only

The way in which dictionaries work is one of the coolest things in computer science:
the "hash table". We'll look more into this later, but the consequence of this is
that things would totally break if you changed a key in a dictionary.

So, you can only use **immutable** things as keys.

``` python
{{d['session01/python/structures.py|idio|pycon']["ImmutableKeys"]}}
```

## No guarantee of order

Another consequence of the way dictionaries work is that there's no guaranteed order among the
elements:

``` python
{{d['session01/python/structures.py|idio|pycon']["Unordered"]}}
```

## Sets

A set works like a dictionary, but with just keys.

There's no guaranteed order, elements cannot occur twice.

``` python
{{d['session01/python/structures.py|idio|pycon']["Set"]}}
```
