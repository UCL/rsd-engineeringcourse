---
title: Operator Overloading
---
{% if not notebook %}
## Operator overloading

Imagine we wanted to make a library to describe some kind of symbolic algebra system:

{{pyfrag('07','all','algebra1')}}

So that $5x^2y+7x+2$ might be constructed as:

{{pyfrag('07','all','algebra2')}}

This is pretty cumbersome.

What we'd really like is to have `2x+y` give an appropriate expression.

First, we'll define things so that we can construct our terms and expressions in different ways.

{{pyfrag{'07','all','Polyconstruct'}}}
{{pyfrag{'07','all','ExpressionConstruct'}}}

We could define add() and multiply() operations on expressions and terms:

{{pyfrag('07','all','OperatorFunctions')}}
{{pyfrag('07','all','ExpressionFunctions')}}

We can now construct the above expression as:

{{pyfrag('07','all','withfunc')}}

This is better, but we still can't write the expression in a 'natural' way.

However, we can define what `*` and `+` do when applied to Terms!:

{{pyfrag('07','all','withop')}}

This is called operator overloading. We can define what add and multiply mean when applied to our class.

Note that this only works so far if we multiply on the right-hand-side!
However, we can define a multiplication that works backwards, which is used as a fallback if the left multiply raises an error:

{{pyfrag('07','all','RightOp')}}

{{pyfrag('07','all','RightUse')}}

It's not easy at the moment to see if these things are working!

{{pyfrag('07','all','HardTest')}}

We can add another operator method `__str__`, which defines what happens if we try to print our class:

{{pyfrag('07','all','StringOverload')}}
{{pyfrag('07','all','ExpressionStringOverload')}}
{{pyfrag('07','all','UseString')}}

We can add lots more operators to classes. `__eq__` to determine if objects are
equal. `__getitem__` to apply [1] to your object. Probably the most exciting
one is `__call__`, which allows us to define other classes that *behave like
functions*! We call these callables.

{{pyfrag('07','all','Callable')}}

We've now come full circle in the blurring of the distinction between functions and objects! The full power of functional programming is really remarkable.

If you want to know more about the topics in this lecture, using a different
language syntax, I recommend you watch the [Abelson and Sussman](https://www.youtube.com/watch?v=2Op3QLzMgSY)
"Structure and Interpretation of Computer Programs" lectures. These are the Computer Science
equivalent of the Feynman Lectures!
{% endif %}
