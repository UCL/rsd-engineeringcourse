---
title: Issues
---

##Software Issue Management

###Issues

Code has *bugs*.

It also has things it should do *features*.

A good project has an organised way of managing these.
To do this you should use an Issue Tracker.

###Some Issue Trackers

There are lots of good issue trackers.

The most commonly used open source ones are [Trac](http://trac.edgewall.org/) and [Redmine](http://www.redmine.org/)

Cloud based issue trackers include [Lighthouse](http://lighthouseapp.com/) and [GitHub](https://github.com/blog/831-issues-2-0-the-next-generation)

Commercial solutions include [Jira](https://www.atlassian.com/software/jira)

In this course, we'll use the GitHub issue tracker for our examples.

###Anatomy Of An Issue

* Reporter
* Description
* Owner
* Type [Bug, Feature]
* Component
* Status
* Severity

###Reporting a Bug

The description should make the bug reproducible:

* Version
* Steps

If possible, submit a minimal reproducing code fragment.

###Owning an Issue

* Whoever the issue is assigned to works next
* If an issue needs someone else's work, assign it to them.

###Status 

* Submitted
* Accepted
* Underway
* Blocked


###Resolutions

* Resolved
* Will Not Fix
* Not reproducible
* Not a bug (working as intended)

###Bug Triage

Some organisations use a severity matrix based on:

* Severity [Wrong answer, crash, unusable, workaround, cosmetic...]
* Frequency [All users, most users, some users...]

###The Backlog

The list of all the bugs that need to be fixed or
features that have been requested is called the "backlog".

###Development Cycles

Development goes in *cycles*.

Cycles range in length from a week to three months.

In a given cycle:

* Decide which features should be implemented
* Decide which bugs should be fixed
* Move these issues from the Backlog into the current cycle. (Aka Sprint)



###GitHub issues

GitHub doesn't have separate fields for status, component, severity etc.
Instead, it just has labels, which you can create and delete.

See for example [IPython](https://github.com/ipython/ipython/issues?labels=type-bug&page=1&state=open)
