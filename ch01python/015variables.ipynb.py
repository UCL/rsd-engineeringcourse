# ---
# jupyter:
#   jekyll:
#     display_name: Variables
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Variables
#
# ## Variable assignment
#
# Python has built-in support for arithmetic expressions and so can be used as a calculator. When we evaluate an expression in Python, the result is displayed, but not necessarily stored anywhere.

# %%
2 + 2

# %%
4 * 2.5

# %% [markdown]
# If we want to access the result in subsequent code, we have to store it. We put it in a box, with a name on the box. This is a _variable_. In Python we _assign_ a value to a variable using the _assignment operator_ `=`

# %%
four = 2 + 2
four

# %% [markdown]
# As well as numeric [literal values](https://en.wikipedia.org/wiki/Literal_(computer_programming)) Python also has built in support for representing textual data as sequences of characters, which in computer science terminology are termed [_strings_](https://en.wikipedia.org/wiki/String_(computer_science)). Strings in Python are indicated by enclosing their contents in either a pair of single quotation marks `'...'` or a pair of double quotation marks `"..."`, for example

# %%
greeting = "hello world"

# %% [markdown]
# ## Naming variables
#
# We can name variables with any combination of lower and uppercase characters, digits and underscores `_` providing the first character is not a digit and the name is not a [reserved keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

# %%
fOuR = 4

# %%
four_integer = 4

# %%
integer_4 = 4

# %%
# invalid as name cannot begin with a digit
4_integer = 4

# %%
# invalid as for is a reserved word
for = 4

# %% [markdown]
# It is good practice to give variables descriptive and meaningful names to help make code self-documenting. As most modern development environments (including Jupyter Lab!) offer _tab completion_ there is limited disadvantage from a keystroke perspective of using longer  names. Note however that the names we give variables only have meaning to us:

# %%
two_plus_two = 5

# %% [markdown]
# ## _Aside:_ Reading error messages

# %% [markdown]
# We have already seen a couple of examples of Python error messages. It is important, when learning to program, to develop an ability to read an error message and find, from what can initially seem like confusing noise, the bit of the error message which tells you where the problem is.
#
# For example consider the following

# %%
number_1 = 1
number_2 = "2"
sum_of_numbers = number_1 + number_2

# %% [markdown]
# We may not yet know what `TypeError` or `Traceback` refer to. However, we can see that the error happens on the _third_ line of our code cell. We can also see that the error message: 
#
# > `unsupported operand type(s) for +: 'int' and 'str'`
#  
# ...tells us something important. Even if we don't understand the rest, this is useful for debugging!

# %% [markdown]
# ## Undefined variables and `None` 
#
# If we try to evaluate a variable that hasn't ever been defined, we get an error. 

# %%
seven

# %% [markdown]
# In Python names are case-sensitive so for example `six`, `Six` and `SIX` are all different variable names

# %%
six = 6
six

# %%
Six

# %% [markdown]
# There is a special `None` keyword in Python which can be assigned to variables to indicate a variable with no-value. This is _not_ the same as an undefined variable:

# %%
nothing

# %%
nothing = None
nothing

# %%
print(nothing)

# %% [markdown]
# Anywhere we can use a literal value, we can instead use a variable name, for example

# %%
5 + four * six

# %%
scary = six * six * six
scary

# %% [markdown]
# *Supplementary Materials*: There's more on variables at 
# [Software Carpentry](https://swcarpentry.github.io/python-novice-inflammation/01-intro/index.html).

# %% [markdown]
# ## Reassignment and multiple labels

# %% [markdown]
# We can reassign a variable - that is change what is in the box the variable labels.

# %%
scary = 25
scary

# %% [markdown]
# The data that was previously labelled by the variable is lost. No labels refer to it any more - so it has been [_garbage collected_](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)). We might imagine something pulled out of the box, and disposed of, to make way for the next occupant. In reality, though, it is the _label_ that has moved. 
#
# We can see this more clearly if we have more than one label referring to the same box

# %%
name = "Grace Hopper"
nom = name
print(name)
print(nom)

# %% [markdown]
# and we move just one of those labels:

# %%
nom = "Grace Brewster Murray Hopper"
print(name)
print(nom)

