# ---
# jupyter:
#   jekyll:
#     display_name: Testing Basics
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Testing

# %% [markdown]
# When programming, it is very important to know that the code we have written does what it was intended. Unfortunately, this step is often skipped in scientific programming, especially when developing code for our own personal work.
#
# Researchers sometimes check that their code behaves correctly by manually running it on some sample data and inspecting the results. However, it is much better and safer to automate this process, so the tests can be run often -- perhaps even after each new commit! This not only reassures us that the code behaves as it should at any given moment, it also gives us more flexibility to change it, because we have a way of knowing when we have broken something by accident.
#
# In this chapter, we will mostly look at how to write **unit tests**, which check the behaviour of small parts of our code. We will work with a particular framework for Python code, but the principles we discuss are general. We will also look at how to use a debugger to locate problems in our code, and services that simplify the automated running of tests.

# %% [markdown]
# ## A few reasons not to do testing

# %% [markdown]
# Sensibility                               | Sense
#   ------------------------------------    |  -------------------------------------
#   **It's boring**                         |  *Maybe*
#   **Code is just a one off throwaway**    |  *As with most research codes*
#   **No time for it**                      |  *A bit more code, a lot less debugging*
#   **Tests can be buggy too**              |  *See above*
#   **Not a professional programmer**       |  *See above*
#   **Will do it later**                    | *See above*

# %% [markdown]
# ## A few reasons to do testing
#
# * **laziness**: testing saves time
# * **peace of mind**: tests (should) ensure code is correct
# * **runnable specification**: best way to let others know what a function should do and
#     not do
# * **reproducible debugging**: debugging that happened and is saved for later reuse
# * **code structure / modularity**: since we may have to call parts of the code independently during the tests
# * **ease of modification**: since results can be tested

# %% [markdown]
# ## Not a panacea
#
# > Trying to improve the quality of software by doing more testing is like trying to lose weight by
# > weighing yourself more often.
#     - Steve McConnell

# %% [markdown]
#  * Testing won't correct a buggy code
#  * Testing will tell you were the bugs are...
#  * ... if the test cases *cover* the bugs

# %% [markdown]
# If the test cases do not cover the bugs, things can go horribly wrong - an example for this is [Therac-25](https://en.wikipedia.org/wiki/Therac-25).

# %% [markdown]
# ## Tests at different scales
#
# Level of test               |Area covered by test
# --------------------------  |----------------------
# **Unit testing**            |smallest logical block of work (often < 10 lines of code)
# **Component testing**       |several logical blocks of work together
# **Integration testing**     |all components together / whole program
#
#
# <br>
# <div class="fragment fade-in">
# Always start at the smallest scale! 
#
# <div class="fragment grow">
# If a unit test is too complicated, go smaller.
# </div>
# </div>

# %% [markdown]
# ## Legacy code hardening
#
# * Very difficult to create unit-tests for existing code
# * Instead we make a **regression test**
# * Run program as a black box:
#
# ```
# setup input
# run program
# read output
# check output against expected result
# ```
#
# * Does not test correctness of code
# * Checks code is a similarly wrong on day N as day 0

# %% [markdown]
# ## Testing vocabulary
#
# * **fixture**: input data
# * **action**: function that is being tested
# * **expected result**: the output that should be obtained
# * **actual result**: the output that is obtained
# * **coverage**: proportion of all possible paths in the code that the tests take

# %% [markdown]
# ## Branch coverage:

# %% [markdown] attributes={"classes": [" python"], "id": ""}
# ```python
# if energy > 0:
#     ! Do this 
# else:
#     ! Do that
# ```

# %% [markdown]
# Is there a test for both `energy > 0` and `energy <= 0`?
