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

##Factory Pattern

###Factory Pattern

Here's what the Gang of Four Book says about Factory Method:

Intent:  Define an interface for creating an object, but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

Applicability: Use the Factory method pattern when:

* A class can't anticipate the class of objects it must create
* A class wants its subclasses to specify the objects it creates

This is pretty hard to understand, so let's look at an example.

###Factory UML

![Structure](session06/figures/factory.png)

###Factory Example

An "agent based model" is one like the Boids model from last week:
agents act and interact under certain rules. Complex phenomena can be described by simple
agent behaviours.

{{pyfrag('06','agents','model')}}

###Agent model constructor

This logic is common to many kinds of Agent based model, so we can imagine a common class
for agent based models: the constructor could parse a configuration specifying how many agents of each type to create,
their initial conditions and so on.

However, this common constructor doesn't know what kind of agent to create; as a common base, it could be a model of boids,
or the agents could be remote agents on foreign servers, or they could even be physical hardware robots connected to the driving model
over Wifi!

We need to defer the construction of the agents. We can do this with polymorphism: each derived class of the ABM can have an appropriate
method to create its agents:

{{pyfrag('06','agents','construct')}}

This is the *factory method* pattern: a common design solution to the need to defer the construction of daughter objects to a derived class.

###Agent derived classes

{{pyfrag('06','agents','boids')}}

Agents are the base product, boids or robots are a ConcreteProduct.

{{pyfrag('06','agents','web')}}

There is no need to define an explicit base interface for the "Agent" concept in Python: anything that responds to "simulate" and "interact" 
methods will do: this is our Agent concept.

###Refactoring to Patterns

I personally have got into a terrible tangle trying to make base classes which somehow
"promote" themselves into a derived class based on some code in the base class.

This is an example of an "Antipattern": like a Smell, this is a recognised Wrong Way
of doing things.

What I should have written was a Creator with a FactoryMethod.

##Builder

{% if notebook %}
{{ pyfrag('06','builder', 'setup')}}
{% endif %}

###Builder Pattern

Intent: Separate the steps for constructing a complex object from its final representation.

![UML](session06/figures/builder.png)

###Builder example

Let's continue our Agent Based modelling example.

There's a lot more to defining a model than just adding agents of different kinds: we need to define boundary conditions,
specify wind speed or light conditions.

We could define all of this for an imagined advanced Model with a very very long constructor, with lots of optional arguments:

{{pyfrag('06','builder','nobuilder')}}

###Builder preferred to complex constructor

However, long constructors easily become very complicated. Instead, it can be cleaner to define a Builder for models. A builder is like a 
deferred factory: each step of the construction process is implemented as an individual method call, and the completed object
is returned when the model is ready.
{% if notebook %}

{{pyfrag('06','builder','simplemodel')}}
{% endif %}
{{pyfrag('06','builder','builder')}}

Inheritance of an Abstract Builder for multiple concrete builders could be used where there might be multiple ways to build models
with the same set of calls to the builder: for example a version of the model builder yielding models which can be executed
in parallel on a remote cluster.

###Using a builder

{{pyfrag('06','builder','use')}}

###Avoid staged construction without a builder.

We could, of course, just add all the building methods to the model itself, rather than having the model be yielded from a separate builder.

This is an antipattern that is often seen: a class whose `__init__` constructor alone is insufficient for it to be ready to use. A series of
methods must be called, in the right order, in order for it to be ready to use.

This results in very fragile code: its hard to keep track of whether an object instance is "ready" or not. Use of the builder pattern to
keep deferred construction in 

###Builder Message Sequence

![MessageSequence](session06/figures/builder_seq.png)

##Strategy


{% if notebook %}

{{ pyfrag('06','sunspots', 'imports')}}
%matplotlib inline
{% endif %}

##Strategy Pattern

Define a family of algorithms, encapsulate each one, and make them interchangeable. 
Strategy lets the algorithm vary independently from clients that use it.

###Strategy pattern example: sunspots

Consider the sequence of sunspot observations:

{{ pyfrag('06','sunspots', 'load_data')}}

