# ---
# jupyter:
#   jekyll:
#     display_name: Conditionality
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Control and Flow

# %% [markdown]
# ### Turing completeness

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
# ### Conditionality

# %% [markdown]
# Conditionality is achieved through Python's `if` statement:

# %%
x = 5

if x < 0:
    print(f"{x} is negative")

# %% [markdown]
# The absence of output here means the if clause prevented the print statement from running.

# %%
x = -10

if x < 0:
    print(f"{x} is negative")

# %% [markdown]
# The first time through, the print statement never happened.

# %% [markdown]
# The **controlled** statements are indented. Once we remove the indent, the statements will once again happen regardless. 

# %% [markdown]
# ### Else and Elif

# %% [markdown]
# Python's if statement has optional elif (else-if) and else clauses:

# %%
x = 5
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
# Try editing the value of x here, and note that other sections are found.

# %%
choice = 'high'

if choice == 'high':
    print(1)
elif choice == 'medium':
    print(2)
else:
    print(3)

# %% [markdown]
# ### Comparison

# %% [markdown]
# `True` and `False` are used to represent **boolean** (true or false) values.

# %%
1 > 2

# %% [markdown]
# Comparison on strings is alphabetical.

# %%
"UCL" > "KCL"

# %% [markdown]
# But case sensitive:

# %%
"UCL" > "kcl"

# %% [markdown]
# There's no automatic conversion of the **string** True to true:

# %%
True == "True"

# %% [markdown]
# In python two there were subtle implied order comparisons between types, but it was  bad style to rely on these.
# In python three, you cannot compare these.

# %%
'1' < 2

# %%
'5' < 2

# %%
'1' > 2

# %% [markdown]
# Any statement that evaluates to `True` or `False` can be used to control an `if` Statement.

# %% [markdown]
# ### Automatic Falsehood

# %% [markdown]
# Various other things automatically count as true or false, which can make life easier when coding:

# %%
mytext = "Hello"

# %%
if mytext:
    print("Mytext is not empty")
    

# %%
mytext2 = ""

# %%
if mytext2:
    print("Mytext2 is not empty")

# %% [markdown]
# We can use logical not and logical and to combine true and false:

# %%
x = 3.2
if not (x > 0 and isinstance(x, int)):
    print(x,"is not a positive integer")

# %% [markdown]
# `not` also understands magic conversion from false-like things to True or False.

# %%
not not "Who's there!" # Thanks to Mysterious Student

# %%
bool("")

# %%
bool("Graham")

# %%
bool([])

# %%
bool(['a'])

# %%
bool({})

# %%
bool({'name': 'Graham'})

# %%
bool(0)

# %%
bool(1)

# %% [markdown]
# But subtly, although these quantities evaluate True or False in an if statement, they're not themselves actually True or False under ==:

# %%
[] == False

# %%
bool([]) == False

# %% [markdown]
# ### Indentation

# %% [markdown]
# In Python, indentation is semantically significant.
# You can choose how much indentation to use, so long as you
# are consistent, but four spaces is
# conventional. Please do not use tabs.
#
# In the notebook, and most good editors, when you press `<tab>`, you get four spaces.
#     

# %% [markdown]
# No indentation when it is expected, results in an error:

# %%
x = 2

# %%
if x > 0:
print(x)

# %% [markdown]
# but:

# %%
if x > 0:
    print(x)

# %% [markdown]
# ###  Pass

# %% [markdown]
#
# A statement expecting identation must have some indented code.
# This can be annoying when commenting things out. (With `#`)
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
# So the `pass` statement is used to do nothing.
#
#
#

# %%
if x > 0:
    # print x
    pass

print("Hello")
