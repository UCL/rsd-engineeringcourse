---
title: Tools
---

##Testing Frameworks

###What a frameworks is for

<p align="left">Frameworks should simplify our lives:</p>

* Should be easy to add simple test
* Should be possible to create complex test:
    * Fixtures
    * Setup/Tear down
    * Parameterized tests (same test, mostly same input)
* Run all tests, e.g. ``make test``
* Run only some tests, e.g. ``ctest -R electronic .``
* **Report failing tests**
* Additional goodies, such as code coverage

###Testing Frameworks

* Language agnostic: [CTest](http://www.cmake.org/cmake/help/v2.8.12/ctest.html)

    | Test runner for executables, bash scripts, etc...
    | Great for legacy code hardening

* C unit-tests:
    all c++ frameworks,
    [Check](http://check.sourceforge.net/),
    [CUnit](http://cunit.sourceforge.net)

* C++ unit-tests:
    [CppTest](http://cpptest.sourceforge.net/),
    [Boost::Test](http://www.boost.org/doc/libs/1_55_0/libs/test/doc/html/index.html),
    [google-test](https://code.google.com/p/googletest/),
    [Catch](https://github.com/philsquared/Catch) (best)

* Python unit-tests:

    | [nose](https://nose.readthedocs.org/en/latest/) includes test discovery, coverage, etc
    | [unittest](http://docs.python.org/2/library/unittest.html) comes with standard python library
    | [py.test](http://pytest.org/latest/), branched off of nose

* R unit-tests:
    [RUnit](http://cran.r-project.org/web/packages/RUnit/index.html),
    [svUnit](http://cran.r-project.org/web/packages/svUnit/index.html)
    (works with [SciViews](http://www.sciviews.org/) GUI)

* Fortran unit-tests:
    [funit](http://nasarb.rubyforge.org/funit/),
    [pfunit](http://sourceforge.net/projects/pfunit/)(works with MPI)


###Mocking Frameworks

* C: [CMocka](http://www.cmocka.org/)
* C++: [googlemock](https://code.google.com/p/googlemock/)
* Python: [Mock](http://www.voidspace.org.uk/python/mock/)
  ([unittest.mock](http://docs.python.org/dev/library/unittest.mock) in python 3.3),
  [doublex](https://pypi.python.org/pypi/doublex)

###Nose Framework: Usage

<div align="left">
[nose](https://nose.readthedocs.org/en/latest/) is a python framework:

``` bash
$ cd my_package_directory
$ nosetests
```

```
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

* automagically finds files ``test_*.py``
* collects all subroutines called ``test_*``
* runs tests and reports results

<br>
Some options:

* help: `nosetests --help`
* test only a given file: `nosetests test_file.py`
* compute coverage: `nosetests --with-coverage`
</div>

###Nose: Writing Tests

<div align="left">
In a file ``test_[meaningful_name].py``:

* Check that something is true

``` python
from nose.tools import assert_true
from my_module import my_function

def test_my_function_returns_true():
    argument = "something, anything"
    actual = my_function(something)
    assert_true(actual, "some description")
```

* Check expected result and actual results are equal

``` python
def test_set_equality():
    from nose.tools import assert_equal, assert_not_equal
    assert_equal(set([1, 2]), set([2, 1]), "Sets are order independent")
    assert_not_equal(set([1, 2]), set([1, 3]), "Sets elements matter")
```

* Check that an exception is raised

``` python
def test_exception_is_raised():
    from nose.tools import assert_raises
    with assert_raises(ValueError) as exception:
        raise ValueError("I'm the wrong value")
```
