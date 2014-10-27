---
title: Refactoring
---

##Refactoring

###Refactoring

To refactor is to:

* Make a change to the design of some software
* Which improves the structure or readability
* But which leaves the actual behaviour of the program completely unchanged.


###A word from the Master

> Refactoring is a controlled technique for improving the design of an existing code base. 
Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". 
However the cumulative effect of each of these transformations is quite significant. 
By doing them in small steps you reduce the risk of introducing errors. 
You also avoid having the system broken while you are carrying out the restructuring - 
which allows you to gradually refactor a system over an extended period of time.

-- Martin Fowler

###List of known refactorings

The next few sections will present some known refactorings

We'll show before and after code, present any new coding techniques needed to do the refactoring,
and describe *code smells*: how you know you need to refactor.

###Replace magic numbers with constants

Smell: Raw numbers appear in your code

Before

{{pyfrag('05','refactoring','magic_before')}}

after:

{{pyfrag('05','refactoring','magic_after')}}

###Replace repeated code with a function

Smell: Fragments of repeated code appear

Before:

{{pyfrag('05','refactoring','function_before')}}

After:

{{pyfrag('05','refactoring','function_after')}}

###Change of variable name

Smell: Code needs a comment to explain what it is for

Before:

{{pyfrag('05','refactoring','names_before')}}

After:

{{pyfrag('05','refactoring','names_after')}}


###Separate a complex expression into a local variable

Smell: An expression becomes long

{{pyfrag('05','refactoring','temporary_before')}}

vs

{{pyfrag('05','refactoring','temporary_after')}}

###Replace loop with iterator

Smell: Loop variable is an integer from 1 to something

Before:

{{pyfrag('05','refactoring','iterator_before')}}

After:

{{pyfrag('05','refactoring','iterator_after')}}

###Replace hand-written code with library code

Smell: It feels like surely someone else must have done this at some point

Before:

{{pyfrag('05','refactoring','library_before')}}

After:

{{pyfrag('05','refactoring','library_after')}}

See [Numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html),
    [Pandas](http://pandas.pydata.org/)

###Replace set of arrays with array of structures

Smell: A function needs to work corresponding indices of several arrays:

Before:

{{pyfrag('05','refactoring','arrays')}}

After:

{{pyfrag('05','refactoring','structures')}}

Warning: this refactoring greatly improves readability but can make code slower,
depending on memory layout. Be careful.

###Replace constants with a configuration file

Smell: You need to change your code file to explore different research scenarios

Before:

{{pyfrag('05','refactoring','config_before')}}

After:

{{notebookfile('05','config.yaml')}}

{{pyfrag('05','refactoring','config_after')}}

See [YAML](http://www.yaml.org/) and [PyYaml](http://pyyaml.org/)
and [Python OS](http://docs.python.org/2/library/os.html)

###Replace global variables with function arguments

Smell: A global variable is assigned and then used inside a called function:

{{pyfrag('05','refactoring','globals')}}

Becomes:

{{pyfrag('05','refactoring','arguments')}}

###Merge neighbouring loops

Smell: Two neighbouring loops have the same for statement

{{pyfrag('05','refactoring','loops')}}

Becomes:

{{pyfrag('05','refactoring','merged')}}


###Break a large function into smaller units

Smell: A function or subroutine no longer fits on a page in your editor
Smell: A line of code is indented more than three levels
Smell: A piece of code interacts with the surrounding code through just a few variables

Before:

{{pyfrag('05','refactoring','subroutine_before')}}

After:

{{pyfrag('05','refactoring','subroutine_after')}}

###Separate code concepts into files or modules

Smell: You find it hard to locate a piece of code

Smell: You get a lot of version control conflicts

Before:

{{pyfrag('05','refactoring','files_before')}}

After:

{{pyfrag('05','refactoring','files_after')}}

###Refactoring is a safe way to improve code

You may think you can see how to rewrite a whole codebase to be better

However, you may well get lost halfway through the exercise.

By making the changes as small, reversible, incremental steps,
you can reach your target design more reliably.

###Tests and Refactoring

Badly structured code cannot be unit tested. There are no "units".

Before refactoring, ensure you have a robust regression test.

This will allow you to *Refactor with confidence*

As you refactor, if you create any new units (functions, modules, classes),
add new tests for them.

###Refactoring Summary

* Replace magic numbers with constants
* Replace repeated code with a function
* Change of variable/function/class name
* Replace loop with iterator
* Replace hand-written code with library code
* Replace set of arrays with array of structures
* Replace constants with a configuration file
* Replace global variables with function arguments
* Break a large function into smaller units
* Separate code concepts into files or modules

And many more

Read [The Refactoring Book](http://www.amazon.co.uk/Refactoring-Improving-Design-Existing-Technology/dp/0201485672)

