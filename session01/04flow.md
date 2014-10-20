---
title: Control and flow
---

# Control and flow

## If, Elif, Else

Python's if statement has optional if and elif clauses.
Use of elif means there is no separate `case` statement.

``` python
{{d['session01/python/flow.py|idio|pycon']['If']}}
```

## Comparison

`True` and `False` are used to represent **boolean** values.
Comparison on strings is alphabetical.

``` python
{{d['session01/python/flow.py|idio|pycon']['Comparison']}}
```

## Indentation

In Python, indentation is semantically significant.
You can choose how much indentation to use, so long as you
are consistent, but four spaces is
conventional. Please do not use tabs.

``` python
{{d['session01/python/flow.py|idio|pycon']['Indentation']}}
```

## Pass

A statement expecting identation must have some indented code.
This can be annoying when commenting things out. (With `#`)

``` python
{{d['session01/python/flow.py|idio|pycon']['EmptyIndent']}}
```

So the `pass` statement is used to do nothing.

``` python
{{d['session01/python/flow.py|idio|pycon']['Pass']}}
```


## Iteration

Use `for` ... `in` to iterate over **iterables**:

``` python
{{d['session01/python/flow.py|idio|pycon']['Iteration']}}
```

## Iterables

Any sequence type is iterable:

``` python
{{d['session01/python/flow.py|idio|pycon']['Sequence']}}
```

## Dictionaries are Iterables

All sequences are iterables. Some iterables are not sequences,
including sets and dictionaries.

``` python
{{d['session01/python/flow.py|idio|pycon']['DictionaryIteration']}}
```

## Unpacking and Iteration

Unpacking can be useful with iteration:

``` python
{{d['session01/python/flow.py|idio|pycon']['UnpackingIteration']}}
```

for example, to iterate over the items in a dictionary as pairs:

``` python
{{d['session01/python/flow.py|idio|pycon']['Items']}}
```

## Break, Continue

* Continue skips to the next turn of a loop
* Break stops the loop early

``` python
{{d['session01/python/flow.py|idio|pycon']['Break']}}
```

## Break, Continue and Else

* An else clause on a loop is executed iff the end of the loop is reached 

``` python
{{d['session01/python/flow.py|idio|pycon']['ForElse']}}
```

## List and Dictionary Comprehensions

If you write a for loop inside a list or dict constructor, you magic up a list.
This can make for concise but hard to read code, so be careful.

``` python
{{d['session01/python/flow.py|idio|pycon']['Comprehensions']}}
```

## Zip and dictionary construction

You can use "zip" to zip two iterables together.
An iterable of pairs can be used to construct a dictionary

``` python
{{d['session01/python/flow.py|idio|pycon']['Zip']}}
```


