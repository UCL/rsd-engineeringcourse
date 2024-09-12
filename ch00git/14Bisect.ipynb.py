# ---
# jupyter:
#   jekyll:
#     display_name: Bisect
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Debugging With Git Bisect
# 
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook
# 
# You can use
#
# ``` bash
# git bisect
# ```
#
# to find out which commit caused a bug.

# %% [markdown]
# ## An example repository
#
# In a nice open source example, I found an arbitrary exemplar on github

# %% jupyter={"outputs_hidden": true}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
os.chdir(git_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# rm -rf bisectdemo
# git clone https://github.com/UCL-ARC-RSEing-with-Python/bisectdemo.git

# %% jupyter={"outputs_hidden": true}
bisect_dir=os.path.join(git_dir,'bisectdemo')
os.chdir(bisect_dir)

# %% attributes={"classes": [" bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# python squares.py 2 # 4

# %% [markdown]
# This has been set up to break itself at a random commit, and leave you to use
# bisect to work out where it has broken:

# %% attributes={"classes": [" bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# ./breakme.sh > break_output

# %% [markdown]
# Which will make a bunch of commits, of which one is broken, and leave you in the broken final state

# %% jupyter={"outputs_hidden": false} language="bash"
# python squares.py 2 # Error message

# %% [markdown]
# ## Bisecting manually

# %% attributes={"classes": [" bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git bisect start
# git bisect bad # We know the current state is broken
# git switch main
# git bisect good # We know the main branch state is OK

# %% [markdown]
# Bisect needs one known good and one known bad commit to get started

# %% [markdown]
# ## Solving Manually

# %% [markdown] attributes={"classes": [" bash"], "id": ""}
# ``` bash
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 #Crash
# git bisect bad
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# ```
#

# %% [markdown]
# And eventually:

# %% [markdown] attributes={"classes": [" bash"], "id": ""}
# ``` bash
# git bisect good
#     Bisecting: 0 revisions left to test after this (roughly 0 steps)
#
# python squares.py 2
#     4
#
# git bisect good
# 2777975a2334c2396ccb9faf98ab149824ec465b is the first bad commit
# commit 2777975a2334c2396ccb9faf98ab149824ec465b
# Author: Shawn Siefkas <shawn.siefkas@meredith.com>
# Date:   Thu Nov 14 09:23:55 2013 -0600
#
#     Breaking argument type
#
# ```

# %% [markdown]
# Stop the bisect process with:
#
# ``` bash
# git bisect reset
# ```

# %% [markdown]
# ## Solving automatically
#
# If we have an appropriate unit test, we can do all this automatically:
#
# (*NOTE*: You don't need [to redirect the `stderr` and `stdout`](https://linuxize.com/post/bash-redirect-stderr-stdout/) (with `&>`) of `git bisect run` to a file when running these commands outside a jupyter notebook (i.e., on a shell). This is done here so the errors appears with the right commits)

# %% attributes={"classes": [" bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git bisect start
# git bisect bad HEAD # We know the current state is broken
# git bisect good main # We know main is good
# git bisect run python squares.py 2 &> gitbisect.out
# cat gitbisect.out

# %% [markdown]
# Boom!
