---
title: Floating Point
---

##Testing with Floating Points

###Floating points are not Reals

<div align="left">
Floating points are inaccurate representations of real numbers:

`1.0 == 0.99999999999999999`<code style="color:red">00</code> is true to the last bit.

<div class="fragment roll-in">
This can lead to numerical errors during calculations: $1000 (a - b) \neq 1000a - 1000b$

``` python
>>> 1000.0 * 1.0 - 1000.0 * 0.9999999999999998
2.2737367544323206e-13

>>> 1000.0 * (1.0 - 0.9999999999999998)
2.220446049250313e-13
```

<div class="fragment fade-in">
*Both* results are wrong: `2e-13` is the correct answer.
</div>
</div>

<div class="fragment roll-in">
The size of the error will depend on the magnitude of the floating points:

``` python
>>> 1000.0 * 1e5 - 1000.0 * 0.9999999999999998e5
1.4901161193847656e-08
```
The result should be `2e-8`.
</div>


###Comparing floating points

<div align="left">
Comparison can be absolute:

``` python
def test_compare_two_scalars():
  from nose.tools import assert_almost_equal
  assert_almost_equal( 0.7, 0.7 + 1e-6, delta = 1e-5)
```

<div class="fragment roll-in">
Or relative:

``` python
def test_compare_two_scalars():
  from nose.tools import assert_almost_equal
  magnitude = 0.7
  assert_almost_equal(0.7, 0.7 + 1e-5, delta = magnitude * 1e-5)
```
Where `magnitude` depends on the intrinsic of the calculations.
</div>

<div class="fragment roll-in">
<br>
For instance, if calculations is a result of differences between large numbers,

``` python
>>> (1e15 + 1.4) - (1e15 + 0.7)
0.625
```

then `magnitude = 1e15`.
</div>

</div>


###Comparing vectors of floating points

<div align="left">
Numerical vectors are best represented using [numpy](http://www.numpy.org/).

``` python
from numpy import array, pi

vector_of_reals = array([0.1, 0.2, 0.3, 0.4]) * pi
```


Numpy ships with a number of assertions (in ``numpy.testing``) to make
comparison easy:

``` python
def test_compare_vectors_of_reals():
  from numpy import array, pi
  from numpy.testing import assert_allclose
  expected = array([0.1, 0.2, 0.3, 0.4, 1e-12]) * pi
  actual = array([0.1, 0.2, 0.3, 0.4, 2e-12]) * pi
  actual[:-1] += 1e-6

  assert_allclose(actual, expected, rtol=1e-5, atol=1e-8)
```

It compares the difference between `actual` and `expected` to ``atol + rtol * abs(expected)``.
</div>
