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
# # Introduction
#
# ## Why teach Python?
#
# * In this first session, we will introduce [Python](http://www.python.org).
# * This course is about programming for data analysis and visualisation in research.
# * It's not mainly about Python.
# * But we have to use some language.
#
# ### Why Python?
#
# * Python has a readable [syntax](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
#   that makes it relatively quick to pick up.
# * Python is popular in research, and has lots of libraries for science.
# * Python interfaces well with faster languages.
# * Python is free, so you'll never have a problem getting hold of it, wherever you go.
#
#
# ### Why write programs for research?
#
# * Not just labour saving.
# * Scripted research can be tested and reproduced.
#
# ### Sensible input - reasonable output
#
# Programs are a rigorous way of describing data analysis for other researchers, as well as for computers.
#
# Computational research suffers from people assuming each other's data manipulation is correct.
# By sharing _readable_, _reproducible_ and _well-tested_ code, which makes all of the data processing
# steps used in an analysis explicit and checks that each of those steps behaves as expected, we enable
# other researchers to understand and assesss the validity of those analysis steps for themselves.
# In a research code context the problem is generally not so much _garbage in, garbage out_, but _sensible
# input, reasonable output_: 'black-box' analysis pipelines that given sensible looking data inputs produce
# reasonable appearing but incorrect analyses as outputs.
#
# ## Many kinds of Python
#
# ### Python notebooks
#
# A particularly easy way to get started using Python, and one particularly suited to the sort of
# exploratory work common in a research context, is using [Jupyter](https://jupyter.org/https://jupyter.org/)
# notebooks. 
#
# In a notebook, you can easily mix code with discussion and commentary, and display the results
# outputted by code alongside the code itself, including graphs and other data visualisations. 
#
# For example if we wish to plot a figure-eight curve
# ([lemniscate](https://en.wikipedia.org/wiki/Lemniscate_of_Gerono)), we can include the parameteric
# equations $x = \sin(2\theta) / 2, y = \cos(\theta), \theta \in [0, 2\pi)$ which mathematically define
# the curve as well as corresponding Python code to plot the curve and the output of that code all within
# the same notebook:

# %%
# Plot lemniscate curve
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
x = np.sin(2 * theta) / 2
y = np.cos(theta)
fig, ax = plt.subplots(figsize=(3, 6))
lines = ax.plot(x, y)

# %% [markdown]
#
# #### Notebook cells
#
# Jupyter notebooks consist of sequence of _cells_. Cells can be of two main types:
#
#   * _Markdown cells_: Cells containing descriptive text and discussion with rich-text formatting
#     via the [Markdown](https://en.wikipedia.org/wiki/Markdown) text markup language.
#   * _Code cells_: Cells containing Python code, which is displayed with syntax highlighting.
#     The results returned by the computation performed when running the cell are displayed below the cell as the cell _output_, with Jupyter having a _rich display_ system allowing embedding a range of different outputs including for example static images, videos and interactive widgets.
#
# The document you are currently reading is a Jupyter notebook, and this text you are reading is 
# Markdown cell in the notebook. Below we see an example of a code cell.

# %%
print("This cell is a code cell")

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# Code cell inputs are numbered, with the cell output shown immediately below the input. Here the output
# is the text that we instruct the cell to print to the standard output stream. Cells will also display
# a representation of the value outputted by the last line in the cell, if any. For example

# %%
print("This text will be displayed\n")
"This is text will also be displayed\n"

