# ---
# jupyter:
#   jekyll:
#     display_name: Maze Solution
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ### Solution: my Maze Model

# %% [markdown]
# Here's one possible solution to the Maze model. Yours will probably be different, and might be just as good.
# That's the artistry of software engineering: some solutions will be faster, others use less memory, while others will
# be easier for other people to understand. Optimising and balancing these factors is fun!

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
# Some important points:

# %% [markdown]
# * The whole solution is a complete nested structure.
# * I used indenting to make the structure easier to read.
# * Python allows code to continue over multiple lines, so long as sets of brackets are not finished.
# * There is an **empty** person list in empty rooms, so the type structure is robust to potential movements of people.
# * We are nesting dictionaries and lists, with string and integer data.

# %%
people_so_far = 0

for room_name in house:
    people_so_far = people_so_far + len(house[room_name]["people"])

print(people_so_far)
