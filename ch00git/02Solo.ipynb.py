# ---
# jupyter:
#   jekyll:
#     display_name: Solo Git
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Solo work with Git

# %% [markdown]
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook

# %% [markdown]
# So, we're in our git working directory:

# %% jupyter={"outputs_hidden": false}
import os
top_dir = os.getcwd()
git_dir = os.path.join(top_dir, 'learning_git')
working_dir = os.path.join(git_dir, 'git_example')
os.chdir(working_dir)
working_dir

# %% [markdown]
# ## A first example file
#
# So let's create an example file, and see how to start to manage a history of changes to it.

# %% [markdown]
#     <my editor> index.md # Type some content into the file.

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
Mountains in the UK   
===================   
England is not very mountainous.   
But has some tall hills, and maybe a mountain or two depending on your definition.


# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false}
# cat index.md

# %% [markdown]
# ## Telling Git about the File
#
# So, let's tell Git that `index.md` is a file which is important, and we would like to keep track of its history:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git add index.md

# %% [markdown]
# Don't forget: Any files in repositories which you want to "track" need to be added with `git add` after you create them.
#
# ## Our first commit
#
# Now, we need to tell Git to record the first version of this file in the history of changes:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git commit -m "First commit of discourse on UK topography"

# %% [markdown]
# And note the confirmation from Git.
#
# There's a lot of output there you can ignore for now.

# %% [markdown]
# ## Configuring Git with your editor
#
# If you don't type in the log message directly with -m "Some message", then an editor will pop up, to allow you
# to edit your message on the fly.

# %% [markdown]
# For this to work, you have to tell git where to find your editor.

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": true} language="bash"
# git config --global core.editor nano

# %% [markdown]
# You can find out what you currently have with:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git config --get core.editor

# %% [markdown]
# To configure VS Code on your operating system you'll need something like the below, ask a demonstrator to help for your machine.

# %% [markdown] attributes={"classes": [" Bash"], "id": ""}
# ``` bash
# $ git config --global core.editor "code --wait"
# ```

# %% [markdown]
# I'm going to be using `nano` as my editor, but you can use whatever editor you prefer. Find how to setup your favourite editor in [the setup chapter of Software Carpentry's Git lesson](https://swcarpentry.github.io/git-novice/02-setup.html).

# %% [markdown]
# ## Git log
#
# Git now has one change in its history:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log

# %% [markdown]
# You can see the commit message, author, and date...

# %% [markdown]
# ## Hash Codes
#
# The commit "hash code", e.g.
#
# `c438f1716b2515563e03e82231acbae7dd4f4656`
#
# is a unique identifier of that particular revision. 
#
# (This is a really long code, but whenever you need to use it, you can just use the first few characters, however many characters is long enough to make it unique, `c438` for example. )

# %% [markdown]
# ## Nothing to see here
#
# Note that git will now tell us that our "working directory" is up-to-date with the repository: there are no changes to the files that aren't recorded in the repository history:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git status

# %% [markdown]
# Let's edit the file again:
#
#     nano index.md

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
Mountains in the UK   
===================   
England is not very mountainous.   
But has some tall hills, and maybe a mountain or two depending on your definition.

Mount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.


# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false}
# cat index.md

# %% [markdown]
# ## Unstaged changes

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git status

# %% [markdown]
# We can now see that there is a change to "index.md" which is currently "not staged for commit". What does this mean? 
#
# If we do a `git commit` now *nothing will happen*. 
#
# Git will only commit changes to files that you choose to include in each commit.
#
# This is a difference from other version control systems, where committing will affect all changed files. 

# %% [markdown]
# We can see the differences in the file with:

# %% jupyter={"outputs_hidden": false} language="bash"
# git diff

# %% [markdown]
# Deleted lines are prefixed with a minus, added lines prefixed with a plus.

