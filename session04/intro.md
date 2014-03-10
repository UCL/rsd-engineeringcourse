Design
======

Design
------

In this session, we will finally discuss the thing most people think of when they refer to "Software Engineering": the deliberate *design* of software.
We will discuss processes and methodologies for planned development of large-scale software projects: *Software Architecture*.

Object-Oriented Design
----------------------

The software engineering community has, in large part, focused on an object-oriented approach to the design and development of large scale software systems.
The basic concepts of object orientation are necessary to follow much of the software engineering conversation. We will therefore recap some of these.

Design processes
----------------

In addition to object-oriented architecture, software engineers have focused on the development of processes for robust, reliable software development. 
These codified ways of working hope to enable organisations to repeatably and reliably complete complex software projects in a way that minimises both development 
and maintainance costs, and meets user requirements.

Design and research
-------------------

Software engineering theory has largely been developed in the context of commercial software companies.

The extent to which the practices and processes developed for commercial software are applicable in a research context is itself an active area of research.

Recap of Objects and Classes
===================

Classes
-----

Class: A user-defined type

```python
class MyClass(object):
    pass
```

```cpp
class MyClass {
}
```

Instances
---------

Instance: A particular object *instantiated* from a class.

``` python
my_object  =MyClass()
```

``` cpp
MyClass  my_object = MyClass();
MyClass* my_object = new MyClass();
```

Method
------

Method: A function which is "built in" to a class

``` python
class MyClass(object):
    def someMethod(self,argument):
        pass

my_object.someMethod(value)
```

```cpp
class MyClass {
    void someMethod(argument){
    }
}

my_object.someMethod(value);
```

Constructor
-----------

Constructor: A special method called when instantiating a new object

``` python
class MyClass(object):
    def __init__(self,argument):
        pass

my_object = MyClass(value)
```

``` cpp
class MyClass {
    MyClass(argument){
    }
}

MyClass my_object=MyClass(value);

```
Member Variable
---------------

Inheritance
===========


