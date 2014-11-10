---
title: Introduction
---

## Introduction

Code can often be annoyingly full of "boiler-plate" code: characters you don't really want to have to type.

Not only is this tedious, it's also time-consuming and dangerous: unnecessary code is an unnecessary potential place for mistakes.

There are two important phrases in software design that we've spoken of before in this context:

> Once And Only Once

> Don't Repeat Yourself (DRY)

All concepts, ideas, or instructions should be in the program in just one place.
Every line in the program should say something useful and important.

We refer to code that respects this principle as DRY code.

In this lecture, we'll look at some techniques that can enable us to refactor away repetitive code.

Since in many of these places, the techniques will involve working with
functions as if they were variables, we'll learn some **functional**
programming. We'll also learn more about the innards of how Python implements
classes.

We'll also think about how to write programs that *generate* the more verbose, repetitive program we could otherwise write.
We call this **metaprogramming**.

Before we start on the details, we'll introduce a few examples.

Consider a bunch of variables, each of which need initialising and incrementing:

{{pyfrag('07','all','variables')}}
The right hand side of these assignments doesn't respect the DRY principle. We
could of course define a variable for our initial value:

{{pyfrag('07','all','constant')}}
However, this is still not as DRY as it could be: what if we wanted to replace
the assignment with, say, a class constructor and a buy operation:

{{pyfrag('07','all','toclass')}}
We had to make the change in three places. Whenever you see a situation where a
refactoring or change of design might require you to change the code in
multiple places, you have an opportunity to make the code DRYer.

In this case, metaprogramming for incrementing these variables would involve
just a loop over all the variables we want to initialise:

{{pyfrag('07','all','loop')}}
However, this trick **doesn't** work for initialising a new variable:

{{pyfrag('07','all','newerror', exec=False)}}
So can we declare a new variable programmatically? Given a list of the
**names** of fruit baskets we want, initialise a variable with that name?

{{pyfrag('07','all','names')}}

Wow, we can! Every module or class in Python, is, under the hood, a special
dictionary, storing the values in its **namespace**. So we can create new
variables by assigning to this dictionary. globals() gives a reference to the
attribute dictionary for the current module

{{pyfrag('07','all','globals')}}
This is **metaprogramming**.

I would NOT recommend using it for an example as trivial as the one above. 
A better, more Pythonic choice here would be to use a data structure to manage your set of fruit baskets:

{{pyfrag('07','all','dictionary')}}
Or even, using a dictionary comprehension:

{{pyfrag('07','all','comprehension')}}
Which is the nicest way to do this, I think. Code which feels like
metaprogramming is needed to make it less repetitive can often instead be DRYed
up using a refactored data structure, in a way which is cleaner and more easy
to understand. Nevertheless, metaprogramming is worth knowing. 

## Functional Programming

Understanding to think in a *functional programming* style is almost as
important as object orientation for building DRY, clear scientific software,
and is just as conceptually difficult.

Programs are composed of functions: they take data in (which we call
*parameters* or *arguments*) and send data out (through `return` statements.)

A conceptual trick which is often used by computer scientists to teach the core
idea of functional programming is this: to write a program,
in theory, you only ever need functions with **one** argument, even when you think you need two or more. Why?

Let's define a program to add two numbers:

{{pyfrag('07','all','add')}}
How can we do this, in a version which only defined functions of one argument?
In order to understand this, we'll have to understand several of the concepts
of functional programming. Let's start with a program which just adds five to
something:

{{pyfrag('07','all','addfive')}}
OK, we could define lots of these, one for each number we want to add. But that
would be infinitely repetitive. So, let's try to metaprogram that: we want a
function which returns these add_N() functions.

Let's start with the easy case: a function which returns a function which adds 5 to something:

{{pyfrag('07','all','funcgen')}}
OK, so what happened there? Well, we defined a function **inside** the other function. We can always do that:

{{pyfrag('07','all','thirty')}}
When we do this, the functions enclosed inside the outer function are **local** functions, and can't be seen outside:

{{pyfrag('07','all','scope')}}
There's not really much of a difference between functions and other variables
in python. A function is just a variable which can have () put after it to call
the code!

{{pyfrag('07','all','call')}}
And we know that one of the things we can do with a variable is `return` it. So we can return a function, and then call it outside:

{{pyfrag('07','all','deferred')}}

So now, to finish this, we just need to return a function to add an arbitrary amount:

{{pyfrag('07','all','curry')}}
We can make this even prettier: let's make another variable pointing to our define_adder() function:

{{pyfrag('07','all','rename')}}
And now we can do the real magic:

