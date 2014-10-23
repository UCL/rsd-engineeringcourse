---
title: Debugging
---

##Using a Debugger

###Step by step through the code

Debugger

:   Program to test other programs. Allows programmers to suspend execution of the target program
    and inspect variables at that point.

<br>

* Mac -- compiled languages:
  [Xcode](https://developer.apple.com/library/ios/documentation/ToolsLanguages/Conceptual/Xcode_Overview/DebugYourApp/DebugYourApp.html)
* Windows -- compiled languages:
  [Visual Studio](http://msdn.microsoft.com/en-us/library/bb483011.aspx)
* Linux: [DDD](https://www.gnu.org/software/ddd/)
* all platforms: [eclipse](http://www.eclipse.org), [gdb](http://www.sourceware.org/gdb/) (DDD and
  eclipse are GUIs for gdb)
* python: [spyder](http://pythonhosted.org/spyder/index.html),
          [pdb](http://docs.python.org/2/library/pdb.html)
* R: [RStudio](http://www.rstudio.com/ide/docs/debugging/overview),
  [debug](http://stat.ethz.ch/R-manual/R-devel/library/base/html/debug.html),
  [browser](http://stat.ethz.ch/R-manual/R-devel/library/base/html/browser.html)

###Using the python debugger

<div align="left">
Copy the following into a file:
</div>

``` python
def energy(x):
   from numpy import array, sum
   x = array(x)
   return sum(x * (x - 1))

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

if __name__ == "__main__":
  partial_derivative(energy, [5, 6, 7, 8, 0, 1], 5)
```


###Basic Navigation:

<div align="left">
Basic command to navigate the code and the python debugger:

* `help`: prints the help
* `help n`: prints help about command `n`
* `n`(ext): executes one line of code. Executes and steps **over** functions.
* `s`(tep): step into current function in line of code
* `l`(ist): list program around current position
* `w`(where): prints current stack (where we are in code)
* `[enter]`: repeats last command

<br>
The python debugger is a python shell: it can print and compute values, and even change the values
of the variables at that point in the program.
</div>

###Breakpoints

<div align="left">
Break points tell debugger where and when to stop

``` python
>>> restart  # restart session
>>> b energy # program will stop when entering energy
>>> c        # continue program until break point is reached
```

Alternatively, break-points can be set on files: `b file.py:20` will stop on line 20 of `file.py`.

<div class="fragment=roll in">
Break-points can run subject  to a given condition evaluating to true

``` python
>>> cl # clear all breakpoints
>>> b energy, x[5] == 2
>>> restart
>>> c
```

</div>

</div>

###Post-Mortem

<div align="left">
Debugging when something goes wrong:

1. add `raise Exception("OMG!")` somewhere in the code
1. run `python -m pdb file.py`
1. hit `c`

<br>
The program should stop where the exception was raised

1. use `w` and `l` for position in code and in call stack
1. use `up` and `down` to navigate up and down the call stack
1. inspect variables along the way to understand failure
</div>
