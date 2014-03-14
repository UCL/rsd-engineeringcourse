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
my_object = MyClass()
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
    def someMethod(self, argument):
        pass

my_object.someMethod(value)
```

```cpp
class MyClass {
    void someMethod(int argument){
    }
}

my_object.someMethod(value);
```

Constructor
-----------

Constructor: A special method called when instantiating a new object

``` python
class MyClass(object):
    def __init__(self, argument):
        pass

my_object = MyClass(value)
```

``` cpp
class MyClass {
    MyClass(argument){
    }
}

MyClass my_object = MyClass(value);

```
Member Variable
---------------

Member variable: a value stored inside an instance of a class.

``` python
class MyClass(object):
    def __init__(self):
        self.member = "Value"

my_object = MyClass()
assert(my_object.member == "Value")
```

``` cpp
class MyClass {
    MyClass()
    : member("Value")
    {
    }
    std::string member;
}

MyClass my_object = MyClass(value);
assert( my_object.value == "Value");
```

Access control
--------------

Controls whether member variables and methods can be accessed from outside the class.

```python
class MyClass(object):
    def __secret_method(self): pass
    def _semi_secret_method(self): pass
    def public_method(self):
        self.__secret_method__ # OK

MyClass().__secret_method() # Generates error
MyClass()._semi_secret_method() # Works, but forbidden by convention
MyClass().public_method() # OK
```

```cpp
class MyClass {
    public:
        void public_method(){
            private_method(); //OK
        }
    private:
        void private_method(){}
}
MyClass x = MyClass();
x.public_method(); // OK
x.private_method(); // Raises error
```

Access methods
--------------

Members should be private and accessed by accessors, so that
should the storage change, client code doesn't need to change.

```python
class Person(object):
    def __init__(self):
        self._name = "James Hetherington"

    @property
    def name(self):
        return self._name

assert(Person().name == "James Hetherington")
```

becomes:

```python
class Person(object):
    def __init__(self):
        self._first = "James"
        self._second = "Hetherington"

    @property
    def name(self):
        return self._first + " " + self._second

assert(Person().name == "James Hetherington") 
# Client code unchanged!
```

Access methods (C++)
--------------------

```cpp
class Person(object){
private:
    std::string first;
    std::string second;

public:
    std::string getName():
        return self._first + " " + self._second;
}
```

Class Members
-------------

*Class*, or *static* members, belong to the class as a whole, and are shared between instances.

``` python
class Counted(object):
    number_created=0
    def __init__(self):
        Counted.number_created+=1

    @classmethod
    def howMany(cls):
        return cls.number_created

Counted.howMany() # 0
x=Counted()
Counted.howMany() # 1
z=[Counted() for x in range(5)]
Counted.howMany() # 6 
```

```cpp
class Counted{
private:
    static int number_created;
public:
    Counted(){
        number_created++;
    }
    static int howMany(){
        return number_created;
    }
}

Counted::number_created=0;
cout<< Counted::howMany() << endl;
Counted x=Counted();
cout<< Counted::howMany() << endl;

```

Object-Based programming concepts
---------------------------------

* Class
* Instance
* Member variable
* Method
* Constructor
* Access control
* Static methods
* Accessor methods

UML
---

We have seen that these concepts are common between different object oriented languages.
Thus, when we design our program using these concepts, we can think at an architectural level,
independent of language syntax.

UML is a conventional diagrammatic notation used to describe "class structures" and other higher level
aspects of software design.

Computer scientists get worked up about formal correctness of UML diagrams and learning the conventions precisely.
Working programmers can still benefit from using UML to describe their designs.

UML for objects
---------------

UML represents class members and methods like this:

![Basic class UML](http://yuml.me/diagram/plain/class/[ClassName|+public_member;-private_member|+publicMethod();-privateMethod()])

(The above diagram is generated by the following:

```
http://yuml.me/diagram/boring/class/[ClassName|+publicmember;-privatemember|
+publicMethod();-privateMethod()]
```

using the [YUML](http://yuml.me/) online UML drawing tool.

Inheritance
===========

Object-based vs object-oriented
-------------------------------

Using Objects doesn't mean your code is object-oriented.

Object-oriented programs make use of *inheritance*.

Inheritance
-----------

* Inheritance allows related classes to share code
* Inheritance allows a program to reflect the *ontology* of kinds of thing in a program.

Ontology and inheritance
------------------------

* A bird is a kind of animal
* An eagle is a kind of bird
* A starling is also a kind of bird

* All animals can be born and die
* Only birds can fly (Ish.)
* Only eagles hunt
* Only starlings flock

Inheritance in python
---------------------

``` python
class Animal(object):
    def beBorn(self): print "I exist"
    def die(self): print "Argh!"

class Bird(Animal):
    def fly(self): print "Whee!"

class Eagle(Bird):
    def hunt(self): print "I'm gonna eatcha!"

