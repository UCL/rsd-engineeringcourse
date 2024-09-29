# ---
# jupyter:
#   jekyll:
#     display_name: Collaboration
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Collaboration

# %% [markdown]
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook
# 
# ## Form a team

# %% [markdown]
# Now we're going to get to the most important question of all with Git and GitHub: working with others.
#
# Organise into pairs. You're going to be working on the website of one of the two of you, together, so decide who is going to be the leader, and who the collaborator.

# %% [markdown]
# ## Giving permission
#
# The leader needs to let the collaborator have the right to make changes to his code.
#
# In GitHub, go to `Settings` on the right, then `Collaborators & teams` on the left.
#
# Add the user name of your collaborator to the box. They now have the right to push to your repository.

# %% [markdown]
# ## Obtaining a colleague's code
#
# Next, the collaborator needs to get a copy of the leader's code. For this example notebook,
# I'm going to be collaborating with myself, swapping between my two repositories.
# Make yourself a space to put it your work. (I will have two)

# %% jupyter={"outputs_hidden": true}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(git_dir)

# %% language="bash"
# pwd
# rm -rf partner_repo # cleanup after previous example
#

# %% [markdown]
# Next, the collaborator needs to find out the URL of the repository: they should go to the leader's repository's GitHub page, and note the URL on the top of the screen. Make sure the "ssh" button is pushed, the URL should begin with `git@github.com`. 
#
# Copy the URL into your clipboard by clicking on the icon to the right of the URL, and then:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# pwd
# git clone git@github.com:UCL/github-example.git partner_repo

