---
title: DRY programming tricks
---

## DRY programming tricks

### DRY programming tricks

Unnecessary code is a home for unnecessary mistakes, so **d**on't **r**epeat **y**ourself. This session explored techniques for refactoring away repetitive code, and introduced the concepts of functional programming, exception handling, decorators, and operator overloading. Our exercise was to write a library to handle quantities with units, creating an opportunity to apply some of these concepts.

### Writing a library to handle units

We were looking for:

* Readable code and sensible tests (always!)
* Simple, well-structured library
* Clear system for unit definitions
* Operator overloading for handling units (\*,==,+)

### Project layout

``` bash
└── uclunit
    ├── CITATION.md
    ├── LICENSE.md
    ├── README.md
    ├── demo.py
    ├── setup.py
    ├── test
    │   ├── __init__.py
    │   └── tests.py
    └── uclunit
        ├── __init__.py
        ├── convert.py
        ├── loadunits.py
        └── units.yaml
```

### Configuration file for definitions

Units can be defined in a configuration file and imported as a dictionary using the YAML library.

``` yaml
length: 
  meters: 1.
  millimeters: 0.001
  centimeters: 0.01
  kilometers: 1000.

weight:
  grams: 1.
  ...
```

<!--
### Title

Before:

``` python

```

After:

``` python

```
!-->

### Sample solution

A sample solution is available at: 
https://github.com/tompollard/rsd-engineeringcourse/tree/solution_07ex/session07/solutions/uclunit

