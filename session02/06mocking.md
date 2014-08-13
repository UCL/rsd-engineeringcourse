---
title: Mocking
---

Definition
----------

<div align="left">
mock

:    *verb*, 

     1. to tease or laugh at in a scornful or contemptuous manner
     1. to make a replica or imitation of something

<div class="fragment roll-in">
mocking 

:    *computer science*, to simulate the behavior of real objects in controlled ways.
</div>

<div class="fragment roll-in">
stub routine 

:    A routine that a simulate a more computationally expensive routine, without actually performing
     any calculation. 

     Strictly speaking, the term Mocking is reserved for object-oriented approaches
</div>

For libraries/frameworks, see [this slide](#/MockingFrameworks).
</div>

Recording calls with Mock
-------------------------

<div align="left">
Mock objects record the calls made to them:

~~~~~~~~~~~~~{.python}
>>> from mock import Mock
>>> function = Mock(name="myroutine", return_value=2)
>>> function(1)
2
>>> function(1, "hello", {'a': True})
2
>>> function.mock_calls
[call(1), call(1, 'hello', {'a': True})]
~~~~~~~~~~~~~

Mock objects can return different values for each call

~~~~~~~~~~~~~{.python}
>>> function = Mock(name="myroutine", side_effect=[2, "a"])
>>> function(1)
2
>>> function(1, "hello", {'a': True})
"a"
>>> function() # No more values to return --> mock throws a StopIteration exception
StopIteration error thrown in ....
~~~~~~~~~~~~~

The arguments of each call can be recovered

~~~~~~~~~~~~~{.python}
>>> function = Mock(name="myroutine", return_value=2)
>>> function([0, 1], 1)
2
>>> name, args, kwargs = function.mock_calls[0]
>>> name # function was called 
''
>>> args # arguments where those given here
([0, 1], 1)
>>> kwargs # No keyword arguments
{}
~~~~~~~~~~~~~

</div>


Testing functions that call other functions
-------------------------------------------

~~~~~~~~~~~~{.python}
def callee(x): pass # Does something complicated

def caller_function(x):
   value = callee(x)
   second_arg = # something complicated with value
   return callee(second_arg)
~~~~~~~~~~~~

Black-box

:    Give `caller_function` a function for which we think we know the result: e.g. small analytical
     model, rather than big expensive calculation.

     We do not need to know how `caller_function` works. 

Clear-box

:    Give `caller_function` a mock object such that we know when and how the argument function is
     called.

     We know something of the internals of `caller_function`. We want to verify that the argument
     function is called as expected. 

<br>
<div align="left" class="frament fade-in">
`caller_function` must be tested in *isolation* from the rest of the code, so that bugs from one do
not contaminate the other. 
</div>

Exercise: derivative function
-----------------------------

<div align="left">
Goal

:   compute the derivative of the diffusion model from [the previous exercise](#/diffusion).

Description

:   create a function that takes a function, an integer density, and an index $i$, and returns the
    right-derivative   $f(n_i + 1) - f(n_i)$

~~~~~~~~~~~~~~{.python}
def partial_derivative(function, x, index):
  """ Computes right derivative of function over integers

      :Parameters:
         function: callable object
           The function for which to compute the delta/derivative
         x: array of integers
           The point at which to compute the right-derivative
         index: integer
           Partial derivative direction.
  """
  from numpy import array
  # Computes left value
  left_value = function(x)

  # Copies and modifies x. Could do it without copy, but that complicates mocking.
  x = array(x)
  x[index] += 1
  right_value = function(x)

  return right_value - left_value
~~~~~~~~~~~~~~

</div>
