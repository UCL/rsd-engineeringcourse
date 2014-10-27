### "setup"
value=0
bird_types=["Starling", "Hawk"]
import numpy as np
from mock import Mock
average=np.mean
hawk=Mock()
starling=Mock()
Mock.__sub__=Mock()
### "intro"
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def grow_up(self):
        self.age+=1

james=Person("James",37)
james.home="London"
### "declare"
class MyClass(object):
    pass
### "instance"
my_object = MyClass()
### "method"
class MyClass(object):
    def someMethod(self, argument):
        pass

my_object=MyClass()
my_object.someMethod(value)
### "constructor"
class MyClass(object):
    def __init__(self, argument):
        pass

my_object = MyClass(value)
### "member"
class MyClass(object):
    def __init__(self):
        self.member = "Value"

my_object = MyClass()
assert(my_object.member == "Value")
### "structure_before"
from random import random
birds = [{"position": random(),
          "velocity": random(),
          "type": kind} for kind in bird_types]

average_position = average([bird["position"] for bird in birds])
### "structure_after"
class Bird(object):
    def __init__(self,type):
        from random import random
        self.type = type
        self.position = random()
        self.velocity = random()

birds = [Bird(type) for type in bird_types]
average_position = average([bird.position for bird in birds])
### "method_before"
def can_see(source,target):
    return (source.facing-target.facing)<source.viewport

if can_see(hawk,starling):
    hawk.hunt()

### "method_after"
class Bird(object):
    def can_see(self,target):
        return (self.facing-target.facing)<self.viewport

if hawk.can_see(starling):
    hawk.hunt()

### "member_before"
class Person(object):
    def __init__(self, genes):
        self.genes=genes
    def reproduce_probability(self,age): pass
    def death_probability(self,age): pass
    def emigrate_probability(self,age): pass

### "member_after"
class Person(object):
    def __init__(self, genes, age):
        self.age=age
        self.genes=genes
    def reproduce_probability(self): pass
    def death_probability(self): pass
    def emigrate_probability(self): pass

### "global_before"
name="James"
birthday=[19,10,76]
today=[29,10]
if today==birthday[0:2]:
    print "Happy Birthday, ", name
else:
    print "No birthday for you today."

### "global_after"
class Person(object):
    def __init__(self, birthday, name):
        self.birth_day=birthday[0]
        self.birth_month=birthday[1]
        self.birth_year=birthday[2]
        self.name=name
    def check_birthday(self, today_day, today_month):
        if not self.birth_day == today_day:
            return False
        if not self.birth_month == today_month:
            return False
        return True
    def greet_appropriately(self, today):
        if self.check_birthday(*today):
            print "Happy Birthday", self.name
        else:
            print "No birthday for you."

james=Person([19,10,76],"James")
james.greet_appropriately([29,10])

