---
title: Comments
---

##Comments

###Why comment?

* You're writing code for people, as well as computers.
* Comments can help you build code, by respresenting your design
* Comments explain subtleties in the code which are not obvious from the syntax
* Comments explain *why* you wrote the code the way you did

###Bad Comments

"I write good code, you can tell by the number of comments."

This is wrong.

###Comments which are obvious

{{pyfrag('05','comments','obvious')}}

###Comments which could be replaced by better style

{{pyfrag('05','comments','style1')}}

Is good. But:

{{pyfrag('05','comments','style2')}}

is probably better.

###Comments vs expressive code 

> The proper use of comments is to compensate for our failure to express yourself in code. 
Note that I used the word failure. I meant it. Comments are always failures.

-- Robert Martin, [Clean Code](http://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882).

I wouldn't disagree, but still, writing "self-documenting" code is very hard, so do comment if you're unsure!

###Comments which belong in an issue tracker

{{pyfrag('05','comments','issues')}}

BUT comments that reference issues in the tracker can be good.

E.g.

{{pyfrag('05','comments','issuesOK')}}

is OK.

###Comments which only make sense to the author today

{{pyfrag('05','comments','selfish')}}

###Comments which are unpublishable

{{pyfrag('05','comments','rude')}}

##Good comments

###Pedagogical comments

Code that *is* good style, but you're not familiar with, or 
that colleagues might not be familiar with

{{pyfrag('05','comments','teaching')}}

###Other good comments

Comments which explain coding definitions or reasons for programming choices.
{{pyfrag('05','comments','other')}}

