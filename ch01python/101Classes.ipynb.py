# ---
# jupyter:
#   jekyll:
#     display_name: Classes
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Defining your own classes

# %% [markdown]
# ### User Defined Types

# %% [markdown]
# A **class** is a user-programmed Python type (since Python 2.2!)

# %% [markdown]
# It can be defined like:

# %%
class Room:
    pass


# %% [markdown]
# Or:

# %%
class Room():
    pass


# %% [markdown]
# Or:

# %%
class Room:
    pass


# %% [markdown]
# What's the difference? Before Python 2.2 a class was distinct from all other Python types, which caused some odd behaviour. To fix this, classes were redefined as user programmed types by extending `object`, e.g., class `room(object)`.
#
# So most Python 2 code will use this syntax as very few people want to use old style python classes. Python 3 has formalised this by removing old-style classes, so they can be defined without extending `object`, or indeed without braces.
#

# %% [markdown]
# Just as with other python types, you use the name of the type as a function to make a variable of that type:

# %%
zero = int()
type(zero)

# %%
myroom = Room()
type(myroom)

# %% [markdown]
# In the jargon, we say that an **object** is an **instance** of a particular **class**.
#
# `__main__` is the name of the scope in which top-level code executes, where we've defined the class `Room`.

# %% [markdown]
# Once we have an object with a type of our own devising, we can add properties at will:

# %%
myroom.name = "Living"

# %%
myroom.name

# %% [markdown]
# The most common use of a class is to allow us to group data into an object in a way that is 
# easier to read and understand than organising data into lists and dictionaries.

# %%
myroom.capacity = 3
myroom.occupants = ["Graham", "Eric"]


# %% [markdown]
# ### Methods

# %% [markdown]
# So far, our class doesn't do much!

# %% [markdown]
# We define functions **inside** the definition of a class, in order to give them capabilities, just like the methods on built-in
# types.

# %%
class Room:
    def overfull(self):
        return len(self.occupants) > self.capacity


# %%
myroom = Room()
myroom.capacity = 3
myroom.occupants = ["Graham", "Eric"]

# %%
myroom.overfull()

# %%
myroom.occupants.append(['TerryG'])

# %%
myroom.occupants.append(['John'])

# %%
myroom.overfull()


# %% [markdown]
# When we write methods, we always write the first function argument as `self`, to refer to the object instance itself,
# the argument that goes "before the dot".

# %% [markdown]
# This is just a convention for this variable name, not a keyword. You could call it something else if you wanted.

# %% [markdown]
# ### Constructors

# %% [markdown]
# Normally, though, we don't want to add data to the class attributes on the fly like that. 
# Instead, we define a **constructor** that converts input data into an object. 

# %%
class Room:
    def __init__(self, name, exits, capacity, occupants=[]):
        self.name = name
        self.occupants = occupants  # Note the default argument, occupants start empty
        self.exits = exits
        self.capacity = capacity

    def overfull(self):
        return len(self.occupants) > self.capacity


# %%
living = Room("Living Room", {'north': 'garden'}, 3)

# %%
living.capacity


# %% [markdown]
# Methods which begin and end with **two underscores** in their names fulfil special capabilities in Python, such as
# constructors.

# %% [markdown]
# ### Object-oriented design

# %% [markdown]
# In building a computer system to model a problem, therefore, we often want to make:
#
# * classes for each *kind of thing* in our system
# * methods for each *capability* of that kind
# * properties (defined in a constructor) for each *piece of information describing* that kind
#

# %% [markdown]
# For example, the below program might describe our "Maze of Rooms" system:

# %% [markdown]
# We define a "Maze" class which can hold rooms:

# %%
class Maze:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        room.maze = self  # The Room needs to know which Maze it is a part of
        self.rooms[room.name] = room

    def occupants(self):
        return [occupant for room in self.rooms.values()
                for occupant in room.occupants.values()]

    def wander(self):
        """Move all the people in a random direction"""
        for occupant in self.occupants():
            occupant.wander()

    def describe(self):
        for room in self.rooms.values():
            room.describe()

    def step(self):
        self.describe()
        print("")
        self.wander()
        print("")

    def simulate(self, steps):
        for _ in range(steps):
            self.step()


# %% [markdown]
# And a "Room" class with exits, and people:

