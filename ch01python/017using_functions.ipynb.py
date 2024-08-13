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
# ## Using functions
#
# Functions in Python (and other programming languages) are modular units of code which specify a set
# of instructions to perform when the function is _called_ in code. Functions may take one or more
# input values as _arguments_ and may _return_ an output value. Functions can also have _side-effects_
# such as printing information to a display. 
#
# ### Calling functions in Python
#
# Python provides a range of useful [built-in functions](https://docs.python.org/3/library/functions.html)
# for performing common tasks. For example the `len` function returns the length of a sequence object
# (such as a string) passed as input argument. To _call_ a function in Python we write the name of the
# function followed by a pair of parentheses `()`, with any arguments to the function being put inside
# the parentheses:

# %%
len("pneumonoultramicroscopicsilicovolcanoconiosis")

# %% [markdown]
# If a function can accept more than one argument they are separated by commas. For example the
# built-in `max` function when passed a pair of numeric arguments returns the larger value from
# the pair:

# %%
max(1, 5)

# %% [markdown]
# Another built-in function which we have already seen several times is `print`. Unlike `len` and
# `max`, `print` does not have an explicit return value as its purpose is to print a string representation
# of the argument(s) to a text display such as the output area of a notebook code cell. For functions
# like `print` which do not have an explicit return value, the special null value `None` we encountered
# previously will be used as the value of a call to the function if used in an expression or assigned to
# a variable:

# %%
return_value = print("Hello")
print(return_value)

# %% [markdown]
# Function calls can be placed anywhere we can use a literal value or a variable name, for example

# %%
name = "Jim"
len(name) * 8

# %%
total_length = len("Mike") + len("Bob")
print(total_length)

# %% [markdown]
# ### Using methods
#
# Objects come associated with a bunch of functions designed for working on objects of that type. We access these with a
# dot, just as we do for data attributes:

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
#
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
# ### Getting help on functions
#
# The built-in `help` function, when passed a function, prints documentation for the function, which typically
# includes a description of the what arguments can be passed and what the function returns. For example

# %%
help(max)

# %% [markdown]
# In Jupyter notebooks an alternative way of displaying the documentation for a function is to write the function
# names followed by a question mark character `?`

# %%
# max?

# %% [markdown]
# The 'dir' function, when applied to an object, lists all its attributes (properties and methods):

# %%
dir("Hexxo")

# %% [markdown]
# Most of these are confusing methods beginning and ending with __, part of the internals of python.
#
# Again, just as with error messages, we have to learn to read past the bits that are confusing, to the bit we want:

# %%
"Hexxo".replace("x", "l")

# %%
help("FIsh".replace)

# %% [markdown]
# ### Positional and keyword arguments and default values
#
# There are two ways of passing arguments to function in Python. In the examples so far the function arguments have
# only been identified by the position they appear in the argument list of the function. An alternative is to use
# named or _keyword_ arguments, by prefixing some or all of the arguments with the argument name followed by an equals
# sign. For example, there is a built-in function `round` which rounds decimal numbers to a specified precision. Using
# the `help` function we can read the documentation for `round` to check what arguments it accepts
#

# %%
help(round)

# %% [markdown]
# We see that `round` accepts two arguments, a `number` argument which specifies the number to round and a `ndigits`
# argument which specifies the number of decimal digits to round to. One way to call `round` is by passing positional
# arguments in the order specified in function signature `round(number, ndigits=None)` with the first argument
# corresponding to `number` and the second `ndigits`. For example

# %%
pi = 3.14159265359
round(pi, 2)

# %% [markdown]
# To be more expicit about which parameters of the function the arguments we are passing correspond to, we can instead
# however pass the arguments by name (as _keyword arguments_)

# %%
round(number=pi, ndigits=2)

# %% [markdown]
# We can in-fact mix and match position and keyword arguments, _providing that all keyword arguments come after any positional arguments_

# %%
round(pi, ndigits=2)

# %%
round(number=pi, 2)

# %% [markdown]
# Unlike positional arguments the ordering of keyword arguments does not matter so for example the following is also valid
# and equivalent to the calls above

# %%
round(ndigits=2, number=pi)

# %% [markdown]
# In the documentation for `round` we see that the second argument in the function signature is written `ndigits=None`.
# This indicates that `ndigits` is an _optional_ argument which takes the default value `None` if it is not specified.
# The documentation further states that
#
# > The return value is an integer if `ndigits` is omitted or `None`  
#
# which indicates that when `ndigits` is left as its default value (that is the argument is omitted or explicitly set
# to `None`) the `round` function returns the value of `number` rounded to the nearest integer. The following are all
# equivalent therefore

# %%
round(pi)

# %%
round(number=pi)

# %%
round(number=pi, ndigits=None)

# %% [markdown]
# ### Functions are just a type of object!
#
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
# ### Operators
#
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
#
# In python, these functions **do** exist, but they're actually **methods** of the first input: they're the mysterious `__` functions we saw earlier (Two underscores.)

# %%
x.__add__(7)

# %% [markdown]
# We call these symbols, `+`, `-` etc, "operators".
#
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
#
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
