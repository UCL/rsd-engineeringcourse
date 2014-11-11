---
title: DRY Programming Tricks
---

## Introduction

### Avoid Boiler-Plate

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

### Metaprogramming Example

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

{{pyfrag('07','all','newerror')}}
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

### Notebook

This lecture is available as an [IPython Notebook](http://nbviewer.ipython.org/url/development.rc.ucl.ac.uk/training/engineering/session07/session07/python/session07.ipynb)
