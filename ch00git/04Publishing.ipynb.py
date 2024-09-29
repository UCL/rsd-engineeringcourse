# ---
# jupyter:
#   jekyll:
#     display_name: Publishing
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Publishing

# %% [markdown]
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook

# %% [markdown]
# We're still in our working directory:

# %% jupyter={"outputs_hidden": false}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)
working_dir

# %% [markdown]
# ## Sharing your work

# %% [markdown]
# So far, all our work has been on our own computer. But a big part of the point of version control is keeping your work safe, on remote servers. Another part is making it easy to share your work with the world In this example, we'll be using the "GitHub" cloud repository to store and publish our work. 
#
# If you have not done so already, you should create an account on [GitHub](https://github.com/): go to [GitHub's website](https://github.com/), fill in a username and password, and click on "sign up for GitHub". 

# %% [markdown]
# ## Creating a repository
#
# Ok, let's create a repository to store our work. Hit "[new repository](https://github.com/new)" on the right of the github home screen.
#
# Fill in a short name, and a description. Choose a "public" repository. Don't choose to initialize the repository with a README. That will create a repository with content and we only want a placeholder where to upload what we've created locally.

# %% [markdown]
# ## Paying for GitHub
#
# For this course, you should use public repositories in your personal account for your example work: it's good to share! GitHub is free for open source, but in general, charges a fee if you want to keep your work private. 
#
# In the future, you might want to keep your work on GitHub private. 
#
# Students can get free private repositories on GitHub, by going to [GitHub Education](https://education.github.com/) and filling in a form (look for the Student Developer Pack). 
#
# UCL pays for private GitHub repositories for UCL research groups: you can find the service details on the [Advanced Research Computing Centre's website](https://www.ucl.ac.uk/advanced-research-computing/expertise/research-software-development/research-software-development-tools/support-ucl-2).

# %% [markdown]
# ## Adding a new remote to your repository
#
# Instructions will appear, once you've created the repository, as to how to add this new "remote" server to your repository, in the lower box on the screen. Mine say:

# %% jupyter={"outputs_hidden": true} language="bash"
# git remote add origin git@github.com:UCL/github-example.git

# %% attributes={"classes": ["Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git push -uf origin main # You shouldn't need the extra `f` switch. We use it here to force the push and rewrite that repository.
#       #You should copy the instructions from YOUR repository.

# %% [markdown]
# ## Remotes
#
# The first command sets up the server as a new `remote`, called `origin`. 
#
# Git, unlike some earlier version control systems is a "distributed" version control system, which means you can work with multiple remote servers. 
#
# Usually, commands that work with remotes allow you to specify the remote to use, but assume the `origin` remote if you don't. 
#
# Here, `git push` will push your whole history onto the server, and now you'll be able to see it on the internet! Refresh your web browser where the instructions were, and you'll see your repository!

# %% [markdown]
# Let's add these commands to our diagram:

# %% jupyter={"outputs_hidden": false}
message="""
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Staging Area -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
Local Repository -> Remote Repository : git push
"""
from wsd import wsd
# %matplotlib inline
wsd(message)

# %% [markdown]
# ## Playing with GitHub
#
# Take a few moments to click around and work your way through the GitHub interface. Try clicking on 'index.md' to see the content of the file: notice how the markdown renders prettily.
#
# Click on "commits" near the top of the screen, to see all the changes you've made. Click on the commit number next to the right of a change, to see what changes it includes: removals are shown in red, and additions in green.

# %% [markdown]
# ## Working with multiple files

# %% [markdown]
# ## Some new content
#
# So far, we've only worked with one file. Let's add another:

# %% [markdown]
# ``` bash
# nano lakeland.md
# ```

# %% jupyter={"outputs_hidden": false}
# %%writefile lakeland.md
Lakeland  
========   
  
Cumbria has some pretty hills, and lakes too.  

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false}
# cat lakeland.md

# %% [markdown]
# ## Git will not by default commit your new file

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} magic_args="--no-raise-error" language="bash"
# git commit -m "Try to add Lakeland"

# %% [markdown]
# This didn't do anything, because we've not told git to track the new file yet.

# %% [markdown]
# ## Tell git about the new file

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git add lakeland.md
# git commit -m "Add lakeland"

# %% [markdown]
# Ok, now we have added the change about Cumbria to the file. Let's publish it to the origin repository.

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git push

# %% [markdown]
# Visit GitHub, and notice this change is on your repository on the server. We could have said `git push origin` to specify the remote to use, but origin is the default.

# %% [markdown]
# ## Changing two files at once

# %% [markdown]
# What if we change both files?

# %% jupyter={"outputs_hidden": false}
# %%writefile lakeland.md
Lakeland  
========   
  
Cumbria has some pretty hills, and lakes too

Mountains:
* Helvellyn

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
Mountains and Lakes in the UK   
===================   
Engerland is not very mountainous.
But has some tall hills, and maybe a
mountain or two depending on your definition.

# %% jupyter={"outputs_hidden": false} language="bash"
# git status

# %% [markdown]
# These changes should really be separate commits. We can do this with careful use of git add, to **stage** first one commit, then the other.

# %% jupyter={"outputs_hidden": false} language="bash"
# git add index.md
# git commit -m "Include lakes in the scope"

# %% [markdown]
# Because we "staged" only index.md, the changes to lakeland.md were not included in that commit.

# %% jupyter={"outputs_hidden": false} language="bash"
# git add lakeland.md
# git commit -m "Add Helvellyn"

# %% jupyter={"outputs_hidden": false} language="bash"
# git log --oneline

# %% jupyter={"outputs_hidden": false} language="bash"
# git push

# %% jupyter={"outputs_hidden": false}
message="""
participant "Cleese's remote" as M
participant "Cleese's repo" as R
participant "Cleese's index" as I
participant Cleese as C

note right of C: nano index.md
note right of C: nano lakeland.md

note right of C: git add index.md
C->I: Add *only* the changes to index.md to the staging area

note right of C: git commit -m "Include lakes"
I->R: Make a commit from currently staged changes: index.md only

note right of C: git add lakeland.md
note right of C: git commit -m "Add Helvellyn"
C->I: Stage *all remaining* changes, (lakeland.md)
I->R: Make a commit from currently staged changes

note right of C: git push
R->M: Transfer commits to Github
"""
wsd(message)
