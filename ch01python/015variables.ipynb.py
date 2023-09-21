# ---
# jupyter:
#   jekyll:
#     display_name: Variables
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Variables

# %% [markdown]
# ### Variable Assignment

# %% [markdown]
# When we generate a result, the answer is displayed, but not kept anywhere.

# %%
2 * 3

# %% [markdown]
# If we want to get back to that result, we have to store it. We put it in a box, with a name on the box. This is a **variable**.

# %%
six = 2 * 3

# %%
print(six)

# %% [markdown]
# If we look for a variable that hasn't ever been defined, we get an error. 

# %%
print(seven)

# %% [markdown]
# That's **not** the same as an empty box, well labeled:

# %%
nothing = None

# %%
print(nothing)

# %%
type(None)

# %% [markdown]
# (None is the special python value for a no-value variable.)

# %% [markdown]
# *Supplementary Materials*: There's more on variables at [Software Carpentry's Python lesson](https://swcarpentry.github.io/python-novice-inflammation/01-intro.html).

# %% [markdown]
# Anywhere we could put a raw number, we can put a variable label, and that works fine:

# %%
print(5 * six)

# %%
scary = six * six * six

# %%
print(scary)

# %% [markdown]
# ### Reassignment and multiple labels

# %% [markdown]
# But here's the real scary thing: it seems like we can put something else in that box:

# %%
scary = 25

# %%
print(scary)

# %% [markdown]
# Note that **the data that was there before has been lost**. 

# %% [markdown]
# No labels refer to it any more - so it has been "Garbage Collected"! We might imagine something pulled out of the box, and thrown on the floor, to make way for the next occupant.

# %% [markdown]
# In fact, though, it is the **label** that has moved. We can see this because we have more than one label refering to the same box:

# %%
name = "Eric"

# %%
nom = name

# %%
print(nom)

# %%
print(name)

# %% [markdown]
# And we can move just one of those labels:

# %%
nom = "Idle"

# %%
print(name)

# %%
print(nom)

# %% [markdown]
# So we can now develop a better understanding of our labels and boxes: each box is a piece of space (an *address*) in computer memory.
# Each label (variable) is a reference to such a place.

# %% [markdown]
# When the number of labels on a box ("variables referencing an address") gets down to zero, then the data in the box cannot be found any more.

# %% [markdown]
# After a while, the language's "Garbage collector" will wander by, notice a box with no labels, and throw the data away, **making that box
# available for more data**.

# %% [markdown]
# Old fashioned languages like C and Fortran don't have Garbage collectors. So a memory address with no references to it
# still takes up memory, and the computer can more easily run out.

# %% [markdown]
# So when I write:

# %%
name = "Michael"

# %% [markdown]
# The following things happen:

# %% [markdown]
# 1. A new text **object** is created, and an address in memory is found for it.
# 1. The variable "name" is moved to refer to that address.
# 1. The old address, containing "James", now has no labels.
# 1. The garbage collector frees the memory at the old address.

# %% [markdown]
# **Supplementary materials**: There's an online python tutor which is great for visualising memory and references. Try the [scenario we just looked at](http://www.pythontutor.com/visualize.html#code=name%20%3D%20%22Eric%22%0Anom%20%3D%20name%0Aprint%28nom%29%0Aprint%28name%29%0Anom%20%3D%20%22Idle%22%0Aprint%28name%29%0Aprint%28nom%29%0Aname%20%3D%20%22Michael%22%0Aprint%28name%29%0Aprint%28nom%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).
#
# Labels are contained in groups called "frames": our frame contains two labels, 'nom' and 'name'.

# %% [markdown]
# ### Objects and types

# %% [markdown]
# An object, like `name`, has a type. In the online python tutor example, we see that the objects have type "str".
# `str` means a text object: Programmers call these 'strings'. 

# %%
type(name)

# %% [markdown]
# Depending on its type, an object can have different *properties*: data fields Inside the object.

# %% [markdown]
# Consider a Python complex number for example:

# %%
z = 3 + 1j

# %% [markdown]
# We can see what properties and methods an object has available using the `dir` function:

# %%
dir(z)

# %% [markdown]
# You can see that there are several methods whose name starts and ends with `__` (e.g. `__init__`): these are special methods that Python uses internally, and we will discuss some of them later on in this course. The others (in this case, `conjugate`, `img` and `real`) are the methods and fields through which we can interact with this object.

# %%
type(z)

# %%
z.real

# %%
z.imag

# %% [markdown]
# A property of an object is accessed with a dot.

# %% [markdown]
# The jargon is that the "dot operator" is used to obtain a property of an object.

# %% [markdown]
# When we try to access a property that doesn't exist, we get an error:

# %%
z.wrong

# %% [markdown]
# ### Reading error messages.

# %% [markdown]
# It's important, when learning to program, to develop an ability to read an error message and find, from in amongst
# all the confusing noise, the bit of the error message which tells you what to change!

# %% [markdown]
# We don't yet know what is meant by `AttributeError`, or "Traceback".

# %%
z2 = 5 - 6j
print("Gets to here")
print(z.wrong)
print("Didn't get to here")

# %% [markdown]
# But in the above, we can see that the error happens on the **third** line of our code cell.

# %% [markdown]
# We can also see that the error message: 
# > 'complex' object has no attribute 'wrong' 
#
# ...tells us something important. Even if we don't understand the rest, this is useful for debugging!

# %% [markdown]
# ### Variables and the notebook kernel

# %% [markdown]
# When I type code in the notebook, the objects live in memory between cells.

# %%
number = 0

# %%
print(number)

# %% [markdown]
# If I change a variable:

# %%
number = number + 1

# %%
print(number)

# %% [markdown]
# It keeps its new value for the next cell.

# %% [markdown]
# But cells are **not** always evaluated in order.

# %% [markdown]
# If I now go back to Input 31, reading `number = number + 1`, I can run it again, with Shift-Enter. The value of `number` will change from 2 to 3, then from 3 to 4 - but the output of the next cell (containing the `print` statement) will not change unless I rerun that too. Try it!

# %% [markdown]
# So it's important to remember that if you move your cursor around in the notebook, it doesn't always run top to bottom.

# %% [markdown]
# **Supplementary material**: (1) [Jupyter notebook documentation](https://jupyter-notebook.readthedocs.io/en/latest/).
