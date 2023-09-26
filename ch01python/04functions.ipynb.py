# ---
# jupyter:
#   jekyll:
#     display_name: Defining functions
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Functions 

# %% [markdown]
# ### Definition

# %% [markdown]
#
# We use `def` to define a function, and `return` to pass back a value:
#
#
#

# %%
def double(x):
    return x * 2

print(double(5), double([5]), double('five'))


# %% [markdown]
# ### Default Parameters

# %% [markdown]
# We can specify default values for parameters:

# %%
def jeeves(name = "Sir"):
    return f"Very good, {name}"


# %%
jeeves()

# %%
jeeves('John')


# %% [markdown]
# If you have some parameters with defaults, and some without, those with defaults **must** go later.

# %% [markdown]
# If you have multiple default arguments, you can specify neither, one or both:

# %%
def jeeves(greeting="Very good", name="Sir"):
    return f"{greeting}, {name}"


# %%
jeeves()

# %%
jeeves("Hello")

# %%
jeeves(name = "John")

# %%
jeeves(greeting="Suits you")

# %%
jeeves("Hello", "Producer")


# %% [markdown]
# ### Side effects

# %% [markdown]
# Functions can do things to change their **mutable** arguments,
# so `return` is optional.
#
# This is pretty awful style, in general, functions should normally be side-effect free.
#
# Here is a contrived example of a function that makes plausible use of a side-effect

# %%
def double_inplace(vec):
    vec[:] = [element * 2 for element in vec]

z = list(range(4))
double_inplace(z)
print(z)

# %%
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[:] = []


# %% [markdown]
# In this example, we're using `[:]` to access into the same list, and write it's data.
#
#     vec = [element*2 for element in vec]
#
# would just move a local label, not change the input.

# %% [markdown]
# But I'd usually just write this as a function which **returned** the output:

# %%
def double(vec):
    return [element * 2 for element in vec]


# %% [markdown]
# Let's remind ourselves of the behaviour for modifying lists in-place using `[:]` with a simple array:

# %%
x = 5
x = 7
x = ['a', 'b', 'c']
y = x

# %%
x

# %%
x[:] = ["Hooray!", "Yippee"]

# %%
y


# %% [markdown]
# ### Early Return

# %% [markdown]
#
# Return without arguments can be used to exit early from a function
#
#
#

# %% [markdown]
# Here's a slightly more plausibly useful function-with-side-effects to extend a list with a specified padding datum.

# %%
def extend(to, vec, pad):
    if len(vec) >= to:
        return # Exit early, list is already long enough.
    
    vec[:] = vec + [pad] * (to - len(vec))


# %%
x = list(range(3))
extend(6, x, 'a')
print(x)

# %%
z = range(9)
extend(6, z, 'a')
print(z)


# %% [markdown]
# ### Unpacking arguments

# %% [markdown]
#
# If a vector is supplied to a function with a '*', its elements
# are used to fill each of a function's arguments. 
#
#
#

# %%
def arrow(before, after):
    return f"{before} -> {after}"

arrow(1, 3)

# %%
x = [1, -1]
arrow(*x)

# %% [markdown]
#
#
#
# This can be quite powerful:
#
#
#

# %%
charges = {"neutron": 0, "proton": 1, "electron": -1}
for particle in charges.items():
    print(arrow(*particle))


# %% [markdown]
#
#
#

# %% [markdown]
# ### Sequence Arguments

# %% [markdown]
# Similiarly, if a `*` is used in the **definition** of a function, multiple
# arguments are absorbed into a list **inside** the function:

# %%
def doubler(*sequence):
    return [x * 2 for x in sequence]


# %%
doubler(1, 2, 3)

# %%
doubler(5, 2, "Wow!")


# %% [markdown]
# ### Keyword Arguments

# %% [markdown]
# If two asterisks are used, named arguments are supplied inside the function as a dictionary:

# %%
def arrowify(**args):
    for key, value in args.items():
        print(f"{key} -> {value}")

arrowify(neutron="n", proton="p", electron="e")


# %% [markdown]
# These different approaches can be mixed:

# %%
def somefunc(a, b, *args, **kwargs):
    print("A:", a)
    print("B:", b)
    print("args:", args)
    print("keyword args", kwargs)


# %%
somefunc(1, 2, 3, 4, 5, fish="Haddock")
