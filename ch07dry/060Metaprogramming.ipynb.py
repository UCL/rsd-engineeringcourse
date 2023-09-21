# ---
# jupyter:
#   jekyll:
#     display_name: Metaprogramming
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Metaprogramming

# %% [markdown]
# Warning: Advanced topic!

# %% [markdown]
# ### Metaprogramming globals

# %% [markdown]
#
# Consider a bunch of variables, each of which need initialising and incrementing:
#
#
#

# %%
bananas = 0
apples = 0
oranges = 0
bananas += 1
apples += 1
oranges += 1

# %% [markdown]
#
#
# The right hand side of these assignments doesn't respect the DRY principle. We
# could of course define a variable for our initial value:
#
#
#

# %%
initial_fruit_count = 0
bananas = initial_fruit_count
apples = initial_fruit_count
oranges = initial_fruit_count


# %% [markdown]
#
#
# However, this is still not as DRY as it could be: what if we wanted to replace
# the assignment with, say, a class constructor and a buy operation:
#
#
#

# %%
class Basket:
    def __init__(self):
        self.count = 0
    def buy(self):
        self.count += 1

bananas = Basket()
apples = Basket()
oranges = Basket()
bananas.buy()
apples.buy()
oranges.buy()

# %% [markdown]
#
#
# We had to make the change in three places. Whenever you see a situation where a
# refactoring or change of design might require you to change the code in
# multiple places, you have an opportunity to make the code DRYer.
#
# In this case, metaprogramming for incrementing these variables would involve
# just a loop over all the variables we want to initialise:
#
#
#

# %%
baskets = [bananas, apples, oranges]
for basket in baskets: 
    basket.buy()

# %% [markdown]
#
#
# However, this trick **doesn't** work for initialising a new variable:
#
#
#

# %%
from pytest import raises
with raises(NameError):
    baskets = [bananas, apples, oranges, kiwis]

# %% [markdown]
#
#
# So can we declare a new variable programmatically? Given a list of the
# **names** of fruit baskets we want, initialise a variable with that name?
#
#
#

# %%
basket_names = ['bananas', 'apples', 'oranges', 'kiwis']

globals()['apples']

# %% [markdown]
#
#
#
# Wow, we can! Every module or class in Python, is, under the hood, a special
# dictionary, storing the values in its **namespace**. So we can create new
# variables by assigning to this dictionary. globals() gives a reference to the
# attribute dictionary for the current module
#
#
#

# %%
for name in basket_names:
    globals()[name] = Basket()


kiwis.count

# %% [markdown]
#
#
# This is **metaprogramming**.
#
# I would NOT recommend using it for an example as trivial as the one above. 
# A better, more Pythonic choice here would be to use a data structure to manage your set of fruit baskets:
#
#
#

# %%
baskets = {}
for name in basket_names:
    baskets[name] = Basket()

baskets['kiwis'].count

# %% [markdown]
#
#
# Or even, using a dictionary comprehension:
#
#
#

# %%
baskets = {name: Basket() for name in baskets}
baskets['kiwis'].count


# %% [markdown]
#
#
# Which is the nicest way to do this, I think. Code which feels like
# metaprogramming is needed to make it less repetitive can often instead be DRYed
# up using a refactored data structure, in a way which is cleaner and more easy
# to understand. Nevertheless, metaprogramming is worth knowing. 
#

# %% [markdown]
# ### Metaprogramming class attributes

# %% [markdown]
# We can metaprogram the attributes of a **module** using the globals() function.
#
# We will also want to be able to metaprogram a class, by accessing its attribute dictionary.
#
# This will allow us, for example, to programmatically add members to a class.

# %%
class Boring: 
    pass


# %% [markdown]
# If we are adding our own attributes, we can just do so directly:

# %%
x = Boring()

x.name = "Michael"

# %%
x.name

# %% [markdown]
# And these turn up, as expected, in an attribute dictionary for the class:

# %%
x.__dict__

# %% [markdown]
# We can use `getattr` to access this special dictionary:

# %%
getattr(x, 'name')

# %% [markdown]
# If we want to add an attribute given it's name as a string, we can use setattr:

# %%
setattr(x, 'age', 75)

x.age

# %% [markdown]
# And we could do this in a loop to programmatically add many attributes.

# %% [markdown]
# The real power of accessing the attribute dictionary comes when we realise that
# there is *very little difference* between member data and member functions.

# %% [markdown]
# Now that we know, from our functional programming, that **a function is just a
# variable that can be *called* with `()`**, we can set an attribute to a function,
# and
# it becomes a member function!

# %%
setattr(Boring, 'describe', lambda self: f"{self.name} is {self.age}")

# %%
x.describe()

# %%
x.describe

# %%
Boring.describe

# %% [markdown]
# Note that we set this method as an attribute of the class, not the instance, so it is available to other instances of `Boring`:

# %%
y = Boring()
y.name = 'Terry'
y.age  = 78

# %%
y.describe()


# %% [markdown]
# We can define a standalone function, and then **bind** it to the class. Its first argument automagically becomes
# `self`.

# %%
def broken_birth_year(b_instance):
    import datetime
    current = datetime.datetime.now().year
    return current - b_instance.age


# %%
Boring.birth_year = broken_birth_year

# %%
x.birth_year()

# %%
x.birth_year

# %%
x.birth_year.__name__


# %% [markdown]
# ### Metaprogramming function locals

# %% [markdown]
# We can access the attribute dictionary for the local namespace inside a
# function with `locals()` but this *cannot be written to*.
#
# Lack of safe
# programmatic creation of function-local variables is a flaw in Python.

# %%
class Person:
    def __init__(self, name, age, job, children_count):
        for name, value in locals().items():
            if name == 'self': 
                continue
            print(f"Setting self.{name} to {value}")
            setattr(self, name, value)


# %%
terry = Person("Terry", 78, "Screenwriter", 0)

# %%
terry.name


# %% [markdown]
# ### Metaprogramming warning!

# %% [markdown]
#
# Use this stuff **sparingly**!
#
# The above example worked, but it produced Python code which is not particularly understandable.
# Remember, your objective when programming is to produce code which is **descriptive of what it does**.
#
# The above code is **definitely** less readable, less maintainable and more error prone than:
#
#
#

# %%
class Person:
    def __init__(self, name, age, job, children_count):
        self.name = name
        self.age = age
        self.job = job
        self.children_count = children_count

# %% [markdown]
#
#
#
# Sometimes, metaprogramming will be **really** helpful in making non-repetitive
# code, and you should have it in your toolbox, which is why I'm teaching you it.
# But doing it all the time overcomplicated matters. We've talked a lot about the
# DRY principle, but there is another equally important principle:
#
# > **KISS**: *Keep it simple, Stupid!*
#
# Whenever you write code and you think, "Gosh, I'm really clever",you're
# probably *doing it wrong*. Code should be about clarity, not showing off.
#
