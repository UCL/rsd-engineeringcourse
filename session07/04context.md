---
title: Context managers and decorators
---

## Context managers

We saw that instead of separately `open`ing and `close`ing a file, we can have
the file be automatically closed using a context manager:

{{pyfrag('07','all','context')}}

How could we define our own one of these, if we too have clean-up code we
always want to run after a calling function has done its work, or set-up code
we want to do first?

We can define a class that meets an appropriate protocol:

{{pyfrag('07','all','context_protocol')}}
However, this is pretty verbose! Again, a generator with `yield` makes for an easier syntax:

{{pyfrag('07','all','context_generator')}}
Again, we use `yield` to temporarily return from a function.

## Decorators

When doing functional programming, we may often want to define mutator
functions which take in one function and return a new function, such as our
derivative example earlier.

{{pyfrag('07','all','repeater')}}

It turns out that, quite often, we want to apply one of these to a function as we're defining a class.
For example, we may want to specify that after certain methods are called, data should always be stored:

{{pyfrag('07','all','reset_required')}}

Python provides some "syntactic sugar" to make this kind of coding prettier:

{{pyfrag('07','all','reset_decorator')}}

Any function which accepts a function as its first argument and returns a function can be used as a **decorator** like this.

Much of Python's standard functionality is implemented as decorators: we've
seen @contextmanager, @classmethod and @attribute. The @contextmanager
metafunction, for example, takes in an iterator, and yields a class conforming
to the context manager protocol.

## Testing and functional programming.

A few weeks ago we saw a test which loaded its test cases from a YAML file and
asserted each input with each output. This was nice and concise, but had one
flaw: we had just one test, covering all the fixtures, so we got just one . in
the test output when we ran the tests, and if any test failed, the rest were
not run. We can do a nicer job with a test **generator**:

{{pyfrag('07','all','test_generator')}}

We also remember seeing `with assert_raises()` used to do negative testing.

We can now imagine how this context manager might be implemented:

{{pyfrag('07','all','assertraises')}}
In fact, we can now use an even easier way to define negative tests: by using `@raises` as a **decorator**:

{{pyfrag('07','all','decorate_raises', check_errors=False)}}

Again, we can imagine how nose might implement this:

{{pyfrag('07','all','my_decorate_raises')}}
