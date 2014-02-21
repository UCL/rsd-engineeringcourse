
Exercises
=========

Catch-up exercises
------------------

If you've not done the GitHub exercises from UCL Software Carpentry, then get together with a partner who is in the same boat,
and work through [those exercises](http://development.rc.ucl.ac.uk/training/carpentry/git.html#example-exercise) as far as [pulling from remotes](http://development.rc.ucl.ac.uk/training/carpentry/git.html#pulling-from-remotes) and then do the section on [Collaboration](http://development.rc.ucl.ac.uk/training/carpentry/git.html#collaboration) as far as [Commit the resolved file](http://development.rc.ucl.ac.uk/training/carpentry/git.html#commit-the-resolved-file)

Further Git Exercises
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

Practice with stash. Make some changes, then:

```bash
git stash
git checkout master
...
git checkout mybranch
git stash apply
```

Merge your branch
-----------------

Once you're back on the main branch, try merging in your branch

``` bash
git checkout master
git merge mybranch
```

Further local experiments
-------------------

Make various more changes, and check you can effectively use

``` bash
git cherry-pick
git log master..<branch>
git checkout <branch> file
```



Creating Git Servers
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

Branches and remotes
--------------------

Make sure you know how to manage sharing branches with a remote, using commands like:

``` bash
git push -u <remote> <branch>
git branch -r #Discover remote branches
git branch -vv #Compare local branches to remotes
git checkout origin/some_branch #Get a branch
                                #from a remote
git push --delete experiment # Delete published branch
```

Pull Requests
-------------

Find a partner, who has a repository on GitHub. The example repository from the software carpentry exercises will do. This time, the collaborator, instead of pulling the leader's code, should *fork* it. Go to the repository on GitHub, and hit "fork" top right.

A new repository will be created on the collaborator's account, which contains all the same stuff. Clone it with `git clone`.
 
Creating a pull request
---------------------

Make some changes on your fork. 

You need to request that the leader accept your changes. The collaborator should go to the page for their *forked* repository and hit the green button to the left of the branch dropdown. On the page that appears, choose "compare across forks".

Choose the right branches and repositories for the "base", the leader's repository, and the "head repo", the collaborator's repository. Ask a demonstrator for help if this is confusing. 

Hit "Click to create a pull request for this comparison".

Give the request a title and a comment, and send it.  

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

However, if the merge is hard, it's common to ask the contributor to pull from the main version into their fork.
Then, once their merge is done, the merge back should be a fast-forward.

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

Git Bisect
======

An example repository
---------------------

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

Getting started with your bisect
--------------------------------

``` bash
git bisect start
git bisect bad # We know the current state is broken
git checkout master
git bisect good # Or just git bisect good master
```

Note it needs one known good and one known bad commit to get started

Solving Manually
----------------

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

Solving automatically
---------------------

``` bash
git bisect bad HEAD # We know the current state is broken
git bisect good master
git bisect run python squares.py 2
> 13cfff692c8c9b9ec3564140c94eb371328cef52 is the first bad commit
```

Issue Tracking
==============

Issue Tracking Exercise
-----------------------

In GitHub, log an example issue for a bug in some software you are working on or use,
and also for a feature request.

Think about reproduction steps.

Discuss the issues with a partner.

Licensing
=========

Licensing
---------

Discuss software licensing and citation issues with your neighbours.