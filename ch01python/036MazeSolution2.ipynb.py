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
capacity = 0
occupancy = 0
for name, room in house.items():
    capacity += room['capacity']
    occupancy += len(room['people'])
print(f"House can fit {capacity} people, and currently has: {occupancy}.")