# %% [markdown]
# ## Staging a file to be included in the next commit
#
# To include the file in the next commit, we have a few choices. This is one of the things to be careful of with git: there are lots of ways to do similar things, and it can be hard to keep track of them all.

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": true} language="bash"
# git add --update

# %% [markdown]
# This says "include in the next commit, all files which have ever been included before". 
#
# Note that `git add` is the command we use to introduce git to a new file, but also the command we use to "stage" a file to be included in the next commit. 

# %% [markdown]
# ## The staging area
#
# The "staging area" or "index" is the git jargon for the place which contains the list of changes which will be included in the next commit.
#
# You can include specific changes to specific files with `git add`, commit them, add some more files, and commit them. (You can even add specific changes within a file to be included in the index.)

# %% [markdown]
# ## Message Sequence Charts

# %% [markdown]
# In order to illustrate the behaviour of Git, it will be useful to be able to generate figures in Python
# of a "message sequence chart" flavour.

# %% [markdown]
# There's a nice online tool to do this, called "[Web Sequence diagrams](https://www.websequencediagrams.com)".

# %% [markdown]
# Instead of just showing you these diagrams, I'm showing you in this notebook how I make them.
# This is part of our "reproducible computing" approach; always generating all our figures from code.

# %% [markdown]
# Here's some quick code in the Notebook to download and display an MSC illustration, using the Web Sequence Diagrams API:

# %% jupyter={"outputs_hidden": false}
# %%writefile wsd.py
import requests
import re
import IPython

def wsd(code):
    response = requests.post("http://www.websequencediagrams.com/index.php", data={
            'message': code,
            'apiVersion': 1,
        })
    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(response.text)
    if m == None:
        print("Invalid response from server.")
        return False
                            
    image=requests.get("http://www.websequencediagrams.com/" + m.group(0))
    return IPython.core.display.Image(image.content)


# %% jupyter={"outputs_hidden": false}
from wsd import wsd
# %matplotlib inline
wsd("Sender->Recipient: Hello\n Recipient->Sender: Message received OK")

# %% [markdown]
# ## The Levels of Git

# %% [markdown]
# Let's make ourselves a sequence chart to show the different aspects of Git we've seen so far:

# %% jupyter={"outputs_hidden": false}
message="""
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
"""
wsd(message)

# %% [markdown]
# ## Review of status

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git status

# %% jupyter={"outputs_hidden": false} language="bash"
# git commit -m "Add a lie about a mountain"

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log

# %% [markdown]
# Great, we now have a file which contains a mistake.

# %% [markdown]
# ## Carry on regardless
#
# In a while, we'll use Git to roll back to the last correct version: this is one of the main reasons we wanted to use version control, after all! But for now, let's do just as we would if we were writing code, not notice our mistake and keep working...

# %% [markdown]
# ```bash
# nano index.md
# ```

# %% jupyter={"outputs_hidden": false}
# %%writefile index.md
Mountains and Hills in the UK   
===================   
England is not very mountainous.   
But has some tall hills, and maybe a mountain or two depending on your definition.

Mount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.


# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false}
# cat index.md

# %% [markdown]
# ## Review of changes

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log | head

# %% [markdown]
# We now have three changes in the history:

# %% attributes={"classes": [" Bash"], "id": ""} jupyter={"outputs_hidden": false} language="bash"
# git log --oneline

# %% [markdown]
# ## Git Solo Workflow

# %% [markdown]
# We can make a diagram that summarises the above story:

# %% jupyter={"outputs_hidden": false}
message="""
participant "Cleese's repo" as R
participant "Cleese's index" as I
participant Cleese as C

note right of C: nano index.md

note right of C: git init
C->R: create

note right of C: git add index.md

C->I: Add content of index.md

note right of C: git commit
I->R: Commit content of index.md

note right of C:  nano index.md

note right of C: git add --update
C->I: Add content of index.md
note right of C: git commit -m "Add a lie"
I->R: Commit change to index.md
"""
wsd(message)
