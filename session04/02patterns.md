---
title: Patterns
---

Class Complexity
----------------

We've seen that using object orientation can produce quite complex class structures, with classes owning each other, instantiating each other,
and inheriting from each other.

There are lots of different ways to design things, and decisions to make.

> Should I inherit from this class, or own it as a member variable? ("is a" vs "has a")

Design Patterns
---------------

Programmers have noticed that there are certain ways of arranging classes that work better than others.

These are called "design patterns".

They were first collected on one of the [world's first Wikis](http://c2.com/cgi/wiki?WelcomeVisitors), 
as the [Portland Pattern Repository](http://c2.com/cgi-bin/wiki?PatternIndex)

Reading a pattern
-----------------

A description of a pattern in a book such as the [Gang Of Four](http://www.amazon.co.uk/Design-patterns-elements-reusable-object-oriented/dp/0201633612)
book usually includes:

* Intent
* Motivation
* Applicability
* Structure
* Participants
* Collaborations
* Consequences
* Implementation
* Sample Code

Introducing Some Patterns
-------------------------

There are lots and lots of design patterns, and it's a great literature to get into to
read about design questions in programming and learn from other people's experience.

We'll just show a few in this session:

* Factory Method
* Builder
* Handle-Body
* Strategy


Factory Method
--------------

Here's what the Gang of Four Book says about Factory Method:

Intent:  Define an interface for creating an object, but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

Applicability: Use the Factory method pattern when:

* A class can't anticipate the class of objects it must create
* A class wants its subclasses to specify the objects it creates

Factory UML
-----------

![Structure](http://yuml.me/diagram/scruffy/class/%5BProduct%5D%5E-%5BConcreteProduct%5D,%20%5BCreator|%20%28v%29%20FactoryMethod%28%29%5D%5E-%5BConcreteCreator|%20FactoryMethod%28%29%5D,%20%5BConcreteCreator%5D-.-%3E%5BConcreteProduct%5D/)

Factory Sample Code
-------------------

```cpp
Product * Creator::Create (ProductId id) {
    if (id == MINE) return new MyProduct;
    if (id == YOURS) return new YourProduct;
    // repeat for remaining products
    return 0;
}
```

Antipattern
-----------

I personally have got into a terrible tangle trying to make base classes which somehow
"promote" themselves into a derived class based on some code in the base class.

This is an example of an "Antipattern": like a Smell, this is a recognised Wrong Way
of doing things. 

What I should have written was a Creator with a FactoryMethod.

Builder
-------

Intent: Separate the steps for constructing of a complex object from its final representation.

```cpp
Maze * MazeGame::CreateMaze (MazeBuilder& builder){
    builder.BuildMaze();
    builder.BuildRoom(1);
    builder.BuildRoom(2);
    builder.BuildDoor(1,2);
    return builder.GetMaze();
}
```

Polymorphism is used, so that `CreateMaze` can create a maze using Ascii graphics,
OpenGL, or a 3d printer, depending on the builder it is given.

Builder UML
-----------

![UML](http://yuml.me/diagram/scruffy/class/%5BDirector|Construct%28%29%5D%3C%3E-%3E%5BBuilder|%20%28a%29%20BuildPart%28%29%5D,%20%5BBuilder%5D%5E-%5BConcreteBuilder|%20BuildPart%28%29;GetResult%28%29%20%5D,%5BConcreteBuilder%5D-.-%3E%5BProduct%5D/)

Builder Message Sequence
------------------------

![MessageSequence](http://www.websequencediagrams.com/cgi-bin/cdraw?lz=CnBhcnRpY2lwYW50IENsaWVudAAGDURpcmVjdG9yABoOb25jcmV0ZUJ1aWxkZXIKADIGLT4ACQ86IG5ldwAUCQBCCAARBSgANA8pCgBhCAAzEwBiBUZpcnN0UGFydAAJIVNlY29uZAAGJVRoaXIAJAYAgSoZR2V0UmVzdWx0Cg&s=rose&h=lrr6P4-8b14Xsl0t)

Fast Arrays
-----------

Object oriented programming works best using *Arrays Of Structures*:

```cpp
class Boid {
    int x;
    int y;
    int xv;
    int yv;
    void go_right(){x+=1;}
}
std::vector<Boid> boids(100);
```

numerical code is sometimes faster with raw structures of arrays:

```cpp
struct boids{
    int xs[100];
    int ys[100];
    int xvs[100];
    int yvs[100];
}
```

How can we do object oriented programming, and still get maximum HPC performance?

HandleBody Pattern
-----------------

``` cpp
class Boid{
    static boids & data;
    int handle;
    void go_right(){data.xs[handle]+=1;}
}
```

With this approach, code can often make use of memory locality, while still writing
object-oriented looking client code.

Strategy
--------

Define a family of algorithms, encapsulate each one, and make them interchangeable. 
Strategy lets the algorithm vary independently from clients that use it.

For example, we pass a `MatrixOperations` object to a complex numerical method. The method delegates
all it's linear algebra needs to the strategy, allowing the strategy to change without the
method changing.

``` cpp
class WeatherSimulation{
    WeatherSimulation(FourierTransformStrategy &, LinearAlgebraStrategy &);

    DoSimulation(){
        fourier_strategy.transform(something);
        ...
        la_strategy.inverse_matrix(something_else);
    }
};

mySimulation=new WeatherSimulation(new FFTW(), new BLAS());
```
