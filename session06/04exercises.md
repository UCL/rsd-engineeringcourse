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

To get hold of my Eagle code, you should either add my repository as a second remote and pull from there,
or make a pull request into your fork of boids from my repository and then pull from your own repository.

To add my repository as a second remote:

``` bash
git remote add jamespjh https://github.com/jamespjh/bad-boids
git fetch jamespjh
git checkout -b eagle
git merge jamespjh/eagle
git push -u origin eagle
```  

###Refactoring to Patterns

The way in which we construct our Boids model's bird content, specifying each of the
model parameters as a constructor, and add birds using `initialise_random`
and `initialise_from_data` is rather clunky.

Create a `ModelBuilder` class with methods to define model parameters and to
add a random boid and boid or boids from data, using the Builder pattern.

You could even create two subclasses of `ModelBuilder` to build either random boids
or boids from a dataset, or have both choices be different methods of a 
