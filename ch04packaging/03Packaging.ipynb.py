# ---
# jupyter:
#   jekyll:
#     display_name: Packaging
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Packaging

# %% [markdown]
#
# Once we've made a working program, we'd like to be able to share it with others.
#
# A good cross-platform build tool is the most important thing: you can always
# have collaborators build from source.
#

# %% [markdown]
# ### Distribution tools

# %% [markdown]
# Distribution tools allow one to obtain a working copy of someone else's package.
#
# - Language-specific tools: 
#  - python: PyPI,
#  - ruby: Ruby Gems, 
#  - perl: CPAN,
#  - R: CRAN
#  
# - Platform specific packagers e.g.:
#  - [`brew`](https://brew.sh/) for MacOS, 
#  - `apt`/`dnf`/`pacman` for Linux or 
#  - [`choco`](https://chocolatey.org/) for Windows.

# %% [markdown]
# ### Laying out a project

# %% [markdown]
#
# When planning to package a project for distribution, defining a suitable
# project layout is essential. A typical layout might look like this:
#
# ```
# repository_name
# |-- module_name
# |   |-- __init__.py
# |   |-- python_file.py
# |   |-- another_python_file.py
# |   `-- test
# |       |-- fixtures
# |       |   `-- fixture_file.yaml
# |       |-- __init__.py
# |       `-- test_python_file.py
# |-- LICENSE.md
# |-- CITATION.md
# |-- README.md
# `-- setup.py
# ```
#
#
#
#

# %% [markdown]
# To achieve this for our `greetings.py` file from the previous session, we can use the commands shown below. We can start by making our directory structure. You can create many nested directories at once using the `-p` switch on `mkdir`.

# %% language="bash"
# mkdir -p greetings_repo/greetings/test/fixtures

# %% [markdown]
# For this notebook, since we are going to be modifying the files bit by bit, we are going to use the [autoreload ipython magic](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) so that we don't need to restart the kernel.

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown]
# ### Using pyproject.toml

# %% [markdown]
# Since June 2020, python's recommendation for creating a package is to specify package information in a `pyproject.toml` file.
# Older projects used a `setup.py` file instead - and in fact the new `pyproject.toml` file in many ways mirrors this old format.
# A lot of projects and packages have not yet switched over from `setup.py` to `pyproject.toml`, so don't be surprised to see a mixture of the two formats when you're looking at other people's packages.

# %% [markdown]
# For our `greetings` package, right now we are adding only the name of the package and its version number.
# This information is included in the `project` section of our `pyproject.toml` file.
#
# But we also need to tell users how to build the package from these specifications.
# This information is specified in the `build-system` section of our `toml` file.
# In this case, we'll be using `setuptools` to build our package, so we list it in the `requires` field.
# We also need `setuptools_scm[toml]` so that `setuptools` can understand the settings we give it in our `.toml` file, and `wheel` to make the package distribution.
#
# Finally, we can set specific options for `setuptools` using additional sections in `pyproject.toml`: in this case, we will tell `setuptools` that it needs to find **and include** all of the files in our `greetings` folder.

# %%
# %%writefile greetings_repo/pyproject.toml

[project]
name = "Greetings"
version = "0.1.0"

[build-system]
requires = ["setuptools", "setuptools_scm[toml]>=6.2", "wheel"]

[tool.setuptools.packages.find]
include = ["greetings*"]

[tool.setuptools_scm]


# %% [markdown]
# We can now install this "package" with pip:

# %% language="bash"
# cd greetings_repo
# pip install .

# %% [markdown]
#
# And the package will be then available to use everywhere on the system. But so far this package doesn't contain anything and there's nothing we can run! We need to add some files first.
#

# %% [markdown]
#
# To create a regular package, we needed to have `__init__.py` files on each subdirectory that we want to be able to import. This is, since version 3.3 and the introduction of [Implicit Namespaces Packages](https://www.python.org/dev/peps/pep-0420/), not needed anymore. However, if you want to use relative imports and `pytest`, then you [still need to have these files](https://github.com/pytest-dev/pytest/issues/1927).
#
# The `__init__.py` files can contain any initialisation code you want to run when the (sub)module is imported.
#
# For this example, and because we are using relative imports in the tests, we are creating the needed `__init__.py` files.

