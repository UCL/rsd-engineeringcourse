class Animal(object):
   def beBorn(self): print "I exist"
   def die(self): print "Argh!"

class Bird(Animal):
   def fly(self): print "Whee!"

class Eagle(Bird):
   def hunt(self): print "I'm gonna eatcha!"

Eagle().beBorn() # prints "I exist"
Eagle().hunt() # prints "I'm gonna eatcha!"
