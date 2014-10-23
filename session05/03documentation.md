---
title: Comments
---

##Documentation

###Documentation is hard

* Good documentation is hard, and very expensive.
* Bad documentation is detrimental.
* Good documentation quickly becomes bad if not kept up-to-date with code changes.
* Professional companies pay large teams of documentation writers.

###Prefer readable code with tests and vignettes

If you don't have the capacity to maintain great documentation,
focus on:

* Readable code
* Automated tests
* Small code samples demonstrating how to use the api

###Comment-based Documentation tools

Documentation tools can produce extensive documentation about your code by pulling out comments near the beginning of functions,
together with the signature, into a web page.

The most popular is [Doxygen](http://www.stack.nl/~dimitri/doxygen/)

[Have a look at an example of some Doxygen output](
http://www.bempp.org/cppref/2.0/group__abstract__boundary__operators.html)

[Sphinx](http://sphinx-doc.org/) is nice for Python, and works with C++ as well.
Here's some [Sphinx-generated output](http://www.bempp.org/pythonref/2.0/bempp_visualization2.html)
and the [corresponding source code](https://github.com/bempp/bempp/blob/master/python/bempp/visualization2.py)
[Breathe](http://michaeljones.github.io/breathe/ ) can be used to make Sphinx and Doxygen work together.

[Roxygen](http://www.rstudio.com/ide/docs/packages/documentation) is good for R.
