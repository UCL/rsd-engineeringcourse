Construction
============

Construction
------------

Software *design* gets a lot of press (Object orientation, UML, design patterns)

In this session we're going to look at advice on software *construction*

Coding Conventions
==================

One code, many layouts:
-----------------------

Consider the following fragment of C++

``` cpp
reactor::Species & reactor::ReactionSystem::NewSpecies(const std::string &name){
	species.push_back(new Species(name));
	return *species.back();
}
```

This could also have been written:

``` cpp
using namespace std;

namespace reactor
{

 species & reactionsystem::new_species(const string& a_Name)
 {

  species.push_back( new species( name ));
  return *(species.back());

 }
}
```

So many choices
---------------

* Layout
* Naming
* Syntax choices

Layout
-----------

```cpp
declaration {
   contents
}
```

vs

```cpp
declaration
{
	contents
}
```

Layout choices
-----------

* Brace style
* Line length
* Indentation
* Whitespace/Tabs

Nameing Conventions
-------------------

``` cpp
ClassName
methodName
variable_name
```

vs

```cpp
ClassName
method_name
l_local_variable
m_instance_variable
s_class_variable
```

Hungarian Notation
-------------

Prefix denotes *type*:

``` c
lAnInteger
lpAPointer
szAString
rwAMatrixRow
```

Newlines
--------

* Newlines make code easier to read
* Newlines make less code fit on a screen

Use newlines to describe your code's *rhythm*

Syntax Choices
--------------

``` cpp
if ((variable==anothervariable++)&&flag1||flag2) do_something;
```

vs

``` cpp
anothervariable++;
bool const variable_equality = variable == anothervariable;
if ((variable_equality && flag1) || flag2) {
   do_something;
}
```

Syntax choices
--------------

* Compound statements
* Explicit operator precedence
* Compound controlled statements
* Namespace choices

Coding Conventions
------------------

You should try to have an agreed policy for your team for these matters.

If your language sponsor has a standard policy, use that.

