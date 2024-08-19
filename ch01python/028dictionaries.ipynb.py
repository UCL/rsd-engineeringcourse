# ---
# jupyter:
#   jekyll:
#     display_name: Dictionaries and Sets
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Dictionaries and Sets

# %% [markdown]
# ## The Python Dictionary

# %% [markdown]
# Python supports a container type called a dictionary.

# %% [markdown]
# This is also known as an "associative array", "map" or "hash" in other languages.

# %% [markdown]
# In a list, we use a number to look up an element:

# %%
names = "Martin Luther King".split(" ")
names[1]

# %% [markdown]
# In a dictionary, we look up an element using **another object of our choice**:

# %%
chapman = {"name": "Graham", "age": 48, 
           "Jobs": ["Comedian", "Writer"] }

# %%
chapman

# %%
print(chapman["Jobs"])

# %%
print(chapman["age"])

# %%
print(type(chapman))

# %% [markdown]
# ### Keys and Values

# %% [markdown]
# The things we can use to look up with are called **keys**:

# %%
chapman.keys()

# %% [markdown]
# The things we can look up are called **values**:

# %%
chapman.values()

# %% [markdown]
# When we test for containment on a `dict` we test on the **keys**:

# %%
"Jobs" in chapman

# %%
"Graham" in chapman

# %%
"Graham" in chapman.values()

# %% [markdown]
# ### Immutable Keys Only

# %% [markdown]
# The way in which dictionaries work is one of the coolest things in computer science:
# the "hash table". This is way beyond the scope of this course, but it has a consequence:
#
# You can only use **immutable** things as keys.

# %%
good_match = {
    ("Lamb", "Mint"): True, 
    ("Bacon", "Chocolate"): False
   }

# %% [markdown]
# but:

# %%
illegal = {
    ["Lamb", "Mint"]: True, 
    ["Bacon", "Chocolate"]: False
   }

# %% [markdown]
# *Supplementary material*: You can start to learn about [the 'hash table'](https://www.youtube.com/watch?v=h2d9b_nEzoA). Though this video is **very** advanced, it's really interesting!

# %% [markdown]
# ### No guarantee of order
#
# Another consequence of the way dictionaries work is that there's no guaranteed order among the
# elements:


# %%
my_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}
print(my_dict)
print(my_dict.values())

# %% [markdown]
# ### Safe Lookup
#
# Some times you want a program to keep working even when a key is looked up but it's not there.
# Python dictionaries offers that through the `get` method.

# %%
x = {"a": 1, "b": 2}

# %%
x["a"]

# %%
x["fish"]

# %%
x.get("a")

# %%
x.get("fish")

# %% [markdown]
# By default `get` returns `None` if the key searched is not in the dictionary.
# However, you can change that default by adding what's the value you want it to return.

# %%
x.get("fish", "tuna") == "tuna"

# %% [markdown]
# ## Sets

# %% [markdown]
# A set is a `list` which cannot contain the same element twice.
# We make one by calling `set()` on any sequence, e.g. a list or string.

# %%
name = "Graham Chapman"
unique_letters = set(name)

# %%
unique_letters

# %% [markdown]
# Or by defining a literal like a dictionary, but without the colons:

# %%
primes_below_ten = { 2, 3, 5, 7}

# %%
print(type(unique_letters))
print(type(primes_below_ten))


# %%
unique_letters

# %% [markdown]
# This will be easier to read if we turn the set of letters back into a string, with `join`:

# %%
print("".join(unique_letters))

# %% [markdown]
# `join` uses the character give to be what joins the sequence given:

# %%
"-".join(["a", "b", "c"])

# %% [markdown]
# Note that a set has no particular order, but is really useful for checking or storing **unique** values.

# %%
alist = [1, 2, 3]
is_unique = len(set(alist)) == len(alist)
print(is_unique)

# %% [markdown]
# Set operations work as in mathematics:

# %%
x = set("Hello")
y = set("Goodbye")

# %%
x & y # Intersection

# %%
x | y # Union

# %%
y - x # y intersection with complement of x: letters in Goodbye but not in Hello

# %% [markdown]
# Your programs will be faster and more readable if you use the appropriate container type for your data's meaning.
# Always use a set for lists which can't in principle contain the same data twice, always use a dictionary for anything
# which feels like a mapping from keys to values.

