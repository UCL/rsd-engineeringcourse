# ---
# jupyter:
#   jekyll:
#     display_name: Branches
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Branches
# 
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook
# 
# Branches are incredibly important to why `git` is cool and powerful.
#
# They are an easy and cheap way of making a second version of your software, which you work on in parallel,
# and pull in your changes when you are ready.

# %% jupyter={"outputs_hidden": true}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git branch # Tell me what branches exist

# %% jupyter={"outputs_hidden": false} language="bash"
# git switch -c experiment # Make a new branch (use instead `checkout -b` if you have a version of git older than 2.23)

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch

# %%
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon
* Glyder Fawr
* Fan y Big
* Cadair Idris

# %% language="bash"
# git add Wales.md
# git commit -m "Add Cadair Idris"

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git switch main # Switch to an existing branch (use `checkout` if you are using git older than 2.23)

# %% jupyter={"outputs_hidden": false} language="bash"
# cat Wales.md

# %% jupyter={"outputs_hidden": false} language="bash"
# git switch experiment

# %% jupyter={"outputs_hidden": false}
# cat Wales.md

# %% [markdown]
# ## Publishing branches
#
# To let the server know there's a new branch use:

# %% jupyter={"outputs_hidden": false} language="bash"
# git push -u origin experiment

# %% [markdown]
# We use `--set-upstream origin` (Abbreviation `-u`) to tell git that this branch should be pushed to and pulled from origin per default.
#
# If you are following along, you should be able to see your branch in the list of branches in GitHub.

# %% [markdown]
# Once you've used `git push -u` once, you can push new changes to the branch with just a git push.

# %% [markdown]
# If others checkout your repository, they will be able to do `git switch experiment` to see your branch content,
# and collaborate with you **in the branch**.

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch -r

# %% [markdown]
# Local branches can be, but do not have to be, connected to remote branches
# They are said to "track" remote branches. `push -u` sets up the tracking relationship.
# You can see the remote branch for each of your local branches if you ask for "verbose" output from `git branch`:

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch -vv

# %% [markdown]
# ## Find out what is on a branch
#
# In addition to using `git diff` to compare to the state of a branch,
# you can use `git log` to look at lists of commits which are in a branch
# and haven't been merged yet.

# %% jupyter={"outputs_hidden": false} language="bash"
# git log main..experiment

# %% [markdown]
# Git uses various symbols to refer to sets of commits.
# The double dot `A..B` means "ancestor of B and not ancestor of A"
#
# So in a purely linear sequence, it does what you'd expect.

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --graph --oneline HEAD~9..HEAD~5

# %% [markdown]
# But in cases where a history has branches,
# the definition in terms of ancestors is important.

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --graph --oneline HEAD~5..HEAD

# %% [markdown]
# If there are changes on both sides, like this:

# %% jupyter={"outputs_hidden": false} language="bash"
# git switch main

# %% jupyter={"outputs_hidden": false}
# %%writefile Scotland.md
Mountains In Scotland
==================

* Ben Eighe
* Cairngorm
* Aonach Eagach


# %% jupyter={"outputs_hidden": false} language="bash"
# git diff Scotland.md

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Scotland.md
# git commit -m "Commit Aonach onto main branch"

# %% [markdown]
# Then this notation is useful to show the content of what's on what branch:

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --left-right --oneline main...experiment

# %% [markdown]
# Three dots means "everything which is not a common ancestor" of the two commits, i.e. the differences between them.

# %% [markdown]
# ## Merging branches

# %% [markdown]
# We can merge branches, and just as we would pull in remote changes, there may or may not be conflicts.

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch
# git merge experiment

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --graph --oneline HEAD~3..HEAD

# %% [markdown]
# ## Cleaning up after a branch

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch -d experiment

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch --remote

# %% jupyter={"outputs_hidden": false} language="bash"
# git push --delete origin experiment 
# # Remove remote branch 
# # - also can use github interface

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch --remote

# %% [markdown]
# ## A good branch strategy
#
# * A `develop` or `main` branch: for general new code - (the cutting edge version of your software)
# * `feature` branches: for specific new ideas. Normally branched out from `main`.
# * `release` branches: when you share code with users. A particular moment of the `develop` process that it's considered stable.
#   * Useful for including security and bug patches once it's been released.
# * A `production` branch: code used for active work. Normally it's the same than the latest release.

# %% [markdown]
# ## Grab changes from a branch
#
# Make some changes on one branch, switch back to another, and use:

# %% [markdown] attributes={"classes": [" bash"], "id": ""}
# ```bash
# git checkout <branch> <path>
# ```

# %% [markdown]
# to quickly grab a file from one branch into another. This will create a copy of the file as it exists in `<branch>` into your current branch, overwriting it if it already existed.
# For example, if you have been experimenting in a new branch but want to undo all your changes to a particular file (that is, restore the file to its version in the `main` branch), you can do that with:
#
# ```
# git checkout main test_file
# ```
#
# Using `git checkout` with a path takes the content of files.
# To grab the content of a specific *commit* from another branch,
# and apply it as a patch to your branch, use:

# %% [markdown]
# ``` bash
# git cherry-pick <commit>
# ```
