# ---
# jupyter:
#   jekyll:
#     display_name: Structures
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Data structures

# %% [markdown]
# ## Nested Lists and Dictionaries

# %% [markdown]
# In research programming, one of our most common tasks is building an appropriate *structure* to model our complicated
# data. Later in the course, we'll see how we can define our own types, with their own attributes, properties, and methods. But probably the most common approach is to use nested structures of lists, dictionaries, and sets to model our data. For example, an address might be modelled as a dictionary with appropriately named fields:

# %%
UCL = {'City': 'London', 
     'Street': 'Gower Street',
     'Postcode': 'WC1E 6BT'}

# %%
MyHouse = {
    'City': 'London',
    'Street': 'Waterson Street',
    'Postcode': 'E2 8HH'
}

# %% [markdown]
# A collection of people's addresses is then a list of dictionaries:

# %%
addresses = [UCL, MyHouse]

# %%
addresses

# %% [markdown]
# A more complicated data structure, for example for a census database, might have a list of residents or employees at each address:

# %%
UCL["People"] = ["Clare", "James", "Owain"]

# %%
MyHouse["People"] = ["Sue", "James"]

# %%
addresses

# %% [markdown]
# Which is then a list of dictionaries, with keys which are strings or lists.

# %% [markdown]
# We can go further, e.g.:

# %%
UCL["Residential"] = False

# %% [markdown]
# And we can write code against our structures:

# %%
leaders = [place["People"][0] for place in addresses]
print(leaders)

# %% [markdown]
# This was an example of a 'list comprehension', which is used to get data of this structure, and which we'll see more of in a moment...

# %% [markdown]
# ## Exercise: a Maze Model.

# %% [markdown]
# Work with a partner to design a data structure to represent a maze using dictionaries and lists.

# %% [markdown]
# * Each place in the maze has a name, which is a string.
# * Each place in the maze has zero or more people currently standing at it, by name.
# * Each place in the maze has a maximum capacity of people that can fit in it.
# * For each place in the maze, you can go from that place to a few other places, using a direction like 'up', 'north', 
# or 'sideways'

# %% [markdown]
# Create an example instance, in a notebook, of a simple structure for your maze:

# %% [markdown]
# * The living room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
# * From the kitchen, you can go south to the living room. It fits 1 person.
# * From the garden you can go inside to living room. It fits 3 people. Sue is currently there.
# * From the bedroom, you can go downstairs. You can also jump out of the window to the garden. It fits 2 people.

# %% [markdown]
# Make sure that your model:
#
# * Allows empty rooms.
# * Allows you to jump out of the upstairs window, but not to fly back up.
# * Allows rooms which people can't fit in.

# %% [markdown]
# As an example of a similar problem, the following code could be used to represent a collection of cities, each of which has a name, a maximum capacity, and potentially some people currently living there.

# %%
cities = [
    {"name": "London", "capacity": 8, "residents": ["Me", "Sue"]},
    {"name": "Edinburgh", "capacity": 1, "residents": ["Dave"]},
    {"name": "Cardiff", "capacity": 1, "residents": []},
]

# %% [markdown]
# We can then check, for instance, how many people currently reside in the third city:

# %%
len(cities[2]["residents"])
