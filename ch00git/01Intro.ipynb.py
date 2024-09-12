# ---
# jupyter:
#   jekyll:
#     display_name: Introduction to Version Control
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

# %% [markdown]
# ## What's version control?
#
# Version control is a tool for __managing changes__ to a set of files.
#
# There are many different __version control systems__: 
#
# - Git 
# - Mercurial (`hg`)
# - CVS
# - Subversion (`svn`)
# - ...

# %% [markdown]
# ## Why use version control?
#
# - Better kind of __backup__.
# - Review __history__ ("When did I introduce this bug?").
# - Restore older __code versions__.
# - Ability to __undo mistakes__.
# - Maintain __several versions__ of the code at a time.

# %% [markdown]
# Git is also a __collaborative__ tool:
#
# - "How can I share my code?"
# - "How can I submit a change to someone else's code?"
# - "How can I merge my work with Sue's?"
#
# ## Git != GitHub
#
# - __Git__: version control system tool to manage source code history.
#
# - __GitHub__: hosting service for Git repositories.

# %% [markdown]
# ## How do we use version control?
#
# Do some programming, then commit our work:
#
# `my_vcs commit`
#
# Program some more.
#
# Spot a mistake:
#
# `my_vcs rollback`
#
# Mistake is undone.

# %% [markdown]
# ## What is version control? (Team version)
#
# Graham             | Eric
# ------------------ |------   
# `my_vcs commit`    | ...
# ...                | Join the team
# ...                | `my_vcs checkout`
# ...                | Do some programming
# ...                | `my_vcs commit`
# `my_vcs update`		 | ...
# Do some programming|Do some programming
# `my_vcs commit`    | ...
# `my_vcs update`    | ...
# `my_vcs merge`     | ...
# `my_vcs commit`    | ...

# %% [markdown]
# ## Scope
#
# This course will use the `git` version control system, but much of what you learn will be valid with other version control 
# tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

# %% [markdown]
# ## Practising with Git

# %% [markdown]
# ## Example Exercise
#
# In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. 
#
# This could be your research, a hobby, or something else. In the end, we will show you how to display the content of these files as a very simple website. 

# %% [markdown]
# ## Programming and documents
#
# The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. 
#
# In later parts of the course, you will use the version control tools you learn today with actual Python code.

# %% [markdown]
# ## Markdown
#
# The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting. This is the convention used in this file, too. 
#
# You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/UCL/ucl_software_carpentry/blob/master/git/git_instructions.md), and compare the [raw text](https://raw.github.com/UCL/ucl_software_carpentry/master/git/git_instructions.md).

# %% [markdown]
# ## Displaying Text in this Tutorial
#
# This tutorial is based on use of the Git command line. So you'll be typing commands in the shell.

# %% [markdown]
# To make it easy for me to edit, I've built it using Jupyter notebook.

# %% [markdown]
# Commands you can type will look like this, using the %%bash "magic" for the notebook.

# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook


# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# echo some output

# %% [markdown]
# with the results you should see below. 

# %% [markdown]
# In this document, we will show the new content of an edited document like this:

# %% jupyter={"outputs_hidden": false}
# %%writefile somefile.md
Some content here

# %% [markdown]
# But if you are following along, you should edit the file using a text editor.
# On either Windows, Mac or Linux, we recommend [VS Code](https://code.visualstudio.com/).

# %% [markdown]
# ## Setting up somewhere to work

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# rm -rf learning_git/git_example # Just in case it's left over from a previous class; you won't need this
# mkdir -p learning_git/git_example
# cd learning_git/git_example

# %% [markdown]
# I just need to move this Jupyter notebook's current directory as well:

# %% jupyter={"outputs_hidden": false}
import os
top_dir = os.getcwd()
top_dir

# %% jupyter={"outputs_hidden": false}
git_dir = os.path.join(top_dir, 'learning_git')
git_dir

# %%
working_dir=os.path.join(git_dir, 'git_example')

# %% jupyter={"outputs_hidden": false}
os.chdir(working_dir)

# %% [markdown]
# ## Solo work
#
# ## Configuring Git with your name and email
#
# First, we should configure Git to know our name and email address:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git config --global user.name "Lancelot the Brave"
# git config --global user.email "l.brave@spamalot.uk"

# %% [markdown]
# Additionally, it's also a good idea to define what's the name of the default branch when we create a repository:

# %% language="bash"
# git config --global init.defaultBranch main

# %% [markdown]
# Historically, the default branch was named `master`. Nowadays, the community and most of the hosting sites have changed the default ([read about this change in GitHub](https://github.com/github/renaming/) and [Gitlab](https://about.gitlab.com/blog/2021/03/10/new-git-default-branch-name/).

# %% [markdown]
# ## Initialising the repository
#
# Now, we will tell Git to track the content of this folder as a git "repository".

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# pwd # Note where we are standing-- MAKE SURE YOU INITIALISE THE RIGHT FOLDER
# git init

# %% [markdown]
# As yet, this repository contains no files:

# %% jupyter={"outputs_hidden": false} language="bash"
# ls

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git status
