---
title: Performance computing
---

## Performance computing

### Performance computing

Profiling allows us to spot and address performance issues with our code. The session on performance programming showed: 

* how the NumPy library can be used to carry out faster array-wise operations
* looked at the implications of data type on performance
* introduced the Big O notation
* demonstrated the speed benefits of Cython

Returning to the Boids code for our exercise, we sought to reimplement the model with NumPy and Cython to make it run as fast as possible.

### Optimising the boids

We were looking for:

* Readable code and sensible tests (always!)
* Profiling to assess performance
* Attempts to optimise, for example with:
    - Appropriate use of data types
    - Cython and/or NumPy
    - Vectorisation of loops
    - Arraywise operations

<!--

Sample solution:
TO DO.
-->