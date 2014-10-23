---
title: Further Git
---

##Further Git

###Distributed VCS concepts (2)

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

###Solo Workflow

![Working alone with git](session02/figures/distributed_solo)

###Publishing

![Publishing with git](session02/figures/distributed_solo_publishing)

###Teams without conflicts

![Teamworking in git](session02/figures/distributed_shared_noconflict)

###Teams with conflicts

![Teamworking in git with conflicts](session02/figures/distributed_shared_conflicted)


##Git Theory

###A revision Graph

![Revisions form a graph](session02/figures/revisions)

###Git concepts

* Each revision has a parent that it is based on
* These revisions form a graph
* Each revision has a unique hash code
  * In Sue's copy, revision 43 is ab3578d6
  * Jim might think that is revision 38, but it's still ab3579d6
* Branches, tags, and HEAD are labels pointing at revisions
* Some operations (like fast forward merges) just move labels.

###The Levels of Git

![The relationship between the staging area, working directory, and
repositories in git.](session02/figures/distributed_concepts)

##Git Reset

###Reset for understanding

Understanding all the things `git reset` can do requires a good
grasp of git theory.

```
git reset <commit> . #reset index of that path to commit
git reset --soft <commit> #Move branch label to commit
git reset <commit> #Move branch label, and reset index to commit ("--mixed")
git reset --hard <commit> #Move branch label, and reset staging area and index to commit
```

###Stash

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

##Branches

###Working with branches

![Using branches](session02/figures/branching)

###Working with branches in git

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



###Merging branches

``` Bash
git checkout master # Switch to master branch
git checkout mybranch somefolder # Grab code from a branch
git merge experiment # Merge the branch in
git branch -d experiment # Delete branch locally

```

###A good branch strategy

* A `production` branch: code used for active work
* A `develop` branch: for general new code
* `feature` branches: for specific new ideas
* `release` branches: when you share code with others
  * Useful for isolated bug fixes

###Find out what is on a branch

In addition to using `git diff` to compare to the state of a branch,
you can use `git log` to look at lists of commits which are in a branch
and haven't been merged yet.

```bash
git log master..experiment
```

###Referencing multiple commits

Git uses various symbols to refer to sets of commits.
The double dot `A..B` means "ancestor of B and not ancestor of A"

So in a linear sequence, it does what you'd expect.

But in cases where a history has branches, like `master..experiment`
It ends up refering to the unmerged content from the experiment branch.

###Log of differences

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

###Grab changes from a branch

Make some changes on one branch, switch back to another, and use:

``` bash
git checkout <branch> <path>
```

To grab a file from one branch into another.

###Cherry-picking

Using `git checkout` with a path takes the content of files.
To grab the content of a specific *commit* from another branch,
and apply it as a patch to your branch, use:

```bash
git cherry-pick <commit>
git cherry-pick somebranch^^^
```

###Tagging

Easy to read labels for revisions
Produce real results *only* with tagged revisions

``` Bash
git tag -a v1.3
git push --tags
```


##Working with multiple remotes

###Distributed versus centralised

Centralised                      Distributed
------------------               --------------
Server has history               Every user has full history
Your computer has one snapshot   Many local branches
To access history, need internet History always available
You commit to remote server      Users synchronise histories
cvs, subversion(svn)             git, mercurial (hg), bazaar (bzr)

###Centralised VCS concepts

* There is one, linear history of changes on the server or **repository**
* Each revision has a unique, sequential identifier (1,2,3,4...)
* You have a **working copy**
* You **update** the working copy to match the state of the repository
* If someone else has changed the repository while you were working:
  * You update to get their changes
  * You have to **resolve conflicts**
  * Then you commit

###Centralised VCS diagram

![A centralised server with three clients](session02/figures/centralised)

###Distributed VCS in principle

![How distributed VCS works in principle](session02/figures/distributed_principle)

###Distributed VCS in practice

![How distributed VCS works in practice](session02/figures/distributed_practice)

``` Bash
git remote add sue ssh://sue.ucl.ac.uk/somerepo
   # Add a second remote
git remote
   # List available remotes
git push sue
   # Push to a specific remote
   # Default is origin
```

###Referencing remotes

You can always refer to commits on a remote like this:

```
git fetch
git log origin.. #abbreviates origin/master..HEAD
```
Which will show you what you've done that's not in the remote's master.

You need to fetch, to update the local copy of what's happening remotely.

###Remotes and tracking branches

```
git branch -vv
* develop 583fd97 [origin/develop: ahead 1] More git tips and tricks
  master  5732041 [origin/master: behind 2] Add generated pdf
  staging 502fa7b [origin/staging] Copy in notes from old rits training repository
```

Local branches can be, but do not have to be, connected to remote branches
They are said to "track" remote branches

###Publishing branches

To let the server know there's a new branch use:

```
git push --set-upstream origin experiment
```

We use `--set-upstream origin` (Abbreviation `-u`) to tell git that this branch should be pushed to and pulled from origin per default.

You should be able to see your branch in the list of branches in GitHub.

###Sharing branches

``` Bash
git push -u origin experiment # Share a recently
                              # made branch
git push origin experiment #Republish a branch
git branch -r #Discover remote branches
git checkout origin/some_branch #Get a branch
                                #from a remote
```

###Pruning branches

Once you get good at branches, you'll end up with loads.

Some will be on the remote, and tracked locally.
Some will be local only.
Some might be deleted locally, but still on the remote

Deleting local branches is easy:

###Pruning locally

Which local branches are merged?

``` bash
git branch --merged
> deadbranch
> * master
git branch -d deadbranch
  # -D to force removal if not merged
git fetch --prune
  # Remove local branches deleted remotely
```