# %%
class Room:
    def __init__(self, name, exits, capacity, maze=None):
        self.maze = maze
        self.name = name
        self.occupants = {}  # Note the default argument, occupants start empty
        self.exits = exits  # Should be a dictionary from directions to room names
        self.capacity = capacity

    def has_space(self):
        return len(self.occupants) < self.capacity

    def available_exits(self):
        return [exit for exit, target in self.exits.items()
                if self.maze.rooms[target].has_space()]

    def random_valid_exit(self):
        import random
        if not self.available_exits():
            return None
        return random.choice(self.available_exits())

    def destination(self, exit):
        return self.maze.rooms[self.exits[exit]]

    def add_occupant(self, occupant):
        occupant.room = self  # The person needs to know which room it is in
        self.occupants[occupant.name] = occupant

    def delete_occupant(self, occupant):
        del self.occupants[occupant.name]

    def describe(self):
        if self.occupants:
            print(f"{self.name}: " + " ".join(self.occupants.keys()))


# %% [markdown]
# We define a "Person" class for room occupants:

# %%
class Person:
    def __init__(self, name, room=None):
        self.name = name

    def use(self, exit):
        self.room.delete_occupant(self)
        destination = self.room.destination(exit)
        destination.add_occupant(self)
        print("{some} goes {action} to the {where}".format(some=self.name,
                                                           action=exit,
                                                           where=destination.name))

    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)


# %% [markdown]
# And we use these classes to define our people, rooms, and their relationships:

# %%
graham = Person('Graham')
eric = Person('Eric')
terryg = Person('TerryG')
john = Person('John')

# %%
living = Room('livingroom', {'outside': 'garden',
                             'upstairs': 'bedroom', 'north': 'kitchen'}, 2)
kitchen = Room('kitchen', {'south': 'livingroom'}, 1)
garden = Room('garden', {'inside': 'livingroom'}, 3)
bedroom = Room('bedroom', {'jump': 'garden', 'downstairs': 'livingroom'}, 1)

# %%
house = Maze('My House')

# %%
for room in [living, kitchen, garden, bedroom]:
    house.add_room(room)

# %%
living.add_occupant(graham)

# %%
garden.add_occupant(eric)
garden.add_occupant(terryg)

# %%
bedroom.add_occupant(john)

# %% [markdown]
# And we can run a "simulation" of our model:

# %%
house.simulate(3)


# %% [markdown]
# ### Object oriented design

# %% [markdown]
# There are many choices for how to design programs to do this. Another choice would be to separately define exits as a different class from rooms. This way, 
# we can use arrays instead of dictionaries, but we have to first define all our rooms, then define all our exits.

# %%
class Maze:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.occupants = []

    def add_room(self, name, capacity):
        result = Room(name, capacity)
        self.rooms.append(result)
        return result

    def add_exit(self, name, source, target, reverse=None):
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
        print("")
        house.wander()
        print("")

    def simulate(self, steps):
        for _ in range(steps):
            self.step()


# %%
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.occupancy = 0
        self.exits = []

    def has_space(self):
        return self.occupancy < self.capacity

    def available_exits(self):
        return [exit for exit in self.exits if exit.valid()]

    def random_valid_exit(self):
        import random
        if not self.available_exits():
            return None
        return random.choice(self.available_exits())

    def add_exit(self, name, target):
        self.exits.append(Exit(name, target))


# %%
class Person:
    def __init__(self, name, room=None):
        self.name = name
        self.room = room

    def use(self, exit):
        self.room.occupancy -= 1
        destination = exit.target
        destination.occupancy += 1
        self.room = destination
        print("{some} goes {action} to the {where}".format(some=self.name,
                                                           action=exit.name,
                                                           where=destination.name))

    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)

    def describe(self):
        print("{who} is in the {where}".format(who=self.name,
                                               where=self.room.name))


# %%
class Exit:
    def __init__(self, name, target):
        self.name = name
        self.target = target

    def valid(self):
        return self.target.has_space()


# %%
house = Maze('My New House')

# %%
living = house.add_room('livingroom', 2)
bed = house.add_room('bedroom', 1)
garden = house.add_room('garden', 3)
kitchen = house.add_room('kitchen', 1)

# %%
house.add_exit('north', living, kitchen, 'south')

# %%
house.add_exit('upstairs', living, bed, 'downstairs')

# %%
house.add_exit('outside', living, garden, 'inside')

# %%
house.add_exit('jump', bed, garden)

# %%
house.add_occupant('Graham', living)
house.add_occupant('Eric', garden)
house.add_occupant('TerryJ', bed)
house.add_occupant('John', garden)

# %%
house.simulate(3)

# %% [markdown]
# This is a huge topic, about which many books have been written. The differences between these two designs are important, and will have long-term consequences for the project. That is the how we start to think about **software engineering**, as opposed to learning to program, and is an important part of this course.

# %% [markdown]
# ### Exercise: Your own solution

# %% [markdown]
# Compare the two solutions above. Discuss with a partner which you like better, and why. Then, starting from scratch, design your own. What choices did you make that are different from mine?
