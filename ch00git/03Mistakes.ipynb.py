# ---
# jupyter:
#   jekyll:
#     display_name: Fixing Mistakes
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Fixing mistakes

# %% [markdown]
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook

# %% [markdown]
# We're still in our git working directory:

# %% jupyter={"outputs_hidden": false}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)
working_dir

# %% [markdown]
# ## Referring to changes with HEAD and ^
#
# The commit we want to revert to is the one before the latest.
#
# `HEAD` refers to the latest commit. That is, we want to go back to the change before the current `HEAD`. 
#
# We could use the hash code (e.g. 73fbeaf) to reference this, but you can also refer to the commit before the `HEAD` as `HEAD^`, the one before that as `HEAD^^`, the one before that as `HEAD~3`.

# %% [markdown]
# ## Reverting
#  
# Ok, so now we'd like to undo the nasty commit with the lie about Mount Fictional.

# %% jupyter={"outputs_hidden": false} language="bash"
# git revert HEAD^

# %% [markdown]
# An editor may pop up, with some default text which you can accept and save. 

# %% [markdown]
# ## Conflicted reverts
#
# You may, depending on the changes you've tried to make, get an error message here. 
#
# If this happens, it is because git could not automagically decide how to combine the change you made after the change you want to revert, with the attempt to revert the change: this could happen, for example, if they both touch the same line. 
#
# If that happens, you need to manually edit the file to fix the problem. Skip ahead to the section on resolving conflicts, or ask a demonstrator to help.

# %% [markdown]
# ## Review of changes
#
# The file should now contain the change to the title, but not the extra line with the lie. Note the log:

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --date=short

# %% [markdown]
# ## Antipatch
#
# Notice how the mistake has stayed in the history.
#
# There is a new commit which undoes the change: this is colloquially called an "antipatch". 
# This is nice: you have a record of the full story, including the mistake and its correction.

# %% [markdown]
# ## Rewriting history
#
# It is possible, in git, to remove the most recent change altogether, "rewriting history". Let's make another bad change, and see how to do this.

# %% [markdown]
# ## A new lie

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
Mountains and Hills in the UK   
===================   
Engerland is not very mountainous.   
But has some tall hills, and maybe a
mountain or two depending on your definition.


# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# cat index.md

# %% jupyter={"outputs_hidden": false} language="bash"
# git diff

# %% jupyter={"outputs_hidden": false} language="bash"
# git add index.md
# git commit -m "Add a silly spelling"

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log --date=short

# %% [markdown]
# ## Using reset to rewrite history

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git reset HEAD^

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log --date=short

# %% [markdown]
# ## Covering your tracks
#
# The silly spelling *is no longer in the log*. This approach to fixing mistakes, "rewriting history" with `reset`, instead of adding an antipatch with `revert`, is dangerous, and we don't recommend it. But you may want to do it for small silly mistakes, such as to correct a commit message.

# %% [markdown]
# ## Resetting the working area
#
# When `git reset` removes commits, it leaves your working directory unchanged -- so you can keep the work in the bad change if you want. 

# %% jupyter={"outputs_hidden": false} language="bash"
# cat index.md

# %% [markdown]
# If you want to lose the change from the working directory as well, you can do `git reset --hard`. 
#
# I'm going to get rid of the silly spelling, and I didn't do `--hard`, so I'll reset the file from the working directory to be the same as in the index:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": true} language="bash"
# git checkout index.md

# %% jupyter={"outputs_hidden": false} language="bash"
# cat index.md

# %% [markdown]
# We can add this to our diagram:

# %% jupyter={"outputs_hidden": false}
message="""
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Staging Area -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
"""
from wsd import wsd
# %matplotlib inline
wsd(message)

# %% [markdown]
# We can add it to Cleese's story:

# %% jupyter={"outputs_hidden": false}
message="""
participant "Cleese's repo" as R
participant "Cleese's index" as I
participant Cleese as C

note right of C: git revert HEAD^

C->R: Add new commit reversing change
R->I: update staging area to reverted version
I->C: update file to reverted version



note right of C: vim index.md
note right of C: git add index.md
note right of C: git commit -m "Add another mistake"
C->I: Add mistake
I->R: Add mistake

note right of C: git reset HEAD^

C->R: Delete mistaken commit
R->I: Update staging area to reset commit

note right of C: git checkout index.md

I->C: Update file to reverted version


"""
wsd(message)
