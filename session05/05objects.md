---
title: Objects
---

##Introduction to Objects


###Classes: User defined types

``` python
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def grow_up(self):
        self.age+=1

james=Person("James",37)
james.home="London"
```


###Declaring a class 

Class: A user-defined type

```python
class MyClass(object):
    pass
```

```cpp
class MyClass {
};
```

###Object instances

Instance: A particular object *instantiated* from a class.

``` python
my_object = MyClass()
```

``` cpp
MyClass  my_object = MyClass();
MyClass* my_object = new MyClass();
```

###Method

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
};

my_object.someMethod(value);
```

###Constructor

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
};

MyClass my_object = MyClass(value);

```
###Member Variable

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
};

MyClass my_object = MyClass();
assert( my_object.member == "Value");
```

##Object refactorings

###Replace add-hoc structure with user defined classes

Smell: A data structure made of nested arrays and dictionaries becomes unwieldy

Before:

``` python
from random import random
birds = [{"position": random(), "velocity": random(), "type": type} for type in bird_types]
average_position = average([bird["position"] for bird in birds])
```

After:

``` python
class Bird(object):
	def __init__(self,type):
        from random import random
		self.type = type
		self.position = random()
		self.velocity = random()

birds = [Bird(type) for type in bird_types]
average_position = average(bird.position for bird in birds)
```

###Replace function with a method

Smell: A function is always called with the same kind of thing

Before:

``` python
def can_see(source,target):
	return (source.facing-target.facing)<source.viewport

if can_see(hawk,starling):
	hawk.hunt()
```

After:

``` python
class Bird(object):
	def can_see(self,target):
		return (self.facing-target.facing)<self.viewport

if hawk.can_see(starling):
	hawk.hunt()
```


###Replace method arguments with class members

Smell: A variable is nearly always used in arguments to 
a class.

```cpp
class Person
{
  Person();
  float reproduce_probability(unsigned int age);
  float death_probability(unsigned int age);
  float emigrate_probability(unsigned int age);
}
```

After:

```cpp
class Person
{
  Person(unsigned int age);
  float reproduce_probability();
  float death_probability();
  float emigrate_probability();
}
```

### Replace global variable with class data 

###Object Oriented Refactoring Summary

* Replace ad-hoc structure with a class
* Replace function with a method
* Replace method argument with class member
* Replace global variable with class data