# %% [markdown]
# ## Variables and memory
#
# We can now better understand our mental model of variables as labels and boxes: each box is a piece of space (an *address*) in computer memory. Each label (_variable_) is a reference to such a place and the data contained in the memory defines an _object_ in Python. Python objects come in different types - so far we have encountered both numeric (integer) and textual (string) types - more on this later.
#
# When the number of labels on a box (_variables referencing an address_) gets down to zero, then the data in the box cannot be accessed any more. This will trigger Python's garbage collector, which will then 'empty' the box (_deallocated the memory at the address_), making it available again to store new data.
#
# Lower-level languages such as C and Fortran do not have garbage collectors as a standard feature. So a memory address with no references to it and which has not been specifically marked as free remains unavailable for other usage, which can lead to difficult to fix [_memory leak_](https://en.wikipedia.org/wiki/Memory_leak) bugs.
#
# When we execute

# %%
name = "Grace Hopper"
nom = name
nom = "Grace Brewster Murray Hopper"
name = "Admiral Hopper"

# %% [markdown]
# the following happens
#
# 1. A new text (_string_) object `"Grace Hopper"` is created at a free address in memory and the variable `name` is set to refer to that address
# 2. The variable `nom` is set to refer to the object at the address referenced by `name`
# 3. A new text (_string_) object `"Grace Brewster Murray Hopper"` is created at a free address in memory and the variable `nom` is set to refer to that address
# 4. A new text (_string_) object `"Admiral Hopper"` is created at a free address in memory, the variable `name` is set to refer to that address and the garbage collector deallocates the memory used to hold `"Grace Hopper"` as this memory is no longer referenced by any variables.

# %% [markdown]
# _Supplementary materials_: The website [Python Tutor](https://pythontutor.com/) has a great interactive tool for visualizing how memory and references work in Python which is great for visualising memory and references. 
# Try the [scenario we just looked at](https://pythontutor.com/visualize.html#code=name%20%3D%20%22Grace%20Hopper%22%0Anom%20%3D%20name%0Anom%20%3D%20%22Grace%20Brewster%20Murray%20Hopper%22%0Aname%20%3D%20%22Admiral%20Hopper%22&cumulative=false&curInstr=4&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

# %% [markdown]
# ## Variables in notebooks and kernels

# %% [markdown]
# When code cells are executed in a notebook, the variable names and values of the referenced objects persist between cells

# %%
number = 1

# %% [markdown]
# There if  we change a variable in one cell

# %%
number = number + 1

# %% [markdown]
# It keeps its new value for the next cell.

# %%
number

# %% [markdown]
# In Jupyter terminology the Python process in which we run the code in a notebook in is termed a _kernel_. The _kernel_ stores the variable names and referenced objects created by any code cells in the notebook that have been previously run. The `Kernel` menu in the menu bar at the top of the JupyterLab interface has an option `Restart kernel...`. Running this will restart the kernel currently being used by the notebook, clearing any currently defined variables and returning the kernel to a 'clean' state. As you cannot restore a kernel once restarted a warning message is displayed asking you to confirm you wish to restart.
#
# ## Cell run order
#
# Cells do **not** have to be evaluated in the order they appear in a notebook.
#
# If we go back to the code cell above with contents `number = number + 1`, and run it again, with <kbd>shift</kbd>+<kbd>enter</kbd> then `number` will change from 2 to 3, then from 3 to 4. Try it! 
#
# However, running cells out of order like this can make it hard to keep track of what values are currently assigned to variables. It also makes it difficult to reproduce computations as getting the same output requires rerunning the cells in the same order, and it will not always be possible to reconstruct what the order used was. 
#
# The number in square brackets in the prompt to the left of code cells, for example `[1]:` indicates the position in the overall cell run order of the last run of the cell. While this allows establishing if a cell last ran before or after another cell, if some cells are run multiple times then their previous run counter values will be overwritten so we lose information about the run order.
#
# In general if you are using notebooks in your own research you should try to make sure the notebook run and produce the desired outputs when the cells are executed sequentially from top to bottom. The `Kernel` menu provides an option to restart the current kernel and run all cells in order from top to bottom. If you just want to run a subset of the cells there is also an option to restart and run all cells from the top to the currently selected cell. The commands are useful for checking that a notebook will produce the expected output and run without errors when the cells are executed in order.