###Pruning remote branches

``` bash
git push --delete experiment # Delete published branch
git push --prune # Dangerous, remove remote branches deleted locally
```

If using github, I recommend removing branches using the
GitHub gui (click branches, then click "view merged branches")

##Pull Requests

###Forking

If you want to collaborate with someone, you don't need to give them the right to change your code directly.

You can collaborate through *pull requests* instead of by granting them access.

This has been found to work *much better* than having to decide who should be allowed
commit access. You can hit "fork" on any github repo, or git clone from any repo you have access to.

###Send a pull request

When you've done some work on a fork, you'll want it merged into the main version.

The collaborator can send the main repository a pull request, saying:

> Hey, have a look at what I've done, and if you like it, merge it in.

###Accepting a pull request

On GitHub, if a pull request doesn't result in a conflict, there's a big green button that
you can press to accept it.

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

##Hosting Servers

###Hosting a local server

* Any repository can be a remote for pulls
* Can pull/push over shared folders or ssh
* Pushing to someone's working copy is dangerous
* Use `git init --bare` to make a copy for pushing
* You don't need to create a "server"

###Hosting a server in the cloud

GitHub and Bitbucket can be used to create repositories in the cloud.

The materials for this course are [on the web](https://github.com/UCL/rsd-engineeringcourse): you can modify them to build your own course!

You can clone the materials for this course:

``` bash
git clone git@github.com:UCL/rsd-engineeringcourse.git
```

##Hunks

###Git Hunks

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

###Interactive add

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

##Rebasing

###Rebase vs merge

A git *merge* is only one of two ways to get someone else's work into yours.
The other is called a rebase.

In a merge, a revision is added, which brings the branches together. Both histories are retained.
In a rebase, git tries to work out

> What would you need to have done, to make your changes, if your colleague had already made theirs?

Git will invent some new revisions, and the result will be a repository with an apparently linear history.

###An example rebase (Jim)

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
danced and spun in the waves
```

###An example rebase (Sue)

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

###An example rebase (Jim merges)


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

###An example rebase (Jim rebases)

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

###Fast Forwards

When Sue now tries to pull Jim's work, the merge will be a *fast forward*:

Jim's work is now based on Sue's, so moving Sue's repository to be in sync with Jim is
just a question of moving Sue's HEAD label.

###Rebasing pros and cons

Some people like the clean, apparently linear history.
But *rebase rewrites history*.
If you've already pushed, or anyone else has got your changes, things will get screwed up.

If you know your changes are still secret, it might be better to rebase to keep the history clean.
If in doubt, just merge.

###Thousands of tiny commits

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

###Using rebase to squash

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

##Debugging

###Debugging With Git Bisect

You can use

``` bash
git bisect
```

to find out which commit caused a bug.

###Git Bisect Details

``` bash
git bisect start
git bisect good
git bisect bad
git bisect good
git bisect reset
```

Automated Bisect

```
git bisect run py.test
```

###An example repository

In a nice open source example, I found an arbitrary exemplar on github

``` bash
git clone git@github.com:shawnsi/bisectdemo.git
cd bisectdemo
python squares.py 2 # 4
```

This has been set up to break itself at a random commit, and leave you to use
bisect to work out where it has broken:

``` bash
./breakme.sh
```

Which will make a bunch of commits, of which one is broken, and leave you in the broken one

``` bash
python squares.py 2 # Error message

###Getting started with your bisect

``` bash
git bisect start
git bisect bad # We know the current state is broken
git checkout master
git bisect good # Or just git bisect good master
```

Note it needs one known good and one known bad commit to get started

###Solving Manually

``` bash
python squares.py 2
git bisect good #OR bad
python squares.py
git bisect good #OR bad
```

And eventually:

``` bash
git bisect good
> Bisecting: 0 revisions left to test after this (roughly 0 steps)
python squares.py 9
> TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
git bisect bad
> 13cfff692c8c9b9ec3564140c94eb371328cef52 is the first bad commit
> Author: Shawn Siefkas <shawn.siefkas@meredith.com>
> Date:   Thu Nov 14 09:23:55 2013 -0600
> Breaking argument type
git bisect reset
```

###Solving automatically

``` bash
git bisect bad HEAD # We know the current state is broken
git bisect good master
git bisect run python squares.py 2
> 13cfff692c8c9b9ec3564140c94eb371328cef52 is the first bad commit
```


##GitHub pages

###Yaml Frontmatter

GitHub will publish repositories containing markdown as web pages, automatically. 

You'll need to add this content:

> ```
>    ---
>    ---
> ```

A pair of lines with three dashes, to the top of each markdown file. This is how GitHub knows which markdown files to make into web pages.
[Here's why](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter) for the curious. 

###The gh-pages branch

GitHub creates github pages when you use a special named branch.

This is best used to create documentation for a program you write, but you can use it for anything.

``` Bash
git checkout -b gh-pages
git push -u origin gh-pages
```
    
The first time you do this, GitHub takes a few minutes to generate your pages. The website will appear at `http://username.github.com/repositoryname`, for example, here's [mine](http://jamespjh.github.com/jh-ucl-swcarpentry-answers/)

###Markdown Hyperlinks

You can use this syntax

    [link text](URL)
    
To create hyperlinks in your pages, so you can link between your documents. Try it! 

###UCL layout for GitHub pages

You can use GitHub pages to make HTML layouts, here's an [example of how to do it](http://github.com/UCL/ucl-github-pages-example), and [how it looks](http://ucl.github.com/ucl-github-pages-example). We won't go into the detail of this now, but after the class, you might want to try this.


