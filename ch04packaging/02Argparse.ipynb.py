# ---
# jupyter:
#   jekyll:
#     display_name: Argparse
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Argparse

# %% [markdown]
# This is the standard library for building programs with a command-line interface. Here we show a short introduction to it, but we recommend to read the [official tutorial](https://docs.python.org/3/howto/argparse.html).

# %% [markdown]
# Let's start by creating a simple `greet` function that accepts some parameters.

# %%
def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting


# %% [markdown]
# Now we have a function that greets whoever we want.

# %%
greet("John", "Cleese", polite=True)

# %% [markdown]
# If we want to create a command line interface for this function, we need to save it on its own file. To add the capability to accept inputs from the command line we are going to use `argparse`.
#
# Rememer, what's under the `if __name__ == "__main__":` block is what's get executed when you run the file!

# %%
# %%writefile greeter.py
# #!/usr/bin/env python
from argparse import ArgumentParser

def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate appropriate greetings")
    parser.add_argument('--title', '-t')
    parser.add_argument('--polite','-p', action="store_true")
    parser.add_argument('personal')
    parser.add_argument('family')
    arguments= parser.parse_args()
    
    message = greet(arguments.personal, arguments.family,
                    arguments.title, arguments.polite)
    print(message)

# %% [markdown]
# Note that we've created arguments for each argument `greet` accepts and kept what's optional in the function (the keyword arguments) to be also optional for its command-line interface (can you spot how?).

# %% [markdown]
# We need to tell the computer that this file can be executed to be able to run this script without calling it with `python` everytime. The computer will know what to use by reading the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) `#!`. If you are using MacOS or Linux, you do the following to create an executable:

# %% language="bash"
# chmod u+x greeter.py

# %% [markdown]
# and then running it as:

# %% magic_args="--no-raise-error" language="bash"
# ./greeter.py

# %% [markdown]
# if you are using Windows' commands or powershell terminal (instead of git-bash), then the shebang is ignored and you will have to call `python` explicitily. Additionally, for the notebooks cells, you need to change `bash` by `cmd`.
#
# ```
# %%cmd
# python greeter.py John Cleese
# ```

# %% language="bash"
# ./greeter.py John Cleese

# %% [markdown]
# We can then use the optional arguments as:

# %% language="bash"
# ./greeter.py --polite John Cleese

# %% language="bash"
# ./greeter.py John Cleese --title Dr

# %% [markdown]
# Yes, [he is](https://en.wikipedia.org/wiki/John_Cleese#Honours_and_tributes)!

# %% [markdown]
# From the error we got above when we called `greeter.py` without arguments, you may have noticed that in the usage message there's also a `-h` optional argument. We know it's optional because it's shown within square brackes, like for `[--polite]`. This new argument, as the usage message seen above, is generated automatically by argparse and you can use it to see the help.

# %% language="bash"
# ./greeter.py --help

# %% [markdown]
# Before we move into the next section, let's clean up our `if __name__ == "__main__":` block by creating a function that keeps the `argparse` magic. We will call that function `process`.

# %%
# %%writefile greeter.py
# #!/usr/bin/env python
from argparse import ArgumentParser

def greet(personal, family, title="", polite=False):
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting

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