# %% language="bash"
#
# touch greetings_repo/greetings/__init__.py

# %% [markdown]
# And we can copy the `greet` function from the [previous section](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch04packaging/02Argparse.html) in the `greeter.py` file.

# %%
# %%writefile greetings_repo/greetings/greeter.py

def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting



# %% [markdown]
# For the changes to take effect, we need to reinstall the library: 

# %% language="bash"
# cd greetings_repo
# pip install .

# %% [markdown]
# And now we are able to import it and use it:

# %%
from greetings.greeter import greet
greet("Terry","Gilliam")


# %% [markdown]
# ### Convert the script to a module

# %% [markdown]
#
# Of course, there's more to do when taking code from a quick script and turning it into a proper module:

# %% [markdown]
# We need to add docstrings to our functions, so people can know how to use them.

# %%
# %%writefile greetings_repo/greetings/greeter.py

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

    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting


# %% [markdown]
# We can see the documentation using `help`.

# %%
help(greet)

# %% [markdown]
# The documentation string explains how to use the function; don't worry about this for now, we'll consider
# this on [the next section](./04documentation.html) ([notebook version](./04documentation.ipynb)).

# %% [markdown]
# ### Write an executable script

# %% [markdown]
#
#
#
#
#
#

# %% [markdown]
# We can create an executable script, `command.py` that uses our greeting functionality and the `process` function we created in the previous section.
#
# Note how we are importing `greet` using [relative imports](https://www.python.org/dev/peps/pep-0328/), where `.greeter` means to look for a `greeter` module within the same directory.

# %%
# %%writefile greetings_repo/greetings/command.py

from argparse import ArgumentParser

from .greeter import greet


def process():
    parser = ArgumentParser(description="Generate appropriate greetings")

    parser.add_argument('--title', '-t')
    parser.add_argument('--polite', '-p', action="store_true")
    parser.add_argument('personal')
    parser.add_argument('family')

    arguments = parser.parse_args()

    print(greet(arguments.personal, arguments.family,
                arguments.title, arguments.polite))


if __name__ == "__main__":
    process()

# %% [markdown]
# #### Specify entry point

# %% [markdown]
# This allows us to create a command to execute part of our library. In this case when we execute `greet` on the terminal, we will be calling the `process` function under `greetings/command.py`.
#
# We can encode this into our package information by specifying the `project.scripts` field in our `pyproject.toml` file.

# %%
# %%writefile greetings_repo/pyproject.toml

[project]
name = "Greetings"
version = "0.1.0"

[project.scripts]
greet = "greetings.command:process"

[build-system]
requires = ["setuptools", "setuptools_scm[toml]>=6.2", "wheel"]

[tool.setuptools.packages.find]
include = ["greetings*"]

[tool.setuptools_scm]

# %% language="bash"
# cd greetings_repo
# pip install -e .

# %% [markdown]
#
# And the scripts are now available as command line commands, so the following commands can now be run:
#
#
#

# %% language="bash"
# greet --help

# %% language="bash"
# greet Terry Gilliam
# greet --polite Terry Gilliam
# greet Terry Gilliam --title Cartoonist

# %% [markdown]
# ### Specify dependencies

# %% [markdown]
# Let's give some life to our output using ascii art

# %%
# %%writefile greetings_repo/greetings/command.py

from argparse import ArgumentParser

from art import art

from .greeter import greet


def process():
    parser = ArgumentParser(description="Generate appropriate greetings")

    parser.add_argument('--title', '-t')
    parser.add_argument('--polite', '-p', action="store_true")
    parser.add_argument('personal')
    parser.add_argument('family')

    arguments = parser.parse_args()

    message = greet(arguments.personal, arguments.family,
                    arguments.title, arguments.polite)
    print(art("cute face"), message)

