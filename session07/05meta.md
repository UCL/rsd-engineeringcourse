---
title: Metaprogramming
---

## Metaprogramming class attributes

In our introductory metaprogramming example, we were working in the root namespace of a module, using the globals() function.

We want to be able to access the attribute dictionary for other objects to do
metaprogramming to, for example, programmatically create class member data or
variables.

{{pyfrag('07','all','getattr')}}

The real power of accessing the attribute dictionary comes when we realise that
there is *very little difference* between member data and member functions.
Now that we know, from our functional programming, that a function is just a
variable that can be *called* with `()`, we can set an attribute to a function,
and
it becomes a member function!

{{pyfrag('07','all','metamember')}}

Note that we set this as an attribute of the class, so it is available to other instances of `Boring`:

{{pyfrag('07','all','modclass')}}
{{pyfrag('07','all','newclassmethod')}}

We can access the attribute dictionary for the local namespace inside a
function with locals() but this *cannot safely be written to*. Lack of safe
programmatic creation of local variables is a flaw in Python.

{{pyfrag('07','all','locals')}}
{{pyfrag('07','all','574')}}
{{pyfrag('07','all','575')}}

## Metaprogramming warning!

Use this stuff **sparingly**!

The above example worked, but it produced Python code which is not particularly understandable.
Remember, your objective when programming is to produce code which is **descriptive of what it does**.

The above code is **definitely** less readable, less maintainable and more error prone than:

{{pyfrag('07','all','dontMP')}}

Sometimes, metaprogramming will be **really** helpful in making non-repetitive
code, and you should have it in your toolbox, which is why I'm teaching you it.
But doing it all the time overcomplicated matters. We've talked a lot about the
DRY principle, but there is another equally important principle:

> **KISS**: *Keep it simple, Stupid!*

Whenever you write code and you think, "Gosh, I'm really clever",you're
probably *doing it wrong*. Code should be about clarity, not showing off.
