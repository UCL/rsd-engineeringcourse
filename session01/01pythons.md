---
title: Many kinds of Python
---

# Many kinds of Python

## Many kinds of Python

There are many different ways to use Python:

* Python interpreter
* Python scripts
* IPython
* IPython Notebook

## Python at the command line

``` bash
$ python
Python 2.7.8 (default, Sep 19 2014, 17:15:25)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.51)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 2*4
8
>>> exit()
$ python -c "print 2*4"
8
```

## Python scripts

``` bash
$echo "print 2*4" > eight.py
$python eight.py
8
$echo '#!/usr/bin/env python' > eight
$cat eight.py >> eight
$chmod u+x eight
$./eight
8
```

## IPython

``` bash
$ ipython
Python 2.7.8 (default, Sep 19 2014, 17:15:25)
Type "copyright", "credits" or "license" for more information.

IPython 2.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 2*4
Out[1]: 8
In [2]: exit
```

## IPython Notebook

``` bash
$ git clone https://github.com/UCL/rsd-engineeringcourse.git
$ cd rsd-engineeringcourse/session01/notebooks
$ ipython notebook
```

![](session01/python/eight.png)
... look in your browser ...

## Install Python and IPython Notebook

* The demonstrators will assist with [installing IPython and git](installation)
