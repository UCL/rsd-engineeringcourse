# ---
# jupyter:
#   jekyll:
#     display_name: Dictionaries
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Dictionaries

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
me = {"name": "James", "age": 39, "Jobs": ["Programmer", "Teacher"]}

# %%
print(me)

# %%
print(me["Jobs"])

# %%
print(type(me))

# %% [markdown]
# ## Keys and Values

# %% [markdown]
# The things we can use to look up with are called **keys**:

# %%
me.keys()

# %% [markdown]
# The things we can look up are called **values**:

# %%
me.values()

# %% [markdown]
# When we test for containment on a `dict` we test on the **keys**:

# %%
"Jobs" in me

# %%
"James" in me

# %%
"James" in me.values()

# %% [markdown]
# ## Immutable Keys Only

# %% [markdown]
# The way in which dictionaries work is one of the coolest things in computer science:
# the "hash table". This is way beyond the scope of this course, but it has a consequence:
#
# You can only use **immutable** things as keys.

# %%
good_match = {("Lamb", "Mint"): True, ("Bacon", "Chocolate"): False}

# %% [markdown]
# but:

# %%
illegal = {[1, 2]: 3}

# %% [markdown]
# *Supplementary material*: You can start to learn about [the 'hash table'](https://www.youtube.com/watch?v=h2d9b_nEzoA). Though this video is **very** advanced I think it's really interesting!

# %% [markdown]
# ## No guarantee of order

# %% [markdown]
#
# Another consequence of the way dictionaries work is that there's no guaranteed order among the
# elements:
#
#
#

# %%
my_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}
print(my_dict)
print(my_dict.values())

# %% [markdown]
# ## Sets

# %% [markdown]
# A set is a `list` which cannot contain the same element twice.

# %%
university = "University College London"
unique_letters = set(university)

# %%
unique_letters

# %%
print("".join(unique_letters))

# %%
"".join(["a", "b", "c"])

# %% [markdown]
# It has no particular order, but is really useful for checking or storing **unique** values.

# %%
alist = [1, 2, 3]
is_unique = len(set(alist)) == len(alist)
print(is_unique)

# %% [markdown]
# ## Safe Lookup

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

# %%
x.get("fish", "tuna") == "tuna"
