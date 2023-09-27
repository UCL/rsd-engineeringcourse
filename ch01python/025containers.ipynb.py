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
# ## Containers

# %% [markdown]
# ### Checking for containment.

# %% [markdown]
# The `list` we saw is a container type: its purpose is to hold other objects. We can ask python whether or not a
# container contains a particular item:

# %%
'Dog' in ['Cat', 'Dog', 'Horse']

# %%
'Bird' in ['Cat', 'Dog', 'Horse']

# %%
2 in range(5)

# %%
99 in range(5)

# %% [markdown]
# ### Mutability

# %% [markdown]
# A list can be modified:

# %%
name = "Sir Michael Edward Palin".split(" ")
print(name)

# %%
name[0] = "Knight"
name[1:3] = ["Mike-"]
name.append("FRGS")

print(" ".join(name))

# %% [markdown]
# ### Tuples

# %% [markdown]
# A `tuple` is an immutable sequence. It is like a list, execpt it cannot be changed. It is defined with round brackets.

# %%
x = 0,
type(x)

# %%
my_tuple = ("Hello", "World")
my_tuple[0] = "Goodbye"

# %%
type(my_tuple)

# %% [markdown]
# `str` is immutable too:

# %%
fish = "Hake"
fish[0] = 'R'

# %% [markdown]
# But note that container reassignment is moving a label, **not** changing an element:

# %%
fish = "Rake" ## OK!

# %% [markdown]
# *Supplementary material*: Try the [online memory visualiser](http://www.pythontutor.com/visualize.html#code=name+%3D++%22Sir+Michael+Edward+Palin%22.split%28%22+%22%29%0A%0Aname%5B0%5D+%3D+%22Knight%22%0Aname%5B1%3A3%5D+%3D+%5B%22Mike-%22%5D%0Aname.append%28%22FRGS%22%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0) for this one.

# %% [markdown]
# ### Memory and containers

# %% [markdown]
#
# The way memory works with containers can be important:
#
#
#

# %%
x = list(range(3))
x

# %%
y = x
y

# %%
z = x[0:3]
y[1] = "Gotcha!"

# %%
x

# %%
y

# %%
z

# %%
z[2] = "Really?"

# %%
x

# %%
y

# %%
z

# %% [markdown]
# *Supplementary material*: This one works well at the [memory visualiser](http://www.pythontutor.com/visualize.html#code=x+%3D+%5B%22What's%22,+%22Going%22,+%22On%3F%22%5D%0Ay+%3D+x%0Az+%3D+x%5B0%3A3%5D%0A%0Ay%5B1%5D+%3D+%22Gotcha!%22%0Az%5B2%5D+%3D+%22Really%3F%22&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0).

# %% [markdown]
# The explanation: While `y` is a second label on the *same object*, `z` is a separate object with the same data. Writing `x[:]` creates a new list containing all the elements of `x` (remember: `[:]` is equivalent to `[0:<last>]`). This is the case whenever we take a slice from a list, not just when taking all the elements with `[:]`.
#
# The difference between `y=x` and `z=x[:]` is important!

# %% [markdown]
# Nested objects make it even more complicated:

# %%
x = [['a', 'b'] , 'c']
y = x
z = x[0:2]

# %%
x[0][1] = 'd'
z[1] = 'e'

# %%
x

# %%
y

# %%
z

# %% [markdown]
# Try the [visualiser](http://www.pythontutor.com/visualize.html#code=x%20%3D%20%5B%5B'a',%20'b'%5D,%20'c'%5D%0Ay%20%3D%20x%0Az%20%3D%20x%5B0%3A2%5D%0A%0Ax%5B0%5D%5B1%5D%20%3D%20'd'%0Az%5B1%5D%20%3D%20'e'&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0) again.
#
# *Supplementary material*: The copies that we make through slicing are called *shallow copies*: we don't copy all the objects they contain, only the references to them. This is why the nested list in `x[0]` is not copied, so `z[0]` still refers to it. It is possible to actually create copies of all the contents, however deeply nested they are - this is called a *deep copy*. Python provides methods for that in its standard library, in the `copy` module. You can read more about that, as well as about shallow and deep copies, in the [library reference](https://docs.python.org/3/library/copy.html).

# %% [markdown]
# ### Identity vs Equality
#
#
# Having the same data is different from being the same actual object
# in memory:

# %%
[1, 2] == [1, 2]

# %%
[1, 2] is [1, 2]

# %% [markdown]
# The == operator checks, element by element, that two containers have the same data. 
# The `is` operator checks that they are actually the same object.

# %% [markdown]
# But, and this point is really subtle, for immutables, the python language might save memory by reusing a single instantiated copy. This will always be safe.

# %%
"Hello" == "Hello"

# %%
"Hello" is "Hello"

# %% [markdown]
# This can be useful in understanding problems like the one above:

# %%
x = range(3)
y = x
z = x[:]

# %%
x == y

# %%
x is y

# %%
x == z

# %%
x is z