{% if notebook %}
``` python
spots=load_sunspots()
plt.plot(spots)
```
{% else %}
![Sunspot cycle 1700-2014](session06/python/spots.png)
{% endif %}

###Sunspot cycle has periodicity

{{ pyfrag('06','sunspots', 'naive_fft')}}

{% if notebook %}
``` python
plt.plot(spectrum)
```
{% else %}
![Sunspot cycle fourier spectrum](session06/python/fixed.png)
{% endif %}

###Years are not constant length

There's a potential problem with this analysis however:

* Years are not constant length
* Leap years exist
* But, the Fast Fourier Transform assumes evenly spaced intervals

###Uneven time series

The Fast Fourier Transform cannot be applied to uneven time series.

We could:

* Ignore this problem, and assume the effect is small
* Interpolate and resample to even times
* Use a method which is robust to unevenly sampled series, such as LSSA

We also want to find the period of the strongest periodic signal in the data, there are
various different methods we could use for this also, such as integrating the fourier series
by quadrature to find the mean frequency, or choosing the largest single value. 

###Uneven time series design

We could implement a base class for our common code between the different approaches,
and define derived classes for each different algorithmic approach. However, this has drawbacks:

* The constructors for each derived class will need arguments for all the numerical method's control parameters,
such as the degree of spline for the interpolation method, the order of quadrature for integrators, and so on.
* Where we have multiple algorithmic choices to make (interpolator, periodogram, peak finder...) the number
of derived classes would explode: `class SunspotAnalyzerSplineFFTTrapeziumNearMode` is a bit unweildy.
* The algorithmic choices are not then available for other projects
* This design doesn't fit with a clean Ontology of "kinds of things": there's no Abstract Base for spectrogram generators...

###Strategy Pattern for Algorithms

* We implement each algorithm for generating a spectrum as its own Strategy class.
* They all implement a common interface
* Arguments to strategy constructor specify parameters of algorithms, such as spline degree
* One strategy instance for each algorithm is passed to the constructor for the overall analysis

###Strategy Pattern for Algorithms

First, we'll define a helper class for our time series.
{{ pyfrag('06','sunspots', 'Series')}}

###Strategy Pattern for Algorithms

Then, our class which contains the analysis code, *except* the numerical methods

{{ pyfrag('06','sunspots', 'Client')}}
###Strategy Pattern for Algorithms

Our existing simple fourier strategy

{{ pyfrag('06','sunspots', 'Naive')}}
###Strategy Pattern for Algorithms

A strategy based on interpolation to a spline

{{ pyfrag('06','sunspots', 'Spline')}}

###Strategy Pattern for Algorithms

A strategy using the Lomb-Scargle Periodogram

{{ pyfrag('06','sunspots', 'Lomb')}}

###Strategy Pattern for Algorithms

Define our concrete solutions with particular strategies

{{ pyfrag('06','sunspots', 'Declare')}}

###Strategy Pattern for Algorithms

Use these new tools to compare solutions

{{ pyfrag('06','sunspots', 'Analyze')}}

###Comparison of different algorithms for frequency spectrum of sunspots.

{% if notebook %}
``` python
plt.plot(*comparison)
plt.xlim(0,16)
```
{% else %}
![3 ways to calculate a frequency spectrum for sunspot data](session06/python/comparison.png)
{% endif %}

###Deviation of year length from average

{% if notebook %}
plt.plot(deviation)
{% else %}
![Deviation of year length from average 1700-2014](session06/python/deviation.png)
{% endif %}

## Model-View-Controller

### Separate graphics from science!

Whenever we are coding a simulation or model we want to:

* Implement the maths of the model
* Visualise, plot, or print out what is going on.

We often see scientific programs where the code which is used to display what is happening is mixed up with the
mathematics of the analysis. This is hard to understand.

We can do better by separating the `Model` from the `View`, and using a "`Controller`" to manage them.

### Model

{{ pyfrag('06','mvc', 'model')}}

### View

{{ pyfrag('06','mvc', 'view')}}


### Controller

{{ pyfrag('06','mvc', 'controller')}}
