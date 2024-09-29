# ---
# jupyter:
#   jekyll:
#     display_name: Installing Libraries
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Packaging your code

# %% [markdown]
# ## Installing Libraries

# %% [markdown]
# We've seen that there are lots of python libraries. But how do we install them?

# %% [markdown]
# The main problem is this: *libraries need other libraries*

# %% [markdown]
# So you can't just install a library by copying code to the computer: you'll find yourself wandering down a tree
# of "dependencies"; libraries needed by libraries needed by the library you want.

# %% [markdown]
# This is actually a good thing; it means that people are making use of each others'
# code. There's a real problem in scientific programming, of people who think they're really clever writing their own
# twenty-fifth version of the same thing.

# %% [markdown]
# So using other people's libraries is good.

# %% [markdown]
# Why don't we do it more? Because it can often be quite difficult to **install** other peoples' libraries!

# %% [markdown]
# Python has developed a good tool for avoiding this: **pip**.

# %% [markdown]
# ### Installing Geopy using Pip

# %% [markdown]
# On a computer you control, on which you have installed python via Anaconda, you will need to open a **terminal**
# to invoke the library-installer program, `pip`.

# %% [markdown]
# * On windows, go to Start -> Anaconda3 -> Anaconda Prompt
# * On mac, start *Terminal*. 
# * On linux, open a bash shell.

# %% [markdown]
# Into this shell, type:
#     
# `pip install geopy`

# %% [markdown]
# The computer will install the package and its dependencies automatically from PyPI (a repository of packages, which we'll talk about later).

# %% [markdown]
# Now, close the Jupyter notebook if you have it open, and reopen it. Check your new library is installed with:

# %%
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook

# install geopy if it is not already installed
%pip install -q geopy

import geopy
geocoder = geopy.geocoders.Nominatim(user_agent="mphy0021") 

# %%
geocoder.geocode('Cambridge', exactly_one=False)

# %% [markdown]
# That was actually pretty easy, I hope. This is how you'll install new libraries when you need them.

# %% [markdown]
# Troubleshooting:
#     
# On mac or linux, you *might* get a complaint that you need "superuser", "root", or "administrator" access. If so type:
#
# * `pip install --user geopy`
#     
# If you get a complaint like: 'pip is not recognized as an internal or external command', try the following:
#         
# * `conda install pip` (if you are using Anaconda - though it should be already available)
# * or follow the [official instructions](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) otherwise.
#

# %% [markdown]
# ### Installing binary dependencies with Conda

# %% [markdown]
# `pip` is the usual Python tool for installing libraries. But there's one area of library installation that is still awkward:
# some python libraries depend not on other **python** libraries, but on libraries in C++ or Fortran.

# %% [markdown]
# This can cause you to run into difficulties installing some libraries. 
# Fortunately, for lots of these, Continuum, the makers of Anaconda, provide a carefully managed set of scripts for installing
# these awkward non-python libraries too. You can do this with the `conda` command line tool, if you're using Anaconda.

# %% [markdown]
# Simply type
#
# * `conda install <whatever>`
#
# instead of `pip install`. This will fetch the python package not from PyPI, but from Anaconda's distribution for your platform, and manage any non-python dependencies too.

# %% [markdown]
# Typically, if you're using Anaconda, whenever you come across a python package you want, you should check if Anaconda
# package it first using `conda search`. If it is there you can `conda install` it, you'll likely have less problems. But Anaconda doesn't package everything, so you'll need to `pip install` from time to time.
#
# The maintainers of packages may have also provided releases of their software via [conda-forge](https://conda-forge.org/), a community-driven project that provides a collection of packages for the anaconda environment. In such case you can [add conda-forge](https://conda-forge.org/#about) to your anaconda installation and use `search` and `install` as explained above.

# %% [markdown]
# ### Where do these libraries go? 

# %%
geopy.__path__

# %% [markdown]
# Your computer will be configured to keep installed Python packages in a particular place.

# %% [markdown]
# Python knows where to look for possible library installations in a list of places, called the `$PYTHONPATH` (`%PYTHONPATH%` in Windows).
# It will try each of these places in turn, until it finds a matching library name.

# %%
import sys
sys.path

# %% [markdown]
# You can add (`append`) more paths to this list, and so allow libraries to be load from there. Thought this is not a recommended practice, let's do it once to understand how the import works.
#
# 1. Create a new directory (_e.g._, `myexemplar`),
# 1. create a file inside that directory (`exemplar.py`),
# 1. write a function inside such file (`exemplar_works`),
# 1. open python, import `sys` and add the path of `myexemplar` to `sys.path`,
# 1. import your new file, and 
# 1. run the function.

# %% [markdown]
# ### Libraries not in PyPI

# %% [markdown]
# Sometimes you'll need to download the source code
# directly. This won't automatically follow the dependency tree, but for simple standalone libraries, is sometimes necessary.

# %% [markdown]
# To install these on windows, download and unzip the library into a folder of your choice, e.g. `my_python_libs`. 
#
# On windows, a reasonable choice
# is the folder you end up in when you open the Anaconda terminal. You can get a graphical view on this folder by typing: `explorer .`

# %% [markdown]
# Make a new folder for your download and unzip the library there.

# %% [markdown]
# Now, you need to move so you're inside your download in the terminal:

# %% [markdown]
# * `cd my_python_libs`
# * `cd <library name>` (e.g. `cd JSAnimation-master`) 

# %% [markdown]
# Now, manually install the library in your PythonPath:

# %% [markdown]
# * `pip install --user .`

# %% [markdown]
# This is all pretty awkward, but it is worth practising this stuff, as most of the power of using programming for
# research resides in all the libraries that are out there. 

# %% [markdown]
# ### Python virtual environments

# %% [markdown]
# Sometimes you need to have different versions of a package installed, or you would like to install a set of libraries that you don't want to affect the rest of the installation in your system. In such cases you can create environments that are isolated from the rest.
#
# There are multiple solutions to this, only for [python](https://docs.python.org/3.6/library/venv.html) or for [anaconda](https://conda.io/docs/user-guide/tasks/manage-environments.html).
# Find more information on [how to create and use the virtual enviroments](https://realpython.com/python-virtual-environments-a-primer/).
