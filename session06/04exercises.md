---
title: Exercises
---

##Exercises

###Refactoring to classes

Complete the exercise on Boids from last week, as far as creating a class for a Boid, if you haven't already.

###Refactoring to Inheritance and Polymorphism

In the Eagle branch in my Boids repository you will find an extension of Boids to support multiple kinds of Bird.
You will see that this suffers from the use of an `if (type)` statement which would be
better implemented with inheritance and polymorphism.

To access the Eagle branch:

``` bash
cd <repository>
git checkout eagle
```

###Refactoring to Patterns: Builder

The way in which we construct our Boids model's bird content, specifying each of the
model parameters as a constructor, and add birds using `initialise_random`
and `initialise_from_data` is rather clunky.

Create a `ModelBuilder` class with methods to define model parameters and to
add a random boid and boid or boids from data, using the Builder pattern.

You could even create two subclasses of `ModelBuilder` to build either random boids
or boids from a dataset.

###Refactoring to Patterns: Model/View

You can apply Model/View to create a separate class to visualise boid models using Matplotlib,
and even perhaps write another viewer to visualise the boids in a different way: perhaps as graphs over time
of dispersal, distance from flock to eagle and average velocity.

###Using UML

You should also use [YUML](http://yuml.me) or another UML tool to visualise your class structure.

You don't have to do all these things to pass the assignment: any minimally object-oriented implementation of the boids
will pass.


