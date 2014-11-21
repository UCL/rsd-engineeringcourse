---
title: Further Git
---

## Further Git
### More complex codes require more careful management.

We're now starting to work with more complicated projects, with work running on several strands.

Mistakes are becoming more common. We need to take our understanding of Git up a notch.

First, a recap:

###Distributed VCS concepts

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