{{pyfrag('07','all','currying')}}
You may have noticed something a bit weird:

In the definition of `define_adder`, `increment` is a local variable. It should have gone out of scope and died at the end of the definition. How can the amount the returned adder function is adding still be kept?

This is called a **closure**. In Python, whenever a function definition references a variable in the surrounding scope, it is preserved within the function definition.

You can close over global module variables as well:

{{pyfrag('07','all','closure')}}
And note that the closure stores a reference to the variable in the surrounding scope: ("Late Binding")

{{pyfrag('07','all','late')}}
We often want to apply a function to each variable in an array, to return a new array. We can do this with a list comprehension:

{{pyfrag('07','all','comprehension')}}
But this is sufficiently common that there's a quick built-in:

{{pyfrag('07','all','map')}}
This **map** operation is really important conceptually when understanding
efficient parallel programming: different computers can apply the *mapped*
function to their input at the same time. We call this Single Program, Multiple
Data. (SPMD) **map** is half of the **map-reduce** functional programming
paradigm which is key to the efficient operation of much of today's "data
science" explosion. 

Let's continue our functional programming mind-stretch by looking at **reduce** operations.

We very often want to loop with some kind of accumulator, such as when finding a mean, or finding a maximum:

{{pyfrag('07','all','accumulate')}}
These operations, where we have some variable which is building up a result,
and the result is updated with some operation, can be gathered together as a
functional program, taking in the operation to be used to combine results as an
argument:

{{pyfrag('07','all','accum_generalise')}}
Now, because these operations, _bigger, and _add, are such that e.g. (a+b)+c = a+(b+c) , i.e. they are **associative**, we could apply our accumulation
to the left half and the right half of the array, each on a different computer, and then combine the two halves:

1+2+3+4=(1+2)+(3+4)

Indeed, with a bigger array, we can divide-and-conquer more times:

1+2+3+4+5+6+7+8=((1+2)+(3+4))+((5+6)+(7+8))

So with enough parallel computers, we could do this operation on eight numbers
in three steps: first, we use four computers to do one  each of the pairwise
adds.

Then, we use two computers to add the four totals.

Then, we use one of the computers to do the final add of the two last numbers.

You might be able to do the maths to see that with an N element list, the
number of such steps is proportional to the logarithm of N.

We say that with enough computers, reduction operations are O(ln N)

This course isn't an introduction to algorithms, but we'll talk more about this
O() notation when we think about programming for performance.

Anyway, this accumulate-under-an-operation process, is so fundamental to
computing that it's usually in standard libraries for languages which allow
functional programming:

{{pyfrag('07','all','reduce')}}
When doing functional programming, we often want to be able to define a function on the fly:

{{pyfrag('07','all','lambda')}}
The syntax here is that these two definitions are identical:

{{pyfrag('07','all','lambda_same')}}

lambda defines an "anonymous" function.

{{pyfrag('07','all','lambda_closure')}}
The above fragment defined a lambda function as a **closure** over `base`. If you understood that, you've got it! 

{{pyfrag('07','all','pretty_max')}}

## Using functional programming

Probably the most common use in research computing for functional programming
is the application of a numerical method to a function. For example:
{% if notebook %}
```
% matplotlib inline
```
{% endif %}

{{pyfrag('07','all','funcalgo')}}

Sometimes such tools return another function:

{{pyfrag('07','all','derivative')}}

Of course, coding your own numerical methods is bad:

{{pyfrag('07','all','stdlib')}}
If you've done a moderate amount of calculus, then you'll find similarities
between functional programming in computer science and Functionals in the
calculus of variations.

## Iterators

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

{{pyfrag('07','all','iterable_protocol')}}

Technically, the **iterator** protocol is to implement both `__iter__` and
`next`, while the **iterable** protocol is to implement `__iter__` and return
an **iterator**.

## Generators

There's a fair amount of "boiler-plate" in the above class-based definition of
an iterable. Python provides another way to specify something
which meets the iterator protocol: generators.

{{pyfrag('07','all','generator')}}

A function which has `yield` statements instead of a `return` statement returns
**temporarily**. Each call of next() returns control to the function. Where it
left off. Control passes back-and-forth between the generator and the caller.
Our fibonnaci example therefore becomes:

{{pyfrag('07','all','fib_generator')}}

## Exceptions

When we learned about testing, we saw that Python complains when things go wrong by raising an "Exception" naming a type of error:

{{pyfrag('07','all','divzero', check_errors=False)}}
Exceptions are objects, forming a class hierarchy. We just raised an instance
of the ZeroDivisionError class, making the program crash.

