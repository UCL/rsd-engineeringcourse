# ---
# jupyter:
#   jekyll:
#     display_name: Conditionality
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Control and Flow

# %% [markdown]
# ## Turing completeness

# %% [markdown]
# Now that we understand how we can use objects to store and model our data, we only need to be able to control the flow of our
# program in order to have a program that can, in principle, do anything!
#
# Specifically we need to be able to:
#
# * Control whether a program statement should be executed or not, based on a variable. "Conditionality"
# * Jump back to an earlier point in the program, and run some statements again. "Branching"

# %% [markdown]
# Once we have these, we can write computer programs to process information in arbitrary ways: we are *Turing Complete*!

# %% [markdown]
# ## Conditionality

# %% [markdown]
# Conditionality is achieved through Python's `if` statement:

# %%
x = -3
if x < 0:
    print(x, "is negative")
    print("This is controlled")
print("Always run this")

# %% [markdown]
# The **controlled** statements are indented. Once we remove the indent, the statements will once again happen regardless of whether the `if` statement is true of false.

# %% [markdown]
# As a side note, note how we included the values of `x` in the first print statement. This is a handy syntax for building strings that contain the values of variables. You can read more about it at this [Python String Formatting Best Practices guide](https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat) or in the [official documentation](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals).

# %% [markdown]
# ## Else and Elif

# %% [markdown]
# Python's if statement has optional elif (else-if) and else clauses:

# %%
x = -3
if x < 0:
    print("x is negative")
else:
    print("x is positive")

# %%
x = 5
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")

# %% [markdown]
# Try editing the value of x here, and note which section of the code is run and which are not.

# %%
choice = "dlgkhdglkhgkjhdkjgh"

if choice == "high":
    print(1)
elif choice == "medium":
    print(2)
else:
    print(3)

# %% [markdown]
# ## Comparison

# %% [markdown]
# `True` and `False` are used to represent **boolean** (true or false) values.

# %%
1 > 2

# %% [markdown]
# Comparison on strings is alphabetical - letters earlier in the alphabet are 'lower' than later letters.

# %%
"A" < "Z"

# %%
"UCL" > "King's"

# %% [markdown]
# There's no automatic conversion of the **string** True to the **boolean variable** `True`:

# %%
True == "True"

# %% [markdown]
# Be careful not to compare values of different types. At best, the language won't allow it and an issue an error, at worst it will allow it and do some behind-the-scenes conversion that may be surprising.

# %%
"1" < 2

# %% [markdown]
# Any statement that evaluates to `True` or `False` can be used to control an `if` Statement. Experiment with numbers (integers and floats) - what is equivalent to `True`?

# %%
0 == False

# %% [markdown]
# ## Automatic Falsehood

# %% [markdown]
# Various other things automatically count as true or false, which can make life easier when coding:

# %%
mytext = "Hello"
if mytext:
    print("Mytext is not empty")

mytext2 = ""
if mytext2:
    print("Mytext2 is not empty")

# %% [markdown]
# We can use logical `not` and logical `and` to combine true and false:

# %%
x = 3.2
if not (x > 0 and type(x) == int):
    print(x, "is not a positive integer")

# %% [markdown]
# `not` also understands magic conversion from false-like things to True or False.

# %%
not not "Who's there!"  #  Thanks to Mysterious Student

# %%
bool("")

# %%
bool("James")

# %%
bool([])

# %%
bool(["a"])

# %%
bool({})

# %%
bool({"name": "James"})

# %%
bool(0)

# %%
bool(1)

# %%
not 2 == 3

# %% [markdown]
# But subtly, although these quantities evaluate True or False in an if statement, they're not themselves actually True or False under ==:

# %%
[] == False

# %%
bool([]) == bool(False)

# %% [markdown]
# ## Indentation

# %% [markdown]
# In Python, indentation is semantically significant.
# You can choose how much indentation to use, so long as you
# are consistent, but four spaces is
# conventional. Please do not use tabs.
#
# In the notebook, and most good editors, when you press `<tab>`, you get four spaces.
#     

# %%
if x > 0:
    print(x)

# %% [markdown]
# ##  Pass

# %% [markdown]
#
# A statement expecting identation must have some indented code or it will create an error.
# This can be annoying when commenting things out (with `#`) inside a loop or conditional statement.
#
#
#

# %%
if x > 0:
    # print x
print("Hello")

# %% [markdown]
#
#
#
# So the `pass` statement (or `...`) is used to do nothing.
#
#
#

# %%
if x > 0:
    pass
print("Hello")
