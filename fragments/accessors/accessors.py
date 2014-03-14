class Person(object):
   def __init__(self):
      self._name = "James Hetherington"

   @property
   def name(self):
      return self._name
  
assert(Person().name == "James Hetherington")
