# ---
# jupyter:
#   jekyll:
#     display_name: Object Oriented Design
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Class design

# %% [markdown]
#
# The concepts we have introduced are common between different object oriented languages.
# Thus, when we design our program using these concepts, we can think at an architectural level,
# independent of language syntax.
#
# In Python:
#

# %%
class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    def move(self, delta_t):
        self.position += self.velocity * delta_t


# %% [markdown]
# In C++:
#
# ``` cpp
# class Particle {
#     std::vector<double> position;
#     std::vector<double> velocity;
#     Particle(std::vector<double> position, std::vector<double> velocity);
#     void move(double delta_t);
# }
# ```

# %% [markdown]
# In Fortran:
#
# ``` fortran
# type particle
#     real :: position
#     real :: velocity
#   contains
#     procedure :: init
#     procedure :: move
# end type particle
# ```

# %% [markdown]
# ## UML

# %% [markdown]
#
# UML is a conventional diagrammatic notation used to describe "class structures" and other higher level
# aspects of software design.
#
# Computer scientists get worked up about formal correctness of UML diagrams and learning the conventions precisely.
# Working programmers can still benefit from using UML to describe their designs.
#

# %% [markdown]
# ## YUML

# %% [markdown]
# We can see a YUML model for a Particle class with `position` and `velocity` data and a `move()` method using
# the [YUML](http://yuml.me/) online UML drawing tool ([example](http://yuml.me/diagram/boring/class/[Particle|position;velocity|move%28%29])).
#
# ```
#     http://yuml.me/diagram/boring/class/[Particle|position;velocity|move%28%29]
# ```

# %% [markdown]
# Here's how we can use Python code to get an image back from YUML:

# %%
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests
from IPython.display import Image

def yuml(model):
    result = requests.get("http://yuml.me/diagram/boring/class/" + model)
    return Image(result.content)


# %%
yuml("[Particle|position;velocity|move()]")


# %% [markdown]
# The representation of the `Particle` class defined above in UML is done with a box with three sections. The name of the class goes on the top, then the name of the member variables in the middle, and the name of the methods on the bottom. We will see later why this is useful.

# %% [markdown]
# ## Information Hiding

# %% [markdown]
#
# Sometimes, our design for a program would be broken if users start messing around with variables we don't want them to change.
#
# Robust class design requires consideration of which subroutines are intended for users to use, and which are internal.
# Languages provide features to implement this: access control. 
#
# In python, we use leading underscores to control whether member variables and methods can be accessed from outside the class:
#  - single leading underscore (`_`) is used to document it's private but people could use it if wanted (thought they shouldn't);
#  - double leading underscore (`__`) raises errors if called.
#
#
#

# %%
class MyClass:
    def __init__(self):
        self.__private_data = 0
        self._private_data = 0
        self.public_data = 0
    
    def __private_method(self): pass
    
    def _private_method(self): pass
    
    def public_method(self): pass
    
    def called_inside(self):
        self.__private_method()
        self._private_method()
        self.__private_data = 1
        self._private_data = 1
        

MyClass().called_inside()

# %%
MyClass()._private_method() # Works, but forbidden by convention

# %%
MyClass().public_method() # OK

print(MyClass()._private_data)

# %%
print(MyClass().public_data)

# %%
MyClass().__private_method() # Generates error

# %%
print(MyClass().__private_data) # Generates error


# %% [markdown]
# ## Property accessors

# %% [markdown]
#
# Python provides a mechanism to make functions appear to be variables. This can be used if you want to
# change the way a class is implemented without changing the interface:
#
#
#

# %%
class Person:
    def __init__(self):
        self.name = "Graham Chapman"

assert(Person().name == "Graham Chapman")


# %% [markdown]
#
#
#
# becomes:
#
#
#

# %%
class Person(object):
    def __init__(self):
        self._first = "Graham"
        self._second = "Chapman"
        

    @property
    def name(self):
        return f"{self._first} {self._second}"

assert(Person().name == "Graham Chapman")
 

# %% [markdown]
# Making the same external code work as before.

# %% [markdown]
#
#
#
# Note that the code behaves the same way to the outside user.
# The implementation detail is hidden by private variables.
# In languages without this feature, such as C++, it is best to always
# make data private, and always
# access data through functions:
#
#
#

# %%
class Person(object):
    def __init__(self):
        self._name = "Graham Chapman"
        
    def name(self):  # an access function
        return self._name

assert(Person().name() == "Graham Chapman")


# %% [markdown]
# But in Python this is unnecessary because the `@property` capability.
#

# %% [markdown]
# Another way could be to create a member variable `name` which holds the full name. However, this could lead to inconsistent data. If we create a `get_married` function, then the name of the person won't change!

# %%
class Person(object):
    def __init__(self, first, second):
        self._first = first
        self._second = second
        self.name = f"{self._first} {self._second}"
        
    def get_married(self, to):
        self._second = to._second

