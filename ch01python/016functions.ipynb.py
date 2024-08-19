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
# # Functions

# %% [markdown]
# ## Definition

# %% [markdown]
#
# We use `def` to define a function, and `return` to pass back a value:
#
#
#

# %%
def double(x):
    return x * 2


# %%
double(5)

# %%
double([5])

# %%
double("five")


# %% [markdown]
# ## Default Parameters

# %% [markdown]
# We can specify default values for parameters:

# %%
def jeeves(name="Sir"):
    return f"Very good, {name}"


# %%
jeeves()

# %%
jeeves("James")


# %% [markdown]
# If you have some parameters with defaults, and some without, those with defaults **must** go later.
#
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
# ## Side effects

# %% [markdown]
#
# Functions can do things to change their **mutable** arguments,
# so `return` is optional.
#
# This is pretty awful style, in general, functions should normally be side-effect free.
#
# Here is a contrived example of a function that makes plausible use of a side-effect.
#
# Note that the function below uses `[:]`. This is used to update the contents of
# the list, and though this function is not returning anything, it's changing the
# elements of the list.

# %%
def double_inplace(vec):
    vec[:] = [element * 2 for element in vec]


z = [0, 1, 2, 3]  #  This could be simplified using list(range(4))
double_inplace(z)
print(z)

# %% [markdown]
# In this example, we're using `[:]` to access into the same list, and write its data. Whereas, if we do
#
#     vec = [element * 2 for element in vec]
#
# would just move a local label, not change the input - *i.e.*, a new container is created and the label `vec` is moved from the old one to the new one.
#
# A more common case would be to this as a function which **returned** the output:

 # %%
def double(vec):
    return [element * 2 for element in vec]

# %% [markdown]
# Let's remind ourselves of this behaviour with a simple array:

# %%
x = 5
x = 7
x = ["a", "b", "c"]
y = x

# %%
x

# %%
x[:] = ["Hooray!", "Yippee"]

# %%
y


# %% [markdown]
# ## Early Return
#
# Having multiple `return` statements is a common practice in programming.
# These `return` statements can be placed far from each other, allowing a
# function to return early if a specific condition is met.
#
# For example, a function `isbigger` could be written as:
# ```
# def isbigger(x, limit=20):
#     return x > limit
# ```
# However, what if you want to print a message on the screen when a smaller
# value has been found? That's what we do below, where the function below
# returns early if a number greater than given limit.

# %%
def isbigger(x, limit=20):
    if x > limit:
        return True
    print("Value is smaller")
    return False


isbigger(25, 15)

# %%
isbigger(40, 15)


# %% [markdown]
#
# The dynamic typing of Python also makes it easy to return different types
# of values based on different conditions, but such code is not considered
# a good practice. It is also a good practice to have a default return value
# in the function if it is returning something in the first place. For instance,
# the function below could use an `elif` or an `else` condition for the second
# `return` statement, but that would not be a good practice. In those cases,
# Python would be using the implicit `return` statement. For example, what's
# returned in the following example when the argument `x` is equal to the `limit`?

# %%
def isbigger(x, limit=20):
    if x > limit:
        return True
    elif x < limit:
        print("Value is smaller")
        return False

# %%
# Write your own code to find out

# %% [markdown]
#
# Return without arguments can be used to exit early from a function
#
# Here's a slightly more plausibly useful function-with-side-effects to extend a list with a specified padding datum.

# %%
def extend(to, vec, pad):
    if len(vec) >= to:
        return  # Exit early, list is already long enough.
    vec[:] = vec + [pad] * (to - len(vec))


# %%
x = [1, 2, 3]
extend(6, x, "a")
print(x)

# %%
z = list(range(9))
extend(6, z, "a")
print(z)


# %% [markdown]
# ## Unpacking arguments

# %% [markdown]
#
# If a vector is supplied to a function with a `*`, its elements
# are used to fill each of a function's arguments.
#
#
#

# %%
def arrow(before, after):
    return f"{before} -> {after}"


print(arrow(1, 3))

# %%
x = [1, -1]

print(arrow(*x))

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

# %%
charges.items()

# %%
for particle in charges.items():
    print(arrow(*particle))


# %% [markdown]
# ## Sequence Arguments

# %% [markdown]
# Similiarly, if a `*` is used in the **definition** of a function, multiple
# arguments are absorbed into a list **inside** the function:

# %%
def doubler(*sequence):
    return [x * 2 for x in sequence]


print(doubler(1, 2, 3, "four"))


# %% [markdown]
# ## Keyword Arguments

# %% [markdown]
#
# If two asterisks are used, named arguments are supplied as a dictionary:
#
#
#

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

somefunc(1, 2, 3, 4, 5, fish="Haddock")
