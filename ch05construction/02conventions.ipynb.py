# ---
# jupyter:
#   jekyll:
#     display_name: Coding Conventions
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Coding Conventions
#
# Let's import a few variables from context.py that will be used in the following lesson.

# %%
from context import (
    sEntry,
    iOffset,
    entry,
    offset,
    anothervariable,
    variable,
    flag1,
    flag2,
    do_something,
)

# %% [markdown]
# ## One code, many layouts:
#
# Consider the following fragment of python:
#
#
#

# %%
import species
def AddToReaction(name, reaction):
    reaction.append(species.Species(name))


# %% [markdown]
#
#
#
# this could also have been written:
#
#
#

# %%
from species import Species

def add_to_reaction(a_name,
                    a_reaction):
    l_species = Species(a_name)
    a_reaction.append( l_species )


# %% [markdown]
#
#
#

# %% [markdown]
# ## So many choices

# %% [markdown]
#
# * Layout
# * Naming
# * Syntax choices
#

# %% [markdown]
# ## Layout

# %%
reaction = {
    "reactants": ["H", "H", "O"],
    "products": ["H2O"]
}

# %% [markdown]
#
#
#
#

# %%
reaction2=(
{
  "reactants":
  [
    "H",
    "H",
    "O"
  ],
  "products":
  [
    "H2O"
  ]
}
)


# %% [markdown]
# ## Layout choices

# %% [markdown]
#
# * Brace style
# * Line length
# * Indentation
# * Whitespace/Tabs
#
# Inconsistency will produce a mess in your code! Some choices will make your code harder to read, whereas others may affect the code. For example, if you copy/paste code with tabs in a place that's using spaces, they may appear OK in your screen but it will fail when running it.

# %% [markdown]
# ## Naming Conventions

# %% [markdown]
# [Camel case](https://en.wikipedia.org/wiki/Camel_case) is used in the following example, where class name is in UpperCamel, functions in lowerCamel and underscore_separation for variables names. This convention is used broadly in the python community.

# %%
class ClassName:
    def methodName(variable_name):
        instance_variable = variable_name


# %% [markdown]
# This other example uses underscore_separation for all the names.

# %%
class class_name:
    def method_name(a_variable):
        m_instance_variable = a_variable


# %% [markdown]
# ## Hungarian Notation

# %% [markdown]
#
# Prefix denotes *type*:
#
#
#

# %%
fNumber = float(sEntry) + iOffset

# %% [markdown]
# So in the example above we know that we are creating a `f`loat number as a composition of a `s`tring entry and an `i`nteger offset.
#
# People may find this useful in languages like Python where the type is intrisic in the variable.

# %%
number = float(entry) + offset

# %% [markdown]
# ## Newlines

# %% [markdown]
#
# * Newlines make code easier to read
# * Newlines make less code fit on a screen
#
# Use newlines to describe your code's *rhythm*.
#

# %% [markdown]
# ## Syntax Choices

# %% [markdown]
# The following two snippets do the same, but the second is separated into more steps, making it more readable.

# %%
anothervariable += 1
if ((variable == anothervariable) and flag1 or flag2): do_something()

# %%
anothervariable = anothervariable + 1
variable_equality = (variable == anothervariable)
if ((variable_equality and flag1) or flag2):
    do_something()

# %% [markdown]
# We create extra variables as an intermediate step. Don't worry about the performance now, the compiler will do the right thing.
#
# What about operator precedence? Being explicit helps to remind yourself what you are doing.

# %% [markdown]
# ## Syntax choices

# %% [markdown]
#
# * Explicit operator precedence
# * Compound expressions
# * Package import choices
#

# %% [markdown]
# ## Coding Conventions

# %% [markdown]
#
# You should try to have an agreed policy for your team for these matters.
#
# If your language sponsor has a standard policy, use that. For example:
#
# - **Python**: [PEP8](https://www.python.org/dev/peps/pep-0008/)
# - **R**: [Google's guide for R](https://google.github.io/styleguide/Rguide.xml), [tidyverse style guide](https://style.tidyverse.org/)
# - **C++**: [Google's style guide](https://google.github.io/styleguide/cppguide.html), [Mozilla's](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Coding_Style)
# - **Julia**: [Official style guide](https://docs.julialang.org/en/v1/manual/style-guide/index.html)
#

# %% [markdown]
# ## Lint

# %% [markdown]
#
# There are automated tools which enforce coding conventions and check for common mistakes.
#
# These are called ** formatters** and **linters**. Some widely used linters and formatters in the Python ecosystem ar -
#  - [pycodestyle](https://pypi.org/project/pycodestyle/): check your code against PEP8
#  - [pylint](https://www.pylint.org/): useful information about the quality of your code
#  - [black](https://github.com/psf/black): code formatter written in Python
#  - [ruff](https://github.com/astral-sh/ruff): blazing fast code formatter and linter written in Rust with ideas borrowed from Pythonic linters and formatters


# %% [markdown]
# Most of such tools can be directly used on Python files / repositories using a CLI utility. For instance -


# %% magic_args="--no-raise-error" language="bash"
# pycodestyle species.py

# %% magic_args="--no-raise-error" language="bash"
# pylint species.py

# %% magic_args="--no-raise-error" language="bash"
# ruff check species.py

# %% [markdown]
# These linters can be configured to choose which points to flag and which to ignore.
#
# Do not blindly believe all these automated tools! Style guides are **guides** not **rules**.

# %% [markdown]
#
# It is a good idea to run a linter before every commit, or include it in your CI tests.
#
# [`pre-commit`](https://pre-commit.com) allows developers to add tools like linters and formatters
# as git hooks, such that they run before every commit. The hooks can be installed locally using -
# 
# ```bash
# pip install pre-commit
# pre-commit install  # provided a .pre-commit-config.yaml is present in your repository
# ```
# 
# This would run the checks every time a commit is created locally. The checks will only run on the files
# modified by that commit.


# %% [markdown]
# Finally, there are tools like [editorconfig](https://editorconfig.org/) to help sharing the conventions used within a project, where each contributor uses different IDEs and tools.
# There are also bots like [pep8speaks](https://pep8speaks.com/) and [pre-commit.ci](https://pre-commit.ci) that comments/run checks on contributors' pull requests suggesting what to change to follow the conventions for the project.
#
