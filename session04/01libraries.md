---
title: Libraries
---

##Careful use of Libraries

###Drawbacks of libraries.

* Sometimes, libraries are not looked after by their creator: code that is not maintained *rots*:
  * It no longer works with later versions of *upstream* libraries.
  * It doesn't work on newer platforms or systems.
  * Features that are needed now, because the field has moved on, are not added

* Sometimes, libraries are hard to get working:
  * For libraries in pure python, this is almost never a problem
  * But many libraries involve *compiled components*: these can be hard to install.

###Contribute, don't duplicate

* You have a duty to the ecosystem of scholarly software:
  * If there's a tool or algorithm you need, find a project which provides it.
  * If there are features missing, or problems with it, fix them, [don't create your own](http://xkcd.com/927/) library.

###How to choose a library

* When was the last commit?
* How often are there commits?
* Can you find the lead contributor on the internet?
* Do they respond when approached:
    * emails to developer list
    * personal emails
    * tweets
    * [irc](https://freenode.net)
    * issues raised on GitHub?
* Are there contributors other than the lead contributor?
* Is there discussion of the library on Stack Exchange?
* Is the code on an open version control tool like GitHub?
* Is it on standard package repositories. (PyPI, apt/yum/brew)
* Are there any tests?
* Download it. Can you build it? Do the tests pass?
* Is there an open test dashboard? (Travis/Jenkins/CDash)
* What dependencies does the library itself have? Do they pass this list?
* Are different versions of the library clearly labeled with version numbers?
* Is there a changelog?

###Sensible Version Numbering

The best approach to version numbers clearly distinguishes kinds of change:

Given a version number MAJOR.MINOR.PATCH, e.g. 2.11.14 increment the:

* MAJOR version when you make incompatible API changes,
* MINOR version when you add functionality in a backwards-compatible manner, and
* PATCH version when you make backwards-compatible bug fixes.

This is called [Semantic Versioning](http://semver.org)

##Python Libraries

###The Python Standard Library

Python comes with a powerful [standard library](https://docs.python.org/2/library/).

Learning python is as much about learning this library as learning the language itself.

You've already seen a few packages in this library: `math`, `pdb`, `pytest`, `datetime`.

###The Python Package Index

Python's real power, however, comes with the Python Package Index: [PyPI](https://pypi.python.org/pypi).
This is a huge array of libraries, with all kinds of capabilities, all easily installable from the 
command line or through your Python distribution.

###Pip

Packages from PyPI are installed using Pip.

``` bash
pip list # See what you have installed
pip search <term> # Search PyPI for a package
sudo pip install <package> # install a package
sudo pip install <package> --upgrade # upgrade
sudo pip uninstall <package>
```

##Some libraries

###Argparse

This is the standard library for building programs with a command-line interface.

{{ notebookfile('04','greeter.py') }}

{{ bashfile('04','greetings.sh') }}

###Operating system paths and files

When loading and saving files, standard libraries allow you to manage file names,
in an operating-system independent way:

{% if notebook %}
``` python
__file__ = "session04.ipynb" # No __file__ in notebook!
```
{% endif %}


{{ pyfrag('04','system', 'paths', execute=False) }}

And you'll want to be able to read and write to files:

{{ pyfrag('04','system','files', execute=False) }}

Note the use of the `csv` library to read csv files as well.

###Context managers

There's a better way to handle opening and closing files

{{ pyfrag('04','system', 'context', execute=False) }}

This syntax using `with` is called a context manager.
It is used when a library wants stuff to happen both before **and** after client code is called.

Here, [`yaml`](http://www.yaml.org) is another standard file format for data files similar to XML or CSV.

###Working with web resources

To interact with resources on the web, you need a way to work with URLs: escaping characters that
can't appear in URLs, composing ?foo=bar web argument strings and so on.

We can use the [requests](http://docs.python-requests.org/en/latest/) library from PyPI for this.

{{ pyfrag('04','web', 'URL') }}

And you can download files from the web, accessing headers and the body of the response:

{{ pyfrag('04','web', 'download') }}

Libraries even allow you to parse HTML content, to find the data you want within a page:

{{ pyfrag('04','web', 'parse')}}

{% if notebook %}
``` python
import IPython
IPython.core.display.Image(map_here.content)
```
{% else %}
![Image downloaded from google using requests](session04/python/map.png)
{% endif %}
