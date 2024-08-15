# ---
# jupyter:
#   jekyll:
#     display_name: Looping
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Iteration

# %% [markdown]
# Our other aspect of control is looping back on ourselves.
#
# We use `for` ... `in` ... to "iterate" over lists:

# %%
mylist = [3, 7, 15, 2]

for element in mylist:
    print(element ** 2)

# %% [markdown]
# Each time through the loop, the value in the `element` slot is updated to the **next** value in the sequence.

# %% [markdown]
# ## Iterables

# %% [markdown]
#
# Any sequence type is iterable:
#
#
#

# %%
vowels = "aeiou"

sarcasm = []

for letter in "Okay":
    if letter.lower() in vowels:
        repetition = 3
    else:
        repetition = 1
    sarcasm.append(letter * repetition)

"".join(sarcasm)

# %% [markdown]
# The above is a little puzzle, work through it to understand why it does what it does.

# %% [markdown]
# ## Dictionaries are Iterables

# %% [markdown]
# All sequences are iterables. Some iterables (things you can `for` loop over) are not sequences (things with you can do `x[5]` to), for example **sets**.

# %%
import datetime

now = datetime.datetime.now()

founded = {"Eric": 1943, "UCL": 1826, "Cambridge": 1209}

current_year = now.year

for thing in founded:
    print(f"{thing} is {current_year - founded[thing]} years old.")

# %%
thing = "UCL"

founded[thing]

# %%
founded

# %%
founded.items()

# %% [markdown]
# ## Unpacking and Iteration

# %% [markdown]
#
# Unpacking can be useful with iteration:
#
#
#

# %%
triples = [
    [4, 11, 15], 
    [39, 4, 18]
]

# %%
for whatever in triples:
    print(whatever)

# %%
a, b = [36, 7]

# %%
b

# %%
for first, middle, last in triples:
    print(middle)

# %%
# A reminder that the words you use for variable names are arbitrary:
for hedgehog, badger, fox in triples:
    print(badger)

# %% [markdown]
#
#
#
# For example, to iterate over the items in a dictionary as pairs:
#
#
#

# %%
for name, year in founded.items():
    print(f"{name} is {current_year - year} years old.")

# %%
for name in founded:
    print(f"{name} is {current_year - founded[name]} years old.")

# %% [markdown]
# ## Break, Continue

# %% [markdown]
#
# * Continue skips to the next turn of a loop
# * Break stops the loop early
#
#
#

# %%
for n in range(50):
    if n == 20:
        break
    if n % 2 == 0:
        continue
    print(n)

# %% [markdown]
# These aren't useful that often, but are worth knowing about. There's also an optional `else` clause on loops, executed only if the loop gets through all its iterations without a `break` or `return`. This can help to keep the code cleaner avoiding to have a condition to check that something happened.


# %% [markdown]
# For example if someone goes to a cheese shop and wants a piece of cheese from one of their favourites could be written as it follows.

# %%
shop = ['Wenslydale (shop assistant)', 'Bazouki player', 'Customer']
for cheese_type in ['red Leciester', 'Tilsit', 'Caerphilly']:
    if found := cheese_type in shop:
        print(f"Buy {cheese_type} and leave")

if not found:
    print("Left empty-handed")

# %% [markdown]
# Whereas using `else` the second `if` condition and the `found` variable wouldn't be needed:

# %%
shop = ['Wenslydale (shop assistant)', 'Bazouki player', 'Customer']
for cheese_type in ['Red Leciester', 'Tilsit', 'Caerphilly']:
    if cheese_type in shop:
        print(f"Buy {cheese_type} and leave")
        break
else:
    print("Left empty-handed")

# %% [markdown]
# Note that we've used the `:=` walrus operator (introduced in python 3.8 from [PEP572](https://peps.python.org/pep-0572/)).
# The example above is based on [The Cheese Shop](http://www.montypython.50webs.com/scripts/Series_3/61.htm) sketch from the Monty Python. The sketch goes over a longer list of cheeses.


# %% [markdown]
# ## Exercise: the Maze Population

# %% [markdown]
# Take your maze data structure. Write a program to count the total number of people in the maze, and also determine the total possible occupants.
