class Person(object):
   def __init__(self):
      self._first = "James"
      self._second = "Hetherington"

   @property
   def name(self):
      return self._first+" "+self._second
  
assert(Person().name == "James Hetherington")
