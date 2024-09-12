# ---
# jupyter:
#   jekyll:
#     display_name: Refactoring
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Refactoring

# %% [markdown]
# Let's import first the context for this chapter.

# %%
from context import *

# %% [markdown]
# Let's put ourselves in an scenario - that you've probably been in before. Imagine you are changing a large piece of legacy code that's not well structured, introducing many changes at once, trying to keep in your head all the bits and pieces that need to be modified to make it all work again. And suddenly, your officemate comes and ask you to go for coffee... and you've lost all track of what you had in your head and need to start again.
#
# Instead of doing so, we could use a more robust approach to go from nasty ugly code to clean code in a safer way.

# %% [markdown]
# ## Refactoring

# %% [markdown]
#
# To refactor is to:
#
# * Make a change to the design of some software
# * Which improves the structure or readability
# * But which leaves the actual behaviour of the program completely unchanged.
#
#

# %% [markdown]
# ## A word from the Master

# %% [markdown]
#
# > Refactoring is a controlled technique for improving the design of an existing code base. 
# Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". 
# However the cumulative effect of each of these transformations is quite significant. 
# By doing them in small steps you reduce the risk of introducing errors. 
# You also avoid having the system broken while you are carrying out the restructuring - 
# which allows you to gradually refactor a system over an extended period of time.
#
# -- Martin Fowler [Refactoring](https://martinfowler.com/books/refactoring.html) [[UCL library](https://ucl-new-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=UCL_LMS_DS21146093980004761)].
#

# %% [markdown]
# ## List of known refactorings

# %% [markdown]
#
# The next few sections will present some known refactorings.
#
# We'll show before and after code, present any new coding techniques needed to do the refactoring, and describe [*code smells*](https://en.wikipedia.org/wiki/Code_smell): how you know you need to refactor.
#

# %% [markdown]
# ## Replace magic numbers with constants

# %% [markdown]
#
# Smell: Raw numbers appear in your code
#
# Before: 
#
#
#

# %%
data = [math.sin(x) for x in np.arange(0,3.141,3.141/100)]
result = [0]*100
for i in range(100):
    for j in range(i+1, 100):
        result[j] += data[i] * data[i-j] / 100

# %% [markdown]
#
#
#
# after:
#
#
#

# %%
resolution = 100
pi = 3.141
data = [math.sin(x) for x in np.arange(0, pi, pi/resolution)]
result = [0] * resolution
for i in range(resolution):
    for j in range(i + 1, resolution):
        result[j] += data[i] * data[i-j] / resolution

# %% [markdown]
#
#
#

# %% [markdown]
# ## Replace repeated code with a function

# %% [markdown]
#
# Smell: Fragments of repeated code appear.
#
# Fragment of model where some birds are chasing each other: if the angle of view of one can see the prey, then start hunting, and if the other see the predator, then start running away.
#
# Before:
#
#
#

# %%
if abs(hawk.facing - starling.facing) < hawk.viewport:
    hawk.hunting()

if abs(starling.facing - hawk.facing) < starling.viewport:
    starling.flee()


# %% [markdown]
#
#
#
# After:
#
#
#

# %%
def can_see(source, target):
    return (source.facing - target.facing) < source.viewport

if can_see(hawk, starling):
    hawk.hunting()

if can_see(starling, hawk):
    starling.flee()

# %% [markdown]
#
#
#

# %% [markdown]
# ## Change of variable name

# %% [markdown]
#
# Smell: Code needs a comment to explain what it is for.
#
# Before:
#
#
#

# %%
z = find(x,y)
if z:
    ribe(x)

# %% [markdown]
#
#
#
# After:
#
#
#

# %%
gene = subsequence(chromosome, start_codon)
if gene:
    transcribe(gene)

# %% [markdown]
# ## Separate a complex expression into a local variable

# %% [markdown]
#
# Smell: An expression becomes long.
#
#
#

# %%
if ((my_name == your_name) and flag1 or flag2): do_something()

# %% [markdown]
#
#
#
# vs
#
#
#

# %%
same_names = (my_name == your_name)
flags_OK = flag1 or flag2
if same_names and flags_OK:
    do_something()

# %% [markdown]
# ## Replace loop with iterator

# %% [markdown]
#
# Smell: Loop variable is an integer from 1 to something.
#
# Before:
#
#
#

# %%
sum = 0
for i in range(resolution):
    sum += data[i]

# %% [markdown]
#
#
#
# After:
#
#
#

# %%
sum = 0
for value in data:
    sum += value

# %% [markdown]
# ## Replace hand-written code with library code

# %% [markdown]
#
# Smell: It feels like surely someone else must have done this at some point.
#
# Before:
#
#
#

# %%
xcoords = [start + i * step for i in range(int((end - start) / step))]

# %% [markdown]
#
#
#
# After:
#
#
#

# %%
import numpy as np
xcoords = np.arange(start, end, step)


# %% [markdown]
#
#
#
# See [Numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html),
#     [Pandas](http://pandas.pydata.org/).
#

# %% [markdown]
# ## Replace set of arrays with array of structures

# %% [markdown]
#
# Smell: A function needs to work corresponding indices of several arrays:
#
# Before:
#
#
#

