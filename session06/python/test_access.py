from nose.tools import raises

class MyClass(object):
   def __secret_method(self): pass
   def _semi_secret_method(self): pass
   def public_method(self):
      self.__secret_method() # OK

@raises(AttributeError)
def test_secret():
   MyClass().__secret_method() # Generates error

def test_unsecret():
   MyClass()._semi_secret_method() # Works, but forbidden by convention
   MyClass().public_method() # OK