if __name__ == "__main__":
    process()

# %% [markdown]
# We use the `dependencies` field of the `project` section in our `pyproject.toml` file to specify the packages we depend on.
# We provide the names of the packages as a list of strings.

# %%
# %%writefile greetings_repo/pyproject.toml

[project]
name = "Greetings"
version = "0.1.0"
dependencies = [
    "art",
]

[project.scripts]
greet = "greetings.command:process"

[build-system]
requires = ["setuptools", "setuptools_scm[toml]>=6.2", "wheel"]

[tool.setuptools.packages.find]
include = ["greetings*"]

[tool.setuptools_scm]

# %% [markdown]
# When installing the package now, pip will also install the dependencies automatically.

# %% language="bash"
# cd greetings_repo
# pip install -e .

# %% language="bash"
# greet Terry Gilliam

# %% [markdown]
# ### Installing from GitHub

# %% [markdown]
#
# We could now submit "greeter" to PyPI for approval, so everyone could `pip install` it.
#
# However, when using git, we don't even need to do that: we can install directly from any git URL:
#

# %% [markdown]
# ```bash
# pip install git+git://github.com/UCL-ARC-RSEing-with-Python/greeter
# ```

# %% [markdown]
# ```bash
# $ greet Lancelot the-Brave --title Sir
# Hey, Sir Lancelot the-Brave.
# ```

# %% [markdown]
# <hr>
# There are a few additional text files that are important to add to a package: a readme file, a licence file and a citation file.

# %% [markdown]
#
#

# %% [markdown]
# ### Write a readme file

# %% [markdown]
# The readme file might look like this:

# %%
# %%writefile greetings_repo/README.md

# Greetings!

This is a very simple example package used as part of the UCL
[Research Software Engineering with Python](development.rc.ucl.ac.uk/training/engineering) course.

## Installation

```bash
pip install git+git://github.com/UCL-ARC-RSEing-with-Python/greeter
```

## Usage
    
Invoke the tool with `greet <FirstName> <Secondname>` or use it on your own library:

```python
from greeting import greeter

greeter.greet(user.name, user.lastname)
```

# %% [markdown]
# ### Write a license file

# %% [markdown]
# We will discus more about [licensing in a later section](https://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch04packaging/07Licensing.html). For now let's assume we want to release this package into the public domain:

# %%
# %%writefile greetings_repo/LICENSE.md

(C) University College London 2014

This "greetings" example package is granted into the public domain.

# %% [markdown]
# ### Write a citation file

# %% [markdown]
# A citation file will inform our users how we would like to be cited when refering to our software:

# %%
# %%writefile greetings_repo/CITATION.md

If you wish to refer to this course, please cite the URL
http://github-pages.ucl.ac.uk/rsd-engineeringcourse/

Portions of the material are taken from [Software Carpentry](http://software-carpentry.org/)

# %% [markdown]
# You may well want to formalise this using the [codemeta.json](https://codemeta.github.io/) standard or the [citation file format](http://citation-file-format.github.io/) - these don't have wide adoption yet, but we recommend it.

# %% [markdown]
# ### Define packages and executables

# %% [markdown]
# We need to create `__init__` files for the source and the tests.
# ```bash
# touch greetings/greetings/test/__init__.py
# touch greetings/greetings/__init__.py
# ```

# %% [markdown]
# ### Write some unit tests

# %% [markdown]
# We can now write some tests to our library. 
#
# Remember, that we need to create the empty `__init__.py` files so that `pytest` can follow the relative imports.

# %% language="bash"
# touch greetings_repo/greetings/test/__init__.py

# %% [markdown]
#
# Separating the script from the logical module made this possible.
#
#
#
#
#
#

# %%
# %%writefile greetings_repo/greetings/test/test_greeter.py

import os

import yaml

from ..greeter import greet

def test_greet():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures',
                           'samples.yaml')) as fixtures_file:
        fixtures = yaml.safe_load(fixtures_file)
        for fixture in fixtures:
            answer = fixture.pop('answer')
            assert greet(**fixture) == answer