E.g. [Python PEP8](http://legacy.python.org/dev/peps/pep-0008/)

E.g. [Google's guide for R](https://google-styleguide.googlecode.com/svn/trunk/Rguide.xml)

E.g. [Google's style guide for C++](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml)

Comments
========

Bad Comments
--------

"I write good code, you can tell by the number of comments."

This is wrong.

Comments which are obvious
---------------------------

``` cpp
i += 1 ; // Add one to i
j += 1 ; // Increment the index variable
```

``` python
for element in array: # Loop over elements
```

Comments which could be replaced by better style
------------------------------------------------

```cpp
for (int i=0;i<agent_count;i++){ // for each agent
agt[i].theta+=ws[i]; // Increment the angle of each agent by its angular velocity
agt[i].x+=r*sin(agt[i].theta); // Move the agent by the step-size r in the direction indicated
agt[i].y+=r*cos(agt[i].theta);
}
```

compared to:

``` cpp
for (Agent& agent: agents){ // C++11 range-based for loop
  agent.turn();
  agent.move();
}

Agent::turn(){
   direction+=angular_velocity;
}
Agent::move(){
   // Angle is measured clockwise from +ve y-axis
   x+=step_length*sin(direction);
   y+=step_length*cos(direction);
}
```

Comments which could be replaced by better style
------------------------------------------------


“The proper use of comments is to compensate for our failure to express yourself in code. 
Note that I used the word failure. I meant it. Comments are always failures.”

-- Robert Martin, [Clean Code](http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882).

Comments which belong in an issue tracker
-----------------------------------------

``` cpp
delete x; // Code crashes here sometimes
```

``` cpp
class Agent {
   // TODO: Implement pretty-printer method
}
```

``` cpp
typedef const struct direct direct_t; // Doesn't compile on OSX
```

BUT 

``` cpp
if (x->safe()){ // Guard added as temporary fix to #32
   delete x;
}
```

is OK.

Comments which only make sense to the author today
--------------------------------------------------

``` cpp
agent.turn(); // Turtle Power!
agent.move();
delete *agent; // Shredder!
```

Comments which are unpublishable
--------------------------------

``` cpp
// Stupid supervisor made me write this code
// So I did it while very very drunk.
```

Good comments
=============

Pedagogical comments
--------------------

Code that *is* good style, but you're not familiar with, or 
that colleagues might not be familiar with

``` cpp
for (auto agent : agents) { \\ C++11 range based for loop 
```

``` python

# This is how you define a decorator in python
def double(decorated_function):
   # Here, the result function forms a closure over the decorated function
   def result_function(input):
     return decorated_function(decorated_function(input))
   # The returned result is a function
   return result_function

@double
def try_me_twice():
   pass
```

Documentation as comments
-------------------------

``` cpp
//! \brief Creates parameter structure from HDF5 input.
//! \param[in] _filename File to read data from
//! \param[in] _flags when opening file
//! \tparam DIMS number of dimensions. Should be 2 or 3, and the content of the file should
//! correspond.
//! \tparam T_SCALAR type of scalar to use in calculations. Should be float, double, or long
//! double.
template<t_dimensionality DIMS, class T_SCALAR KWAVE_MACRO>
  ElastikParameters<DIMS, T_SCALAR> parameters_from_hdf5( std::string const &_filename,
                                                          unsigned int _flags = H5F_ACC_RDONLY ) {
    return parameters_from_hdf5<DIMS, t_real>(HDF5_File(_filename, _flags));
  }
```
Documentation as comments
-------------------------

``` python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    ... #content    
```

``` 
>>> help(complex)
 |  complex(real[, imag]) -> complex number
 |
 |  Create a complex number from a real part and an optional imaginary part.
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.
```


Other good comments
-------------------

``` cpp
double angle; // clockwise from +ve y-axis
vector<int> nonzero_indices; // Use sparse model as memory constrained
// Populate the collision count arrays.
for (unsigned collisionType = 0; collisionType < COLLISION_TYPES; collisionType++)
{
   midDomainProcCollisions[collisionType] = midDomainBlockNumbers[collisionType].size();
   domainEdgeProcCollisions[collisionType] = domainEdgeBlockNumbers[collisionType].size();
}
```

Documentation
=============

Documentation is hard
---------------------

* Good documentation is hard, and very expensive.
* Bad documentation is detrimental.
* Good documentation quickly becomes bad if not kept up-to-date with code changes.
* Professional companies pay large teams of documentation writers.

Prefer readable code with tests and vignettes
---------------------------------------------

If you don't have the capacity to maintain great documentation,
focus on:

* Readable code
* Automated tests
* Small code samples demonstrating how to use the api

Comment-based Documentation tools
-------------------

Documentation tools can produce extensive documentation about your code by pulling out comments near the beginning of functions,
together with the signature, into a web page.

The most popular is [Doxygen](http://www.stack.nl/~dimitri/doxygen/)

[Have a look at an example of some Doxygen output](
http://www.bempp.org/cppref/2.0/group__abstract__boundary__operators.html)

[Sphinx](http://sphinx-doc.org/) is nice for Python, and works with C++ as well.
Here's some [Sphinx-generated output](http://www.bempp.org/pythonref/2.0/bempp_visualization2.html)
and the [corresponding source code](https://github.com/bempp/bempp/blob/master/python/bempp/visualization2.py)
[Breathe](http://michaeljones.github.io/breathe/ ) can be used to make Sphinx and Doxygen work together.

[Roxygen](http://www.rstudio.com/ide/docs/packages/documentation) is good for R.

Refactoring
===========

Refactoring
-----------

To refactor is to:

* Make a change to the design of some software
* Which improves the structure or readability
* But which leaves the actual behaviour of the program completely unchanged.


A word from the Master
----------------------

> Refactoring is a controlled technique for improving the design of an existing code base. Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". However the cumulative effect of each of these transformations is quite significant. By doing them in small steps you reduce the risk of introducing errors. You also avoid having the system broken while you are carrying out the restructuring - which allows you to gradually refactor a system over an extended period of time.

-- Martin Fowler

List of known refactorings
--------------------------

The next few sections will present some known refactorings

We'll show before and after code, present any new coding techniques needed to do the refactoring,
and describe *code smells*: how you know you need to refactor.

Replace magic numbers with constants
------------------------------------

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

Replace repeated code with a function
-------------------------------------

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

Change of variable name
-----------------------

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


Replace loop with iterator
--------------------------

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

Replace hand-written code with library code
-------------------------------------------

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

Replace set of arrays with array of structures
-------------------------------------

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

Replace add-hoc structure with user defined classes
---------------------------------------------------

Smell: A data structure made of nested arrays and dictionaries becomes unwieldy

Before:

``` python
from random import random
birds = [{"position": random(), "velocity": random(), "type": type} for type in bird_types]
average_position = average([bird["position"] for bird in birds])
```

After:

``` python
class Bird(Object):
	def __init__(type):
    from random import random
		self.type = type
		self.position = random()
		self.velocity = random()

birds = [Bird(type) for type in bird_types]
average_position = average(bird.position for bird in birds)
```


Replace function with a method
------------------------------

Smell: A function is always called with the same kind of thing

Before:

``` python
def can_see(source,target):
	return (source.facing-target.facing)<source.viewport

if can_see(hawk,starling):
	hawk.hunt()
```

After:

``` python
class Bird(Object):
	def can_see(self,target):
		return (self.facing-target.facing)<self.viewport

if hawk.can_see(starling):
	hawk.hunt()
```

Replace constants with a configuration file
-------------------------------------------

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

Replace global variables with function arguments
------------------------------------------------

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

Replace method arguments with class members
---------------------------------------------

Smell: A variable is nearly always used in arguments to 
a class.

```cpp
class Person
{
  Person();
  float reproduce_probability(unsigned int age);
  float death_probability(unsigned int age);
  float emigrate_probability(unsigned int age);
}
```

After:

```cpp
class Person
{
  Person(unsigned int age);
  float reproduce_probability();
  float death_probability();
  float emigrate_probability();
}
```

Break a large function into smaller units
-----------------------------------------

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

class Predator(Object):
   def predate(self,prey):
      if predator.can_see(prey):
         predator.hunt(prey)
      if predator.can_reach(prey):
         predator.eat(prey)
```

Separate code concepts into files or modules
--------------------------------------------

Smell: You find it hard to locate a piece of code<br>
Smell: You get a lot of version control conflicts

Before:

```python
class One(Object):
   ...


class Two(Object):
  def __init__():
    self.child=One()
```

After:

``` python
from anotherfile import One

class Two(Object):
   def __init__():
      self.child=One()
```


Refactoring is a safe way to improve code
-----------------------------------------

You may think you can see how to rewrite a whole codebase to be better

However, you may well get lost halfway through the exercise.

By making the changes as small, reversible, incremental steps,
you can reach your target design more reliably.

Tests and Refactoring
---------------------

Badly structured code cannot be unit tested. There are no "units".

Before refactoring, ensure you have a robust regression test.

This will allow you to *Refactor with confidence*

As you refactor, if you create any new units (functions, modules, classes)

Refactoring Summary
-------------------

* Replace magic numbers with constants
* Replace repeated code with a function
* Change of variable/function/class name
* Replace loop with iterator
* Replace hand-written code with library code
* Replace set of arrays with array of structures
* Replace ad-hoc structure with a class
* Replace function with a method
* Replace constants with a configuration file
* Replace global variables with function arguments
* Replace method argument with class member
* Break a large function into smaller units
* Separate code concepts into files or modules

And many more

Read [The Refactoring Book](http://www.amazon.co.uk/Refactoring-Improving-Design-Existing-Technology/dp/0201485672)

Exercise: The Boids
===================

Flocking
--------

> The aggregate motion of a flock of birds, a herd of land animals, or a school of fish is a beautiful and familiar part of the natural world... The aggregate motion of the simulated flock is created by a distributed behavioral model much like that at work in a natural flock; the birds choose their own course. Each simulated bird is implemented as an independent actor that navigates according to its local perception of the dynamic environment, the laws of simulated physics that rule its motion, and a set of behaviors programmed into it... The aggregate motion of the simulated flock is the result of the dense interaction of the relatively simple behaviors of the individual simulated birds. 

-- Craig W. Reynolds, "Flocks, Herds, and Schools: A Distributed Behavioral Model", *Computer Graphics* **21** _4_ 1987, pp 25-34
See the [original paper](http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/)

Boids
-----

* Collision Avoidance: avoid collisions with nearby flockmates
* Velocity Matching: attempt to match velocity with nearby flockmates
* Flock Centering: attempt to stay close to nearby flockmates

Bad_Boids
---------

I have written some _very bad_ code implementing Boids, based on [Konrad Parker's](http://www.kfish.org/) pseudocode.

Here's the [Github link](https://github.com/jamespjh/bad-boids).

Please fork it on GitHub, and clone your fork.

``` bash
git clone     git@github.com:yourname/bad-boids.git # OR
git clone https://github.com/yourname/bad-boids.git
```


Look at the birdies!
--------------------

Run bad_boids:

```bash
cd bad_boids
python bad_boids.py
```

You should be able to see some birds flying around, and then disappearing as they leave the window.

Your Task
---------

Transform bad_boids into better code, while making sure it still works.

A regression test
-----------------

First, have a look at the regression test I made.

To create it, I saved out the before and after state
for one iteration of some boids, using ipython:

``` python
import yaml
import boids
from copy import deepcopy
before=deepcopy(boids.boids)
boids.update_boids(boids.boids)
after=boids.boids
fixture={"before":before,"after":after}
fixture_file=open("fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
```

A regression test
-----------------

Then, I used the fixture file to define the test:

```python
from boids import update_boids
from nose.tools import assert_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    assert_equal(regression_data["after"],boid_data)
```

Make the regression test fail
-----------------------------

Check the tests pass:

``` bash
nosetests
```

Edit the file to make the test fail, see the fail, then reset it:

```bash
git checkout boids.py
```

Start Refactoring
-----------------

Look at the code, consider the [list of refactorings](#refactoring-summary), and make changes

Each time, do a git commit on your fork, and write a commit message explaining the 
refactoring you did.

Try to keep the changes as small as possible.

If your refactoring creates any units, (functions, modules, or classes)
write a unit test for the unit.


