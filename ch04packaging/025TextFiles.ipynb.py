# ---
# jupyter:
#   jekyll:
#     display_name: Writing Libraries
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Python not in the Notebook

# %% [markdown]
# We will often want to save our Python classes, for use in multiple Notebooks.
# We can do this by writing text files with a .py extension, and then `importing` them.

# %% [markdown]
# ### Writing Python in Text Files

# %% [markdown]
# You can use a text editor like [VS Code](https://code.visualstudio.com/) or [Spyder](https://www.spyder-ide.org/). If you create your own Python files ending in `.py`, then you can import them with `import` just like external libraries.

# %% [markdown]
# You can also maintain your library code in a Notebook, and use `%%writefile` to create your library, though this is not encouraged!

# %% [markdown]
# Libraries are usually structured with multiple files, one for each class.

# %% [markdown]
# We will be turning the code we have written for the maze into a library, so that other code can reuse it.

# %% [markdown]
# We group our modules into packages, by putting them together into a folder. You can do this with explorer, or using a shell, or even with Python:

# %%
import os
if 'mazetool' not in os.listdir(os.getcwd()):
    os.mkdir('mazetool')

# %%
# %%writefile mazetool/maze.py

from .room import Room
from .person import Person

class Maze(object):
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.occupants = []
        
    def add_room(self, name, capacity):
        result = Room(name, capacity)
        self.rooms.append(result)
        return result
        
    def add_exit(self, name, source, target, reverse= None):
        source.add_exit(name, target)
        if reverse:
            target.add_exit(reverse, source)
            
    def add_occupant(self, name, room):
        self.occupants.append(Person(name, room))
        room.occupancy += 1
    
    def wander(self):
        "Move all the people in a random direction"
        for occupant in self.occupants:
            occupant.wander()
                
    def describe(self):
        for occupant in self.occupants:
            occupant.describe()
            
    def step(self):
        house.describe()
        print()
        house.wander()
        print()
        
    def simulate(self, steps):
        for _ in range(steps):
            self.step()


# %%
# %%writefile mazetool/room.py
from .exit import Exit


class Room(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.occupancy = 0
        self.exits = []
        
    def has_space(self):
        return self.occupancy < self.capacity
    
    def available_exits(self):
        return [exit for exit in self.exits if exit.valid() ]
            
    def random_valid_exit(self):
        import random
        if not self.available_exits():
            return None
        return random.choice(self.available_exits())
    
    def add_exit(self, name, target):
        self.exits.append(Exit(name, target))
    


# %%
# %%writefile mazetool/person.py

class Person(object):
    def __init__(self, name, room = None):
        self.name=name
        self.room=room
    
    def use(self, exit):
        self.room.occupancy -= 1
        destination=exit.target
        destination.occupancy +=1
        self.room=destination
        print(self.name, "goes", exit.name, "to the", destination.name)
    
    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)
            
    def describe(self):
        print(self.name, "is in the", self.room.name)


# %%
# %%writefile mazetool/exit.py

class Exit(object):
    def __init__(self, name, target):
        self.name = name
        self.target = target
    
    def valid(self):
        return self.target.has_space()


# %% [markdown]
# In order to tell Python that our "mazetool" folder is a Python package, 
# we have to make a special file called `__init__.py`. If you import things in there, they are imported as part of the package:

# %%
# %%writefile mazetool/__init__.py
from .maze import Maze # Python 3 relative import

# %% [markdown]
# In this case we are making it easier to import `Maze` as we are making it available one level above.

# %% [markdown]
# ### Loading Our Package

# %% [markdown]
# We just wrote the files, there is no "Maze" class in this notebook yet:

# %%
myhouse = Maze('My New House')

# %% [markdown]
# But now, we can import Maze, (and the other files will get imported via the chained Import statements, starting from the `__init__.py` file.

# %%
import mazetool

# %% [markdown]
# Let's see how we can access the files we created:

# %%
mazetool.exit.Exit

# %%
from mazetool import Maze

# %%
house = Maze('My New House')
living = house.add_room('livingroom', 2)

# %% [markdown]
# Note the files we have created are on the disk in the folder we made:

# %%
import os

# %%
os.listdir(os.path.join(os.getcwd(), 'mazetool') )


# %% [markdown]
# You may get also `.pyc` files. Those are "Compiled" temporary python files that the system generates to speed things up. They'll be regenerated
# on the fly when your `.py` files change. They may appear inside the `__pycache__` directory.

# %% [markdown]
# ### The Python Path

# %% [markdown]
# We want to `import` these from notebooks elsewhere on our computer:
# it would be a bad idea to keep all our Python work in one folder.

# %% [markdown]
# The best way to do this is to learn how to make our code
# into a proper module that we can install. We'll see more on that in a [few lectures' time](./03Packaging.html) ([notebook](./03Packaging.ipynb)).

# %% [markdown]
# Alternatively, we can add a folder to the "`PYTHONPATH`", where python searches for modules:

# %%
import sys
print('\n'.join(sys.path[-3:]))

# %%
from pathlib import Path
sys.path.append(os.path.join(Path.home(), 'devel', 'libraries', 'python'))

# %%
print(sys.path[-1])

# %% [markdown]
# I've thus added a folder to the list of places searched. If you want to do this permanently, you should set the `PYTHONPATH` Environment Variable,
# which you can learn about in a shell course, or can read about online for your operating system.
