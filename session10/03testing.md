---
title: Testing
---

## Testing

### Testing

Tests save time, improve code quality, and give peace of mind. In the testing session, we learnt how to incorporate tests using frameworks like Nose, reviewed mocking and debugging, and discussed test-driven development. Our exercise was to apply this new knowledge to implement and test a Monte-Carlo algorithm.

### The Monte-Carlo exercise

We are looking for:

* Tidy, well-commented code with consistent syntax (e.g. [PEP8](https://www.python.org/dev/peps/pep-0008/))
* Sensible set of tests
* Appropriate use of functions and/or classes
* Evidence of tests written alongside code in the commit history

### Sensible tests

To create tests, break the task into logical, bite-size chunks. For example:

``` python
def test_input_sanity():
    """ Check incorrect input do fail """
    pass

def test_move_particle_one_over():
    """ Check density is change by a particle hopping left or right. """
    pass

def test_equal_probability():
    """ Check particles have equal probability of movement. """
    pass

def test_stop_simulation():
    """ Checks that if observe returns False, iteration stops. """
    pass
```

### Using functions and classes




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
https://github.com/UCL/rsd-engineeringcourse/tree/staging/session03/solutions


