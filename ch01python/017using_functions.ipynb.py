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
# # Using functions
#
# Functions in Python (and other programming languages) are modular units of code which specify a set of instructions to perform when the function is _called_ in code. Functions may take one or more input values as _arguments_ and may _return_ an output value. Functions can also have _side-effects_ such as printing information to a display. 
#
# ## Calling functions in Python
#
# Python provides a range of useful [built-in functions](https://docs.python.org/3/library/functions.html) for performing common tasks. For example the `len` function returns the length of a sequence object (such as a string) passed as input argument. To _call_ a function in Python we write the name of the function followed by a pair of parentheses `()`, with any arguments to the function being put inside the parentheses:

# %%
len("pneumonoultramicroscopicsilicovolcanoconiosis")

# %% [markdown]
# If a function can accept more than one argument they are separated by commas. For example the built-in `max` function when passed a pair of numeric arguments returns the larger value from the pair:

# %%
max(1, 5)

# %% [markdown]
# Another built-in function which we have already seen several times is `print`. Unlike `len` and `max`, `print` does not have an explicit return value as its purpose is to print a string representation of the argument(s) to a text display such as the output area of a notebook code cell. For functions like `print` which do not have an explicit return value, the special null value `None` we encountered previously will be used as the value of a call to the function if used in an expression or assigned to a variable:

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
# ## Getting help on functions
#
# The built-in `help` function, when passed a function, prints documentation for the function, which typically includes a description of the what arguments can be passed and what the function returns. For example

# %%
help(max)

# %% [markdown]
# In Jupyter notebooks an alternative way of displaying the documentation for a function is to write the function names followed by a question mark character `?`

# %%
# max?

# %% [markdown]
# ## Positional and keyword arguments and default values
#
# There are two ways of passing arguments to function in Python. In the examples so far the function arguments have only been identified by the position they appear in the argument list of the function. An alternative is to use named or _keyword_ arguments, by prefixing some or all of the arguments with the argument name followed by an equals sign. For example, there is a built-in function `round` which rounds decimal numbers to a specified precision. Using the `help` function we can read the documentation for `round` to check what arguments it accepts
#

# %%
help(round)

# %% [markdown]
# We see that `round` accepts two arguments, a `number` argument which specifies the number to round and a `ndigits` argument which specifies the number of decimal digits to round to. One way to call `round` is by passing positional arguments in the order specified in function signature `round(number, ndigits=None)` with the first argument corresponding to `number` and the second `ndigits`. For example

# %%
pi = 3.14159265359
round(pi, 2)

# %% [markdown]
# To be more expicit about which parameters of the function the arguments we are passing correspond to, we can instead however pass the arguments by name (as _keyword arguments_)

# %%
round(number=pi, ndigits=2)

# %% [markdown]
# We can in-fact mix and match position and keyword arguments, _providing that all keyword arguments come after any positional arguments_

# %%
round(pi, ndigits=2)

# %%
round(number=pi, 2)

# %% [markdown]
# Unlike positional arguments the ordering of keyword arguments does not matter so for example the following is also valid and equivalent to the calls above

# %%
round(ndigits=2, number=pi)

# %% [markdown]
# In the documentation for `round` we see that the second argument in the function signature is written `ndigits=None`. This indicates that `ndigits` is an _optional_ argument which takes the default value `None` if it is not specified. The documentation further states that
#
# > The return value is an integer if `ndigits` is omitted or `None`  
#
# which indicates that when `ndigits` is left as its default value (that is the argument is omitted or explicitly set to `None`) the `round` function returns the value of `number` rounded to the nearest integer. The following are all equivalent therefore

# %%
round(pi)

# %%
round(number=pi)

# %%
round(number=pi, ndigits=None)

# %% [markdown]
# ## Functions are objects
#
# A powerful feature of Python (and one that can take a little while to wrap your head around) is that functions are just a particular type of object and so can be for example assigned to variables or passed as arguments to other functions. We have in fact already seen examples of this when using the `help` function, with a function passed as the (only) argument to `help`. We can also assign functions to variables

# %%
my_print = print
my_print

# %%
help(my_print)

# %%
my_print("Hello")

# %% [markdown]
# While giving function aliases like this may not seem particularly useful at the moment, we will see that the ability to pass functions to other functions and assign functions to variables can be very useful in certain contexts.
