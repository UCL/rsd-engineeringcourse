# ---
# jupyter:
#   jekyll:
#     display_name: Maze Files Solution
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %%
house = {
    'living': {
        'exits': {
            'north': 'kitchen',
            'outside': 'garden',
            'upstairs': 'bedroom'
        },
        'people': ['James'],
        'capacity': 2
    },
    'kitchen': {
        'exits': {
            'south': 'living'
        },
        'people': [],
        'capacity': 1
    },
    'garden': {
        'exits': {
            'inside': 'living'
        },
        'people': ['Sue'],
        'capacity': 3
    },
    'bedroom': {
        'exits': {
            'downstairs': 'living',
            'jump': 'garden'
        },
        'people': [],
        'capacity': 1
    }
}

# %% [markdown]
# Save the maze with json:

# %%
import json

# %%
with open('maze.json', 'w') as json_maze_out:
    json_maze_out.write(json.dumps(house))

# %% [markdown]
# Consider the file on the disk:

# %% language="bash"
# cat 'maze.json'

# %% [markdown]
# and now load it into a different variable:

# %%
with open('maze.json') as json_maze_in:
    maze_again = json.load(json_maze_in)

# %%
maze_again

# %% [markdown]
# Or with YAML:

# %%
import yaml

# %%
with open('maze.yaml', 'w') as yaml_maze_out:
    yaml_maze_out.write(yaml.dump(house))

# %% language="bash"
# cat 'maze.yaml'

# %%
with open('maze.yaml') as yaml_maze_in:
    maze_again = yaml.safe_load(yaml_maze_in)

# %%
maze_again
