---
title: Testing
---

## Testing

### Testing

Tests save time, improve code quality, and give peace of mind. In the testing session, we learnt about:

* how to incorporate tests using frameworks like Nose
* mocking and debugging
* test-driven development. 

### The Monte-Carlo exercise

The exercise was to apply our new knowledge to implement and test a Monte-Carlo algorithm. We are looking for:

* Tidy, well-commented code with consistent syntax (e.g. [PEP8](https://www.python.org/dev/peps/pep-0008/))
* Sensible set of tests
* Appropriate use of functions and/or classes
* Evidence of tests written alongside code in the commit history

### Sensible tests

To create tests, break the task into logical, bite-size chunks. For example:

``` python
def test_input_sanity():
    """ Check incorrect inputs do fail """
    pass

def test_move_particle_one_over():
    """ Check density is change by a particle hopping left or right. """
    pass

def test_accept_change():
    """ Check that move is accepted if second energy is lower """
    pass
```

### Using functions and classes

We can repeat the logic of writing tests to organise our code into functions and classes:

``` python
class MonteCarlo(object):
    """ A simple Monte Carlo implementation """

    def __init__(self, temperature=100, itermax=100):
        """ Initialise simulation with inputs """
        pass

    def change_density(self, density):
        """ Move one particle left or right. """
        pass

    def accept_change(self, prior, successor):
        """ Returns true if should accept change. """
        pass
```

### Sample solution

A sample solution is available at: 
[https://github.com/UCL/rsd-engineeringcourse/tree/staging/session03/solutions](https://github.com/UCL/rsd-engineeringcourse/tree/staging/session03/solutions)


