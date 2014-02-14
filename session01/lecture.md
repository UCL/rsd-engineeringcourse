% Collaborating and Managing Code
% James Hetherington

Git Reminder
============

Distributed VCS concepts (2)
----------------------------

* You have a *working copy*
* You pick a subset of the changes in your working copy
  to add to the next commit
* Changes to be included in the next commit are kept in a
  **staging area** (a.k.a. **index**)
* When you commit you commit:
  * From the staging area
  * To the local repository
* You **push** to **remote** repositories to share or publish
* You **pull** (or fetch) to bring in changes from a remote

Solo Workflow
-----------------------------

![Working alone with git](assets/distributed_solo)

Publishing
-------------------------------

![Publishing with git](assets/distributed_solo_publishing)

Teams without conflicts
------------------------------------------

![Teamworking in git](assets/distributed_shared_noconflict)

Teams with conflicts
------------------------------------------

![Teamworking in git with conflicts](assets/distributed_shared_conflicted)


Git Theory
==========

A revision Graph
----------------

![Revisions form a graph](assets/revisions)

Git concepts
------------------------

* Each revision has a parent that it is based on
* These revisions form a graph
* Each revision has a unique hash code
  * In Sue's copy, revision 43 is ab3578d6
  * Jim might think that is revision 38, but it's still ab3579d6
* Branches, tags, and HEAD are labels pointing at revisions
* Some operations (like fast forward merges) just move labels.

The Levels of Git
----------------

![The relationship between the staging area, working directory, and
repositories in git.](assets/distributed_concepts)

Git Reset
=========

Reset for understanding
-----------------------

Understanding all the things `git reset` can do requires a good
grasp of git theory.

```
git reset <commit> . #reset index of that path to commit
git reset --soft <commit> #Move branch label to commit
git reset <commit> #Move branch label, and reset index to commit ("--mixed")
git reset --hard <commit> #Move branch label, and reset staging area and index to commit
```

Branches
========

Working with branches
---------------------

![Using branches](assets/branching)

Working with branches in git
----------------------------

``` Bash
git branch # Tell me what branches exist
```
```
   * master # Asterisk tells me which one
     experiment # I am currently on
```
``` Bash
git checkout -b somebranch # Make a new branch
git checkout master # Switch to an existing branch
```

Sharing branches
----------------

``` Bash
git push -u origin experiment # Share a recently
                              # made branch
git push origin experiment #Republish a branch
git branch -r #Discover remote branches
git checkout origin/some_branch #Get a branch
                                #from a remote
```

Merging branches
----------------

``` Bash
git checkout master # Switch to master branch
git checkout mybranch somefolder # Grab code from a branch
git merge experiment # Merge the branch in
git branch -d experiment # Delete branch locally
git push --delete experiment # Delete published branch
```

A good branch strategy
----------------------

* A `production` branch: code used for active work
* A `develop` branch: for general new code
* `feature` branches: for specific new ideas
* `release` branches: when you share code with others
  * Useful for isolated bug fixes

Working with multiple remotes
=============================

Distributed versus centralised
------------------------------

Centralised                      Distributed
------------------               --------------
Server has history               Every user has full history
Your computer has one snapshot   Many local branches
To access history, need internet History always available
You commit to remote server      Users synchronise histories
cvs, subversion(svn)             git, mercurial (hg), bazaar (bzr)

Centralised VCS concepts
------------------------

* There is one, linear history of changes on the server or **repository**
* Each revision has a unique, sequential identifier (1,2,3,4...)
* You have a **working copy**
* You **update** the working copy to match the state of the repository
* If someone else has changed the repository while you were working:
  * You update to get their changes
  * You have to **resolve conflicts**
  * Then you commit

Centralised VCS diagram
-----------------------

![A centralised server with three clients](assets/centralised)

Distributed VCS in principle
----------------------------

![How distributed VCS works in principle](assets/distributed_principle)

Distributed VCS in practice
----------------------------

![How distributed VCS works in practice](assets/distributed_practice)

