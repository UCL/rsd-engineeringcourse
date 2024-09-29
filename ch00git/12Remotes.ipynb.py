# ---
# jupyter:
#   jekyll:
#     display_name: Remotes
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Working with multiple remotes
# 
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook
# 
# ## Distributed versus centralised
#
# Older version control systems (cvs, svn) were "centralised"; the history was kept only on a server,
# and all commits required an internet.
#
# Centralised                    |  Distributed
# -------------------------------|--------------------------
# Server has history             |Every user has full history
# Your computer has one snapshot |  Many local branches
# To access history, need internet| History always available
# You commit to remote server     | Users synchronise histories
# cvs, subversion(svn)            | git, mercurial (hg), bazaar (bzr)

# %% [markdown]
# With modern distributed systems, we can add a second remote. This might be a personal *fork* on github:

# %% jupyter={"outputs_hidden": false}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git switch main
# git remote add arc git@github.com:UCL-ARC-RSEing-with-Python/github-example.git
# git remote -v

# %% [markdown]
# We can push to a named remote:

# %% jupyter={"outputs_hidden": false}
# %%writefile Pennines.md

Mountains In the Pennines
========================

* Cross Fell
* Whernside

# %% jupyter={"outputs_hidden": false} language="bash"
# git add Pennines.md
# git commit -m "Add Whernside"

# %% jupyter={"outputs_hidden": false} language="bash"
# git push -uf arc main

# %% [markdown]
# ## Referencing remotes
#
# You can always refer to commits on a remote like this:

# %% jupyter={"outputs_hidden": false} language="bash"
# git fetch
# git log --oneline --left-right arc/main...origin/main

# %% [markdown]
# To see the differences between remotes, for example.
#
# To see what files you have changed that aren't updated on a particular remote, for example:

# %% jupyter={"outputs_hidden": false} language="bash"
# git diff --name-only origin/main

# %% [markdown]
# When you reference remotes like this, you're working with a cached copy of the last time you interacted with the remote. You can do `git fetch` to update local data with the remotes without actually pulling. You can also get useful information about whether tracking branches are ahead or behind the remote branches they track:

# %% jupyter={"outputs_hidden": false} language="bash"
# git branch -vv

# %% [markdown]
# ## Hosting Servers
#
# ## Hosting a local server
#
# * Any repository can be a remote for pulls
# * Can pull/push over shared folders or ssh
# * Pushing to someone's working copy is dangerous
# * Use `git init --bare` to make a copy for pushing
# * You don't need to create a "server" as such, any 'bare' git repo will do.

# %% jupyter={"outputs_hidden": false}
bare_dir = os.path.join(git_dir, 'bare_repo')
os.chdir(git_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# mkdir -p bare_repo
# cd bare_repo
# git init --bare

# %% jupyter={"outputs_hidden": false}
os.chdir(working_dir)

# %% jupyter={"outputs_hidden": false} language="bash"
# git remote add local_bare ../bare_repo
# git push -u local_bare main

# %% jupyter={"outputs_hidden": false} language="bash"
# git remote -v

# %% [markdown]
# You can now work with this local repository, just as with any other git server.
# If you have a colleague on a shared file system, you can use this approach to collaborate through that file system.

# %% [markdown]
# ## Home-made SSH servers
#
# Classroom exercise: Try creating a server for yourself using a machine you can SSH to:

# %% [markdown]
# ``` bash
# ssh <mymachine>
# mkdir mygitserver
# cd mygitserver
# git init --bare
# exit
# git remote add <somename> ssh://user@host/mygitserver
# git push -u <somename> main
# ```

# %% [markdown]
# ## SSH keys and GitHub
#
# Classroom exercise: If you haven't already, you should set things up so that you don't have to keep typing in your
# password whenever you interact with GitHub via the command line.
#
# You can do this with an "ssh keypair". You may have created a keypair in the
# Software Carpentry shell training. Go to the [ssh settings
# page](https://github.com/settings/ssh) on GitHub and upload your public key by
# copying the content from your computer. (Probably at .ssh/id_rsa.pub)
#
# If you have difficulties, the instructions for this are [on the GitHub
# website](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