{{pyfrag('07','all','hierarchy')}}
So we can see that a zero division error is a particular kind of Arithmetic Error.

{{pyfrag('07','all','typerror')}}

When we were looking at testing, we saw that it is important for code to crash with a meaningful exception type when something is wrong.
We raise an Exception with `raise`. Often, we can look for an appropriate exception from the standard set to raise. 

However, we may want to define our own exceptions. Doing this is as simple as inheriting from Exception:

{{pyfrag('07','all','custom')}}
You can add custom data to your exception:

{{pyfrag('07','all','customdata')}}
The real power of exceptions comes, however, not in letting them crash the program, but in letting your program handle them. We say that an exception has been "thrown" and then "caught".

{{pyfrag('07','all','handling')}}
Note that we specify only the error we expect to happen and want to handle. Sometimes you see code that catches everything:

{{pyfrag('07','all','omnicatch')}}
There was a mistyped function name there, but we did not notice the error, as the generic except caught it. 
Therefore, we should catch only the error we want.

{{pyfrag('07','all','threereads')}}

This last code has a flaw: the file was successfully opened, the missing key was noticed, but not explicitly closed. It's normally OK, as python will close the file as soon as it notices there are no longer any references to datasource in memory, after the function exits. But this is not good practice, you should keep a file handle for as short a time as possible.

{{pyfrag('07','all','finally')}}

The `finally` clause is executed whether or not an exception occurs.

The last optional clause of a `try` statement, an `else` clause is called only if an exception is NOT raised. It can be a better place than the `try` clause to put code other than that which you expect to raise the error, and which you do not want to be executed if the error is raised. It is executed in the same circumstances as code put in the end of the `try` block, the only difference is that errors raised during the `else` clause are not caught. Don't worry if this seems useless to you; most languages implementations of try/except don't support such a clause.

{{pyfrag('07','all','tryelse')}}
Exceptions do not have to be caught close to the part of the program calling
them. They can be caught anywhere "above" the calling point in
the call stack: control can jump arbitrarily far in the program: up to the `except` clause of the "highest" containing try statement.

{{pyfrag('07','all','stackexample')}}

## Design with Exceptions

Now we know how exceptions work, we need to think about the design implications... How best to use them.

Traditional software design theory will tell you that they should only be used
to describe and recover from **exceptional** conditions: things going wrong.
Normal program flow shouldn't use them.

Python's designers take a different view: use of exceptions in normal flow is
considered OK. For example, all iterators raise a `StopIteration` exception to
indicate the iteration is complete.

A commonly recommended python design pattern is to use exceptions to determine
whether an object implments a protocol (concept/interface), rather than testing
on type.

For example, we might want a function which can be supplied *either* a data
series *or* a path to a location on disk where data can be found. We can
examine the type of the supplied content:

{{pyfrag('07','all','typecheck')}}

However, we can also use the try-it-and-handle-exceptions approach to this. 

{{pyfrag('07','all','duckexception')}}

This approach is more extensible, and **behaves properly if we give it some
other data-source which responds like a dictionary or string.**

{{pyfrag('07','all','duckextension')}}

Sometimes we want to catch an error, partially handle it, perhaps add some
extra data to the exception, and then re-raise to be caught again further up
the call stack. 

The keyword "`raise`" with no argument in an `except:` clause will cause the
caught error to be re-thrown. Doing this is the only circumstance where it is
safe to do except: without catching a specfic type of error.

{{pyfrag('07','all','rethrow')}}
It can be useful to catch and re-throw an error as you go up the chain, doing any clean-up needed for each layer of a program.

The error will finally be caught and not re-thrown only at a higher program
layer that knows how to recover. This is known as the "throw low catch high"
principle.


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
## Exercise

Numbers have units. $5\mathrm{m}^2$ is not $5\mathrm{J}$. $6\mathrm{J}$ is the
same as $6\mathrm{kg}\mathrm{m}^2\mathrm{s}^{2}$ which is the same as
$2\mathrm{N} \cdot 3\mathrm{m}$

Write a python library to implement handling quantities with units, and
converting between units, with a github repostiory and a setup.py file, and
some unit tests.

You should define operators for multiply, equality, and add for your class.

Your unit tests should include things like:
``` raw
assert(5*meters == 0.005*kilometers)
assert((60*seconds).to(minutes).value==1)
assert((60*seconds).to(minutes).unit==minutes)
with assert_raises(IncompatibleUnitsError):
    5*meters+2*seconds
```
You don't have to implement every unit! You might want to load your unit definitions from a yaml config file.

