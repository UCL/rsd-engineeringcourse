---
title: Collaboration
---

##Introduction

###What Version Control is For

* Managing Code Inventory
    * "When did I introduce this bug"?
    * Undoing Mistakes
* Working with other programmers
    * "How can I merge my work with Jim's"

###What is version control?

Do some programming

`my_vcs commit`

Program some more

Realise mistake

`my_vcs rollback`

Mistake is undone

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


