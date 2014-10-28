---
title: Patterns
---

##Patterns

###Class Complexity

We've seen that using object orientation can produce quite complex class structures, with classes owning each other, instantiating each other,
and inheriting from each other.

There are lots of different ways to design things, and decisions to make.

> Should I inherit from this class, or own it as a member variable? ("is a" vs "has a")

###Design Patterns

Programmers have noticed that there are certain ways of arranging classes that work better than others.

These are called "design patterns".

They were first collected on one of the [world's first Wikis](http://c2.com/cgi/wiki?WelcomeVisitors), 
as the [Portland Pattern Repository](http://c2.com/cgi-bin/wiki?PatternIndex)

###Reading a pattern

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

###Introducing Some Patterns

There are lots and lots of design patterns, and it's a great literature to get into to
read about design questions in programming and learn from other people's experience.

We'll just show a few in this session:

* Factory Method
* Builder
* Handle-Body
* Strategy

###Factory Method

Here's what the Gang of Four Book says about Factory Method:

Intent:  Define an interface for creating an object, but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

Applicability: Use the Factory method pattern when:

* A class can't anticipate the class of objects it must create
* A class wants its subclasses to specify the objects it creates

###Factory UML

![Structure](session07/figures/factory)

###Factory Sample Code

```python
class Model(object):
  def __init__(config_path, individual_factory):
    self.entites=[]
    for entity in yaml.load(open(config_path)) 
      self.entities.append(individual_factory.create(entity['species']))
  def simulate(self):
    for entity in entities:
      for target in entities:
        entity.interact(target)
      entity.simulate()

class 2DFactory(object):
  def create(self, species):
    return 2DAnimal(species)

class RemoteFactory(object):
  def __init__(self, url):
    self.url=url
    connection=AmazonCompute.connect(url)
  def create(self, species):
    return OnlineAnimal(species, connection)

class RobotFactory(object): pass
```

###Refactoring to Patterns

I personally have got into a terrible tangle trying to make base classes which somehow
"promote" themselves into a derived class based on some code in the base class.

This is an example of an "Antipattern": like a Smell, this is a recognised Wrong Way
of doing things.

What I should have written was a Creator with a FactoryMethod.

###Builder

Intent: Separate the steps for constructing a complex object from its final representation.

```python 
CreateMaze(builder){
    builder.BuildMaze();
    builder.BuildRoom(1);
    builder.BuildRoom(2);
    builder.BuildDoor(1,2);
    return builder.GetMaze();
}
```

Polymorphism is used, so that `CreateMaze` can create a maze using Ascii graphics,
OpenGL, or a 3d printer, depending on the builder it is given.

###Builder UML

![UML](session07/figures/builder)

###Builder Message Sequence

![MessageSequence](session07/figures/builder_seq)

###Strategy

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