``` Bash
git remote add sue ssh://sue.ucl.ac.uk/somerepo
   # Add a second remote
git remote
   # List available remotes
git push sue
   # Push to a specific remote
   # Default is origin
```



Hosting Servers
===============

Hosting a local server
----------------------

* Any repository can be a remote for pulls
* Can pull/push over shared folders or ssh
* Pushing to someone's working copy is dangerous
* Use `git init --bare` to make a copy for pushing
* You don't need to create a "server"

Hosting a server in the cloud
-----------------------------

GitHub and Bitbucket can be used to create repositories in the cloud.

The materials for this course are [on the web](https://github.com/UCL/rsd-engineeringcourse): you can modify them to build your own course!

You can clone the materials for this course:

``` bash
git clone git@github.com:UCL/rsd-engineeringcourse.git
```

Conflicts
=========

Conflicts
---------

Content from different branches or remotes, when merged, can *conflict*.

When you pull, instead of offering a commit message, it says:

> ```
> CONFLICT (content): Merge conflict in index.md  
> Automatic merge failed; fix conflicts
>    and then commit the result.  
> ```

Resolving conflicts
-------------------

Git couldn't work out how to merge the two different sets of changes.

You now need to manually resolve the conflict.

Edit the file. It should look something like this:

> ```
>     <<<<<<< HEAD  
>     Wales is hillier than England, 
>             but not quite as hilly as Scotland.  
>     =======  
>     Wales is much hillier than England, 
>             but not as hilly as Scotland.  
>     >>>>>>> dba9bbf3bcab1008b4d59342392cc70890aaf8e6
> ```  

The syntax with `<<<` `===` and `>>>` shows the differences. 

To resolve a conflict, you must manually edit the file, 
to combine the changes as seems sensible and get rid of the symbols.

Next you must add and commit the merged result:

    git commit -a      
    
A suggested commit message appears, which you can accept, and then you can `push` the merged result.

Tagging
=======

Easy to read labels for revisions
Produce real results *only* with tagged revisions

``` Bash
git tag -a v1.3
git push --tags
```

Hunks
=====

Git Hunks
---------

A "Hunk" is one git change. This changeset has three hunks:

``` diff
+import matplotlib
+import numpy as np
 
 from matplotlib import pylab
 from matplotlib.backends.backend_pdf import PdfPages

+def increment_or_add(key,hash,weight=1):
+       if key not in hash:
+               hash[key]=0
+       hash[key]+=weight
+
 data_path=os.path.join(os.path.dirname(
                        os.path.abspath(__file__)),
-regenerate=False
+regenerate=True
```

Interactive add
---------------

`git add` and `git reset` can be used to stage/unstage a whole file,
but you can use interactive mode to stage by hunk, choosing
yes or no for each hunk.

```
git add -p myfile.py

```
``` diff
+import matplotlib
+import numpy as np
#Stage this hunk [y,n,a,d,/,j,J,g,e,?]?
```

Rebasing
========

Rebase vs merge
---------------

A git *merge* is only one of two ways to get someone else's work into yours.
The other is called a rebase.

In a merge, a revision is added, which brings the branches together. Both histories are retained.
In a rebase, git tries to work out

> What would you need to have done, to make your changes, if your colleague had already made theirs?

Git will invent some new revisions, and the result will be a repository with an apparently linear history.

An example rebase (Jim)
---------------------

Initial state:

Revision ab34:

```
It was clear and cold,
and the slimy monsters
```

Revision de56, child of ab34:

```
It was clear and cold,
and the slimy monsters
danced and span in the waves
```

An example rebase (Sue)
---------------------

Revision ab34:

```
It was clear and cold,
and the slimy monsters
```

Revision aj72, child of ab34:

```
'Twas brillig, 
and the slithy toves
```

An example rebase (Jim merges)
------------------------------


```bash
git pull sue
```

Revision ab34:

```
It was clear and cold,
and the slimy monsters
```

Revision de56, child of ab34:

```
It was clear and cold,
and the slimy monsters
danced and span in the waves
```



Revision kp42, child of de56 and of aj72:

```
'Twas brillig, 
and the slithy toves
danced and span in the waves
```

An example rebase (Jim rebases)
------------------------------

```bash
git pull sue --rebase 
# or git rebase mybranch
```

Revision ab34:

```
It was clear and cold,
and the slimy monsters
```

Revision aj72, child of ab34:

```
'Twas brillig, 
and the slithy toves
```

Revision lz46, child of aj72:

```
'Twas brillig, 
and the slithy toves
danced and span in the waves
```

Fast Forwards
-------------

When Sue now tries to pull Jim's work, the merge will be a *fast forward*:

Jim's work is now based on Sue's, so moving Sue's repository to be in sync with Jim is
just a question of moving Sue's HEAD label.

Rebasing pros and cons
----------------------

Some people like the clean, apparently linear history.
But *rebase rewrites history*.
If you've already pushed, or anyone else has got your changes, things will get screwed up.

If you know your changes are still secret, it might be better to rebase to keep the history clean.
If in doubt, just merge.

Thousands of tiny commits
------------------------------

A common use of rebase is to rebase your work on top of one of your earlier commits,
in interactive mode, to "squash" several commits that should really be one:

``` bash
git log
```
```
ab11 A great piece of work
de73 Fix a typo
ll54 Fix another typo
```

Using rebase to squash
----------------------

``` bash
git rebase -i ab11 #OR HEAD^^
```

```
pick ab11 A great piece of work
pick de73 Fix a typo
pick ll54 Fix another typo

# Rebase 60709da..30e0ccb onto 60709da
#
# Commands:
#  p, pick = use commit
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
```

Exercises
=========

Catch-up exercises
==================

If you've not done the GitHub exercises from UCL Software Carpentry, then get together with a partner who is in the same boat,
and work through [those exercises](http://development.rc.ucl.ac.uk/training/carpentry/git.html#example-exercise) as far as [pulling from remotes](http://development.rc.ucl.ac.uk/training/carpentry/git.html#pulling-from-remotes) and then do the section on [Collaboration](http://development.rc.ucl.ac.uk/training/carpentry/git.html#collaboration) as far as [Commit the resolved file](http://development.rc.ucl.ac.uk/training/carpentry/git.html#commit-the-resolved-file)

Further Exercises
=================

Interactive add
---------------

Use
```
git add -p somefile #Add by hunk 
git add -i #Consider files interactively
```

To decide what to add interactively.

Create a branch
---------------

In your test repository, make yourself a branch.

```bash
git checkout -b mybranch
git branch
```

Switch branches
---------------

Make some changes to it, and try to switch back to the main branch
(You won't be able to do so if there are uncommitted changes.)

```bash
git checkout master
git commit -a
git checkout master
```

Stash some changes
------------------

If you find you want to switch branch, or pull, but you're not ready to commit,
you can use

```bash
git stash
git checkout master
...
git checkout mybranch
git stash apply
```

The "Stash" is a way of temporarily saving your working area, and can help out in a pinch.

Merge your branch
-----------------

Once you're back on the main branch, try merging in your branch

``` bash
git merge mybranch
```

Find out what is on a branch
----------------------------

In addition to using `git diff` to compare to the state of a branch,
you can use `git log` to look at lists of commits which are in a branch
and haven't been merged yet.

```bash
git log master..experiment
```

Referencing multiple commits
----------------------------

Git uses various symbols to refer to sets of commits.
The double dot `A..B` means "ancestor of B and not ancestor of A"

So in a linear sequence, it does what you'd expect.

But in cases where a history has branches, like `master..experiment`
It ends up refering to the unmerged content from the experiment branch.

Log of differences
------------------

``` bash
git log --left-right master...experiment
```

```
< ab34 A commit on master but not experiment
< d63e ditto
> l6mn A commit on experiment but not on master
```

Three dots means "everything which is not a common ancestor".

It therefore will show the differences between branches.

Grab changes from a branch
--------------------------

Make some changes on one branch, switch back to another, and use:

``` bash
git checkout <branch> <path>
```

To grab a file from one branch into another.

Cherry-picking
--------------

Using `git checkout` with a path takes the content of files.
To grab the content of a specific *commit* from another branch, 
and apply it as a patch to your branch, use:

```bash
git cherry-pick <commit>
git cherry-pick somebranch^^^
```

Creating servers
================

File system servers
-------------------

Try working with multiple remotes by making another server for yourself on your local computer.

``` bash
cd <somewhere else>
mkdir myotherrepo
cd myotherrepo
git init --bare
cd <back to my main repository>
git remote add localbackup /full/path/to/local/repository
git push localbackup
```

You can now work with this local repository, just as with any other git server.
If you have a colleague on a shared file system, you can use this approach to collaborate through that file system.

SSH servers
-----------

Try creating a server for yourself using a machine you can SSH to:

```
ssh <mymachine>
mkdir mygitserver
cd mygitserver
git init --bare
exit
git remote add <somename> ssh://user@host/mygitserver
git push
```

Referencing remotes
-------------------

You can always refer to commits on a remote like this:

```
git fetch
git log origin.. #abbreviates origin/master..HEAD
```
Which will show you what you've done that's not in the remote's master.

You need to fetch, to update the local copy of what's happening remotely.

Remotes and tracking branches
-----------------------------

```
git branch -vv
* develop 583fd97 [origin/develop: ahead 1] More git tips and tricks
  master  5732041 [origin/master: behind 2] Add generated pdf
  staging 502fa7b [origin/staging] Copy in notes from old rits training repository
```

Local branches can be, but do not have to be, connected to remote branches
They are said to "track" remote branches

Publishing branches
-------------------

Let the server know there's a new branch with:

```
git push --set-upstream origin experiment
```

We use `--set-upstream origin` (Abbreviation `-u`) to tell git that this branch should be pushed to and pulled from origin per default.

You should be able to see your branch in the list of branches in GitHub.

Pull Requests
=============

Forking
-------

If you want to collaborate with someone, but you don't want to give them the right to change your code directly, you can collaborate through *pull requests* instead of by granting them access.

For this exercise, you should find a partner, who has a repository on GitHub. The example repository from the software carpentry exercises will do. This time, the collaborator, instead of pulling the leader's code, should *fork* it. Go to the repository on GitHub, and hit "fork" top right.

A new repository will be created on the collaborator's account, which contains all the same stuff. Clone it with `git clone`.

Pushing to your forks
---------------------

Both of you can make changes.

Now, both of you will be able to push: you're pushing to different repositories!
 
Create a pull request
---------------------

You need to request that the leader accept your changes. The collaborator should go to the page for their *forked* repository and hit the green button to the left of the branch dropdown. On the page that appears, choose "compare across forks".

Choose the right branches and repositories for the "base", the leader's repository, and the "head repo", the collaborator's repository. Ask a demonstrator for help if this is confusing. 

Hit "Click to create a pull request for this comparison".

Give the request a title and a comment, and send it.  

Note you can comment on and discuss the contribution using the pull request: this is great for open source projects with many people working together.

Accepting a pull request
------------------------

The leader should now see a link to the pull request on their github home page. Have a read through the changes, and if you think it's fine, then merge it, using the big green button. The button only appears if GitHub can 
work out how to merge the fork without conflicts.

If that works, make some more changes, with new pull requests, until you get a conflicted merge, and there's no nice green merge button.

Accepting a conflicted pull request
-----------------------------------

If there's a conflict, there won't be a big green button.

Instead, the leader needs to get hold of the collaborators' code, and merge it in manually.

To do this, you need to add the collaborator's fork in your repository as a *second remote*

``` bash
git remote add <remotename> <collaborators URL>
git pull remotename
# resolve conflicts
git commit -a
git push
```

Rebasing and squashing
======================

Rebasing
--------

Get together with a partner, or use a branch or a remote of your own, and set yourself up a
situation where you'd be about to merge. Instead, use a rebase.

Use `git log --graph --oneline` to see how the changes have been applied as a linear sequence.

Squashing
---------

Make several commits which should really be one, then use

```bash
git rebase -i <commit>
```
to squash them.

