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

me=Person(37,"Programmer")
me.birthday()
assert(me.age == 38)
