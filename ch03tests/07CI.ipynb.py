# ---
# jupyter:
#   jekyll:
#     display_name: Continuous Integration
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Continuous Integration
#
# Continuous integration (CI) is a software development practice that involves integrating new code to a shared repository regularly (typically at least once a day). The integrated changes are then automatically checked by the CI system on test servers, which allows to detect problems early.
#
# ## Test servers
#
# The test servers of the CI system might be configured to: 
#
# 1. run tests nightly
# 2. run tests after each commit to GitHub (or other shared repository)
# 3. run tests on different platforms (e.g. to check that tests pass for different Python versions, or on different operating systems)
#
# There are a number of technologies that can be used to set up a CI system to work with a GitHub repository either on your own server or on a remote machine ([GitHub Actions](https://docs.github.com/en/actions), [Travis CI](https://blog.travis-ci.com/2019-05-30-setting-up-a-ci-cd-process-on-github), [CircleCI](https://circleci.com/), ...). Various UCL research groups run servers that can be used to do this automatically. We currently recommend GitHub Actions as the CI system of choice, which has a quite generous offering for open source projects.
#
# When configuring a CI system, it's important to weigh up the usefulness of the test settings you cover against the energy consumption that will incur from running the tests frequently. For example, you might want to set up the CI system to run a more extensive suite of tests when a PR to the `main` branch is opened, and only run a small number of important tests at every commit. You could also decide that you don't need to test your code for all Python versions, but only for an old version and a recent one.

# %% [markdown]
# ## Memory and profiling
#
# For compiled languages (C, C++, Fortran):
# * Checking for memory leaks with [valgrind](http://valgrind.org/):
#   `valgrind --leak-check=full program`
# * Checking cache hits and cache misses with
#   [cachegrind](http://valgrind.org/docs/manual/cg-manual.html):
#   `valgrind --tool=cachegrind program`
# * Profiling the code with [callgrind](http://valgrind.org/docs/manual/cl-manual.html):
#   `valgrind --tool=callgrind program`

# %% [markdown]
# * Python: profile with [the standard library](https://docs.python.org/3/library/profile.html) or [runsnake](http://www.vrplumber.com/programming/runsnakerun/)
# * R: [Rprof](http://stat.ethz.ch/R-manual/R-devel/library/utils/html/Rprof.html)
