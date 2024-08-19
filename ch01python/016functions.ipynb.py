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

# %%
def product(x=5, y=7):
    return x * y


# %%
product(9)

# %%
product(y=11)

# %%
product()


# %% [markdown]
# ## Side effects

# %% [markdown]
#
# Functions can do things to change their **mutable** arguments,
# so `return` is optional.
#
#
#

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

# %%
def isbigger(x, limit=20):
    if x > limit:
        return True
    print("Got here")
    return False


isbigger(25, 15)

# %%
isbigger(40, 15)


# %% [markdown]
#
# Return without arguments can be used to exit early from a function
#
#
#

# %%
def extend(to, vec, pad):
    if len(vec) >= to:
        return
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
    return str(before) + " -> " + str(after)


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
        print(key + " -> " + value)


arrowify(neutron="n", proton="p", electron="e")
