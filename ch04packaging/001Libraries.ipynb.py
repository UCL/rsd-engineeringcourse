# ---
# jupyter:
#   jekyll:
#     display_name: Libraries
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Libraries

# %% [markdown]
# ## Libraries are awesome

# %% [markdown]
#
# The strength of a language lies as much in the set of libraries available, as it does
# in the language itself.
#
# A great set of libraries allows for a very powerful programming style:
#
# * Write minimal code yourself
# * Choose the right libraries
# * Plug them together
# * Create impressive results
#
# Not only is this efficient with your programming time, it's also more efficient with computer
# time.
#
# The chances are any algorithm you might want to use has already been programmed better by someone else.

# %% [markdown]
# ## Drawbacks of libraries.

# %% [markdown]
#
# * Sometimes, libraries are not looked after by their creator: code that is not maintained *rots*:
#     * It no longer works with later versions of *upstream* libraries.
#     * It doesn't work on newer platforms or systems.
#     * Features that are needed now, because the field has moved on, are not added
#
# * Sometimes, libraries are hard to get working:
#     * For libraries in pure python, this is almost never a problem
#     * But many libraries involve *compiled components*: these can be hard to install.
#

# %% [markdown]
# ## Contribute, don't duplicate

# %% [markdown]
#
# * You have a duty to the ecosystem of scholarly software:
#     * If there's a tool or algorithm you need, find a project which provides it.
#     * If there are features missing, or problems with it, fix them, [don't create your own](http://xkcd.com/927/) library.
#

# %% [markdown]
# ## How to choose a library

# %% [markdown]
#
# * Is the code on an open version control tool like GitHub?
#     * When was the last commit?
#     * How often are there commits?
# * Can you find the lead contributor on the internet?
# * Do they respond when approached:
#     * emails to developer list
#     * personal emails
#     * tweets
#     * [irc](https://freenode.net)/[gitter](https://gitter.im/)/[slack](https://slack.com/)/[[matrix]](https://element.io/)
#     * issues raised on GitHub
# * Are there contributors other than the lead contributor?
# * Is there discussion of the library on Stack Exchange?
# * Is it on standard package repositories? (PyPI, apt/yum/brew)
# * Are there any tests?
# * Download it. Can you build it? Do the tests pass?
# * Is there an open test dashboard? (Travis/Jenkins/CDash)
# * What dependencies does the library itself have? Do they pass this list?
# * Are different versions of the library clearly labeled with version numbers?
# * Is there a changelog?
#

# %% [markdown]
# ## Sensible Version Numbering

# %% [markdown]
#
# The best approach to version numbers clearly distinguishes kinds of change:
#
# Given a version number MAJOR.MINOR.PATCH, e.g. 2.11.14 increment the:
#
# * MAJOR version when you make incompatible API changes,
# * MINOR version when you add functionality in a backwards-compatible manner, and
# * PATCH version when you make backwards-compatible bug fixes.
#
# This is called [Semantic Versioning](http://semver.org).
#

# %% [markdown]
# ## The Python Standard Library

# %% [markdown]
#
# Python comes with a powerful [standard library](https://docs.python.org/3/library/).
#
# Learning python is as much about learning this library as learning the language itself.
#
# You've already seen a few packages in this library: `math`, `pdb`, `datetime`.
#

# %% [markdown]
# ## The Python Package Index

# %% [markdown]
#
# Python's real power, however, comes with the Python Package Index: [PyPI](https://pypi.org/).
# This is a huge array of libraries, with all kinds of capabilities, all easily installable from the 
# command line or through your Python distribution.
#
