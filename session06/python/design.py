
### "pyclass"
class Particle(object):
    def __init__(self, position, velocity):
       self.position=position
       self.velocity=velocity
    def move(self, delta_t):
       self.position+= self.velocity*delta_t
### "hiding"
class MyClass(object):
    def __private_method(self): pass
    def _private_method(self): pass
    def public_method(self): pass

#MyClass().__private_method() # Generates error
MyClass()._private_method() # Works, but forbidden by convention
MyClass().public_method() # OK
### "accessors1"
class Person(object):
    def __init__(self):
        self.name = "James Hetherington"

assert(Person().name == "James Hetherington")
### "accessors2"
class Person(object):
    def __init__(self):
        self._first = "James"
        self._second = "Hetherington"
    @property
    def name(self):
        return self._first + " " + self._second

assert(Person().name == "James Hetherington")
### "accessors3"
class Person(object):
    def __init__(self):
        self._name = "James Hetherington"
    def name(self):
        return self._name

assert(Person().name() == "James Hetherington")
### "classmethod"
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
### "inheritance"
class Animal(object):
    def beBorn(self): print "I exist"
    def die(self): print "Argh!"

class Bird(Animal):
    def fly(self): print "Whee!"

class Eagle(Bird):
    def hunt(self): print "I'm gonna eatcha!"

Eagle().beBorn()
Eagle().hunt()
### "super"
class Animal(object):
    def __init__(self, age):
        self.age=age

class Person(Animal):
    def __init__(self, age, name):
        super(Person, self).__init__(age)
        self.name=name
### "inheritance_factor1"
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
### "inheritance_factor2"
class Animal(object):
    def __init__(self, age): 
        self.age = age
    def birthday(self): 
        self.age += 1

class Person(Animal):
    def __init__(self, age, job):
        self.job = job
        super(Person, self).__init__(age)
### "polymorphism"
class Dog(object):
    def noise(self):
        return "Bark"

class Cat(object):
    def noise(self):
        return "Miaow"

class Pig(object):
    def noise(self): return "Oink"

class Cow(object):
    def noise(self): return "Moo"

animals=[Dog(), Dog(), Cat(), Pig(), Cow(), Cat()]
for animal in animals:
    print animal.noise()
### "base"
class Animal(object):
    def noise(self): return "I don't make a noise."

class Dog(Animal):
    def noise(self): return "Bark"

class Worm(Animal):
    pass

class Poodle(Animal):
    pass

animals=[Dog(), Worm(), Pig(), Cow(), Poodle()]
for animal in animals:
    print animal.noise()
### "undefined"
class Animal(object): pass

class Worm(Animal): pass

# Worm().noise() # Generates error
### "case"
class Animal(object):
    def __init__(self,type): self.type=type
    def noise(self): 
        if self.type=="Dog":
            return "Bark"
        elif self.type=="Cat":
            return "Miaow"
        elif self.type=="Cow":
            return "Moo"
