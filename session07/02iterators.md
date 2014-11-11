---
title: Iterators and Generators
---

## Iterators and Generators

### Iterators

We've seen that in Python, anything which can be iterated over is called an iterable:

{{pyfrag('07','all','iterable')}}
Surprisingly often, we want to iterate over something that takes a moderately
large amount of storage to store. For example, our map images in the
green-graph example.

Our solution last time involved making an array of all the maps between London
and Birmingham. This kept them all in memory *at the same time*: first we
downloaded all the maps, then we counted the green pixels in each of them. This
would NOT work if we used more points. We could do this with a for loop and an
append(), but that's not as elegant as using a **generator**

Consider the basic python `range` function:

{{pyfrag('07','all','range')}}
While this was executing, the range() statement allocated a million integers.
This is very inefficient. We don't actually need a million integers, just each
integer in turn up to a million.

{{pyfrag('07','all','xrange', check_errors=False)}}

Similarly:

{{pyfrag('07','all','iteritems')}}

We can make our own iterators by defining classes that implement next() and __iter__() methods: this is the iterator protocol.

For each of the concepts we've talked about, python defines a protocol, a set of methods a class must implement, in order to be treated as a member of that concept.

For the iterator protocol, the protocol that defines things that support `for x in y:`, the methods that must be supported are `next()` and `__iter__()`.

{{pyfrag('07','all','iterator_protocol')}}

In fact, if, to be iterated over, a class just wants to behave as if it were some other iterable, you can just implement `__iter__` and return `iter(some_other_iterable)`, without implementing `next`.  For example, an image class might want to implement some metadata, but behave just as if it were just a 1-d pixel array when being iterated:
{% if not notebook %}
![](session07/python/colors.png)
{% endif %}
{{pyfrag('07','all','iterable_protocol')}}

Technically, the **iterator** protocol is to implement both `__iter__` and
`next`, while the **iterable** protocol is to implement `__iter__` and return
an **iterator**.

### Generators

There's a fair amount of "boiler-plate" in the above class-based definition of
an iterable. Python provides another way to specify something
which meets the iterator protocol: generators.

{{pyfrag('07','all','generator')}}

A function which has `yield` statements instead of a `return` statement returns
**temporarily**. Each call of next() returns control to the function. Where it
left off. Control passes back-and-forth between the generator and the caller.
Our fibonacci example therefore becomes:

{{pyfrag('07','all','fib_generator')}}
{% if not notebook %}
![](session07/python/fibonacci.png)
{% endif %}

