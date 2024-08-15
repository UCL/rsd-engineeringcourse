# ---
# jupyter:
#   jekyll:
#     display_name: Comprehensions
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Comprehensions

# %% [markdown]
# ## The list comprehension

# %% [markdown]
# If you write a for loop **inside** a pair of square brackets for a list, you magic up a list as defined.
# This can make for concise but hard to read code, so be careful.

# %%
result = []
for x in range(10):
    result.append(2 ** x)

print(result)

# %% [markdown]
# is the same as

# %%
[2 ** x for x in range(10)]

# %% [markdown]
# You can do quite weird and cool things with comprehensions:

# %%
[len(str(2 ** x)) for x in range(20)]

# %% [markdown]
# You can write an `if` statement in comprehensions too: 

# %%
[2 ** x for x in range(30) if x % 3 == 0]

# %% [markdown]
# Consider the following, and make sure you understand why it works:

# %%
"".join([letter for letter in "James Hetherington" if letter.lower() not in "aeiou"])

# %% [markdown]
# ## Comprehensions versus building lists with `append`:

# %% [markdown]
# This code:

# %%
result = []
for x in range(30):
    if x % 3 == 0:
        result.append(2 ** x)
print(result)

# %% [markdown]
# does the same as the comprehension above. The comprehension is generally considered more readable.

# %% [markdown]
# Comprehensions are therefore an example of what we call 'syntactic sugar': they do not increase the capabilities of the language.

# %% [markdown]
# Instead, they make it possible to write the same thing in a more readable way. 

# %% [markdown]
# Everything we learn from now on will be either syntactic sugar or interaction with something other than idealised memory, such as a storage device or the internet. Once you have variables, conditionality, and branching, your language can do anything. (And this can be proved.)

# %% [markdown]
# ## Nested comprehensions

# %% [markdown]
# If you write two `for` statements in a comprehension, you get a single array generated over all the pairs:

# %%
[x - y for x in range(4) for y in range(4)]

# %% [markdown]
# You can select on either, or on some combination:

# %%
[x - y for x in range(4) for y in range(4) if x >= y]

# %% [markdown]
# If you want something more like a matrix, you need to do *two nested* comprehensions!

# %%
[[x - y for x in range(4)] for y in range(4)]

# %% [markdown]
# Note the subtly different square brackets.

# %% [markdown]
# Note that the list order for multiple or nested comprehensions can be confusing:

# %%
[x + y for x in ["a", "b", "c"] for y in ["1", "2", "3"]]

# %%
[[x + y for x in ["a", "b", "c"]] for y in ["1", "2", "3"]]

# %% [markdown]
# ## Dictionary Comprehensions

# %% [markdown]
# You can automatically build dictionaries by using a list comprehension syntax, but with curly brackets and a colon:

# %%
{((str(x)) * 3): x for x in range(3)}

# %% [markdown]
# ## List-based thinking

# %% [markdown]
# Once you start to get comfortable with comprehensions, you find yourself working with containers, nested groups of lists 
# and dictionaries, as the 'things' in your program, not individual variables. 

# %% [markdown]
# Given a way to analyse some dataset, we'll find ourselves writing stuff like:
#
#     analysed_data = [analyse(datum) for datum in data]
#     
#     analysed_data = map(analyse, data)

# %% [markdown]
# There are lots of built-in methods that provide actions on lists as a whole:

# %%
any([True, False, True])

# %%
all([True, False, True])

# %%
max([1, 2, 3])

# %%
sum([1, 2, 3])

# %% [markdown]
# One common method is `map`, which works like a simple list comprehension: it applies one function to every member of a list.

# %%
[str(x) for x in range(10)]

# %%
map(str, range(10))

# %% [markdown]
# Its output is this strange-looking `map` object, which can be iterated over (with a `for`) or turned into a list:

# %%
for element in map(str, range(10)):
    print(element)

# %%
list(map(str, range(10)))

# %% [markdown]
# So I can write:
#     
#     analysed_data = list(map(analyse, data))

# %% [markdown]
# ## Exercise: Occupancy Dictionary

# %% [markdown]
# Take your maze data structure. Write a program to print out a new dictionary, which gives,
# for each room's name, the number of people in it. Don't add in a zero value in the dictionary for empty rooms.

# %% [markdown]
# The output should look similar to:

# %%
{"bedroom": 1, "garden": 3, "kitchen": 1, "living": 2}
