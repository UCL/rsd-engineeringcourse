# ---
# jupyter:
#   jekyll:
#     display_name: Modules
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Using Libraries

# %% [markdown]
# ## Import

# %% [markdown]
# To use a function or type from a python library, rather than a **built-in** function or type, we have to import the library.

# %%
math.sin(1.6)

# %%
import math

# %%
math.sin(1.6)

# %% [markdown]
# We call these libraries **modules**:

# %%
type(math)

# %% [markdown]
# The tools supplied by a module are *attributes* of the module, and as such, are accessed with a dot.

# %%
dir(math)

# %% [markdown]
# They include properties as well as functions:

# %%
math.pi

# %% [markdown]
# You can find out where on your storage medium a library has been imported from:

# %%
print(math.__file__)

# %% [markdown]
# Some modules do not use the `__file__` attribute so you may get an error:
#
# ``` python
# AttributeError: module 'modulename' has no attribute '__file__'
# ```
#
# If this is the case `print(modulename)` should display a description of the module object which will include an indication if the module is a 'built-in' module written in C (in which case the file path will not be specified) or the file path to the module otherwise.

# %%
print(math)

# %% [markdown]
# Note that `import` does *not* install libraries from PyPI. It just makes them available to your current notebook session, assuming they are already installed. Installing libraries is harder, and we'll cover it later.
# So what libraries are available? Until you install more, you might have just the modules that come with Python, the *standard library*.

# %% [markdown]
# **Supplementary Materials**: Review the [list of standard library modules](https://docs.python.org/library/).

# %% [markdown]
# If you installed via Anaconda, then you also have access to a bunch of modules that are commonly used in research.
#
# **Supplementary Materials**: Review the [list of modules that are packaged with Anaconda by default on different architectures](http://docs.continuum.io/anaconda/pkg-docs.html) (choose your operating system and see which packages have a tick mark).
#
# We'll see later how to add more libraries to our setup.

# %% [markdown]
# ## Why bother?

# %% [markdown]
# Why bother with modules? Why not just have everything available all the time?
#
# The answer is that there are only so many names available! Without a module system, every time I made a variable whose name matched a function in a library, I'd lose access to it. In the olden days, people ended up having to make really long variable names, thinking their names would be unique, and they still ended up with "name clashes". The module mechanism avoids this.

# %% [markdown]
# ## Importing from modules

# %% [markdown]
# Still, it can be annoying to have to write `math.sin(math.pi)` instead of `sin(pi)`.
# Things can be imported *from* modules to become part of the current module:

# %%
import math

print(math.sin(math.pi))

# %%
from math import sin

print(sin(math.pi))

# %% [markdown]
# Importing one-by-one like this is a nice compromise between typing and risk of name clashes.

# %% [markdown]
# It *is* possible to import **everything** from a module, but you risk name clashes.

# %%
pi = "pie"


def sin(x):
    print(f"eat {x}")

print(sin(pie))
    
from math import *

print(sin(pi))

# %% [markdown]
# ## Import and rename

# %% [markdown]
# You can rename things as you import them to avoid clashes or for typing convenience

# %%
import math as m

print(m.cos(0))

# %%
pi = 3
from math import pi as realpi

print(sin(pi), sin(realpi))