# %%
def can_see(i, source_angles, target_angles, source_viewports):
    return abs(source_angles[i] - target_angles[i]) < source_viewports[i]


# %% [markdown]
#
#
#
# After:
#
#
#

# %%
def can_see(source, target):
    return (source["facing"] - target["facing"]) < source["viewport"]


# %% [markdown]
#
#
#
# Warning: this refactoring greatly improves readability but can make code slower,
# depending on memory layout. Be careful.
#

# %% [markdown]
# ## Replace constants with a configuration file

# %% [markdown]
#
# Smell: You need to change your code file to explore different research scenarios.
#
# Before:
#
#
#

# %%
flight_speed = 2.0 # mph
bounds = [0, 0, 100, 100]
turning_circle = 3.0 # m
bird_counts = {"hawk": 5, "starling": 500}

# %% [markdown]
#
#
#
# After:
#
#
#
#
#
#

# %%
# %%writefile config.yaml
bounds: [0, 0, 100, 100]
counts:
    hawk: 5
    starling: 500
speed: 2.0
turning_circle: 3.0

# %% [markdown]
#
#
#
#
#

# %%
config = yaml.safe_load(open("config.yaml"))

# %% [markdown]
#
# See [YAML](http://www.yaml.org/) and [PyYaml](http://pyyaml.org/),
# and [Python's os module](https://docs.python.org/3/library/os.html).
#

# %% [markdown]
# ## Replace global variables with function arguments

# %% [markdown]
#
# Smell: A global variable is assigned and then used inside a called function:
#
#
#

# %%
viewport = pi/4

if hawk.can_see(starling):
    hawk.hunt(starling)

class Hawk(object):
    def can_see(self, target):
        return (self.facing - target.facing) < viewport


# %% [markdown]
#
#
#
# Becomes:
#
#
#

# %%
viewport = pi/4
if hawk.can_see(starling, viewport):
    hawk.hunt(starling)

class Hawk(object):
    def can_see(self, target, viewport):
        return (self.facing - target.facing) < viewport


# %% [markdown]
# ## Merge neighbouring loops

# %% [markdown]
#
# Smell: Two neighbouring loops have the same for statement
#
#
#

# %%
for bird in birds:
    bird.build_nest()

for bird in birds:
    bird.lay_eggs()

# %% [markdown]
#
#
#
# Becomes:
#
#
#

# %%
for bird in birds:
    bird.build_nest()
    bird.lay_eggs()


# %% [markdown]
# Though there may be a case where all the nests need to be built before the birds can start laying eggs.

# %% [markdown]
# ## Break a large function into smaller units

# %% [markdown]
#
# * Smell: A function or subroutine no longer fits on a page in your editor.
# * Smell: A line of code is indented more than three levels.
# * Smell: A piece of code interacts with the surrounding code through just a few variables.
#
# Before:
#
#
#

# %%
def do_calculation():
    for predator in predators:
        for prey in preys:
            if predator.can_see(prey):
                predator.hunt(prey)
            if predator.can_reach(prey):
                predator.eat(prey)


# %% [markdown]
#
#
#
# After:
#
#
#

# %%
def do_calculation():
    for predator in predators:
        for prey in preys:
            predate(predator, prey)

def predate(predator, prey):
    if predator.can_see(prey):
        predator.hunt(prey)
    if predator.can_reach(prey):
        predator.eat(prey)


# %% [markdown]
# ## Separate code concepts into files or modules

# %% [markdown]
#
# Smell: You find it hard to locate a piece of code.
#
# Smell: You get a lot of version control conflicts.
#
# Before:
#
#
#

# %%
class One(object):
    pass

class Two(object):
    def __init__():
        self.child = One()


# %% [markdown]
#
#
#
# After:
#
#
#

# %%
# %%writefile anotherfile.py
class One(object):
    pass


# %%
from anotherfile import One

class Two(object):
    def __init__():
        self.child = One()

# %% [markdown]
# ## Refactoring is a safe way to improve code

# %% [markdown]
#
# You may think you can see how to rewrite a whole codebase to be better.
#
# However, you may well get lost halfway through the exercise.
#
# By making the changes as small, reversible, incremental steps,
# you can reach your target design more reliably.
#

# %% [markdown]
# ## Tests and Refactoring

# %% [markdown]
#
# Badly structured code cannot be unit tested. There are no "units".
#
# Before refactoring, ensure you have a robust regression test.
#
# This will allow you to *Refactor with confidence*.
#
# As you refactor, if you create any new units (functions, modules, classes),
# add new tests for them.
#

# %% [markdown]
# ## Refactoring Summary

# %% [markdown]
#
# * Replace magic numbers with constants
# * Replace repeated code with a function
# * Change of variable/function/class name
# * Replace loop with iterator
# * Replace hand-written code with library code
# * Replace set of arrays with array of structures
# * Replace constants with a configuration file
# * Replace global variables with function arguments
# * Break a large function into smaller units
# * Separate code concepts into files or modules
#
# And many more...
#
# Read [The Refactoring Book](https://martinfowler.com/books/refactoring.html).
#
#
#
