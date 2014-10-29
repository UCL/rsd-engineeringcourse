---
title: Conventions
---

{% if notebook %}
##Setup

{{pyfrag('05','comments','setup')}}
{{pyfrag('05','objects','setup')}}
{{pyfrag('05','conventions','setup')}}
{{pyfrag('05','refactoring','setup')}}
Define some mocks so that the notebook will work
{% endif %}

##Coding Conventions

###One code, many layouts:

Consider the following fragment of python:

{{pyfrag('05','conventions','dense')}}

this could also have been written:

{{pyfrag('05','conventions','sparse')}}

###So many choices

* Layout
* Naming
* Syntax choices

###Layout

{{pyfrag('05','conventions','layout1')}}
{{pyfrag('05','conventions','layout2')}}

###Layout choices

* Brace style
* Line length
* Indentation
* Whitespace/Tabs

###Naming Conventions

{{pyfrag('05','conventions','naming1')}}
{{pyfrag('05','conventions','naming2')}}

###Hungarian Notation

Prefix denotes *type*:

{{pyfrag('05','conventions','naming3')}}

###Newlines

* Newlines make code easier to read
* Newlines make less code fit on a screen

Use newlines to describe your code's *rhythm*

###Syntax Choices

{{pyfrag('05','conventions','syntax1')}}
{{pyfrag('05','conventions','syntax2')}}

###Syntax choices

* Explicit operator precedence
* Compound expressions
* Package import choices

###Coding Conventions

You should try to have an agreed policy for your team for these matters.

If your language sponsor has a standard policy, use that.

E.g. [Python PEP8](http://legacy.python.org/dev/peps/pep-0008/)

E.g. [Google's guide for R](https://google-styleguide.googlecode.com/svn/trunk/Rguide.xml)

E.g. [Google's style guide for C++](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml)

###Lint

There are automated tools which enforce coding conventions and check for common mistakes.

These are called *linters*

E.g. `pip install` [pep8](https://pypi.python.org/pypi/pep8)

{{ bashfile('05','pep_example.sh')}}

It is a good idea to run a linter before every commit, or include it in your CI tests.
