---
title: Git and GitHub
---

##Practicing with Git

###Example Exercise

In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice. 

This could be your research, a hobby of yours, or something else. In the end, we will show you how to display the content of these files as a very simple website. 

###Programming and documents

The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too. 

In later parts of the course, you will use the version control tools you learn today with actual Python code.

###Markdown

The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting. This is the convention used in this file, too. 

You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/UCL/ucl_software_carpentry/blob/master/git/git_instructions.md), and compare the [raw text](https://raw.github.com/UCL/ucl_software_carpentry/master/git/git_instructions.md).

###Displaying Text in this Tutorial

This tutorial is based on use of the Git command line. Commands you can type will look like this:

``` Bash
    echo some output
```

and results you should see will look like this:

> ```
> some output
> ```

Content you should replace with appropriate content related to your example, in your example files, is like this:

> Something about mountains

###Setting up somewhere to work

``` Bash
mkdir my_swcarpentry_solutions/
mkdir my_swcarpentry_solutions/my_swcarpentry_git_solution
cd my_swcarpentry_solutions/my_swcarpentry_git_solution
```

##Solo work

###Configuring Git with your name and email

First, we should configure Git to know our name and email address:

``` Bash
git config --global user.name "Your Name Here"
git config --global user.email "your_email@ucl.ac.uk"
```

###Initialising the repository

Now, we will tell Git to track the content of this folder as a git "repository".

``` Bash
git init
```

> ```
> Initialized empty Git repository in 
> my_swcarpentry_solutions/my_swcarpentry_git_solution`
> ```

As yet, this repository contains no files:

``` Bash
ls output
git status
```

>```
>    # On branch   
>    #  
>    # Initial commit  
>    #  
>    # nothing to commit (create/copy files 
>    #    and use "git add" to track) 
>```

###A first example file

So let's create an example file, and see how to start to manage a history of changes to it. 


``` Bash
vim index.md # Type some content into the file.
cat index.md
```

>    Mountains in the UK   
>    ===================   
>    England is not very mountainous.   
>    But has some tall hills, and maybe a mountain or two depending on your definition.    

###Telling Git about the File

So, let's tell Git that `index.md` is a file which is important, and we would like to keep track of its history:

``` Bash
git add index.md
```
   
Don't forget: Any files in repositories which you want to "track" need to be added with `git add` after you create them.

###Our first commit

Now, we need to tell Git to record the first version of this file in the history of changes:

``` Bash
git commit
```
    
With any luck, an editor has just popped up, into which you can provide a "commit message": a note as to what this revision changes in the file.
    
Set your commit message, save, and quit:

> First commit of discourse on UK topography

And note the confirmation from Git:

> ```
> [master (root-commit) c438f17] First commit of discourse on UK topography  
> 1 file changed, 6 insertions(+)  
> create mode 100644 index.md   
> ```

There's a lot of output there you can ignore for now.

###Configuring Git with your editor

In the setup, you should have told Git where to find your editor, if you haven't,
the previous step didn't work. Do this now:

``` Bash
git config --global core.editor "myeditor"
```

You can find out what you currently have with:

``` Bash
git config --get core.editor
```

e.g. on windows with Notepad++:

``` Bash
git config --global core.editor "'C:/Program Files (x86)/Notepad++
   /notepad++.exe' -multiInst  -nosession -noPlugin"
```

I'm going to be using `vim` as my editor, but you can use whatever editor you prefer. (Windows users could use "Notepad++", Mac users could use "textmate" or "sublime text", linux users could use `vim`, `nano` or `emacs`.)

###Git log

Git now has one change in its history:

``` Bash
git log
```
 
> ```   
>   commit c438f1716b2515563e03e82231acbae7dd4f4656     
>   Author: James Hetherington <j.hetherington@ucl.ac.uk>    
>   Date:   Wed Apr 3 15:32:33 2013 +0100   
>       First commit of discourse on UK topography     
> ```

You can see the commit message, author, and date...

###Hash Codes

The commit "hash code", 

`c438f1716b2515563e03e82231acbae7dd4f4656`

is a unique identifier of that particular revision. 

(This is a really long code, but whenever you need to use it, you can just use the first few characters, however many characters is long enough to make it unique, `c438` for example. )

###Nothing to see here

Note that git will now tell us that our "working directory" is up-to-date with the repository: there are no changes to the files that aren't recorded in the repository history:

``` Bash
git status
```
> ```    
> # On branch master
> # nothing to commit (working directory clean)
> ```

###Making another change

Make a change to the file:

``` Bash
vim index.md
cat index.md
```
    
>    Mountains in the UK  
>    ===================   
>    England is not very mountainous.  
>    But it has some tall hills, and maybe a mountain or two depending on your definition.  
>    Mount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.   

###Unstaged changes

``` Bash
    git status
```

> ```
>    # On branch master  
>    # Changes not staged for commit:  
>    #   (use "git add <file>..." to >
>    # update what will be committed)  
>    #   (use "git checkout -- <file>..." to 
>    # discard changes in working directory)  
>    #  
>    #	modified:   index.md  
>    #   
> ```

We can now see that there is a change to "index.md" which is currently "not staged for commit". What does this mean? 

If we do a `git commit` now *nothing will happen*. 

Git will only commit changes to files that you choose to include in each commit.

This is a difference from other version control systems, where committing will affect all changed files. 

###Staging a file to be included in the next commit

To include the file in the next commit, we have a few choices. This is one of the things to be careful of with git: there are lots of ways to do similar things, and it can be hard to keep track of them all. 

``` Bash
git add --update
```

This says "include in the next commit, all files which have ever been included before". 

Note that `git add` is the command we use to introduce git to a new file, but also the command we use to "stage" a file to be included in the next commit. 

###The staging area

The "staging area" or "index" is the git jargon for the place which contains the list of changes which will be included in the next commit.

You can include specific changes to specific files with git add, commit them, add some more files, and commit them. (You can even add specific changes within a file to be included in the index.)

###The Levels of Git

![The relationship between the staging area, working directory, and
repositories in git.](session02/figures/distributed_concepts_local)


###Review of status

``` Bash
git status
```

> ```
>    # On branch master  
>    # Changes to be committed:  
>    #   (use "git reset HEAD <file>..." to unstage)  
>    #  
>    #	modified:   index.md  
>    #  
> ```

###Commit the mistake

``` Bash
git commit
git log
```

> ```
>    commit 50280520d33592d093773dfd3e5de4c3da7e1a09  
>    Author: James Hetherington 
>    Date:   Wed Apr 3 15:49:02 2013 +0100  
>
>        Add a lie about a mountain  
>
>    commit c438f1716b2515563e03e82231acbae7dd4f4656  
>    Author: James Hetherington 
>    Date:   Wed Apr 3 15:32:33 2013 +0100  
>
>        First commit of discourse on UK topography
> ```

Great, we now have a file which contains a mistake.

###Carry on regardless

In a while, we'll use Git to roll back to the last correct version: this is one of the main reasons we wanted to use version control, after all! But for now, let's do just as we would if we were writing code, not notice our mistake and keep working...

``` Bash
vim index.md
cat index.md
```

>  Mountains and Hills in the UK  

###Commit with a built-in-add

``` Bash
git commit -a
```    

This last command, `git commit -a` automatically adds changes to all tracked files to the staging area, as part of the commit command. So, if you never want to just add changes to some tracked files but not others, you can just use this and forget about the staging area!

###Review of changes

``` Bash
git log | head
```
    
> ```
> commit 0bae9055dca14f659154e1d9a50409751b59aad8 
> Author: James Hetherington <j.hetherington@ucl.ac.uk>  
> Date:   Wed Apr 3 15:55:38 2013 +0100  
>  
>    Change title  
> ```

We now have three changes in the history:
 
``` Bash
git log --oneline
```

> ```
> 0bae905 Change title  
> 5028052 Add a lie about a mountain  
> c438f17 First commit of discourse on UK topography  
> ```

###Git Solo Workflow

![Working alone with git](session02/figures/distributed_solo) 

##Fixing Mistakes

###Reverting
 
Ok, so now we'd like to undo the nasty commit with the lie about Mount Fictional.

    git revert 5028

A commit window pops up, with some default text which you can accept and save. 

###Conflicted reverts

You may, depending on the changes you've tried to make, get an error message here. 

If this happens, it is because git could not automagically decide how to combine the change you made after the change you want to revert, with the attempt to revert the change: this could happen, for example, if they both touch the same line. 

If that happens, you need to manually edit the file to fix the problem. [Skip ahead][Resolving conflicts] or ask a demonstrator to help.

###Review of changes

The file should now contain the change to the title, but not the extra line with the lie. Note the log:

> ```
> commit d6959031d5722cb2b22c408e704e894bce7713e9  
> Author: James Hetherington <j.hetherington@ucl.ac.uk>  
> Date:   Wed Apr 3 16:13:19 2013 +0100  
>    Revert "Add a lie about a mountain"  
>    This reverts commit 50280520d33592d093773dfd3e5de4c3da7e1a09.   
> ```

###Antipatch

Notice how the mistake has stayed in the history.

There is a new commit which undoes the change: this is colloquially called an "antipatch". 
This is nice: you have a record of the full story, including the mistake and its correction.

###Rewriting history

It is possible, in git, to remove the most recent change altogether, "rewriting history". Let's make another bad change, and see how to do this.

###A new lie

``` Bash
vim index.md
cat index.md
```

> Engerland is not very mountainous.  

``` Bash
git commit -a
git log | head
```
> ```
> ...Add a silly spelling    
> ```



###Referring to changes with HEAD and ^

The commit we want to revert to is the one before the latest.

`HEAD^` refers to the commit before the "head", which is the latest change. That is, we want to go back to the change before the current one. 

We could have used the hash code to reference this, but you can also refer to the commit before the `HEAD` as `HEAD^`, the one before that as `HEAD^^`, the one before that as `HEAD~3`.

###Using reset to rewrite history

``` Bash
git reset HEAD^
```

> ```
> Unstaged changes after reset:  
> M	index.md      
> ```

``` Bash
git log --oneline
```
> ```
>    53f4b50 Revert "Add a lie about a mountain" 
>                   This reverts commit 50280520d  
>    0bae905 Change title  
>    5028052 Add a lie about a mountain  
>    c438f17 First commit of discourse on UK topography  
> ```

###Covering your tracks

The silly spelling is gone, and *it isn't even in the log*. This approach to fixing mistakes, "rewriting history" with `reset`, instead of adding an antipatch with `revert` is dangerous, and we don't recommend it. But you may want to do it for small silly mistakes, such as to correct a commit message.

###Resetting the working area

When git reset removes commits, it leaves your working directory unchanged -- so you can keep the work in the bad change if you want. 

If you want to lose the change from the working directory as well, you can do `git reset --hard`. 

I'm going to get rid of the silly spelling, and I didn't do `--hard`, so I'll reset the file from the working directory to be the same as in the index:

``` Bash
git checkout index.md
```

###The Levels of Git

![The relationship between the staging area, working directory, and
repository in git.](session02/figures/distributed_concepts_fixing)    

##Publishing

###Sharing your work

So far, all our work has been on our own computer. But a big part of the point of version control is keeping your work safe, on remote servers. Another part is making it easy to share your work with the world In this example, we'll be using the "GitHub" cloud repository to store and publish our work. 

If you have not done so already, you should create an account on GitHub: go to [https://github.com/](https://github.com/), fill in a username and password, and click on "sign up for free". 

###SSH keys and GitHub

You may want to set things up so that you don't have to keep typing in your password whenever you interact with GitHub via the command line.

You can do this with an "ssh keypair". You may have created a keypair in the Software Carpentry shell training. Go to the [ssh settings page](https://github.com/settings/ssh) on GitHub and upload your public key by copying the content from your computer. (Probably at .ssh/id_rsa.pub)

If you have difficulties, the instructions for this are [on the GitHub website](https://help.github.com/articles/generating-ssh-keys). Ask your demonstrator for help here if you need it.

###Creating a repository

Ok, let's create a repository to store our work. Hit "new repository" on the right of the github home screen, or click [here](https://github.com/new). 

Fill in a short name, and a description. Choose a "public" repository. Don't choose to add a Readme.

###Paying for GitHub

For this software carpentry course, you should use public repositories in your personal account for your example work: it's good to share! GitHub is free for open source, but in general, charges a fee if you want to keep your work private. 

In the future, you might want to keep your work on GitHub private. 

Students can get free private repositories on GitHub, by going to [https://github.com/edu] and filling in a form. 

UCL pays for private GitHub repositories for UCL research groups: you can find the service details on our [web page](../../infrastructure/github.html).

###Adding a new remote to your repository

Instructions will appear, once you've created the repository, as to how to add this new "remote" server to your repository, in the lower box on the screen. Mine say:


```Bash
git remote add origin git@github.com:jamespjh/jh-ucl-swcarpentry-answers.git
git push -u origin master
```

Follow these instructions.

###Remotes

The first command sets up the server as a new `remote`, called `origin`. 

Git, unlike some earlier version control systems is a "distributed" version control system, which means you can work with multiple remote servers. 

Usually, commands that work with remotes allow you to specify the remote to use, but assume the `origin` remote if you don't. 

Here, `git push` will push your whole history onto the server, and now you'll be able to see it on the internet! Refresh your web browser where the instructions were, and you'll see your repository!

###The Levels of Git

![The relationship between the staging area, working directory, and
repository in git.](session02/figures/distributed_concepts_publishing) 

###Distributed VCS With Publishing

![Publishing with git](session02/figures/distributed_solo_publishing)

###Playing with GitHub

Take a few moments to click around and work your way through the GitHub interface. Try clicking on 'index.md' to see the content of the file: notice how the markdown renders prettily.

Click on "commits" near the top of the screen, to see all the changes you've made. Click on the commit number next to the right of a change, to see what changes it includes: removals are shown in red, and additions in green.

##Working with multiple files

###Some new content

So far, we've only worked with one file. Let's add another:

``` Bash
vim lakeland.md
cat lakeland.md
```
 
>    Lakeland  
>    ========   
>  
>    Cumbria has some pretty hills, and lakes too.  

###Git will not by default commit your new file

``` Bash
    git commit -a
```

> ```
>   # On branch master
>    # Untracked files:
>    #   (use "git add <file>..." to 
>    #   include in what will be committed)
>    #
>    #	lakeland.md
>    nothing added to commit but untracked files present 
>     (use "git add" to track)
> ```

This didn't do anything, because we've not told git to track the new file yet.

###Tell git about the new file

``` Bash
git add lakeland.md
git commit -a
```

Ok, now we have added the change about Cumbria to the file. Let's publish it to the origin repository.

``` Bash
git push
```

> ```    
>    Counting objects: 4, done.  
>    Delta compression using up to 8 threads.  
>    Compressing objects: 100% (3/3), done.  
>    Writing objects: 100% (3/3), 343 bytes, done.  
>    Total 3 (delta 0), reused 0 (delta 0)  
>    To git@github.com:jamespjh/
>           jh-ucl-swcarpentry-answers.git  
>       53f4b50..9e8b69c  master -> master    
> ```

Visit GitHub, and notice this change is on your repository on the server. We could have said `git push origin` to specify the remote to use, but origin is the default.

##Editing directly on GitHub

###Editing directly on GitHub

Note that you can also make changes in the GitHub website itself. Visit one of your files, and hit "edit".

Make a change in the edit window, and add an appropriate commit message.

That change now appears on the website, but not in your local copy. (Verify this). 

###Pulling from remotes

To get the change into your local copy, do:

``` Bash
git pull
```
> ```    
>    remote: Counting objects: 5, done.  
>    remote: Compressing objects: 100% (3/3), done.  
>    remote: Total 3 (delta 1), reused 0 (delta 0)  
>    Unpacking objects: 100% (3/3), done.  
>    From github.com:jamespjh/jh-ucl-swcarpentry-answers  
>       9e8b69c..d2a1854  master     -> answers/master  
>    Updating 9e8b69c..d2a1854  
>    Fast-forward  
>     index.md | 8 ++++++++  
>     1 file changed, 8 insertions(+)   
> ```

and check the change is now present on your local version. `git pull` will fetch changes on the server into your local copy: this is important when you are collaborating with others, as we shall see.

###The Levels of Git

![The relationship between the staging area, working directory, and
local and remote repositories in git.](session02/figures/distributed_concepts_sharing)

##Collaboration

###Form a team

Now we're going to get to the most important question of all with Git and GitHub: working with others.

Organise into pairs. You're going to be working on the website of one of the two of you, together, so decide who is going to be the leader, and who the collaborator.

###Distributed VCS in principle

![How distributed VCS works in principle](session02/figures/distributed_principle)

###Distributed VCS in practice

![How distributed VCS works in practice](session02/figures/distributed_practice)

###Giving permission

The leader needs to let the collaborator have the right to make changes to his code.

In GitHub, go to `settings` on the right, then `collaborators` on the left.

Add the user name of your collaborator to the box. They now have the right to push to your repository.

###Obtaining a colleague's code

Next, the collaborator needs to get a copy of the leader's code. Make yourself a space to put it:

``` Bash
cd .. # To get out of your own solution, and 
      # back to a safe place in your working area
mkdir carpentry-collaborations
cd carpentry-collaborations
```

Next, the collaborator needs to find out the URL of the repository: they should go to the leader's repository's GitHub page, and note the URL on the top of the screen. Make sure the "ssh" button is pushed, the URL should begin with `git@github.com`. 

Copy the URL into your clipboard by clicking on the icon to the right of the URL, and then:

``` Bash
   git clone git@github.com:/... #Subsitute the right URL from your clipboard
```

###Nonconflicting changes

Now, both of you should make some changes. To start with, make changes to *different* files. This will mean your work doesn't "conflict". Later, we'll see how to deal with changes to a shared file.

Both of you should commit, but not push.

One of you should now push with `git push`

###Rejected push

The other should then push, but should receive an error message:

> ```
> To git@github.com:jamespjh/
>         jh-ucl-swcarpentry-answers.git  
> ! [rejected]     master -> master (non-fast-forward)  
> error: failed to push some refs to 
>  'git@github.com:jamespjh/
>        jh-ucl-swcarpentry-answers.git'  
> hint: Updates were rejected because 
>      the tip of your current branch is behind  
> hint: its remote counterpart. 
>          Merge the remote changes (e.g. 'git pull')  
> hint: before pushing again.  
> hint: See the 'Note about fast-forwards' 
>       in 'git push --help' for details.  
> ```

Do as it suggests:

    git pull


###Merge commits

Note a window pops up with a suggested default commit message. This commit is special: it is a *merge* commit. It is a commit which combines your collaborator's work with your own.

Now, push again with `git push`. This time it works. If you look on GitHub, you'll now see that it contains both sets of changes.

###Nonconflicted commits to the same file

Go through the whole process again, but this time, both of you should make changes to a single file, but make sure that you don't touch the same *line*. Again, the merge should work as before.

###Sharing without conflicts

![Teamworking in git](session02/figures/distributed_shared_noconflict)

###Conflicting commits

Finally, go through the process again, but this time, make changes which touch the same line.

When you pull, instead of offering a commit message, it says:

> ```
> CONFLICT (content): Merge conflict in index.md  
> Automatic merge failed; fix conflicts
>    and then commit the result.  
> ```

###Resolving conflicts

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

Manually edit the file, to combine the changes as seems sensible and get rid of the symbols.

###Commit the resolved file

Now commit the merged result:

    git commit -a      
    
A suggested commit message appears, which you can accept, and then you can `push` the merged result. Check everything is fine on GitHub.

###A revision graph

![Revisions form a graph](session02/figures/revisions)

###Distributed VCS in teams with conflicts

![Teamworking in git with conflicts](session02/figures/distributed_shared_conflicted)

###The Levels of Git

![The relationship between the staging area, working directory, and
local and remote repositories in git.](session02/figures/distributed_concepts_all)

##Social Coding

###GitHub as a social network

In addition to being a repository for code, and a way to publish code, GitHub is a social network.  

You can follow the public work of other coders: go to the profile of your collaborator in your browser, and it the "follow" button. 

[Here's mine](https://github.com/jamespjh) : if you want to you can follow me.

Using GitHub to build up a good public profile of software projects you've worked on is great for your CV!