# %% [markdown]
# There is a small difference in the formatting of the output here, with the `print` function displaying
# the text without quotation mark delimiters and with any _escaped_ special characters (such as the
# `"\n"` newline character here) processed.
#
# #### Markdown formatting
#
# The Markdown language used in Markdown cells provides a simple way to add basic text formatting to the
# rendered output while aiming to be retain the readability of the original Markdown source. For example
# to achieve the following rendered output text
#
# **bold**, *italic*, ~~striketrough~~, `monospace`
#
# * Bullet
#
# > Quote
#
# [Link to search](https://duckduckgo.com/)
#
# We can use the following Markdown text
#
# ```Markdown
# **bold**, *italic*, ~~striketrough~~, `monospace`
#
# * Bullet
#
# > Quote
#
# [Link to search](https://duckduckgo.com/)
# ```
#
# For more information
# [see this tutorial notebook in the official Jupyter documentation](https://nbviewer.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Working%20With%20Markdown%20Cells.ipynb).
#
# #### Editing and running cells in the notebook
#
# When working with the notebook, you can either be editing the content of a cell (termed _edit mode_),
# or outside the cells, navigating around the notebook (termed _command mode_).
#
# * When in _edit mode_ in a cell, press <kbd>esc</kbd> to leave it and change to _command mode_. 
# * When navigating between cells in _command mode_, press <kbd>enter</kbd> to change in to _edit mode_ in the selected cell.
# * When in _command mode_:
#   * The currently selected cell will be shown by a <div style='display: inline; border-right: solid 5px #1976d2; padding-right: 2px;'>blue highlight</div> to the left of the cell.
#   * Use the arrow keys <kbd>▲</kbd> and <kbd>▼</kbd> to navigate up and down between cells.
#   * Press <kbd>a</kbd> to add a new cell above the currently selected cell.
#   * Press <kbd>b</kbd> to add a new cell below the currently selected cell.
#   * Press <kbd>d</kbd><kbd>d</kbd> to delete the currently selected cell.
#   * Press <kbd>m</kbd> to change a code cell to a Markdown cell.
#   * Press <kbd>y</kbd> to change a Markdown cell to a code cell.
#   * Press <kbd>shift</kbd>+<kbd>l</kbd> to toggle displaying line numbers on the currently selected cell.
#   * Press <kbd>shift</kbd>+<kbd>enter</kbd> to run the code in a currently selected code cell and move to the next cell. 
#   * Press <kbd>ctrl</kbd>+<kbd>enter</kbd> to run the code in a currently selected code cell and keep the current cell selected. 
#   * Press <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>c</kbd> to access the command palette and search useful actions in the notebook.
# * When in _edit mode_:
#   * Press <kbd>tab</kbd> to suggest completions of variable names and object attribute. (Try it!)
#   * Press <kbd>shift</kbd>+<kbd>tab</kbd> when in the argument list of a function to display a pop-up showing documentation for the function.
#
# *Supplementary material*: Learn more about
# [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html/).
#
# ### Python interpreters
#
# An alternative to running Python code via a notebook interface is to run commands in a
# Python _interpreter_ (also known as an _interactive shell_ or _read-eval-print-loop (REPL)_).
# This is similar in concept to interacting with your operating system via a command-line interface
# such as the `bash` or `zsh` shells in Linux and MacOS or `Command Prompt` in Windows. A Python
# interpreter provides a _prompt_ into which we can type Python code corresponding to commands we
# wish to execute; we then execute this code by hitting  <kbd>enter</kbd> with any output from the
# computation being displayed before returning to the prompt again.
#
# We will not further explore using Python via an interpreter in this course but if you wish to
# learn more about such command-line interfaces we recommend you attend one of the
# [Software Carpentry](https://software-carpentry.org/lessons/https://software-carpentry.org/lessons/)
# workshops (sessions are regularly organised by [our group](http://rits.github-pages.ucl.ac.uk/software-carpentry/)),
# which covers this and other skills for computationally based research.

# %% [markdown]
# ### Python libraries
#
# A very common requirement in research (and all other!) programming is needing to reuse code in
# multiple different files. While it may seem that copying-and-pasting is an adequate solution to this
# problem, this should generally be avoided wherever possible and code which we wish to reuse
# _factored out_ in to _libraries_ which we we can _import_ in to other files to access the functionality
# of this code. 
#
# Compared to copying and pasting code, writing and using libraries has the major advantage of meaning
# if we spot a bug in the code we only need to fix it once in the underlying library, and we straight away
# have the fixed code available everywhere the library is used rather than having to separately implement
# the fix in each file it is used. This similarly applies to for example adding new features to a piece of
# code. By creating libraries we also make it easier for other researchers to use our code.
#
# While it is simple to use libraries within a notebook (and we have already seen examples of this when we
# imported the Python libraries NumPy and Matplotlib in the figure-eight plot example above), it is non-trivial
# to use code from one notebook in another without copying-and-pasting. To create Python libraries we therefore
# generally write the code in to text files with a `.py` extension which in Python terminology are called _modules_.
# The code can in these file can then be used in notebooks (or other modules) using the Python `import` statement.
# For example the cell below creates a file `draw_eight.py` in the same directory as this notebook containing Python
# code defining a _function_ (we will cover how to define and call functions later in the course) which creates a
# figure-eight plot and return the figure object.

# %%
# %%writefile draw_eight.py
# The above line tells the notebook to write the rest of the cell content to a file draw_eight.py

import numpy as np
import matplotlib.pyplot as plt

def make_figure():
    theta = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plt.subplots(figsize=(3, 6))
    ax.plot(np.sin(2 * theta) / 2, np.cos(theta))
    return fig


# %% [markdown]
# We can use this code in the notebook by _importing_ the `draw_eight` module and then _calling_ the
# `make_figure` function defined in the module.

# %%
import draw_eight  # Load the library
fig = draw_eight.make_figure()

# %% [markdown]
# We will cover how to import and use functionality from libraries, how to install third-party libraries
# and how to write your own libraries that can be shared and used by other in this course.
#
# ### Python scripts
#
# While Jupyter notebooks are a great medium for learning how to use Python and for exploratory work,
# there are some drawbacks:
#
#   * The require Jupyter Lab (or a similar application) to be installed to run the notebook.
#   * It can be difficult to run notebooks non-interactively, for example when scheduling a job on a cluster [such as those offered by UCL Research Computing](https://www.rc.ucl.ac.uk/docs/Background/Cluster_Computing).
#   * The flexibility of being able to run the code in cells in any order can also make it difficult to reason how outputs were produced and can lead to non-reproducible analyses.
#   
# In some settings it can therefore be preferrable to write Python _scripts_ - that is files (typically with
# a `.py` extension) which contain Python code which completely describes a computational task to perform
# and that can be run by  passing the name of the script file to the `python` program in a command-line
# environment. Optionally scripts may also allow passing in arguments from the command-line to control
# the execution of the script. As scripts are generally run from text-based terminals, non-text outputs such
# as images will generally be saved to files on disk.
#
# Python scripts are well suited to for example for describing computationally demanding simulations or analyses
# to run as long jobs on a remote server or cluster, or tasks where the input and output is mainly at the file level
# - for instance batch processing a series of data files.