graham = Person("Graham", "Chapman")
david = Person("David", "Sherlock")
assert(graham.name == "Graham Chapman")
graham.get_married(david)
assert(graham.name == "Graham Sherlock")


# %% [markdown]
# This type of situation could makes that the object data structure gets inconsistent with itself. Making variables being out of sync with other variables. Each piece of information should only be stored in once place! In this case, `name` should be calculated each time it's required as previously shown.
# In database design, this is called [Normalisation](https://en.wikipedia.org/wiki/Database_normalization).

# %% [markdown]
# ### UML for private/public

# %% [markdown]
# We prepend a `+`/`-` on public/private member variables and methods:

# %%
yuml("[Particle|+public;-private|+publicmethod();-privatemethod]")


# %% [markdown]
# ## Class Members

# %% [markdown]
#
# *Class*, or *static* members, belong to the class as a whole, and are shared between instances.
#
# This is an object that keeps a count on how many have been created of it.
#

# %%
class Counted:
    number_created = 0
    
    def __init__(self):
        Counted.number_created += 1
        
    @classmethod
    def howMany(cls):
        return cls.number_created

Counted.howMany()  # 0
x = Counted()
Counted.howMany()  # 1
z = [Counted() for x in range(5)]
Counted.howMany()  # 6 


# %% [markdown]
# The data is shared among all the objects instantiated from that class. Note that in `__init__` we are not using `self.number_created` but the name of the class. The `howMany` function is not a method of a particular object. It's called on the class, not on the object. This is possible by using the `@classmethod` decorator.

# %% [markdown]
# ## Inheritance and Polymorphism

# %% [markdown]
# ## Object-based vs Object-Oriented

# %% [markdown]
#
# So far we have seen only object-based programming, not object-oriented programming.
#
# Using Objects doesn't mean your code is object-oriented.
#
# To understand object-oriented programming, we need to introduce **polymorphism** and **inheritance**.
#

# %% [markdown]
# ## Inheritance

# %% [markdown]
#
# * Inheritance is a mechanism that allows related classes to share code.
# * Inheritance allows a program to reflect the *[ontology](https://en.wikipedia.org/wiki/Ontology_(information_science))* of kinds of thing in a program.
#

# %% [markdown]
# ## Ontology and inheritance

# %% [markdown]
#
# * A bird is a kind of animal
# * An eagle is a kind of bird
# * A starling is also a kind of bird
# * All animals can be born and die
# * Only birds can fly (Ish.)
# * Only eagles hunt
# * Only starlings flock
#

# %% [markdown]
# ## Inheritance in python

# %% [markdown]
#
#
#

# %%
class Animal:
    def beBorn(self):
        print("I exist")
    def die(self): 
        print("Argh!")

class Bird(Animal):
    def fly(self): 
        print("Whee!")

class Eagle(Bird):
    def hunt(self): 
        print("I'm gonna eatcha!")

class Starling(Bird):
    def flew(self): 
        print("I'm flying away!")

Eagle().beBorn()
Eagle().hunt()


# %% [markdown]
# ## Inheritance terminology

# %% [markdown]
# Here are two equivalents definition, one coming from C++ and another from Java:
# * A *derived class* _derives_ from a *base class*.
# * A *subclass* _inherits_ from a *superclass*.
#
# These are different terms for the same thing.
# So, we can say:
#
# * Eagle is a subclass of the Animal superclass.
# * Animal is the base class of the Eagle derived class.
#
# Another equivalent definition is using the synonym *child* / *parent* for *derived* / *base* class:
# * A *child class* extends a *parent class*.
#

# %% [markdown]
# ## Inheritance and constructors

# %% [markdown]
# To use implicitly constructors from a *superclass*, we can use `super` as shown below.

# %%
class Animal:
    def __init__(self, age):
        self.age = age

