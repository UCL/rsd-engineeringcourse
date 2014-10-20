---
title: Simple data manipulation and plotting
---

# Working with and visualising data

## Why write software to manage your data and plots? 

We should use programs for our entire research pipeline.

Not just main simulation or numerical code, but also the small scripts which we use to
tidy up data and produce plots. 

This should be code, so that the whole research pipeline
is recorded for reproducibility. Data manipulation in spreadsheets cannot be shared or
checked. 

It should be *good* code, because research conclusions are just as wrong if the
plotting script is wrong as if the code that generates the data is wrong.

## Analysing patient data

(The next few slides are taken from Software Carpentry materials and are (CC-BY) the contributors at
https://github.com/swcarpentry/bc/blob/master/team.md)

You can follow along in an [IPython Notebook](http://nbviewer.ipython.org/github/UCL/rsd-engineeringcourse/blob/staging/session01/notebooks/session1.ipynb)

## The data


Imagine you are studying inflammation in patients who have been given a new treatment for arthritis, 
and need to analyze the first dozen data sets. The data sets are stored in 
comma-separated values (CSV) format: 
each row holds information for a single patient, and the columns represent successive days. 
The first few rows of our first file look like this:

``` csv
{{d['session01/data/inflammation-01.csv'][0:500]}}...
```

## The task

We want to:

*   load that data into memory,
*   calculate the average inflammation per day across all patients, and
*   plot the result.

This will give us a good overview of various concepts in Python, which we'll
return to some of after this initial survey.

## Loading data

It's almost always wrong to do things yourself.

Someone's probably written a program already. 
Python makes it easy to find and use other people's libraries.

In this case, we want to use a python library to load and parse the csv data, and manipulate it as 
a matrix.

``` python
{{d['session01/python/numpy_nb.py|idio|pycon']['Starting']}}
```
Here we've called a **function** `loadtxt` from a **module** `numpy`, and
assigned it to a **variable** data. This course assumes you're happy with very basic
programming concepts like function and variable. The IPython notebook contains more detail.

## Types

``` python
{{d['session01/python/numpy_nb.py|idio|pycon']['Types1']}}
```

We've jumped straight in and used a `numpy.ndarray` (numerical python) matrix type for our data.
It's similar to a basic python `Array` type; we'll talk more about the differences later.

For now, it's important to know that Python variables have a type, that different types behave differently,
but that, unlike C++ or Fortran, you don't need to say what type of variable something is before you use it.

```python
{{d['session01/python/numpy_nb.py|idio|pycon']['Types2']}}
```

## Slicing

We can **slice** elements from arrays and matrices:

```python
{{d['session01/python/numpy_nb.py|idio|pycon']['Slicing']}}
```

## Methods

We can apply **methods** to objects. Which methods are available depend on the object's type:

``` python
{{d['session01/python/numpy_nb.py|idio|pycon']['Methods']}}
```

## Numpy Tools

Numpy provides cool tools like:

``` python
{{d['session01/python/numpy_nb.py|idio|pycon']['Axes']}}
```

## Plotting

> The purpose of computing is insight, not numbers
--- Richard Hamming

``` python
from matplotlib import pyplot as plt
plt.imshow(data)
plt.show()
```

![](session01/python/image.png)

## Something isn't right here
``` python
plt.plot(data.max(axis=0))
plt.show()
```

![](session01/python/dayrange.png)

## Make it a function

So we've built some figures which help us analyse these data sets.

We know we're going to have lots of similar experiments, so we'll want to wrap the code up into a **function**
which can be used repeatedly:
``` python
{{d['session01/python/analyzer.py|idio|t']['analyze']}}
```

Note that the only way Python knows that we're done with our function block is by unindenting!

## User defined types. 

Note that the result of type(image) is `matplotlib.figure.Figure`: the `matplotlib` library defines
its own new type, called a `class`, with its own methods, like `add_subplot`.

## Make it a module

We'd like our function to be usable by other people. So we'll wrap it up as it's own module.
We copy it out of the notebook into a file, and add a wrapper function to make it easy to call it to
produce an output on disk instead of in a notebook:

`analyzer.py`:
``` python
{{d['session01/python/analyzer.py|idio|t']['generate']}}
```

Here we see a conditional, a default argument value, and use of a library function to remove a file extension.

We can use this in other code, with, for example `import analyzer` and analyzer.generate('inflammation-01.csv', 'dest.png')

## Loop over many files

We'd like to be able to analyse many files at once.

``` python
{{d['session01/python/analyzer.py|idio|t']['bulk_generate']}}
```


## Call from the command line

We'll also add some magic to make it work as a command line tool:

```
#!/usr/bin/env python
...
{{d['session01/python/analyzer.py|idio|t']['main']}}
```

So now we can do:

```bash
chmod u+x analysis.py
./analysis.py data/*.csv
open data/inflammation-01.png
```


