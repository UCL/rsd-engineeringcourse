# ---
# jupyter:
#   jekyll:
#     display_name: Containers
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Containers
#
# Containers are a data type that _contains_ other objects.

# %% [markdown]
# ## Lists

# %% [markdown]
# Python's basic **container** type is the `list`

# %% [markdown]
# We can define our own list with square brackets:

# %%
[1, 3, 7]

# %%
type([1, 3, 7])

# %% [markdown]
# Lists *do not* have to contain just one type:

# %%
various_things = [1, 2, "banana", 3.4, [1, 2]]

# %% [markdown]
# We access an **element** of a list with an `int` in square brackets:

# %%
one = 1
two = 2
three = 3

# %%
my_new_list = [one, two, three]

# %%
middle_value_in_list = my_new_list[1]

# %%
middle_value_in_list

# %%
[1, 2, 3][1]

# %%
various_things[2]

# %%
index = 2
various_things[index]

# %% [markdown]
# Note that list indices start from zero.

# %% [markdown]
# We can quickly make a list containing a range of consecutive integer numbers using the built-in `range` function

# %%
count_to_five = list(range(5))
print(count_to_five)

# %% [markdown]
# We can use a string to join together a list of strings:

# %%
name = ["Grace", "Brewster", "Murray", "Hopper"]
print(" ".join(name))

# %% [markdown]
# And we can split up a string into a list:

# %%
"Ernst Stavro Blofeld".split(" ")

# %% [markdown]
# We can an item to a list:

# %%
name.append("BA")
print(" ".join(name))

# %% [markdown]
# Or we can add more than one:

# %%
name.extend(["MS", "PhD"])
print(" ".join(name))

# %% [markdown]
# Or insert values at different points in the list

# %%
name.insert(0, "Admiral")
print(" ".join(name))

# %% [markdown]
# ## Sequences

# %% [markdown]
# Many other things can be treated like `lists`. Python calls things that can be treated like lists _sequences_.

# %% [markdown]
# A string is one such *sequence type*

# %%
print(count_to_five[1])
print("James"[2])

# %%
print(count_to_five[1:3])
print("Hello World"[4:8])

# %%
print(len(various_things))
print(len("Python"))

# %%
len([[1, 2], 4])

# %% [markdown]
# ## Unpacking

# %% [markdown]
# Multiple values can be **unpacked** when assigning from sequences, like dealing out decks of cards.

# %%
mylist = ["Goodbye", "Cruel"]
a, b = mylist
print(a)

# %%
a = mylist[0]
b = mylist[1]

# %% [markdown]
# ## Checking for containment

# %% [markdown]
# The `list` we saw is a container type: its purpose is to hold other objects. We can ask python whether or not a
# container contains a particular item:

# %%
"Dog" in ["Cat", "Dog", "Horse"]

# %%
"Bird" in ["Cat", "Dog", "Horse"]

# %%
2 in range(5)

# %%
99 in range(5)

# %%
"a" in "cat"

# %% [markdown]
# ## Mutability

# %% [markdown]
# An list can be modified:

# %%
name = "Grace Brewster Murray Hopper".split(" ")
print(name)

# %%
name[0:3] = ["Admiral"]
name.append("PhD")

print(" ".join(name))

# %% [markdown]
# ## Tuples

# %% [markdown]
# A `tuple` is an immutable sequence. It is like a list, execpt it cannot be changed. It is defined with round brackets.

# %%
my_tuple = ("Hello", "World")

# %%
my_tuple

# %% [markdown]
# Trying to modify one of its values will fail:

# %%
my_tuple[0] = "Goodbye"

# %% [markdown]
# `str` is immutable too:

# %%
fish = "Hake"
fish[0] = "R"

# %% [markdown]
# But note that container reassignment is moving a label, **not** changing an element:

# %%
fish = "Rake"  ## OK!

# %% [markdown]
# *Supplementary material*: Try the [online memory visualiser](http://www.pythontutor.com/visualize.html#code=name+%3D++%22Sir+Michael+Edward+Palin%22.split%28%22+%22%29%0A%0Aname%5B0%5D+%3D+%22Knight%22%0Aname%5B1%3A3%5D+%3D+%5B%22Mike-%22%5D%0Aname.append%28%22FRGS%22%29%0A%0Aname%20%3D%20%22King%20Arthur%22&&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0) for this one.

# %% [markdown]
# ## Memory and containers

# %% [markdown]
#
# The way memory works with containers can be important:
#
#
#

# %%
x = list(range(3))
print(x)

# %%
y = x
print(y)

# %%
z = x[0:3]
y[1] = "Gotcha!"
print(x)
print(y)
print(z)

# %%
z[2] = "Really?"
print(x)
print(y)
print(z)

# %% [markdown]
# *Supplementary material*: This one works well at the [memory visualiser](http://www.pythontutor.com/visualize.html#code=x%20%3D%20%5B%22What's%22,%20%22Going%22,%20%22On%3F%22%5D%0Ay%20%3D%20x%0Az%20%3D%20x%5B0%3A3%5D%0A%0Ay%5B1%5D%20%3D%20%22Gotcha!%22%0Az%5B2%5D%20%3D%20%22Really%3F%22&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

# %%
x = ["What's", "Going", "On?"]
y = x
z = x[0:3]

y[1] = "Gotcha!"
z[2] = "Really?"

# %%
x

# %% [markdown]
# The explanation: While `y` is a second label on the *same object*, `z` is a separate object with the same data.

# %% [markdown]
# Nested objects make it even more complicated:

# %%
x = [["a", "b"], "c"]
y = x
z = x[0:2]

x[0][1] = "d"
z[1] = "e"

# %%
x

# %%
y

# %%
z

# %% [markdown]
# Try the [visualiser](http://www.pythontutor.com/visualize.html#code=x%3D%5B%5B'a','b'%5D,'c'%5D%0Ay%3Dx%0Az%3Dx%5B0%3A2%5D%0A%0Ax%5B0%5D%5B1%5D%3D'd'%0Az%5B1%5D%3D'e'&cumulative=false&curInstr=5&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# again.
#
# *Supplementary material*: The copies that we make through slicing are called *shallow copies*: we don't copy all the objects they contain, only the references to them. This is why the nested list in `x[0]` is not copied, so `z[0]` still refers to it. It is possible to actually create copies of all the contents, however deeply nested they are - this is called a *deep copy*. Python provides methods for that in its standard library, in the `copy` module. You can read more about that, as well as about shallow and deep copies, in the [library reference](https://docs.python.org/3/library/copy.html).

# %% [markdown]
# ## Identity versus equality
#
#
# Having the same data is different from being the same actual object
# in memory:

# %%
print([1, 2] == [1, 2])
print([1, 2] is [1, 2])

# %% [markdown]
# The `==` operator checks, element by element, that two containers have the same data. 
# The `is` operator checks that they are actually the same object.

# %%
my3numbers = list(range(3))
print(my3numbers)

# %%
[0, 1, 2] == my3numbers

# %%
[0, 1, 2] is my3numbers

# %% [markdown]
# But, and this point is really subtle, for immutables, the Python language might save memory by reusing a single instantiated copy. This will always be safe.

# %%
word = "Hello"
print("Hello" == word)
print("Hello" is word)
