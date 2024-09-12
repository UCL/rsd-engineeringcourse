# ---
# jupyter:
#   jekyll:
#     display_name: Test Frameworks
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Testing frameworks
# 
# **NOTE:** using bash/git commands is not fully supported on jupyterlite yet (due to single
# thread/process restriction), and the cells below might error out on the browser
# (jupyterlite) version of this notebook
# 
# ## Why use testing frameworks?

# %% [markdown]
# Frameworks should simplify our lives:
#
# * Should be easy to add simple test
# * Should be possible to create complex test:
#     * Fixtures
#     * Setup/Tear down
#     * Parameterized tests (same test, mostly same input)
# * Find all our tests in a complicated code-base 
# * Run all our tests with a quick command
# * Run only some tests, e.g. ``test --only "tests about fields"``
# * **Report failing tests**
# * Additional goodies, such as code coverage

# %% [markdown]
# ## Common testing frameworks

# %% [markdown]
# * Language agnostic: [CTest](http://www.cmake.org/cmake/help/v2.8.12/ctest.html)
#   * Test runner for executables, bash scripts, etc...
#   * Great for legacy code hardening
#     
#
# * C unit-tests:
#     * all c++ frameworks,
#     * [Check](https://libcheck.github.io/check/),
#     * [CUnit](http://cunit.sourceforge.net)
#
#
# * C++ unit-tests:
#     * [CppTest](http://cpptest.sourceforge.net/),
#     * [Boost::Test](http://www.boost.org/doc/libs/1_55_0/libs/test/doc/html/index.html),
#     * [google-test](https://code.google.com/p/googletest/),
#     * [Catch](https://github.com/philsquared/Catch) (best)
#
#
# * Python unit-tests:
#     * [nose](https://nose.readthedocs.org/en/latest/) includes test discovery, coverage, etc
#     * [unittest](https://docs.python.org/3/library/unittest.html) comes with standard python library
#     * [pytest](https://docs.pytest.org/en/latest/index.html), branched off of nose
#
#
# * R unit-tests:
#     * [RUnit](http://cran.r-project.org/web/packages/RUnit/index.html),
#     * [svUnit](http://cran.r-project.org/web/packages/svUnit/index.html)
#     * (works with [SciViews](http://www.sciviews.org/) GUI)
#     
#
# * Fortran unit-tests:
#     * [funit](https://rubygems.org/gems/funit),
#     * [pfunit](http://sourceforge.net/projects/pfunit/)(works with MPI)

# %% [markdown]
# ## pytest framework: usage
#
# [pytest](https://docs.pytest.org/en/latest/) is a recommended python testing framework.

# %% [markdown]
# We can use its tools in the notebook for on-the-fly tests in the notebook. This, happily, includes the negative-tests example we were looking for a moment ago.

# %%
def I_only_accept_positive_numbers(number):
    # Check input
    if number < 0: 
        raise ValueError("Input {} is negative".format(number))

    # Do something


# %%
from pytest import raises

# %%
with raises(ValueError):
    I_only_accept_positive_numbers(-5)


# %% [markdown]
# but the real power comes when we write a test file alongside our code files in our homemade packages:

# %% language="bash"
# mkdir -p saskatchewan
# touch saskatchewan/__init__.py

# %%
# %%writefile saskatchewan/overlap.py
def overlap(field1, field2):
    left1, bottom1, top1, right1 = field1
    left2, bottom2, top2, right2 = field2
    
    overlap_left = max(left1, left2)
    overlap_bottom = max(bottom1, bottom2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)
    # Here's our wrong code again
    overlap_height = (overlap_top - overlap_bottom)
    overlap_width = (overlap_right - overlap_left)
    
    return overlap_height * overlap_width


# %%
# %%writefile saskatchewan/test_overlap.py
from .overlap import overlap

def test_full_overlap():
    assert overlap((1.,1.,4.,4.), (2.,2.,3.,3.)) == 1.0

def test_partial_overlap():
    assert overlap((1,1,4,4), (2,2,3,4.5)) == 2.0
                 
def test_no_overlap():
    assert overlap((1,1,4,4), (4.5,4.5,5,5)) == 0.0


# %% attributes={"classes": [" bash"], "id": ""} magic_args="--no-raise-error" language="bash"
# cd saskatchewan
# pytest

# %% [markdown]
# Note that it reported **which** test had failed, how many tests ran, and how many failed.

# %% [markdown]
# The symbol `..F` means there were three tests, of which the third one failed.

# %% [markdown]
# Pytest will:
#
# * automagically finds files ``test_*.py``
# * collects all subroutines called ``test_*``
# * runs tests and reports results

# %% [markdown]
# Some options:
#
# * help: `pytest --help`
# * run only tests for a given feature: `pytest -k foo` # tests with 'foo' in the test name

# %% [markdown]
# ## Testing with floating points
#
# ## Floating points are not reals
#
#
# Floating points are inaccurate representations of real numbers:
#
# `1.0 == 0.99999999999999999` is true to the last bit.

# %% [markdown]
# This can lead to numerical errors during calculations: $1000 (a - b) \neq 1000a - 1000b$

# %%
1000.0 * 1.0 - 1000.0 * 0.9999999999999998

# %% attributes={"classes": [" python"], "id": ""}
1000.0 * (1.0 - 0.9999999999999998)

# %% [markdown]
# *Both* results are wrong: `2e-13` is the correct answer.
#
# The size of the error will depend on the magnitude of the floating points:

# %% attributes={"classes": [" python"], "id": ""}
1000.0 * 1e5 - 1000.0 * 0.9999999999999998e5

# %% [markdown]
# The result should be `2e-8`.

# %% [markdown]
# ## Comparing floating points
#
# Use the "approx", for a default of a relative tolerance of $10^{-6}$

# %% attributes={"classes": [" python"], "id": ""}
from pytest import approx
assert  0.7 == approx(0.7 + 1e-7) 

# %% [markdown]
# Or be more explicit:

# %% attributes={"classes": [" python"], "id": ""}
magnitude = 0.7
assert 0.7 == approx(0.701 , rel=0.1, abs=0.1)

# %% [markdown]
# Choosing tolerances is a big area of [debate](https://software-carpentry.org/blog/2014/10/why-we-dont-teach-testing.html).

# %% [markdown]
# ## Comparing vectors of floating points
#
# Numerical vectors are best represented using [numpy](http://www.numpy.org/).

# %% attributes={"classes": [" python"], "id": ""}
from numpy import array, pi

vector_of_reals = array([0.1, 0.2, 0.3, 0.4]) * pi

# %% [markdown]
# Numpy ships with a number of assertions (in ``numpy.testing``) to make
# comparison easy:

# %% attributes={"classes": [" python"], "id": ""}
from numpy import array, pi
from numpy.testing import assert_allclose
expected = array([0.1, 0.2, 0.3, 0.4, 1e-12]) * pi
actual = array([0.1, 0.2, 0.3, 0.4, 2e-12]) * pi
actual[:-1] += 1e-6

assert_allclose(actual, expected, rtol=1e-5, atol=1e-8)

# %% [markdown]
# It compares the difference between `actual` and `expected` to ``atol + rtol * abs(expected)``.