Eagle.beBorn() # prints "I exist"
Eagle.hunt() # prints "I'm gonna eatcha!"
```

Inheritance terminology
-----------------------

A *derived class* _derives_ from a *base class*

A *subclass* _inherits_ from a *superclass*

(These are different terms for the same thing.)

E.g. "Eagle is a subclass of the Animal superclass."

Inheritance in C++
------------------

``` cpp
class Eagle: public Bird {
    Eagle() : Bird() // Constructor initialises base class
    {
    }; 
}
```

Inheritance UML diagrams
------------------------

UML shows inheritance with an open triangular arrow pointing from subclass to superclass.

![Bird inheritance diagram](http://yuml.me/diagram/plain/class/[Animal]^-[Bird],[Bird]^-[Eagle],[Bird]^-[Starling])

Aggregation vs Inheritance
--------------------------

If one object *has* or *owns* one or more objects, this is *not* inheritance.

For example, the Boids model from last week owned several Boids,
each Boid owned two 2-vectors, one for position and one for velocity.

Aggregation in UML
------------------

The Boids situation can be represented thus:

![Boid aggregation diagram](http://yuml.me/diagram/plain/class/[Model]<>-*>[Boid],[Boid]position++->[Vector],[Boid]velocity++->[Vector])

The open diamond indicates Aggregation, the closed diamond composition. 
(A given boid might belong to multiple models, a given position vector is forever part of the corresponding Boid.)

The asterisk represents cardinality, a model may contain multiple Boids.

Refactoring to inheritance
--------------------------

Smell: Repeated code between two classes which are both ontologically subtypes of something

Before:

``` python
class Person(object):
    def __init__(self, age, job): 
        self.age = age
        self.job = job

    def birthday(self): 
        self.age += 1

class Pet(object):
    def __init__(self, age, owner): 
        self.age = age
        self.owner = owner

    def birthday(self): 
        self.age += 1
```

After:

``` python
class Animal(object):
    def __init__(self, age): 
        self.age = age

    def birthday(self): 
        self.age += 1

class Person(Animal):
    def __init__(self, age, job):
        self.job = job
        super(Person, self).__init__(age)
```

Refactoring to inheritance (C++)
--------------------------------

``` cpp
class Person{
    int age;
    std::string job;
    Person(int age, std::string job): 
        age(age), job(job)
        {}
}

class Pet{
    int age;
    Person & owner;
    Pet(int age, Person & owner):
        age(age), owner(owner)
        {}
}
```

Becomes:

``` cpp
class Animal{
    int age;
    Animal(int age): age(age) {}
}

class Pet: public Animal {
    Person & owner;
    Pet(int age, Person & owner):
        Animal(age), owner(owner)
    {}
}
```

Polymorphism
============

Polymorphism
------------

``` python
class Dog(Animal):
    def noise(self):
        return "Bark"

class Cat(Animal):
    def noise(self):
        return "Miaow"

animals=[Dog(), Dog(), Cat(), Pig(), Cow(), Cat()]
for animal in animals:
    print animal.noise()
```

This will print "Bark Bark Miaow Oink Moo Miaow"

If two classes support the same method, but it does different things for the two classes, 
then if an object is of an unknown class, calling the method will invoke the version for
whatever class the instance is an instance of.

Polymorphism and Inheritance
----------------------------

In C++, where arrays have to contain things of the same type, polymorphism requires
that all the objects share a common superclass, and that the method which is to be subject
to polymorphism is marked as such with the keyword `virtual`:

``` cpp
class Animal{
    virtual std::string noise(){
        return "I don't know what noise to make.";
    }
}

class Dog: public Animal {
    std::string noise(){
        return "Bark";
    }
}

for(Animal &animal: animals) {
    cout << animal.noise() << endl;
}
```

Pure Virtual Functions
----------------------

In the above example, we had to put in a dummy noise for Animals that don't know what type they are.

Instead, we can deliberately leave this undefined:

``` cpp
virtual std::string noise() =0;
```
This means that if we actually instantiate a base animal, calling noise() would cause a crash.
C++ does not allow classes with pure virtual functions to be instantiated. These are called "abstract classes".

```cpp
Animal * x = new Dog(); // OK
Animal * x = new Animal(); // Doesn't compile.
```

Refactoring to Polymorphism
---------------------------

Smell: a function uses a big set of `if` statements or a `case` statement to decide what to do:

Before:

``` python
class Animal(object):
    def __init__(self,type): self.type=type
    def noise(self): 
        if self.type=="Dog"
            return "Bark"
        elif self.type=="Cat"
            return "Miaow"
        elif self.type=="Cow"
            return "Moo"
        ...
```

which is better replaced by the code above.

Interfaces
----------

In C++, it is common to define classes which consist *only* of pure virtual functions, and no data members.
These special kinds of classes are called *interfaces*.

While C++ allows classes to inherit from more than one superclass, this is generally considered bad style,
unless all but one of the superclasses are interfaces.

Interfaces in UML
-----------------

Interface inheritance in UML is indicated thus:

![Interfaces in UML](http://yuml.me/diagram/plain/class/[<<Animal>>]^-.-[Dog])

Further UML
-----------

UML is a much larger diagram language than the aspects we've shown here.

* Message sequence charts show signals passing back and forth between objects ([Web Sequence Diagrams](https://www.websequencediagrams.com/))

* Entity Relationship Diagrams can be used to show more general relationships between things in a system



