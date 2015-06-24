---
title: Collaboration
---

##Introduction

### Content Overview

- Introduction to Version Control 
- Working on a local repository 
- Version Control with GitHub
- Collaborative Version Control


### What's version control?

Tool for __managing changes__ to a set of files.

Different __version control systems__: 

- Git 
- Mercurial (`hg`)
- CVS
- Subversion (`svn`)
- ...


### Why use version control?

- Better kind of __backup__.
- Review __history__ ("When did I introduce this bug?").
- Restore older __code versions__.
- Ability to __undo mistakes__.
- Maintain __several versions__ of the code at a time.


### Why use version control? (cont.)

Git is also a __collaborative__ tool:

- "How can I share my code?"
- "How can I submit a change to someone else's code?"
- "How can I merge my work with Sue's?"

-### Git != GitHub
-
-- __Git__: version control system tool to manage source code history.
-
-- __GitHub__: hosting service for Git repositories.

###How do we use version control?

Do some programming, then commit our work:

`my_vcs commit`

Program some more.

Spot a mistake:

`my_vcs rollback`

Mistake is undone.

###What is version control? (Team version)

Sue                | James
------------------ |------   
`my_vcs commit`    | ...
...                | Join the team
...                | `my_vcs checkout`
...                | Do some programming
...                | `my_vcs commit`
`my_vcs update`		 | ...
Do some programming|Do some programming
`my_vcs commit`    | ...
`my_vcs update`    | ...
`my_vcs merge`     | ...
`my_vcs commit`    | ...

###Scope

This course will use the `git` version control system, but much of what you learn will be valid with other version control 
tools you may encounter, including subversion (`svn`) and mercurial (`hg`).


