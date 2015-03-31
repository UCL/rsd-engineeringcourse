---
title: Collaboration
---

##Introduction

### Why use version control?

Version control helps us to manage code:

- maintain backups
- review history ("When did I introduce this bug"?)
- undo mistakes
- keep track of versions

Version control helps us to work collaboratively:

- "How can I share my code?"
- "How can I submit a change to someone else's code?"
- "How can I merge my work with Sue's?"

###How do we use version control?

Do some programming, then commit our work:

`my_vcs commit`

Program some more.

Spot a mistake:

`my_vcs rollback`

Mistake is undone.

###What is version control? (Team version)

Sue                 James
------------------ ------   
`my_vcs commit`     
                    Join the team
                    `my_vcs checkout`
                    Do some programming
                    `my_vcs commit`
`my_vcs update`		
Do some programming Do some programming
`my_vcs commit`
`my_vcs update`
`my_vcs merge`
`my_vcs commit`

###Scope

This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).


