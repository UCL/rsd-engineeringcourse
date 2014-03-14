
class Animal(object):
    def __init__(self, age): 
        self.age = age

    def birthday(self): 
        self.age += 1

class Person(Animal):
    def __init__(self, age, job):
        self.job = job
        super(Person, self).__init__(age)


me=Person(37,"Programmer")
me.birthday()
assert(me.age == 38)
