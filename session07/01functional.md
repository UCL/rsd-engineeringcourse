---
title: Functional Programming
---
## Functional programming
### Functional Programming

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
How could we do this, in a fictional version of Python which only defined functions of one argument?
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
### Closures
You may have noticed something a bit weird:

In the definition of `define_adder`, `increment` is a local variable. It should have gone out of scope and died at the end of the definition. How can the amount the returned adder function is adding still be kept?

This is called a **closure**. In Python, whenever a function definition references a variable in the surrounding scope, it is preserved within the function definition.

You can close over global module variables as well:

{{pyfrag('07','all','closure')}}
And note that the closure stores a reference to the variable in the surrounding scope: ("Late Binding")

{{pyfrag('07','all','late')}}

### Map and Reduce
We often want to apply a function to each variable in an array, to return a new array. We can do this with a list comprehension:

{{pyfrag('07','all','comprehension2')}}
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

### Using functional programming

Probably the most common use in research computing for functional programming
is the application of a numerical method to a function. For example:
{% if notebook %}
```
% matplotlib inline
```
{% endif %}

{{pyfrag('07','all','funcalgo')}}
{% if not notebook %}
![](session07/python/solved.png)
{% endif %}
Sometimes such tools return another function:

{{pyfrag('07','all','derivative')}}
{% if not notebook %}
![](session07/python/derived.png)
{% endif %}

Of course, coding your own numerical methods is bad:

{{pyfrag('07','all','stdlib')}}
If you've done a moderate amount of calculus, then you'll find similarities
between functional programming in computer science and Functionals in the
calculus of variations.
