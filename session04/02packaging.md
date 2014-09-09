---
title: Packaging
---

Packaging
---------

Once we've made a working program, we'd like to be able to share it with others.

A good cross-platform build tool is the most important thing: you can always
have collaborators build from source.

Distribution tools
------------------

Distribution tools allow one to obtain a working copy of someone else's package.

Language-specific tools: PyPI, Ruby Gems, CPAN, CRAN
Platform specific packagers e.g. brew, apt/yum

Windows doesn't have anything like `brew install` or `apt-get`
You have to build an 'installer'.

Laying out a project
--------------------

When planning to package a project for distribution, defining a suitable
project layout is essential.

```
├── README.md
├── LICENSE.md
├── setup.py
├── scripts
│   └── greengraph
└── greengraph
    ├── __init__.py
    ├── __main__.py
    ├── greengraph.py
    └── test
        ├── __init__.py
        ├── fixtures
        │   └── london.png
        └── test_greengraph.py
```

Using setuptools
----------------

``` python
from setuptools import setup, find_packages
setup(
    name = "GreenGraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],

    install_requires = ['numpy','geopy','pypng']
)
```

``` bash
python setup.py install #OR even:
sudo pip install git+git://github.com/jamespjh/greengraph@distribution
```

Distributing compiled code
--------------------------

If you're working in C++ or Fortran, there is no language specific repository.
You'll need to write platform installers for as many platforms as you want to
support.

Typically:

* `dpkg` for `apt-get` on Ubuntu and Debian
* `rpm` for `yum` on Redhat and Fedora
* `homebrew` on OSX (Possibly `macports` as well)
* An executable `msi` installer for Windows.

Homebrew
--------

Homebrew: A ruby DSL, you host off your own webpage

See my [installer for the cppcourse example](http://github.com/jamespjh/homebrew-reactor)

If you're on OSX, do:

``` bash
brew tap jamespjh/homebrew-reactor
brew install reactor
```

Using CMake or SCons to generate installers
--------------------------------------------

You can use CMake or SCons to generate installers for Windows and Linux.

CMake has the [CPack](http://www.cmake.org/cmake/help/v2.8.8/cpack.html)
extension which can build dpkg, rpm and windows installers.

SCons has the "Packaging" Builder:

``` python
env = Environment(tools=['default', 'packaging'])
env.Install('/bin/', 'my_program')
env.Package( NAME           = 'foo',
             VERSION        = '1.2.3',
             PACKAGETYPE    = 'rpm')
```
