# ---
# jupyter:
#   jekyll:
#     display_name: Licensing
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Software Licensing

# %% [markdown]
# ### Reuse
#
# This course is distributed under the [Creative Commons By Attribution license](https://creativecommons.org/licenses/by/3.0/), which means you can modify and reuse the materials, so long as you credit [UCL Research IT Services](https://www.ucl.ac.uk/research-it-services/).

# %% [markdown]
# ### Disclaimer
#
# Here we attempt to give some basic advice on choosing a licence for your software. But:
#
# * we are NOT lawyers ([IANAL](https://en.wikipedia.org/wiki/IANAL)),
# * opinions differ (and flamewars are boring),
# * this training does NOT constitute legal advice. 
#
# For an in-depth discussion of software licences, read the O'Reilly book [Understanding Open Source and Free Software Licensing](https://www.oreilly.com/library/view/understanding-open-source/0596005814/).
#
# Your department, or UCL, may have policies about applying licences to code you create while a UCL employee or student. This training doesn't address this issue, and does not represent UCL policy -- seek advice from your supervisor or manager if concerned.

# %% [markdown]
# ### Choose a licence
#
# It is important to choose a licence and to create a *license file* to tell people what it is. 
#
# The licence lets people know whether they can reuse your code and
# under what terms. [This course has one](https://github.com/UCL/rsd-engineeringcourse/blob/master/LICENSE.md), for example.
#
# Your licence file should typically be called LICENSE.txt or similar. GitHub will offer to create a licence file automatically when you create a new repository.

# %% [markdown]
# ### Open source doesn't stop you making money
#
# A common misconception about open source software is the thought that
# open source means you can't make any money. This is *wrong*. 
#
# Plenty of people open source their software and profit from:
#
# * The software under a different licence e.g. [Saxon](http://saxon.sourceforge.net/)
# * Consulting. For example: [Anaconda](https://www.anaconda.com/consulting/) who help maintain NumPy.
# * Manuals. For example: [VTK](http://www.vtk.org/).
# * Add-ons. For example: [Puppet](http://puppetlabs.com/puppet/enterprise-vs-open-source).
# * Server software, which open source client software interacts with. For example: [GitHub API clients](https://github.com/octokit/octokit.rb).

# %% [markdown]
# ### Plagiarism vs promotion
#
# Many researchers worry about people stealing their work if they open source their code. But often the biggest problem is not theft, but the fact no one is aware of your work.
#
# Open source is a way to increase the probability that someone else on the planet will care enough about your work to cite you.
#
# So when thinking about whether to open source your code, think about whether you're more worried about
# anonymity or theft.

# %% [markdown]
# ### Your code *is* good enough
#
# New coders worry that they'll be laughed at if they put their code online. Don't worry. Everyone, including people who've been coding for decades, 
# writes shoddy code that is full of bugs.
#
# The only thing that will make your code better, is *other people reading it*. 
#
# For small scripts that no one but you will ever use,
# my recommendation is to use an open repository anyway. 
# Find a buddy, and get them to comment on it.

# %% [markdown]
# ### Worry about licence compatibility and proliferation
#
# Not all open source code can be used in all projects. Some licences are legally incompatible.
#
# This is a huge and annoying problem. 
# As an author, you might not care, but you can't anticipate the exciting uses people might find by
# mixing your code with someone else's. 
#
# Use a standard licence from the small list that are well-used.
# Then people will understand. *Don't make up your own*.
#
# When you're about to use a licence, see if there's a more common one which is recommended, e.g.:
# using the [opensource.org proliferation report](http://opensource.org/proliferation-report).

# %% [markdown]
# ### Academic licence proliferation
#
# Academics often write their own licence terms for their software.
#
# For example:
#
# >XXXX NON-COMMERCIAL EDUCATIONAL LICENSE
# >Copyright (c) 2013 Prof. Foo.
# >All rights reserved.
# >
# >You may use and modify this software for any non-commercial purpose within your educational 
# >institution. Teaching, academic research, and personal experimentation are examples of purpose 
# >which can be non-commercial.
# >
# >You may redistribute the software and modifications to the software for non-commercial 
# >purposes, but only to eligible users of the software (for example, to another university
# >student or faculty to support joint academic research).
#
# Please don't do this. Your desire to slightly tweak the terms is harmful to the
# future software ecosystem. Also, *Unless you are a lawyer, you cannot do this safely!*

# %% [markdown]
# ### Licences for code, content, and data.
#
# Licences designed for code should not be used to license data or prose.
#
# Don't use Creative Commons for software, or GPL for a book.

