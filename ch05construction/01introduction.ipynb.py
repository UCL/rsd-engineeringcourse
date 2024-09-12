# ---
# jupyter:
#   jekyll:
#     display_name: Construction
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Construction

# %% [markdown]
#
# Software *design* gets a lot of press (Object orientation, UML, design patterns).
#
# In this session we're going to look at advice on software *construction*.
#

# %% [markdown]
# ## Construction vs Design

# %% [markdown]
#
# For a given piece of code, there exist several different ways one could write it:
#
# * Choice of variable names
# * Choice of comments
# * Choice of layout
#
# The consideration of these questions is the area of Software Construction.
#

# %% [markdown]
# ## Low-level design decisions

# %% [markdown]
#
# We will also look at some of the lower-level software design decisions in the context of this section:
#
# * Division of code into subroutines
# * Subroutine access signatures
# * Choice of data structures for readability
#

# %% [markdown]
# ## Algorithms and structures

# %% [markdown]
#
# We will not, in discussing construction, be looking at decisions as to how design questions impact performance:
#
# * Choice of algorithms
# * Choice of data structures for performance
# * Choice of memory layout
#
# We will consider these in a future discussion of performance programming.
#

# %% [markdown]
# ## Architectural design

# %% [markdown]
#
# We will not, in this session, be looking at the large-scale questions of how program components interact,
# the stategic choices that govern how software behaves at the large scale:
#
# * Where do objects get made?
# * Which objects own or access other objects?
# * How can I hide complexity in one part of the code from other parts of the code?
#
# We will consider these in a future session.
#

# %% [markdown]
# ## Construction

# %% [markdown]
#
# So, we've excluded most of the exciting topics. What's left is the bricks and mortar of software:
# how letters and symbols are used to build code which is readable.
#

# %% [markdown]
# ## Literate programming

# %% [markdown]
#
# In literature, books are enjoyable for different reasons:
#
# * The beauty of stories
# * The beauty of plots
# * The beauty of characters
# * The beauty of paragraphs
# * The beauty of sentences
# * The beauty of words
#
# Software has beauty at these levels too: stories and characters correspond to architecture and object design,
# plots corresponds to algorithms, but the rhythm of sentences and the choice of words corresponds
# to software construction.
#

# %% [markdown]
# ## Programming for humans

# %% [markdown]
#
# * Remember you're programming for humans as well as computers
# * A program is the best, most rigorous way to describe an algorithm
# * Code should be pleasant to read, a form of scholarly communication
#
# Read Steve McConnell's [Code Complete](https://en.wikipedia.org/wiki/Code_Complete) [[UCL library](https://ucl-new-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=UCL_LMS_DS21156385750004761&context=L)].
#
#
#
#
#

# %% [markdown]
# ## Setup

# %% [markdown]
# This notebook is based on a number of fragments of code, with an implicit context.
# We've made a library to set up the context so the examples work.

# %%
# %%writefile context.py
from unittest.mock import Mock, MagicMock
class CompMock(Mock):
    def __sub__(self, b):
        return CompMock()
    def __lt__(self,b):
        return True
    def __abs__(self):
        return CompMock()
array=[]
agt=[]
ws=[]
agents=[]
counter=0
x=MagicMock()
y=None
agent=MagicMock()
value=0
bird_types=["Starling", "Hawk"]
import numpy as np
average=np.mean
hawk=CompMock()
starling=CompMock()
sEntry="2.0"
entry ="2.0"
iOffset=1
offset =1
anothervariable=1
flag1=True
variable=1
flag2=False
def do_something(): pass
chromosome=None
start_codon=None
subsequence=MagicMock()
transcribe=MagicMock()
ribe=MagicMock()
find=MagicMock()
can_see=MagicMock()
my_name=""
your_name=""
flag1=False
flag2=False
start=0.0
end=1.0
step=0.1
birds=[MagicMock()]*2
resolution=100
pi=3.141
result= [0]*resolution
import numpy as np
import math
data= [math.sin(y) for y in np.arange(0,pi,pi/resolution)]
import yaml
import os