# %% jupyter={"outputs_hidden": true}
partner_dir = os.path.join(git_dir, 'partner_repo')
os.chdir(partner_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# pwd
# ls

# %% [markdown]
# Note that your partner's files are now present on your disk:

# %% jupyter={"outputs_hidden": false} language="bash"
# cat lakeland.md

# %% [markdown]
# ## Nonconflicting changes
#
# Now, both of you should make some changes. To start with, make changes to *different* files. This will mean your work doesn't "conflict". Later, we'll see how to deal with changes to a shared file.

# %% [markdown]
# Both of you should commit, but not push, your changes to your respective files:

# %% [markdown]
# E.g., the leader:

# %% jupyter={"outputs_hidden": true}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Tryfan
* Yr Wyddfa

# %% jupyter={"outputs_hidden": false} language="bash"
# ls

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Wales.md
# git commit -m "Add wales"

# %% [markdown]
# And the partner:

# %% jupyter={"outputs_hidden": true}
os.chdir(partner_dir)

# %% jupyter={"outputs_hidden": false}
# %%writefile Scotland.md
Mountains In Scotland
==================

* Ben Eighe
* Ben Nevis
* Cairngorm

# %% jupyter={"outputs_hidden": false} language="bash"
# ls

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Scotland.md
# git commit -m "Add Scotland"

# %% [markdown]
# One of you should now push with `git push`:

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% [markdown]
# ## Rejected push

# %% [markdown]
# The other should then push, but should receive an error message:

# %% jupyter={"outputs_hidden": true}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git push

# %% [markdown]
# Do as it suggests. However, we need first to tell git how we want it to act when there are diverging branches (as in this case). We will set the default to be to create a merge commit, then we proceed to `pull`.

# %% jupyter={"outputs_hidden": false} language="bash"
# git config --global pull.rebase false
# git pull

# %% [markdown]
# ## Merge commits
#
# A window may pop up with a suggested default commit message. This commit is special: it is a *merge* commit. It is a commit which combines your collaborator's work with your own.

# %% [markdown]
# Now, push again with `git push`. This time it works. If you look on GitHub, you'll now see that it contains both sets of changes.

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% [markdown]
# The partner now needs to pull down that commit:

# %% jupyter={"outputs_hidden": true}
os.chdir(partner_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# git pull

# %% jupyter={"outputs_hidden": false} language="bash"
# ls

# %% [markdown]
# ## Nonconflicted commits to the same file
#
# Go through the whole process again, but this time, both of you should make changes to a single file, but make sure that you don't touch the same *line*. Again, the merge should work as before:

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Tryfan
* Snowdon

# %% jupyter={"outputs_hidden": false} language="bash"
# git diff

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Wales.md
# git commit -m "Translating from the Welsh"

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --oneline

# %% jupyter={"outputs_hidden": true}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Wales.md
# git commit -m "Add a beacon"

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --oneline

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% [markdown]
# Switching back to the other partner...

# %% jupyter={"outputs_hidden": true}
os.chdir(partner_dir)

# %% jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git push

# %% jupyter={"outputs_hidden": false} language="bash"
# git pull

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --oneline --graph

# %% jupyter={"outputs_hidden": true}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# git pull

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --graph --oneline

# %% jupyter={"outputs_hidden": false}
message="""
participant Palin as P
participant "Palin's repo" as PR
participant "Shared remote" as M
participant "Cleese's repo" as CR
participant Cleese as C

note left of P: git clone
M->PR: fetch commits
PR->P: working directory as at latest commit

note left of P: edit Scotland.md
note right of C: edit Wales.md

git add Scotland.md
note left of P: git commit -m "Add scotland"
P->PR: create commit with Scotland file

git add Wales.md
note right of C: git commit -m "Add wales"
C->CR: create commit with Wales file

note left of P: git push
PR->M: update remote with changes

note right of C: git push
CR-->M: !Rejected change

note right of C: git pull
M->CR: Pull in Palin's last commit, merge histories
CR->C: Add Scotland.md to working directory

note right of C: git push
CR->M: Transfer merged history to remote

"""
from wsd import wsd
# %matplotlib inline
wsd(message)

# %% [markdown]
# ## Conflicting commits
#
# Finally, go through the process again, but this time, make changes which touch the same line.

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon
* Fan y Big

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Wales.md
# git commit -m "Add another Beacon"
# git push

# %% jupyter={"outputs_hidden": true}
os.chdir(partner_dir)

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon
* Glyder Fawr

# %% jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git add Wales.md
# git commit -m "Add Glyder"
# git push

# %% [markdown]
# When you pull, instead of offering an automatic merge commit message, it says:

# %% jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git pull

# %% [markdown]
# ## Resolving conflicts
#
# Git couldn't work out how to merge the two different sets of changes.
#
# You now need to manually resolve the conflict.
#
# It has marked the conflicted area:

# %% jupyter={"outputs_hidden": false} language="bash"
# cat Wales.md

# %% [markdown]
# Manually edit the file, to combine the changes as seems sensible and get rid of the symbols:

# %% jupyter={"outputs_hidden": false}
# %%writefile Wales.md
Mountains In Wales
==================

* Pen y Fan
* Tryfan
* Snowdon
* Glyder Fawr
* Fan y Big

# %% [markdown]
# ## Commit the resolved file
#
# Now commit the merged result:

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Wales.md
# git commit --no-edit # I added a No-edit for this non-interactive session. You can edit the commit if you like.

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% jupyter={"outputs_hidden": true}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# git pull

# %% jupyter={"outputs_hidden": false} language="bash"
# cat Wales.md

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --oneline --graph

# %% [markdown]
# ## Distributed VCS in teams with conflicts

# %% jupyter={"outputs_hidden": false}
message="""
participant Palin as P
participant "Palin's repo" as PR
participant "Shared remote" as M
participant "Cleese's repo" as CR
participant Cleese as C

note left of P: edit the same line in wales.md
note right of C: edit the same line in wales.md
    
note left of P: git add Wales.md
note left of P: git commit -m "update wales.md"
P->PR: add commit to local repo
    
note right of C: git add Wales.md
note right of C: git commit -m "update wales.md"
C->CR: add commit to local repo
    
note left of P: git push
PR->M: transfer commit to remote
    
note right of C: git push
CR->M: !Rejected

note right of C: git pull
M->C: Make conflicted file with conflict markers
    
note right of C: edit file to resolve conflicts
note right of C: git add wales.md
note right of C: git commit
C->CR: Mark conflict as resolved

note right of C: git push
CR->M: Transfer merged history to remote

note left of P: git pull
M->SR: Download Cleese's resolution of conflict.
    
"""

wsd(message)

# %% [markdown]
# ## The Levels of Git

# %% jupyter={"outputs_hidden": false}
message="""
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Staging Area -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
Local Repository -> Remote Repository : git push
Remote Repository -> Local Repository : git fetch
Local Repository -> Working Directory : git merge
Remote Repository -> Working Directory: git pull
"""

wsd(message)

# %% [markdown]
# ## Editing directly on GitHub
#
# ## Editing directly on GitHub
#
# Note that you can also make changes in the GitHub website itself. Visit one of your files, and hit "edit".
#
# Make a change in the edit window, and add an appropriate commit message.
#
# That change now appears on the website, but not in your local copy. (Verify this). 

# %% [markdown]
# Now pull, and check the change is now present on your local version. 

# %% [markdown]
# ## Social Coding
#
# ## GitHub as a social network
#
# In addition to being a repository for code, and a way to publish code, GitHub is a social network.  
#
# You can follow the public work of other coders: go to the profile of your collaborator in your browser, and hit the "follow" button. 
#
# Check out the profiles of [Linus Torvalds](https://github.com/torvalds) - creator of [git](https://git-scm.com/) ([first git commit ever](https://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290)) and [Linux](https://en.wikipedia.org/wiki/Linux) - , [Guido van Rossum](https://github.com/gvanrossum) - creator of Python -, or 
# [James Hetherington](https://github.com/jamespjh) - the creator of these course notes.
#
# Using GitHub to build up a good public profile of software projects you've worked on is great for your CV!