# %% [markdown]
# ### Licensing issues
#
# * Permissive vs share-alike
# * Non-commercial and academic Use Only
# * Patents
# * Use as a web service

# %% [markdown]
# ### Permissive vs share-alike
#
# Some licences require all derived software to be licensed under terms that are similarly free.
# Such licences are called "Share Alike" or "Copyleft".
#
# * Licences in this class include the [GPL](https://opensource.org/licenses/GPL-3.0).
#
# Those that don't are called "Permissive"
#
# * These include [Apache](https://opensource.org/licenses/Apache-2.0), [BSD](https://opensource.org/licenses/BSD-2-Clause), and [MIT](https://opensource.org/licenses/MIT) licences.
#
# If you want your code to be maximally reusable, use a permissive licence
# If you want to force other people using your code to make derivatives open source, use a copyleft licence.
#
# If you want to use code that has a permissive licence, it's safe to use it and keep your code secret.
# If you want to use code that has a copyleft licence, you'll have to release your code under such a licence.

# %% [markdown]
# ### Academic use only
#
# Some researchers want to make their code free for 'academic use only'.
# None of the standard licences state this, and this is a reason why academic bespoke licences proliferate.
#
# However, there is no need for this, in our opinion.
#
# *Use of a standard Copyleft licence precludes derived software from being sold without also publishing the source*
#
# So use of a Copyleft licence precludes commercial use.
#
# This is a very common way of making a business from open source code: offer the code under GPL for free
# but offer the code under more permissive terms, allowing for commercial use, for a fee.

# %% [markdown]
# ### Patents
#
# Intellectual property law distinguishes copyright from patents. 
# This is a complex field, which I am far from qualified to teach!
#
# People who think carefully about intellectual property law distinguish software licences
# based on how they address patents. Very roughly, if you want to ensure that contributors to your project
# can't then go off and patent their contribution, some licences, such as the Apache licence, protect you from this.

# %% [markdown]
# ### Use as a web service
#
# If I take copyleft code, and use it to host a web service, I have not sold the software.
#
# Therefore, under some licences, I do not have to release any derivative software.
# This "loophole" in the GPL is closed by the AGPL ("Affero GPL")

# %% [markdown]
# ### Library linking
#
# If I use your code just as a library, without modifying it or including it directly in my own code, 
# does the copyleft term of the GPL apply?
#
# *Yes*
#
# If you don't want it to, use the LGPL. ("Lesser GPL"). This has an exception for linking libraries.

# %% [markdown]
# ### Citing software
#
# Almost all software licences require people to credit you for what they used ("attribution").
#
# In an academic context, it is useful to offer a statement as to how best to do this,
# citing *which paper to cite in all papers which use the software*.
#
# This is best done with a [CITATION](http://www.software.ac.uk/blog/2013-09-02-encouraging-citation-software-introducing-citation-files) file in your repository.

# %% [markdown]
# > To cite ggplot2 in publications, please use:
# >
# >  H. Wickham. ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag New York, 2016.
# >
# > A BibTeX entry for LaTeX users is
# >
# > @Book{,
#     author = {Hadley Wickham},
#     title = {ggplot2: Elegant Graphics for Data Analysis},
#     publisher = {Springer-Verlag New York},
#     year = {2016},
#     isbn = {978-3-319-24277-4},
#     url = {https://ggplot2.tidyverse.org},
# }

# %% [markdown]
# ### Referencing the licence in every file
#
# Some licences require that you include licence information in every file.
# Others do not. 
#
# Typically, every file should contain something like:
#
# ```python
# # (C) University College London 2010-2014
# # This software is licenced under the terms of the <foo licence>
# # See <somewhere> for the licence details.
# ```

# %% [markdown]
# Check your licence at
# [opensource.org](http://opensource.org/) for details of how to apply it to your software. For example, for the [GPL](http://opensource.org/licenses/GPL-3.0#howto).

# %% [markdown]
# ### Choose a licence
#
# See [GitHub's advice on how to choose a licence](http://choosealicense.com/).

# %% [markdown]
# ### Open source does not equal free maintenance
#
# One common misunderstanding of open source software is that you'll automatically get loads of contributors from around the internets.
# This is wrong. Most open source projects get no commits from anyone else.
#
# Open source does *not* guarantee your software will live on with people adding to it after you stop working on it.
#
# Learn more about these issues from the website of the [Software Sustainability Institute](https://software.ac.uk/resources).
