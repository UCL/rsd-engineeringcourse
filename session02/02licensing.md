---
title: Licensing
---

##Software Licensing

###This course

This course is distributed under the CC-BY license.
Which means you can modify it, and use it to teach your own course,
so long as you credit UCL RITS.

###Disclaimer

I'm going to attempt to give some basic advice on software license choice.

But:

* I am NOT A LAWYER
* Everyone's opinion differs (And flamewars are boring)

If you care, read the [O'Reilly book](http://www.amazon.co.uk/Understanding-Open-Source-Software-Licensing-ebook/dp/B0026OR3J4/ref=tmm_kin_title_0).

This training does not constitute legal advice.

Your department, or UCL, may have policies about applying licenses to code you create while a UCL employee or student.
This training doesn't address this issue, and does not represent UCL policy -- 
seek advice from your supervisor or manager if concerned.

###Have a License File

The most important thing is that you should always choose a license,
even if it is a traditional (C) all rights reserved,
and create a *license file* to tell people what it is.

GitHub will offer to do this automatically when you create a new repository.

Your license file should typically be called LICENSE.txt or similar.

[This course has one](https://github.com/UCL/rsd-engineeringcourse/blob/master/LICENSE.md)

License files are important to let people know whether they can reuse your code, and
under what terms.

###Open source doesn't stop you making money

The most important misconception about open source software is the thought that
open source means you can't make any money.

This is *wrong*.

Plently of people open source their software and sell:

* The software under a different license e.g. [Saxon](http://saxon.sourceforge.net/)
* Consulting e.g. [Continuum](http://continuum.io/consulting) who help maintain NumPy
* Manuals e.g. [VTK](http://www.vtk.org/)
* Add-ons e.g. [Puppet](http://puppetlabs.com/puppet/enterprise-vs-open-source)
* Server software which open source client software talks to e.g. [GitHub API clients](https://github.com/octokit/octokit.rb)

###Plagiarism vs Self-promotion

Many researchers worry about people stealing their work, if they open source their code.

Often, your biggest problem is not theft, but the fact no one is aware of your work.

Open source is a great way to increase the slim probabilty that someone else on the planet will care
about your work enough to cite you.

So when thinking about whether to open source your code, think about whether you're more worried about
anonymity or theft.

###Your code *is* good enough

New coders worry that they'll be laughed at if they put their code online.

Don't worry. Everyone, including people who've been coding for decades, 
writes shoddy code that is full of bugs.

The only thing that will make your code better, is *other people reading it*. 

For small scripts that no one but you will ever use,
my recommendation is to use an open repository anyway. 
Find a buddy, and get them to comment on it.

###Worry about license compatibility and proliferation

Not all open source code can be used in all projects.

Some licenses are legally incompatible.

This is a huge and annoying problem. 
As an author, you might not care, but you can't anticipate the exciting uses people might find by
mixing your code with someone else's. 

Use a standard license from the small list that are well-used.
Then people will understand. *Don't make up your own*.

When you're about to use a license, see if there's a more common one which is recommended, e.g.:
using the [opensource.org proliferation report](http://opensource.org/proliferation-report)

###Academic License Proliferation

Academics often write their own license terms for their software.

For example:

>XXXX NON-COMMERCIAL EDUCATIONAL LICENSE
>Copyright (c) 2013 Prof. Foo.
>All rights reserved.
>
>You may use and modify this software for any non-commercial purpose within your educational 
>institution. Teaching, academic research, and personal experimentation are examples of purpose 
>which can be non-commercial.
>
>You may redistribute the software and modifications to the software for non-commercial 
>purposes, but only to eligible users of the software (for example, to another university
>student or faculty to support joint academic research).

###Academic License Proliferation

Please don't do this. Your desire to slightly tweak the terms is harmful to the
future software ecosystem. Also, 

* Unless you are a lawyer, you cannot do this safely!*

###Licenses for Code, Content, and Data.

Licenses designed for code should not be used to license data or prose.

Don't use Creative Commons for software, or GPL for a book.

###Licensing issues

* Permissive vs Share-Alike
* Noncommercial and Academic Use Only
* Patents
* Use as a web service

###Permissive vs Share-Alike

Some licenses require all derived software to be licensed under terms that are similarly free.
Such licenses are called "Share Alike" or "Copyleft".

* Licenses in this class include the GPL.

Those that don't are called "Permissive"

* These include Apache, BSD, and MIT licenses.

If you want your code to be maximally reusable, use a permissive license
If you want to force other people using your code to make derivatives open source, use a copyleft license.

If you want to use code that has a permissive license, it's safe to use it and keep your code secret.
If you want to use code that has a copyleft license, you'll have to release your code under such a license.

###Academic Use Only

Some researchers want to make their code free for Academic use only.
None of the standard licenses state this, and this is a reason why academic bespoke licenses proliferate.

However, there is no need for this, in my opinion.

*Use of a standard Copyleft license precludes derived software from being sold without also publishing the source*

So use of a Copyleft license precludes commercial use.

This is a very common way of making a business from open source code: offer the code under GPL for free
but offer the code under more permissive terms, allowing for commercial use, for a fee.

###Patents

Intellectual property law distinguishes Copyright from Patents. 
This is a complex field, which I am far from qualified to teach!

People who think carefully about intellectual property law distinguish software licenses
based on how they address patents. Very roughly, if a you want to ensure that contributors to your project
can't then go off and patent their contribution, some licenses, such as the Apache license, protect you from this.

###Use as a web service

If I take copyleft code, and use it to host a web service, I have not sold the software.

Therefore, under some licenses, I do not have to release any derivative software.
This "loophole" in the GPL is closed by the AGPL ("Affero GPL")

###Library Linking

If I use your code just as a library, without modifying it or including it directly in my own code, 
does the copyleft term of the GPL apply?

*Yes*

If you don't want it to, use the LGPL. ("Lesser GPL"). This has an exception for linking libraries.

###Citing Software

Almost all software licenses require people to credit you for what they used. ("Attribution")

In an academic context, it is useful to offer a statement as to how best to do this,
citing *which paper to cite in all papers which use the software*.

This is best done in a [CITATION](http://www.software.ac.uk/blog/2013-09-02-encouraging-citation-software-introducing-citation-files) file in your repository.

```
 To cite ggplot2 in publications, please use:

 H. Wickham. ggplot2: elegant graphics for data analysis. Springer New York,
 2009.

A BibTeX entry for LaTeX users is

@Book{,
   author = {Hadley Wickham},
   title = {ggplot2: elegant graphics for data analysis},
   publisher = {Springer New York},
   year = {2009},
   isbn = {978-0-387-98140-6},
   url = {http://had.co.nz/ggplot2/book},
 }
```

###Referencing the license in every file

Some licenses require that you include license information in every file.
Others do not. 

Typically, every file should contain something like:

```
// (C) University College London 2010-2014
// This software is licensed under the terms of the <foo license>
// See <somewhere> for the license details.
```

Check your license at
opensource.org for details of how to apply it to your software,
, e.g. for the [GPL](http://opensource.org/licenses/GPL-3.0#howto)

###Choose a license

See [GitHub's advice on how to choose a license](http://choosealicense.com/)

###Open source does not equal free maintainance

One common misunderstanding of open source software is that you'll automatically get loads of contributors from around the internets.
This is wrong. Most open source projects get no commits from anyone else.

Open source does *not* guarantee your software will live on with people adding to it after you stop working on it.

Later in the course, we'll offer some advice on [Software Sustainability](http://software.ac.uk/resources/about)
