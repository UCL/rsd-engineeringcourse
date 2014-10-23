---
title: Mocking
---

##Mocking

###Definition

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

</div>

###Recording calls with Mock

<div align="left">
Mock objects record the calls made to them:

``` python
>>> from mock import Mock
>>> function = Mock(name="myroutine", return_value=2)
>>> function(1)
2
>>> function(5, "hello", a=True)
2
>>> function.mock_calls
[call(1), call(5, 'hello', a=True)]
```

The arguments of each call can be recovered

``` python
>>> name, args, kwargs = function.mock_calls[1]
>>> args, kwargs
((1, 'hello'), {'a': True})
```

Mock objects can return different values for each call

``` python
>>> function = Mock(name="myroutine", side_effect=[2, "xyz"])
>>> function(1), function(1, "hello", {'a': True})
(2, "xyz")
>>> function() # No more values to return --> mock throws an exception
StopIteration error thrown in ....
```


</div>


###Testing functions that call other functions

``` python
def minimize(model, start_input):
    start_value = model(start_input)
    # ... more calls to model
    return result
```

Black-box

:    `model` is a function for which we think we know the result:
     e.g. small analytical model, rather than big expensive calculation.

     Internals of `minimize` are irrelevant. Only the result matters.

Clear-box

:    `model` is a mock object

     Sequence of calls to `model` is checked and is part of the test.

<br>
<div align="left" class="frament fade-in">
`minimize` must be tested in *isolation* from the rest of the code!
</div>

###Exercise: derivative function

<div align="left">
Goal

:   compute the derivative of the diffusion model from [the previous exercise](#/diffusion).

Description

:   create a function that takes a function, an integer density, and an index $i$, and returns the
    right-derivative   $f(n_i + 1) - f(n_i)$

``` python
def partial_derivative(function, x, index):
  """ Computes right derivative of function over integers

      :param function: callable object for which to compute the derivative
      :param x: array of integers at which to compute the right-derivative
      :param index: Partial derivative direction.
  """
  from numpy import array

  x_right = array(x).copy()
  x_right[index] += 1
  return function(x) - function(x_right)
```

</div>
