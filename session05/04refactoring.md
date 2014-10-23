---
title: Comments
---

##Refactoring

###Refactoring

To refactor is to:

* Make a change to the design of some software
* Which improves the structure or readability
* But which leaves the actual behaviour of the program completely unchanged.


###A word from the Master

> Refactoring is a controlled technique for improving the design of an existing code base. 
Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". 
However the cumulative effect of each of these transformations is quite significant. 
By doing them in small steps you reduce the risk of introducing errors. 
You also avoid having the system broken while you are carrying out the restructuring - 
which allows you to gradually refactor a system over an extended period of time.

-- Martin Fowler

###List of known refactorings

The next few sections will present some known refactorings

We'll show before and after code, present any new coding techniques needed to do the refactoring,
and describe *code smells*: how you know you need to refactor.

###Replace magic numbers with constants

Smell: Raw numbers appear in your code

Before:

``` python
data= [math.sin(x) for x in np.arange(0,3.141,3.141/100)]
result= [0]*100
for i in range(100):
   for j in range(i+1, 100):
     result[j] += data[i] * data[i-j] / 100
```

after:

``` python
resolution=100
pi=3.141
data= [math.sin(x) for x in np.arange(0,pi,pi/resolution)]
result= [0]*resolution
for i in range(resolution):
   for j in range(i + 1, resolution):
     result[j] += data[i] * data[i-j] / resolution
```

###Replace repeated code with a function

Smell: Fragments of repeated code appear

Before:

``` python
if abs(hawk.facing-starling.facing)<hawk.viewport:
	hawk.hunting()
if abs(starling.facing-hawk.facing)<starling.viewport:
	starling.flee()
```

After:

``` python
def can_see(source,target):
	return (source.facing-target.facing)<source.viewport
if can_see(hawk,starling):
	hawk.hunting()
if can_see(starling,hawk):
	starling.flee()
```

###Change of variable name

Smell: Code needs a comment to explain what it is for

Before:

``` python
z=find(x,y):
if z:
   ribe(x)
```

After:

``` python
gene = subsequence(chromosome, start_codon)
if gene:
    transcribe(gene)
```


###Separate a complex expression into a local variable

Smell: An expression becomes long

``` cpp
if ((my_name==your_name++)&&flag1||flag2) do_something;
```

vs

``` cpp
const bool same_names= (my_name==your_name);
if (same_names && flag1 || flag2) do_something;
```

###Replace loop with iterator

Smell: Loop variable is an integer from 1 to something

Before:

``` python
sum=0
for i in range(resolution):
	sum+=data[i]	
```

After:

``` python
sum=0
for value in data:
	sum+=value
```

###Replace hand-written code with library code

Smell: It feels like surely someone else must have done this at some point

Before:

``` python
xcoords=[start+i*step for i in range(int((end-start)/step))]
```

After:

``` python
import numpy as np
xcoords=np.arange(start,end,step)
```

See [Numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html),
    [Pandas](http://pandas.pydata.org/)

###Replace set of arrays with array of structures

Smell: A function needs to work corresponding indices of several arrays:

Before:

``` python
def can_see(index,source_angles,target_angles,source_viewports):
	return abs(source_angles[i]-target_angles[i])<source_viewports[i]
```

After:

``` python
def can_see(source,target):
	return (source["facing"]-target["facing"])<source["viewport"]
```

Warning: this refactoring improves readability but can make code slower,
depending on memory layout. Be careful.

###Replace constants with a configuration file

Smell: You need to change your code file to explore different research scenarios

Before:

``` python
flight_speed=2.0 # mph
bounds=[0,0,100,100]
turning_circle=3.0 # m
bird_counts: {"hawk": 5, "starling": 500}
```

After:

``` yaml
# config.yml
bounds: [0,0,100,100]
counts:
	hawk: 5
	starling: 500
speed: 2.0
turning_circle: 3.0
```

``` python
config=yaml.load(open(
	os.path.join(os.path.dirname(__file__),"config.yml")))
```

See [YAML](http://www.yaml.org/) and [PyYaml](http://pyyaml.org/)
and [Python OS](http://docs.python.org/2/library/os.html)

###Replace global variables with function arguments

Smell: A global variable is assigned and then used inside a called function:

``` python
viewport=pi/4
if hawk.can_see(starling):
	hawk.hunt(starling)

class Hawk(object):
	def can_see(self,target):
		return (self.facing-target.facing)<viewport
```

Becomes:

``` python
viewport=pi/4
if hawk.can_see(starling,viewport):
	hawk.hunt(starling)

class Hawk(object):
	def can_see(self,target,viewport):
		return (self.facing-target.facing)<viewport

```

###Merge neighbouring loops

Smell: Two neighbouring loops have the same for statement

``` python

for bird in birds:
    bird.build_nest()
for bird in birds:
    bird.lay_eggs()
``` 

Becomes:

``` python
for bird in birds:
    bird.build_nest()
    bird.lay_eggs()
```


###Break a large function into smaller units

Smell: A function or subroutine no longer fits on a page in your editor
Smell: A line of code is indented more than three levels

Before:

``` python
def do_calculation():
   for predator in predators:
      for prey in preys:
          if predator.can_see(prey):
             predator.hunt(prey)
          if predator.can_reach(prey):
             predator.eat(prey)
```

After:

``` python
def do_calculation():
   for predator in predators:
      for prey in preys:
          predator.predate(prey)

class Predator(object):
   def predate(self,prey):
      if predator.can_see(prey):
         predator.hunt(prey)
      if predator.can_reach(prey):
         predator.eat(prey)
```

###Separate code concepts into files or modules

Smell: You find it hard to locate a piece of code

Smell: You get a lot of version control conflicts

Before:

```python
class One(object):
   ...


class Two(object):
  def __init__():
    self.child=One()
```

After:

``` python
from anotherfile import One

class Two(object):
   def __init__():
      self.child=One()
```

###Refactoring is a safe way to improve code

You may think you can see how to rewrite a whole codebase to be better

However, you may well get lost halfway through the exercise.

By making the changes as small, reversible, incremental steps,
you can reach your target design more reliably.

###Tests and Refactoring

Badly structured code cannot be unit tested. There are no "units".

Before refactoring, ensure you have a robust regression test.

This will allow you to *Refactor with confidence*

As you refactor, if you create any new units (functions, modules, classes),
add new tests for them.

###Refactoring Summary

* Replace magic numbers with constants
* Replace repeated code with a function
* Change of variable/function/class name
* Replace loop with iterator
* Replace hand-written code with library code
* Replace set of arrays with array of structures
* Replace constants with a configuration file
* Replace global variables with function arguments
* Break a large function into smaller units
* Separate code concepts into files or modules

And many more

Read [The Refactoring Book](http://www.amazon.co.uk/Refactoring-Improving-Design-Existing-Technology/dp/0201485672)

