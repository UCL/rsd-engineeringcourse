# ---
# jupyter:
#   jekyll:
#     display_name: Documentation
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Documentation

# %% [markdown]
# ## Documentation is hard

# %% [markdown]
#
# * Good documentation is hard, and very expensive.
# * Bad documentation is detrimental.
# * Good documentation quickly becomes bad if not kept up-to-date with code changes.
# * Professional companies pay large teams of documentation writers.
#

# %% [markdown]
# ## Prefer readable code with tests and vignettes

# %% [markdown]
#
# If you don't have the capacity to maintain great documentation,
# focus on:
#
# * Readable code
# * Automated tests
# * Small code samples demonstrating how to use the api
#

# %% [markdown]
# ## Comment-based Documentation tools

# %% [markdown]
#
# Documentation tools can produce extensive documentation about your code by pulling out comments near the beginning of functions,
# together with the signature, into a web page.
#
# The most popular is [Doxygen](http://www.doxygen.nl/).
#
# Here are some other documentation tools used in different languages, have a look at the generated and source examples:
#
#
# | Language | Name                                                                                | Output example                                                                      | source                                                                                                                                           |
# | ---      | ---                                                                                 | ---                                                                                 | ---                                                                                                                                              |
# | Multiple | [Doxygen](http://www.doxygen.nl/)                                                   | [`Array` docs](https://eigen.tuxfamily.org/dox/classEigen_1_1Array.html)            | [`Array` docstring source](https://gitlab.com/libeigen/eigen/-/blob/55e3ae02ac1f13fbcc7a83f5e37a39fd2b142db1/Eigen/src/Core/Array.h#L26-L45)     |
# | Python   | [Sphinx](http://sphinx-doc.org/)                                                    | [`numpy.ones` docs](https://numpy.org/doc/1.21/reference/generated/numpy.ones.html) | [`numpy.ones` docstring source](https://github.com/numpy/numpy/blob/v1.21.0/numpy/core/numeric.py#L149-L206)                                     |
# | R        | [pkgdown](https://pkgdown.r-lib.org/) |  [`stringr`'s `str_unique`](https://stringr.tidyverse.org/reference/str_unique.html)                                                  | [`stringr`'s `str_unique` docstring source](https://github.com/tidyverse/stringr/blob/main/R/unique.R)                                                    |
# | Julia    | [Documnenter.jl](https://juliadocs.github.io/Documenter.jl/stable/)                 | [`ones` docs](https://docs.julialang.org/en/v1/base/arrays/#Base.ones)              | [`ones` docstring source](https://github.com/JuliaLang/julia/blob/ae8452a9e0b973991c30f27beb2201db1b0ea0d3/base/array.jl#L475-L493)              |
# | Fortan   | [FORD](https://github.com/Fortran-FOSS-Programmers/ford)                            | [`arange` docs](https://stdlib.fortran-lang.org/interface/arange.html)              | [`arange` docstring source](https://github.com/fortran-lang/stdlib/blob/d14fca8e7cc36ed5f6f84d2bf576c91c2e54eb07/src/stdlib_math.fypp#L276-L290) |
# | Rust     | [rustdoc](https://doc.rust-lang.org/rustdoc/what-is-rustdoc.html)                   | [`Matrix` docs](https://docs.rs/nalgebra/0.18.0/nalgebra/base/struct.Matrix.html)   | [`Matrix` docstring source](https://github.com/dimforge/nalgebra/blob/8ea8ac70d5ad4bae865e6246a48455bf0b3fa3d2/src/base/matrix.rs#L59-L157)      |
#
# [Breathe](https://breathe.readthedocs.io/en/latest/) can be used to make Sphinx and Doxygen work together (good to keep documentation, for example, of a C++ project that includes Python bindings). [roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) is another good option for R packages.
#
#
#

# %% [markdown]
# ## Example of using Sphinx

# %% [markdown]
# ## Write some docstrings

# %% [markdown]
# We're going to document our "greeter" example from the previous section using docstrings with Sphinx.
#
# There are various conventions for how to write docstrings, but the native Sphinx one doesn't look nice when used with
# the built in `help` system.
#
# In writing Greeter, we used the [docstring conventions from NumPy](https://numpy.org/doc/stable/docs/howto_document.html).
# So we use the [`numpydoc`](https://numpydoc.readthedocs.io/en/latest/) sphinx extension to
# support these (**NOTE:** you will need to install this extension for the later examples to work).

# %% [markdown]
# ```python
# """ 
# Generate a greeting string for a person.
#
# Parameters
# ----------
# personal: str
#     A given name, such as Will or Jean-Luc
#
# family: str
#     A family name, such as Riker or Picard
#
# title: str
#     An optional title, such as Captain or Reverend
#
# polite: bool
#     True for a formal greeting, False for informal.
#
# Returns
# -------
# string
#     An appropriate greeting
# """
# ```

# %% [markdown]
# ## Set up Sphinx

# %% [markdown]
# Install Sphinx using the [appropiate instructions](https://www.sphinx-doc.org/en/master/usage/installation.html) for your system following the documentation online.
# (Note that your output and the linked documentation may differ slightly depending on when you installed Sphinx and what version you're using.)

# %% [markdown]
#
# Invoke the [sphinx-quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html) command to build Sphinx's
# configuration file automatically based on questions
# at the command line:

# %% [markdown]
# ``` bash
# sphinx-quickstart
# ```