class Person(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name


# %% [markdown]
# Read [Raymond Hettinger](https://twitter.com/raymondh)'s [article about `super`](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) to see various real examples.

# %% [markdown]
# ## Inheritance UML diagrams

# %% [markdown]
# UML shows inheritance with an open triangular arrow pointing from subclass to superclass.

# %%
yuml("[Animal]^-[Bird],[Bird]^-[Eagle],[Bird]^-[Starling]%")

# %% [markdown]
# ## Aggregation vs Inheritance

# %% [markdown]
#
# If one object *has* or *owns* one or more objects, this is *not* inheritance.
#
# For example, the boids example we saw few weeks ago, could be organised as an overall Model, which it owns several Boids,
# and each Boid owns two 2-vectors, one for position and one for velocity.
#

# %% [markdown]
# ### Aggregation in UML

# %% [markdown]
# The Boids situation can be represented thus:

# %%
yuml("[Model]<>-*>[Boid],[Boid]position++->[Vector],[Boid]velocity++->[Vector]%")


# %% [markdown]
# The open diamond indicates **Aggregation**, the closed diamond **composition**.
# (A given boid might belong to multiple models, a given position vector is forever part of the corresponding Boid.)
#
# The asterisk represents cardinality, a model may contain multiple Boids. This is a [one to many relationship](https://en.wikipedia.org/wiki/One-to-many_(data_model)). [Many to many relationship](https://en.wikipedia.org/wiki/Many-to-many_(data_model)) is shown with `*` on both sides.

# %% [markdown]
# ### Refactoring to inheritance

# %% [markdown]
#
# Smell: Repeated code between two classes which are both ontologically subtypes of something
#
# Before:
#
#
#

# %%
class Person:
    def __init__(self, age, job): 
        self.age = age
        self.job = job
    def birthday(self): 
        self.age += 1

class Pet:
    def __init__(self, age, owner): 
        self.age = age
        self.owner = owner
    def birthday(self): 
        self.age += 1


# %% [markdown]
#
#
#
# After:
#
#
#

# %%
class Animal:
    def __init__(self, age): 
        self.age = age
    def birthday(self): 
        self.age += 1

class Person(Animal):
    def __init__(self, age, job):
        self.job = job
        super().__init__(age)
        
class Pet(Animal):
    def __init__(self, age, owner):
        self.owner = owner
        super().__init__(age)


# %% [markdown]
# ## Polymorphism

# %%
class Dog:
    def noise(self):
        return "Bark"

class Cat:
    def noise(self):
        return "Miaow"

class Pig:
    def noise(self):
        return "Oink"

class Cow:
    def noise(self):
        return "Moo"

animals = [Dog(), Dog(), Cat(), Pig(), Cow(), Cat()]
for animal in animals:
    print(animal.noise())


# %% [markdown]
#
#
#
# This will print "Bark Bark Miaow Oink Moo Miaow"
#
# If two classes support the same method, but it does different things for the two classes, 
# then if an object is of an unknown class, calling the method will invoke the version for
# whatever class the instance is an instance of.
#

# %% [markdown]
# ## Polymorphism and Inheritance

# %% [markdown]
#
# Often, polymorphism uses multiple derived classes with a common base class.
# However, [duck typing](https://en.wikipedia.org/wiki/Duck_typing) in Python means that all that is required is that the 
# types support a common **Concept** (Such as iterable, or container, or, in this case, the
# Noisy concept.)
#
# A common base class is used where there is a likely **default** that you want several
# of the derived classes to have.
#
#
#

# %%
class Animal:
    def noise(self):
        return "I don't make a noise."

class Dog(Animal):
    def noise(self):
        return "Bark"

class Worm(Animal):
    pass

class Poodle(Dog):
    pass

animals = [Dog(), Worm(), Pig(), Cow(), Poodle()]
for animal in animals:
    print(animal.noise())


# %% [markdown]
# ## Undefined Functions and Polymorphism

# %% [markdown]
#
# In the above example, we put in a dummy noise for Animals that don't know what type they are.
#
# Instead, we can explicitly deliberately leave this undefined, and we get a crash if we access an undefined method.
#
#
#

# %%
class Animal:
    pass

class Worm(Animal):
    pass


# %%
Worm().noise() # Generates error


# %% [markdown]
# ## Refactoring to Polymorphism

# %% [markdown]
#
# Smell: a function uses a big set of `if` statements or a `case` statement to decide what to do:
#
# Before:
#
#
#

# %%
class Animal:
    def __init__(self, animal_kind): 
        self.animal_kind = animal_kind
        
    def noise(self): 
        if self.animal_kind == "Dog":
            return "Bark"
        elif self.animal_kind == "Cat":
            return "Miaow"
        elif self.animal_kind == "Cow":
            return "Moo"


# %% [markdown]
# which is better replaced by the code above.

# %% [markdown]
# ## Interfaces and concepts

# %% [markdown]
#
# In C++, it is common to define classes which declare dummy methods, called "virtual" methods, which specify
# the methods which derived classes must implement. Classes which define these methods, but which cannot be instantiated
# into actual objects, are called "abstract base" classes or "interfaces".
#
# Python's Duck Typing approach means explicitly declaring these is unnesssary: any class concept which implements
# appropriately named methods will do. These as user-defined **concepts**, just as "iterable" or "container" are 
# built-in Python concepts. A class is said to "implement an interface" or "satisfy a concept".
#

# %% [markdown]
# ## Interfaces in UML

# %% [markdown]
# Interfaces implementation (a common ancestor that doesn't do anything but defines methods to share) in UML is indicated thus:

# %%
yuml("[<<Animal>>]^-.-[Dog]")

# %% [markdown]
# ## Further UML

# %% [markdown]
#
# UML is a much larger diagram language than the aspects we've shown here.
#
# * Message sequence charts show signals passing back and forth between objects ([Web Sequence Diagrams](https://www.websequencediagrams.com/)).
#
# * Entity Relationship Diagrams can be used to show more general relationships between things in a system.
#
#
# Read more about UML on Martin Fowler's [book about the topic](https://martinfowler.com/books/uml.html).
#