# %% [markdown]
#
#
#
# Add a fixtures file:
#
#
#
#
#
#

# %%
# %%writefile greetings_repo/greetings/test/fixtures/samples.yaml

- personal: Eric
  family: Idle
  answer: "Hey, Eric Idle."
- personal: Graham
  family: Chapman
  polite: True
  answer: "How do you do, Graahm Chapman."
- personal: Michael
  family: Palin
  title: CBE
  answer: "Hey, CBE Mike Palin."  

# %% [markdown]
# We can now run `pytest`

# %% magic_args="--no-raise-error" language="bash"
#
# cd greetings_repo
# pytest

# %% [markdown]
# However, this hasn't told us that also the third test is wrong too! A better aproach is to parametrize the testfile `greetings_repo/greetings/test/test_greeter.py` as follows:

# %%
# %%writefile greetings_repo/greetings/test/test_greeter.py

import os

import pytest
import yaml

from ..greeter import greet

def read_fixture():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures',
                           'samples.yaml')) as fixtures_file:
        fixtures = yaml.safe_load(fixtures_file)
    return fixtures

@pytest.mark.parametrize("fixture", read_fixture())
def test_greeter(fixture):
    answer = fixture.pop('answer')
    assert greet(**fixture) == answer


# %% [markdown]
# Now when we run `pytest`, we get a failure per element in our fixture and we know all that fails.

# %% magic_args="--no-raise-error" language="bash"
#
# cd greetings_repo
# pytest

# %% [markdown]
# We can also make pytest to check whether the docstrings are correct by adding the `--doctest-modules` flag. We run `pytest --doctest-modules` and obtain the following output:

# %% magic_args="--no-raise-error" language="bash"
#
# cd greetings_repo
# pytest --doctest-modules

# %% [markdown]
# Finally, we typically don't want to include the tests when we distribute our software for our users.
# We can make sure they are not included using the `exclude` option on when telling `setuptools` to find packages.
#
# Additionally, we can make sure that our README and LICENSE are included in our package metadata by declaring them in the `readme` and `license` fields under the `project` section.
# If you're using a particularly common or standard license, you can even provide the name of the license, rather than the file, and your package builder will take care of the rest!

# %%
# %%writefile greetings_repo/pyproject.toml

[project]
name = "Greetings"
version = "0.1.0"
readme = "README.md"
license = { file = "LICENSE.md" }
dependencies = [
    "art",
    "pyyaml",
]

[project.scripts]
greet = "greetings.command:process"

[build-system]
requires = ["setuptools", "setuptools_scm[toml]>=6.2", "wheel"]

[tool.setuptools.packages.find]
include = ["greetings*"]
exclude = ["tests*"]

[tool.setuptools_scm]

# %% [markdown]
# ### Developer Install

# %% [markdown]
#
# If you modify your source files, you would now find it appeared as if the program doesn't change.
#
# That's because pip install **copies** the files.
#
# If you want to install a package, but keep working on it, you can do:

# %% [markdown]
# ```bash
# pip install --editable .
# ```
#
# or, its shorter version:
#
# ```bash
# pip install -e .
# ```

# %% [markdown]
# ### Distributing compiled code

# %% [markdown]
#
# If you're working in C++ or Fortran, there is no language specific repository.
# You'll need to write platform installers for as many platforms as you want to
# support.
#
# Typically:
#
# * `dpkg` for `apt-get` on Ubuntu and Debian
# * `rpm` for `yum`/`dnf` on Redhat and Fedora
# * `homebrew` on OSX (Possibly `macports` as well)
# * An executable `msi` installer for Windows.
#

# %% [markdown]
# #### Homebrew

# %% [markdown]
#
# Homebrew: A ruby DSL, you host off your own webpage
#
# See an [installer for the cppcourse example](http://github.com/jamespjh/homebrew-reactor)
#
# If you're on OSX, do:
#

# %% [markdown]
# ```
# brew tap jamespjh/homebrew-reactor
# brew install reactor
# ```