# %% [markdown]
# Which responds:

# %% [markdown]
# ```
# Welcome to the Sphinx 4.2.0 quickstart utility.
#
# Please enter values for the following settings (just press Enter to
# accept a default value, if one is given in brackets).
#
# Selected root path: .
#
# You have two options for placing the build directory for Sphinx output.
# Either, you use a directory "_build" within the root path, or you separate
# "source" and "build" directories within the root path.
# > Separate source and build directories (y/n) [n]:
#
# The project name will occur in several places in the built documentation.
# > Project name: Greetings
# > Author name(s): James Hetherington
# > Project release []: 0.1
#
# If the documents are to be written in a language other than English,
# you can select a language here by its language code. Sphinx will then
# translate text that it generates into that language.
#
# For a list of supported codes, see
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
# > Project language [en]:
#
# Creating file ./conf.py.
# Creating file ./index.rst.
# Creating file ./Makefile.
# Creating file ./make.bat.
#
# Finished: An initial directory structure has been created.
#
# You should now populate your master file /tmp/index.rst and create other documentation
# source files. Use the Makefile to build the docs, like so:
#    make builder
# where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
# ```

# %% [markdown]
# and then look at and adapt the generated config - a file called
# `conf.py` in the root of the project - with, for example, the extensions we want to use.
# This config file contains the project's Sphinx configuration, as Python variables:

# %% [markdown]
# ``` python
# #Add any Sphinx extension module names here, as strings. They can be
# #extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = [
#     'sphinx.ext.autodoc',  # Support automatic documentation
#     'sphinx.ext.coverage', # Automatically check if functions are documented
#     'sphinx.ext.mathjax',  # Allow support for algebra
#     'sphinx.ext.viewcode', # Include the source code in documentation
#     'numpydoc'             # Support NumPy style docstrings
# ]
# ```

# %% [markdown]
# To proceed with the example, we'll copy a finished conf.py into our folder, though normally you'll always use `sphinx-quickstart`
#

# %% jupyter={"outputs_hidden": false}
# %%writefile greetings/conf.py

import sys
import os

# We need to tell Sphinx where to look for modules
sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinx.ext.autodoc',  # Support automatic documentation
    'sphinx.ext.coverage', # Automatically check if functions are documented
    'sphinx.ext.mathjax',  # Allow support for algebra
    'sphinx.ext.viewcode', # Include the source code in documentation
    'numpydoc'             # Support NumPy style docstrings
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Greetings'
copyright = '2014, James Hetherington'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
pygments_style = 'sphinx'
htmlhelp_basename = 'Greetingsdoc'
latex_elements = {
}

latex_documents = [
  ('index', 'Greetings.tex', 'Greetings Documentation',
   'James Hetherington', 'manual'),
]

man_pages = [
    ('index', 'greetings', 'Greetings Documentation',
     ['James Hetherington'], 1)
]

texinfo_documents = [
  ('index', 'Greetings', u'Greetings Documentation',
   'James Hetherington', 'Greetings', 'One line description of project.',
   'Miscellaneous'),
]

# %% [markdown]
# ## Define the root documentation page

# %% [markdown]
#
# Sphinx uses [RestructuredText](https://docutils.sourceforge.io/rst.html) another wiki markup format similar to Markdown.
#
# You define an "index.rst" file to contain any preamble text you want. The rest is autogenerated by `sphinx-quickstart`
#
#
#
#
#
#

# %% jupyter={"outputs_hidden": false}
# %%writefile greetings/index.rst
Welcome to Greetings's documentation!
=====================================

Simple "Hello, James" module developed to teach research software engineering.

.. autofunction:: greetings.greeter.greet


# %% [markdown]
# ##  Run sphinx

# %% [markdown]
#
# We can run Sphinx using:
#

# %% jupyter={"outputs_hidden": false} language="bash"
# cd greetings/
# sphinx-build . doc

# %% [markdown]
# ## Sphinx output

# %% [markdown]
# Sphinx's output is [html](./greetings/doc/index.html). We just created a simple single function's documentation, but Sphinx will create
# multiple nested pages of documentation automatically for many functions.
#
#
#
#

# %% [markdown]
# ## Doctest - testing your documentation is up to date

# %% [markdown]
# `doctest` is a module included in the standard library. It runs all the code within the docstrings and checks whether the output is what it's claimed on the documentation.
#
# Let's add an example to our greeting function and check it with `doctest`. We are leaving the output with a small typo (missing the closing quote `'`) to see what's the type of output we get from `doctest`.

# %%
# %%writefile greetings/greetings/greeter.py
def greet(personal, family, title="", polite=False):
    """ Generate a greeting string for a person.

    Parameters
    ----------
    personal: str
        A given name, such as Will or Jean-Luc
    family: str
        A family name, such as Riker or Picard
    title: str
        An optional title, such as Captain or Reverend
    polite: bool
        True for a formal greeting, False for informal.

    Returns
    -------
    string
        An appropriate greeting
        
    Examples
    --------
    >>> from greetings.greeter import greet
    >>> greet("Terry", "Jones")
    'Hey, Terry Jones.
    """

    greeting= "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting

# %% magic_args="--no-raise-error" language="bash"
# python -m doctest greetings/greetings/greeter.py

# %% [markdown]
#  

# %% [markdown]
# which clearly identifies a tiny error in our example.

# %% [markdown]
# pytest can run the doctest too if you call it as:
#
# `pytest  --doctest-modules`
