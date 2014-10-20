---
title: Control and flow
---

# Control and flow

## If, Elif, Else

Python's if statement has optional if and elif clauses.
Use of elif means there is no separate `case` statement.

{{ pyfrag('flow','If') }}

## Comparison

`True` and `False` are used to represent **boolean** values.
Comparison on strings is alphabetical.

{{ pyfrag('flow','Comparison') }}

## Indentation

In Python, indentation is semantically significant.
You can choose how much indentation to use, so long as you
are consistent, but four spaces is
conventional. Please do not use tabs.

{{ pyfrag('flow','Indentation') }}

## Pass

A statement expecting identation must have some indented code.
This can be annoying when commenting things out. (With `#`)

{{ pyfrag('flow','EmptyIndent') }}

So the `pass` statement is used to do nothing.

{{ pyfrag('flow','Pass') }}


## Iteration

Use `for` ... `in` to iterate over **iterables**:

{{ pyfrag('flow','Iteration') }}

## Iterables

Any sequence type is iterable:

{{ pyfrag('flow','Sequence') }}

## Dictionaries are Iterables

All sequences are iterables. Some iterables are not sequences,
including sets and dictionaries.

{{ pyfrag('flow','DictionaryIteration') }}

## Unpacking and Iteration

Unpacking can be useful with iteration:

{{ pyfrag('flow','UnpackingIteration') }}

for example, to iterate over the items in a dictionary as pairs:

{{ pyfrag('flow','Items') }}

## Break, Continue

* Continue skips to the next turn of a loop
* Break stops the loop early

{{ pyfrag('flow','Break') }}

## Break, Continue and Else

* An else clause on a loop is executed iff the end of the loop is reached 

{{ pyfrag('flow','ForElse') }}

## List and Dictionary Comprehensions

If you write a for loop inside a list or dict constructor, you magic up a list.
This can make for concise but hard to read code, so be careful.

{{ pyfrag('flow','Comprehensions') }}

## Zip and dictionary construction

You can use "zip" to zip two iterables together.
An iterable of pairs can be used to construct a dictionary

{{ pyfrag('flow','Zip') }}


