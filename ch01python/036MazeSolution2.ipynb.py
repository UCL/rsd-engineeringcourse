# ---
# jupyter:
#   jekyll:
#     display_name: Maze Control Solution
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ### Solution: counting people in the maze

# %% [markdown]
# With this maze structure:

# %%
house = {
    'living' : {
        'exits': {
            'north' : 'kitchen',
            'outside' : 'garden',
            'upstairs' : 'bedroom'
        },
        'people' : ['Graham'],
        'capacity' : 2
    },
    'kitchen' : {
        'exits': {
            'south' : 'living'
        },
        'people' : [],
        'capacity' : 1
    },
    'garden' : {
        'exits': {
            'inside' : 'living'
        },
        'people' : ['David'],
        'capacity' : 3
    },
    'bedroom' : {
        'exits': {
            'downstairs' : 'living',
            'jump' : 'garden'
        },
        'people' : [],
        'capacity' : 1
    }
}

# %% [markdown]
# We can count the occupants and capacity like this:

# %%
for room_name in house:
    print(room_name)

# %%
house

# %%
house.values()

# %%
running_total = 0

for room_data in house.values():
    running_total += len(room_data["people"])

print(running_total)

# %% [markdown]
# As a side note, note how we included the values of `running_total` in the last line. This is a handy syntax for building strings that contain the values of variables. You can read more about it at this [Python String Formatting Best Practices guide](https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat) or in the [official documentation](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals).
