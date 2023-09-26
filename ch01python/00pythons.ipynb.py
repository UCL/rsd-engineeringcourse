# ---
# jupyter:
#   jekyll:
#     display_name: Many kinds of Python
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Introduction to Python

# %% [markdown]
# ## Introduction

# %% [markdown]
# ### Why teach Python?

# %% [markdown]
#
# * In this first session, we will introduce [Python](http://www.python.org).
# * This course is about programming for data analysis and visualisation in research.
# * It's not mainly about Python.
# * But we have to use some language.
#

# %% [markdown]
# ### Why Python?

# %% [markdown]
#
# * Python is quick to program in
# * Python is popular in research, and has lots of libraries for science
# * Python interfaces well with faster languages
# * Python is free, so you'll never have a problem getting hold of it, wherever you go.
#

# %% [markdown]
# ### Why write programs for research?

# %% [markdown]
#
# * Not just labour saving
# * Scripted research can be tested and reproduced
#

# %% [markdown]
# ### Sensible Input  - Reasonable Output

# %% [markdown]
# Programs are a rigorous way of describing data analysis for other researchers, as well as for computers.
#
# Computational research suffers from people assuming each other's data manipulation is correct. By sharing codes,
# which are much more easy for a non-author to understand than spreadsheets, we can avoid the "SIRO" problem. The old saw "Garbage in Garbage out" is not the real problem for science:
#
# * Sensible input
# * Reasonable output
#
#

# %% [markdown]
# ## Many kinds of Python

# %% [markdown]
# ### The Jupyter Notebook

# %% [markdown]
# The easiest way to get started using Python, and one of the best for research data work, is the Jupyter Notebook.

# %% [markdown]
# In the notebook, you can easily mix code with discussion and commentary, and mix code with the results of that code;
# including graphs and other data visualisations.

# %%
### Make plot
# %matplotlib inline
import math

import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 4 * math.pi, 0.1)
eight = plt.figure()
axes = eight.add_axes([0, 0, 1, 1])
axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))

# %% [markdown]
# These notes are created using Jupyter notebooks and you may want to use it during the course. However, Jupyter notebooks won't be used for most of the activities and exercises done in class. To get hold of a copy of the notebook, follow the setup instructions shown on the course website, use the installation in Desktop@UCL (available in the teaching cluster rooms or [anywhere](https://www.ucl.ac.uk/isd/services/computers/remote-access/desktopucl-anywhere)), or go clone the [repository](https://github.com/UCL/rsd-engineeringcourse) on GitHub.

# %% [markdown]
# Jupyter notebooks consist of discussion cells, referred to as "markdown cells", and "code cells", which contain Python. This document has been created using Jupyter notebook, and this very cell is a **Markdown Cell**. 

# %%
print("This cell is a code cell")

# %% [markdown]
# Code cell inputs are numbered, and show the output below.

# %% [markdown]
# Markdown cells contain text which uses a simple format to achive pretty layout, 
# for example, to obtain:
#
# **bold**, *italic*
#
# * Bullet
#
# > Quote
#
# We write:
#
#     **bold**, *italic*
#
#     * Bullet
#
#     > Quote
#
# See the Markdown documentation at [This Hyperlink](http://daringfireball.net/projects/markdown/)

# %% [markdown]
# ### Typing code in the notebook

# %% [markdown]
# When working with the notebook, you can either be in a cell, typing its contents, or outside cells, moving around the notebook.
#
# * When in a cell, press escape to leave it. When moving around outside cells, press return to enter.
# * Outside a cell:
#   * Use arrow keys to move around.
#   * Press `b` to add a new cell below the cursor.
#   * Press `m` to turn a cell from code mode to markdown mode.
#   * Press `shift`+`enter` to calculate the code in the block.
#   * Press `h` to see a list of useful keys in the notebook.
# * Inside a cell:
#   * Press `tab` to suggest completions of variables. (Try it!)

# %% [markdown]
# *Supplementary material*: Learn more about [Jupyter notebooks](https://jupyter.org/).

# %% [markdown]
# The `%%` at the beginning of a cell is called *magics*. There's a [large list of them available](https://ipython.readthedocs.io/en/stable/interactive/magics.html) and you can [create your own](http://ipython.readthedocs.io/en/stable/config/custommagics.html).
#

# %% [markdown]
# ### Python at the command line

# %% [markdown]
# Data science experts tend to use a "command line environment" to work. You'll be able to learn this at our ["Software Carpentry" workshops](http://github-pages.arc.ucl.ac.uk/software-carpentry/), which cover other skills for computationally based research.

# %% language="bash"
# # Above line tells Python to execute this cell as *shell code*
# # not Python, as if we were in a command line
#
# python -c "print(2 * 4)"

# %% [markdown]
# ### Python scripts

# %% [markdown]
# Once you get good at programming, you'll  want to be able to write your own full programs in Python, which work just
# like any other program on your computer. Here are some examples:

# %% language="bash"
# echo "print(2 * 4)" > eight.py
# python eight.py

# %% [markdown]
# We can make the script directly executable (on Linux or Mac) by inserting a [hashbang](https://en.wikipedia.org/wiki/Shebang_(Unix%29)) and [setting the permissions](http://v4.software-carpentry.org/shell/perm.html) to execute.
#
# Note, the `%%writefile` cell magic will write the contents of the cell to the file `fourteen.py`.

# %%
# %%writefile fourteen.py
# #! /usr/bin/env python
print(2 * 7)

# %% language="bash"
# chmod u+x fourteen.py
# ./fourteen.py

# %% [markdown]
# ### Python Modules

# %% [markdown]
# A Python module is a file that contains a set of related functions or other code. The filename must have a `.py` extension.
#
# We can write our own Python modules that we can import and use in other scripts or even in this notebook:
#

# %%
# %%writefile draw_eight.py 
# Above line tells the notebook to treat the rest of this
# cell as content for a file on disk.
import math

import numpy as np
import matplotlib.pyplot as plt

def make_figure():
    """Plot a figure of eight."""

    theta = np.arange(0, 4 * math.pi, 0.1)
    eight = plt.figure()
    axes = eight.add_axes([0, 0, 1, 1])
    axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))

    return eight



# %% [markdown]
# In a real example, we could edit the file on disk
# using a code editor such as [VS code](https://code.visualstudio.com/).

# %%
import draw_eight # Load the library file we just wrote to disk

# %%
image = draw_eight.make_figure()

# %% [markdown]
# Note, we can import our `draw_eight` module in this notebook only if the file is in our current working directory (i.e. the folder this notebook is in).
#
# To allow us to import our module from anywhere on our computer, or to allow other people to reuse it on their own computer, we can create a [Python package](https://packaging.python.org/en/latest/).
#

# %% [markdown]
# ### Python packages
#
# A package is a collection of modules that can be installed on our computer and easily shared with others. We will learn how to create packages later on in this course.
#
# There is a huge variety of available packages to do pretty much anything. For instance, try `import antigravity` or `import this`.
#
