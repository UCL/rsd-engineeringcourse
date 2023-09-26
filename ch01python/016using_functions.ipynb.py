# ---
# jupyter:
#   jekyll:
#     display_name: Using Functions
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Using Functions

# %% [markdown]
# ### Calling functions

# %% [markdown]
# We often want to do things to our objects that are more complicated than just assigning them to variables.

# %%
len("pneumonoultramicroscopicsilicovolcanoconiosis")

# %% [markdown]
# Here we have "called a function".

# %% [markdown]
# The function `len` takes one input, and has one output. The output is the length of whatever the input was.

# %% [markdown]
# Programmers also call function inputs "parameters" or, confusingly, "arguments".

# %% [markdown]
# Here's another example:

# %%
sorted("Python")

# %% [markdown]
# Which gives us back a *list* of the letters in Python, sorted alphabetically (more specifically, according to their [Unicode order](https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0000)).

# %% [markdown]
# The input goes in brackets after the function name, and the output emerges wherever the function is used.

# %% [markdown]
# So we can put a function call anywhere we could put a "literal" object or a variable. 

# %%
len('Jim') * 8

# %%
x = len('Mike')
y = len('Bob')
z = x + y

# %%
print(z)

# %% [markdown]
# ### Using methods

# %% [markdown]
# Objects come associated with a bunch of functions designed for working on objects of that type. We access these with a dot, just as we do for data attributes:

# %%
"shout".upper()

# %% [markdown]
# These are called methods. If you try to use a method defined for a different type, you get an error:

# %%
x = 5

# %%
type(x)

# %%
x.upper()

# %% [markdown]
# If you try to use a method that doesn't exist, you get an error:

# %%
x.wrong

# %% [markdown]
# Methods and properties are both kinds of **attribute**, so both are accessed with the dot operator.

# %% [markdown]
# Objects can have both properties and methods:

# %%
z = 1 + 5j

# %%
z.real

# %%
z.conjugate()

# %%
z.conjugate

# %% [markdown]
# ### Functions are just a type of object!

# %% [markdown]
# Now for something that will take a while to understand: don't worry if you don't get this yet, we'll
# look again at this in much more depth later in the course.
#
# If we forget the (), we realise that a *method is just a property which is a function*!

# %%
z.conjugate

# %%
type(z.conjugate)

# %%
somefunc = z.conjugate

# %%
somefunc()

# %% [markdown]
# Functions are just a kind of variable, and we can assign new labels to them:

# %%
sorted([1, 5, 3, 4])

# %%
magic = sorted

# %%
type(magic)

# %%
magic(["Technology", "Advanced"])

# %% [markdown]
# ### Getting help on functions and methods

# %% [markdown]
# The 'help' function, when applied to a function, gives help on it!

# %%
help(sorted)

# %% [markdown]
# The 'dir' function, when applied to an object, lists all its attributes (properties and methods):

# %%
dir("Hexxo")

# %% [markdown]
# Most of these are confusing methods beginning and ending with __, part of the internals of python.

# %% [markdown]
# Again, just as with error messages, we have to learn to read past the bits that are confusing, to the bit we want:

# %%
"Hexxo".replace("x", "l")

# %%
help("FIsh".replace)

# %% [markdown]
# ### Operators

# %% [markdown]
# Now that we know that functions are a way of taking a number of inputs and producing an output, we should look again at
# what happens when we write:

# %%
x = 2 + 3

# %%
print(x)

# %% [markdown]
# This is just a pretty way of calling an "add" function. Things would be more symmetrical if add were actually written
#
#     x = +(2, 3)
#     
# Where '+' is just the name of the name of the adding function.

# %% [markdown]
# In python, these functions **do** exist, but they're actually **methods** of the first input: they're the mysterious `__` functions we saw earlier (Two underscores.)

# %%
x.__add__(7)

# %% [markdown]
# We call these symbols, `+`, `-` etc, "operators".

# %% [markdown]
# The meaning of an operator varies for different types:

# %%
"Hello" + "Goodbye"

# %%
[2, 3, 4] + [5, 6]

# %% [markdown]
# Sometimes we get an error when a type doesn't have an operator:

# %%
7 - 2

# %%
[2, 3, 4] - [5, 6]

# %% [markdown]
# The word "operand" means "thing that an operator operates on"!

# %% [markdown]
# Or when two types can't work together with an operator:

# %%
[2, 3, 4] + 5

# %% [markdown]
# To do this, put:

# %%
[2, 3, 4] + [5]

# %% [markdown]
# Just as in Mathematics, operators have a built-in precedence, with brackets used to force an order of operations:

# %%
print(2 + 3 * 4)

# %%
print((2 + 3) * 4)

# %% [markdown]
# *Supplementary material*: [Python operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence).
