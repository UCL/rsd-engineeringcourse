---
title: Performance Programming
---

## Performance Programming

### Performance Programming

We've spent most of this course looking at how to make code readable and
reliable. For research work, it is often also important that code is efficient:
that it does what it needs to do quickly.

## Measure First

It is very hard to work out beforehand whether code will be efficient or not:
it is essential to Profile code, to measure its performance, to determine what
aspects of it are slow.

## Two Mandelbrots

### The Mandelbrot Set

You're probably familiar with a famous fractal called the [Mandelbrot Set](https://www.youtube.com/watch?v=AGUlJus5kpY)

For a complex number $c$, $c$ is in the Mandelbrot set if the series $z_{i+1}=z_{i}^2+c$ (With $z_0=c$) stays close to $0$.

Traditionally, we plot a color showing how many steps are needed for
$\left|z_i\right|>2$, whereupon we are sure the series will diverge.

### Simple Implementation

{{pyfrag('08','mandel','TrivialMandel')}}

![](session08/python/mandel.png)

### How does it perform?

{{pyfrag('08','mandel','ResolutionDefine')}}

{{pyfrag('08','mandel','GenerateTrivial',timed="687ms")}}

### We can go faster!

We will learn this lesson to make a version of this code which works on **arrays** of inputs:

{{pyfrag('08','mandel','NumpyMandel')}}
{{pyfrag('08','mandel','NumpyGrid')}}

### Numpy Goes Faster!

{{pyfrag('08','mandel','GenerateNumpy', timed="55ms")}}

And it gives the same answer:

{{pyfrag('08','mandel','NumpyResidual')}}

## The rest is notebooks

The remainder of this lecture is presented as IPython Notebooks

[MandelbrotSets](http://nbviewer.ipython.org/url/development.rc.ucl.ac.uk/training/engineering/session08/Mandels.ipynb)
[NumPy](http://nbviewer.ipython.org/url/development.rc.ucl.ac.uk/training/engineering/session08/Numpy.ipynb)
[Scaling](http://nbviewer.ipython.org/url/development.rc.ucl.ac.uk/training/engineering/session08/Scaling.ipynb)
[Cython](http://nbviewer.ipython.org/url/development.rc.ucl.ac.uk/training/engineering/session08/Cython.ipynb)

These will be integrated into the rest of the lectures in due course.

## Exercise: Numpy and the Boids

Reimplement the boids using NumPy.
Make it as fast as you can: measure the performance versus the default bad_boids and your best object oriented solution.
**Don't** base your NumPy solution on your object oriented solution: I recommend you go back to the original bad boids and start again as you numpify.
