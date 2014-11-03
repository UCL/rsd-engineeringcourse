---
title: Objects
---

##Introduction to Objects


###Classes: User defined types

{{pyfrag('05','objects','intro')}}


###Declaring a class 

Class: A user-defined type

{{pyfrag('05','objects','declare')}}

###Object instances

Instance: A particular object *instantiated* from a class.

{{pyfrag('05','objects','instance')}}

###Method

Method: A function which is "built in" to a class

{{pyfrag('05','objects','method')}}

###Constructor

Constructor: A special method called when instantiating a new object

{{pyfrag('05','objects','constructor')}}

###Member Variable

Member variable: a value stored inside an instance of a class.

{{pyfrag('05','objects','member')}}


##Object refactorings

###Replace add-hoc structure with user defined classes

Smell: A data structure made of nested arrays and dictionaries becomes unwieldy

Before:

{{pyfrag('05','objects','structure_before')}}

After:

{{pyfrag('05','objects','structure_after')}}

###Replace function with a method

Smell: A function is always called with the same kind of thing

Before:

{{pyfrag('05','objects','method_before')}}

After:

{{pyfrag('05','objects','method_after')}}


###Replace method arguments with class members

Smell: A variable is nearly always used in arguments to 
a class.

{{pyfrag('05','objects','member_before')}}

After:

{{pyfrag('05','objects','member_after')}}

### Replace global variable with class and member

Smell: A global variable is referenced by a few functions

{{pyfrag('05','objects','global_before')}}

{{pyfrag('05','objects','global_after')}}

###Object Oriented Refactoring Summary

* Replace ad-hoc structure with a class
* Replace function with a method
* Replace method argument with class member
* Replace global variable with class data

