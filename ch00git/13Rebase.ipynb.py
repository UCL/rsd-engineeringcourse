# ---
# jupyter:
#   jekyll:
#     display_name: Rebase
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Rebasing
#
# ## Rebase vs merge
#
# A git *merge* is only one of two ways to get someone else's work into yours.
# The other is called a rebase.
#
# In a merge, a revision is added, which brings the branches together. Both histories are retained.
# In a rebase, git tries to work out
#
# > What would you need to have done, to make your changes, if your colleague had already made theirs?
#
# Git will invent some new revisions, and the result will be a repository with an apparently linear history. This can be useful if you want a cleaner, non-branching history, but it has the risk of creating inconsistencies, since you are, in a way, "rewriting" history.
#
# ## An example rebase
#
# We've built a [repository to help visualise the difference between a merge and a rebase](https://github.com/UCL-ARC-RSEing-with-Python/wocky_rebase/blob/main/wocky.md).

# %% [markdown]
# The initial state of both collaborators is a text file, wocky.md:
#
# ```
# It was clear and cold,
# and the slimy monsters
# ```

# %% [markdown]
# On the `main` branch, a second commit ('Dancing') has been added:

# %% [markdown]
# ```
# It was clear and cold,
# and the slimy monsters
# danced and spun in the waves
# ```

# %% [markdown]
# On the "Carollian" branch, a commit has been added translating the initial state into Lewis Caroll's language:
#
# ```
# 'Twas brillig,
# and the slithy toves
# ```

# %% [markdown]
# So the logs look like this:

# %% [markdown]
# ```bash
# git log --oneline --graph main
# ```
#
# ```
# * 2a74d89 Dancing
# * 6a4834d Initial state
# ```
#
# ```bash
# git log --oneline --graph carollian
# ```
#
# ```
# * 2232bf3 Translate into Caroll's language
# * 6a4834d Initial state
# ```

# %% [markdown]
# If we now **merge** carollian into main, the final state will include both changes:

# %% [markdown]
# ```
# 'Twas brillig,
# and the slithy toves
# danced and spun in the waves
# ```
#

# %% [markdown]
# But the graph shows a divergence and then a convergence:

# %% [markdown]
# ```
# git log --oneline --graph
# ```
#
# ```
# *   b41f869 Merge branch 'carollian' into main_merge_carollian
# |\
# | * 2232bf3 Translate into Caroll's language
# * | 2a74d89 Dancing
# |/
# * 6a4834d Initial state
# ```

# %% [markdown]
# But if we **rebase**, the final content of the file is still the same, but the graph is different:

# %% [markdown]
# ``` bash
# git log --oneline --graph main_rebase_carollian
# ```
#
# ```
# * df618e0 Dancing
# * 2232bf3 Translate into Caroll's language
# * 6a4834d Initial state
# ```

# %% [markdown]
# We have essentially created a new history, in which our changes come after the ones in the carollian branch. Note that, in this case, the hash for our "Dancing" commit has changed (from `2a74d89` to `df618e0`)!
#
# To trigger the rebase, we did:
#     
# ``` bash
# git switch main
# git rebase carollian
# ```
#
# If this had been a remote, we would merge it with:
#     
# ``` bash
# git pull --rebase
# ```

# %% [markdown]
# ## Fast Forwards
#
# If we want to continue with the translation, and now want to merge the rebased branch into the carollian branch, 
# we get:
#
# ```bash
# git switch carollian
# git merge main
# ```
#
#
# ``` bash
# Updating 2232bf3..df618e0
# Fast-forward
#  wocky.md | 1 +
#  1 file changed, 1 insertion(+)
# ```
#
# The main branch was already **rebased on** the carollian branch, so this merge was just a question of updating *metadata* (moving the label for the carollian branch so that it points to the same commit main does): a "fast forward".
#
# ## Rebasing pros and cons
#
# Some people like the clean, apparently linear history that rebase provides.
#
# But *rebase rewrites history*.
#
# If you've already pushed, or anyone else has got your changes, things will get screwed up.
#
# If you know your changes are still secret, it might be better to rebase to keep the history clean.
# If in doubt, just merge.
#
# ## Squashing
#
# A second way to use the `git rebase` command is to rebase your work on top of one of *your own* earlier commits,
# in interactive mode (`-i`). A common use of this is to "squash" several commits that should really be one, i.e. combine them into a single commit that contains all their changes:

# %% [markdown] attributes={"classes": [" bash"], "id": ""}
# ``` bash
# git log
# ```
#
# ```
# ea15 Some good work
# ll54 Fix another typo
# de73 Fix a typo
# ab11 A great piece of work
# cd27 Initial commit
# ```

# %% [markdown]
# ## Using rebase to squash

# %% [markdown] attributes={"classes": [" bash"], "id": ""}
# If we type 
#
# ``` bash
# git rebase -i ab11 #OR HEAD^^
# ```
#
# an edit window pops up with:

# %% [markdown]
# ```
# pick cd27 Initial commit
# pick ab11 A great piece of work
# pick de73 Fix a typo
# pick ll54 Fix another typo
# pick ea15 Some good work
#
# # Rebase 60709da..30e0ccb onto 60709da
# #
# # Commands:
# #  p, pick = use commit
# #  e, edit = use commit, but stop for amending
# #  s, squash = use commit, but meld into previous commit
# ```

# %% [markdown]
# We can rewrite select commits to be merged, so that the history is neater before we push.
# This is a great idea if you have lots of trivial typo commits.

# %% [markdown]
# ```
# pick cd27 Initial commit
# pick ab11 A great piece of work
# squash de73 Fix a typo
# squash ll54 Fix another typo
# pick ea15 Some good work
# ```
#
# save the interactive rebase config file, and rebase will build a new history:
#
# ``` bash
# git log
# ```
#
# ```
# de82 Some good work
# fc52 A great piece of work
# cd27 Initial commit
# ```

# %% [markdown]
# Note the commit hash codes for 'Some good work' and 'A great piece of work' have changed, 
# as the change they represent has changed.
