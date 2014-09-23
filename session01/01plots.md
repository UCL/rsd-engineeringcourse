
---
title: Simple data manipulation and plotting
---

## Working with and visualising data

# Why write software to manage your data and plots? 

We should use programs for our entire research pipeline.

Not just main simulation or numerical code, but also the small scripts which we use to
tidy up data and produce plots. 

This should be code, so that the whole research pipeline
is recorded for reproducibility. Data manipulation in spreadsheets cannot be shared or
checked. 

It should be *good* code, because research conclusions are just as wrong if the
plotting script is wrong as if the code that generates the data is wrong.

# Analysing patient data

(The next few slides are taken from Software Carpentry materials and are (CC-BY) the contributors at
https://github.com/swcarpentry/bc/blob/master/team.md)

You can follow along in an [IPython Notebook](session01/notebooks/01-numpy.nb)

# The data


Imagine you are studying inflammation in patients who have been given a new treatment for arthritis, 
and need to analyze the first dozen data sets. The data sets are stored in 
comma-separated values (CSV) format: 
each row holds information for a single patient, and the columns represent successive days. 
The first few rows of our first file look like this:

``` csv
0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,v
```

# The task

We want to:

*   load that data into memory,
*   calculate the average inflammation per day across all patients, and
*   plot the result.

This will give us a good overview of various concepts in Python, which we'll
return to some of after this initial survey.

# Loading data

It's almost always wrong to do things yourself.

Someone's probably written a program already. 
Python makes it easy to find and use other people's libraries.

In this case, we want to use a python library to load and parse the csv data, and manipulate it as 
a matrix.

``` python
import numpy
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print data
[[ 0.  0.  1. ...,  3.  0.  0.]
 [ 0.  1.  2. ...,  1.  0.  1.]
 [ 0.  1.  1. ...,  2.  1.  1.]
 ..., 
 [ 0.  1.  1. ...,  1.  1.  1.]
 [ 0.  0.  0. ...,  0.  2.  0.]
 [ 0.  0.  1. ...,  1.  1.  0.]]
```

Here we've called a **function** `loadtxt` from a **module** `numpy`, and
assigned it to a **variable** data. This course assumes you're happy with very basic
programming concepts like function and variable. The IPython notebook contains more detail.

# Types

```python
print type(data)
<type 'numpy.ndarray'>
print data.shape
(60, 40)
```

We've jumped straight in and used a `numpy.ndarray` (numerical python) matrix type for our data.
It's similar to a basic python `Array` type; we'll talk more about the differences later.

For now, it's important to know that Python variables have a type, that different types behave differently,
but that, unlike C++ or Fortran, you don't need to say what type of variable something is before you use it.

```python
print [type("Hello"),type(1), type([1,2,3])]
[<type 'str'>, <type 'int'>, <type 'list'>]
```

# Slicing and methods 

We can **slice** elements from arrays and matrices:

```python
print 'first value in data:', data[0, 0] #Top left element
print data[0:4, 0:10] # Top left few elements
print data[:3, 36:] #First three lines, last few columns
print data[:-1,:] #All but the last line, all columns
```

We can apply **methods** to objects. Which methods are available depend on the object's type:

```
print data.mean() # 6.14875
print data.std() # 4.613
patient_zero=data[0, :]
print 'maximum inflammation for patient 0:', patient_0.max()
print 'maximum inflammation for patient 2:', data[2, :].max()
```

Numpy provides cool tools like:

```
print data.mean(axis=1) # Average over days, per patient
print data.mean(axis=0) # Average over patients, per day
```

# Plotting

> The purpose of computing is insight, not numbers
--- Richard Hamming

``` python
from matplotlib import pyplot
pyplot.imshow(data)
pyplot.show()
```

TODO generate figure

# Something isn't right here
``` python
print 'maximum inflammation per day'
pyplot.plot(data.max(axis=0))
pyplot.show()

print 'minimum inflammation per day'
pyplot.plot(data.min(axis=0))
pyplot.show()
```

TODO generate figure

# Make it a function

So we've built some figures which help us analyse these data sets.

We know we're going to have lots of similar experiments, so we'll want to wrap the code up into a **function**
which can be used repeatedly:

``E python
def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    figure = plt.figure(figsize=(10.0, 3.0))

    subplot_average=figure.add_subplot(1, 3, 1)
    subplot_average.set_ylabel('average')
    subplot_average.plot(data.mean(0))

    subplot_max=figure.add_subplot(1, 3, 2)
    subplot_max.set_ylabel('max')
    subplot_max.plot(data.max(0))

    subplot_min=figure.add_subplot(1, 3, 3)
    subplot_min.set_ylabel('min')
    subplot_min.plot(data.min(0))

    figure.tight_layout()
    return figure

image=analyze('inflammation-01.csv')
```

TODO: Show figure

Note that the only way Python knows that we're done with our function block is by unindenting!
Note that the result of type(image) is `matplotlib.figure.Figure`: the `matplotlib` library defines
its own new type, called a `class`, with its own methods, like `add_subplot`. We'll learn more about classes
later.

# Make it a module

We'd like our function to be usable by other people. So we'll wrap it up as it's own module.
We copy it out of the notebook into a file, and add a wrapper function to make it easy to call it to
produce an output on disk instead of in a notebook:

`analysis.py`:
``` python
import os
def generate(filename, output=False):
    if not output_file:
        output_file = os.path.splitext(filename)[0] + '.png'
    analyze(filename).savefig(output)
```

Here we see a conditional, a default argument value, and use of a library function to remove a file extension.

We can use this in other code, with, for example `import analysis` and analysis.generate('inflammation-01.csv', 'dest.png')

# Loop over many files

We'd like to be able to analyse many files at once.

``` python
def bulk_generate(sources):
    for source in sources:
       generate(source)
```


# Call from the command line

We'll also add some magic to make it work as a command line tool:

```
#!/usr/bin/env python

import sys
...
if if __name__ == "__main__":
    bulk_generate(sys.argv[1:])
```

So now we can do:

```bash
chmod u+x analysis.py
./analysis.py data/*.csv
open data/inflammation-01.png
```


