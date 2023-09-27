# ---
# jupyter:
#   jekyll:
#     display_name: Working with files
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Working with Data

# %% [markdown]
# ## Loading data from files

# %% [markdown]
# ### Loading data

# %% [markdown]
# An important part of this course is about using Python to analyse and visualise data.
# Most data, of course, is supplied to us in various *formats*: spreadsheets, database dumps, or text files in various formats (csv, tsv, json, yaml, hdf5, netcdf)
# It is also stored in some *medium*: on a local disk, a network drive, or on the internet in various ways.
# It is important to distinguish the data format, how the data is structured into a file, from the data's storage, where it is put. 
#
# We'll look first at the question of data *transport*: loading data from a disk, and at downloading data from the internet.
# Then we'll look at data *parsing*: building Python structures from the data.
# These are related, but separate questions.

# %% [markdown]
# ### An example datafile

# %% [markdown]
# Let's write an example datafile to disk so we can investigate it. We'll just use a plain-text file. Jupyter notebook provides a way to do this: if we put
# `%%writefile` at the top of a cell, instead of being interpreted as python, the cell contents are saved to disk.

# %%
# %%writefile mydata.txt
A poet once said, 'The whole universe is in a glass of wine.'
We will probably never know in what sense he meant it, 
for poets do not write to be understood. 
But it is true that if we look at a glass of wine closely enough we see the entire universe. 
There are the things of physics: the twisting liquid which evaporates depending
on the wind and weather, the reflection in the glass;
and our imagination adds atoms.
The glass is a distillation of the earth's rocks,
and in its composition we see the secrets of the universe's age, and the evolution of stars. 
What strange array of chemicals are in the wine? How did they come to be? 
There are the ferments, the enzymes, the substrates, and the products.
There in wine is found the great generalization; all life is fermentation.
Nobody can discover the chemistry of wine without discovering, 
as did Louis Pasteur, the cause of much disease.
How vivid is the claret, pressing its existence into the consciousness that watches it!
If our small minds, for some convenience, divide this glass of wine, this universe, 
into parts -- 
physics, biology, geology, astronomy, psychology, and so on -- 
remember that nature does not know it!

So let us put it all back together, not forgetting ultimately what it is for.
Let it give us one more final pleasure; drink it and forget it all!
   - Richard Feynman

# %% [markdown]
# Where did that go? It went to the current folder, which for a notebook, by default, is where the notebook is on disk.

# %%
import os # The 'os' module gives us all the tools we need to search in the file system
os.getcwd() # Use the 'getcwd' function from the 'os' module to find where we are on disk.

# %% [markdown]
# Can we see if it is there?

# %%
import os
[x for x in os.listdir(os.getcwd()) if ".txt" in x]

# %% [markdown]
# Yep! Note how we used a list comprehension to filter all the extraneous files.

# %% [markdown]
# ### Path independence and `os`

# %% [markdown]
# We can use `dirname` to get the parent folder for a folder, in a platform independent-way.

# %%
os.path.dirname(os.getcwd())

# %% [markdown]
# We could do this manually using `split`:

# %%
"/".join(os.getcwd().split("/")[:-1])

# %% [markdown]
# But this would not work on Windows, where path elements are separated with a `\` instead of a `/`. So it's important 
# to use `os.path` for this stuff.

# %% [markdown]
# **Supplementary Materials**: If you're not already comfortable with how files fit into folders, and folders form a tree,
#     with folders containing subfolders, then look at [this Software Carpentry lesson on navigating the file system](http://swcarpentry.github.io/shell-novice/02-filedir/index.html). 
#
# Satisfy yourself that after using `%%writefile`, you can then find the file on disk with Windows Explorer, OSX Finder, or the Linux Shell.

# %% [markdown]
# We can see how in Python we can investigate the file system with functions in the `os` module, using just the same programming approaches as for anything else.

# %% [markdown]
# We'll gradually learn more features of the `os` module as we go, allowing us to move around the disk, `walk` around the
# disk looking for relevant files, and so on. These will be important to master for automating our data analyses.

# %% [markdown]
# ### Opening files in Python

# %% [markdown]
# So, let's read our file:

# %%
myfile = open('mydata.txt')

# %%
type(myfile)

# %% [markdown]
# Even though the name of this type is not very clear, it offers various ways of accessing the file.
#
# We can go line-by-line, by treating the file as an iterable:

# %%
[x for x in myfile]

# %% [markdown]
# If we do that again, the file has already finished, there is no more data.

# %%
[x for x in myfile]

# %% [markdown]
# We need to 'rewind' it!

# %%
myfile.seek(0)
[len(x) for x in myfile if 'know' in x]

# %% [markdown]
# It's really important to remember that a file is a *different* built in type than a string.

# %% [markdown]
# ### Working with files

# %% [markdown]
# We can read one line at a time with `readline`: 

# %%
myfile.seek(0)
first = myfile.readline()

# %%
first

# %%
second = myfile.readline()

# %%
second

# %% [markdown]
# We can read the whole remaining file with `read`:

# %%
rest = myfile.read()

# %%
rest

# %% [markdown]
# Which means that when a file is first opened, read is useful to just get the whole thing as a string:

# %%
open('mydata.txt').read()

# %% [markdown]
# You can also read just a few characters:

# %%
myfile.seek(1335)

# %%
myfile.read(15)

# %% [markdown]
# ### Converting strings to files

# %% [markdown]
# Because files and strings are different types, we CANNOT just treat strings as if they were files:

# %%
mystring = "Hello World\n My name is James"

# %%
mystring

# %%
mystring.readline()

# %% [markdown]
# This is important, because some file format parsers expect input from a **file** and not a string. 
# We can convert between them using the `StringIO` class of the [io module](https://docs.python.org/3/library/io.html) in the standard library:

# %%
from io import StringIO

# %%
mystringasafile = StringIO(mystring)

# %%
mystringasafile.readline()

# %%
mystringasafile.readline()

# %% [markdown]
# Note that in a string, `\n` is used to represent a newline.

# %% [markdown]
# ### Closing files

# %% [markdown]
# We really ought to close files when we've finished with them, as it makes our work more efficient and safer. (On a shared computer,
# this is particularly important)

# %%
myfile.close()

# %% [markdown]
# Because it's so easy to forget this, python provides a **context manager** to open a file, then close it automatically at
# the end of an indented block:

# %%
with open('mydata.txt') as somefile:
    content = somefile.read()

content

# %% [markdown]
# The code to be done while the file is open is indented, just like for an `if` statement.

# %% [markdown]
# You should pretty much **always** use this syntax for working with files.
# We will see more about context managers in a [later chapter](../ch07dry/025Iterators.html).

# %% [markdown]
# ### Writing files

# %% [markdown]
# We might want to create a file from a string in memory. We can't do this with the notebook's `%%writefile` -- this is
# just a notebook convenience, and isn't very programmable.

# %% [markdown]
# When we open a file, we can specify a 'mode', in this case, 'w' for writing. ('r' for reading is the default.)

# %%
with open('mywrittenfile', 'w') as target:
    target.write('Hello')
    target.write('World')

# %%
with open('mywrittenfile','r') as source:
    print(source.read())

# %% [markdown]
# And we can "append" to a file with mode 'a':

# %%
with open('mywrittenfile', 'a') as target:
    target.write('Hello')
    target.write('James')

# %%
with open('mywrittenfile','r') as source:
    print(source.read())

# %% [markdown]
# If a file already exists, mode 'w' will overwrite it.
