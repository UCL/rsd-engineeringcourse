# ---
# jupyter:
#   jekyll:
#     display_name: Maze comprehension solution
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ### Solution

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
# We can get a simpler dictionary with just capacities like this:

# %%
{name: room['capacity'] for name, room in house.items()}

# %% [markdown]
# To get the current number of occupants, we can use a similar dictionary comprehension. Remember that we can *filter* (only keep certain rooms) by adding an `if` clause:

# %%
{name: len(room['people']) for name, room in house.items() if len(room['people']) > 0}
