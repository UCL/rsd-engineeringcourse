---
title: Libraries
---

## Libraries

### Libraries

Libraries make us powerful. In this session we reviewed:

* good practice in selecting libraries
* tools for package management
* methods for promoting cross-platform independence when creating libraries
* good practice in defining a project layout
* tools for packaging and distributing our own libraries

During the session we demonstrated how existing libraries enable us to find and download a map from the web and measure the density of green space. 

### Packaging the greengraph code

Our exercise focused on packaging code to make it easy to share and reuse. We are looking for:

* Readable code and sensible tests (always!)
* Well-structured package
    - Appropriate project layout
    - Packaging instructions in a setupfile
    - License and documentation
* Script for use of greengraph at the command line

### Project layout

``` bash
├── LICENSE.md
├── README.md
├── greengraph
│   ├── __init__.py
│   ├── greengraph.py
│   └── test
│       ├── __init__.py
│       ├── fixtures
│       │   └── london.png
│       └── test_greengraph.py
├── scripts
│   └── greengraph
└── setup.py
```

### The setupfile (setup.py)

``` python
from setuptools import setup, find_packages
setup(
    name = "GreenGraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']), # dependencies
    scripts = ['scripts/greengraph'],

    install_requires = ['numpy','geopy','pypng'],

    # metadata for upload to PyPI
    author = "James Hetherington",
    author_email = "jamespjh@gmail.com",
    description = "Measure level of greenery from Google Maps",
    license = "MIT",
    keywords = "Environment, geocoding",
    url = "http://development.rc.ucl.ac.uk", # project home page, if any
)
```

### License and documentation

A clear license and readme are crucial for allowing others to reuse your package. The [MIT License](http://opensource.org/licenses/MIT) is a popular open source license that maximises reuse potential:

``` text
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell ...
```

<!--
### Command line script

Before:

``` python

```

After:

``` python

```
!-->

### Sample solution

A sample solution is available at: 
[https://github.com/jamespjh/greengraph/tree/distribution](https://github.com/jamespjh/greengraph/tree/distribution)

