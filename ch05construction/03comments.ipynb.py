# ---
# jupyter:
#   jekyll:
#     display_name: Comments
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Comments

# %% [markdown]
# Let's import first the context for this chapter.

# %%
from context import *

# %% [markdown]
# ## Why comment?

# %% [markdown]
#
# * You're writing code for people, as well as computers.
# * Comments can help you build code, by representing your design
# * Comments explain subtleties in the code which are not obvious from the syntax
# * Comments explain *why* you wrote the code the way you did
#

# %% [markdown]
# ## Bad Comments

# %% [markdown]
#
# "I write good code, you can tell by the number of comments."
#
# This is wrong.
#

# %% [markdown]
# ## Comments which are obvious

# %%
counter = counter + 1 # Increment the counter
for element in array: # Loop over elements
    pass

# %% [markdown]
# ## Comments which could be replaced by better style

# %% [markdown]
# The following piece of code could be a part of a game to move a turtle in a certain direction, with a particular angular velocity and step size.

# %%
for i in range(len(agt)): #for each agent
    agt[i].theta += ws[i]     # Increment the angle of each agent
                              #by its angular velocity
    agt[i].x += r * sin(agt[i].theta) #Move the agent by the step-size
    agt[i].y += r * cos(agt[i].theta) #r in the direction indicated

# %% [markdown]
# we have used comments to make the code readable.
#
#
# Why not make the code readable instead?

# %%
for agent in agents:
    agent.turn()
    agent.move()

class Agent:
    def turn(self):
         self.direction += self.angular_velocity;
    def move(self):
        self.x += Agent.step_length * sin(self.direction)
        self.y += Agent.step_length * cos(self.direction)


# %% [markdown]
# This is probably better. We are using the name of the functions (_i.e._, `turn`, `move`) instead of comments. Therefore, we've got _self-documenting_ code.
#

# %% [markdown]
# ## Comments vs expressive code 

# %% [markdown]
#
# > The proper use of comments is to compensate for our failure to express yourself in code. 
# Note that I used the word failure. I meant it. Comments are always failures.
#
# -- Robert Martin, [Clean Code](https://www.worldcat.org/title/clean-code-a-handbook-of-agile-software-craftsmanship/oclc/1057907478&referer=brief_results) [[UCL library](https://ucl-new-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=UCL_LMS_DS21163090000004761)].
#
# I wouldn't disagree, but still, writing "self-documenting" code is very hard, so do comment if you're unsure!
#

# %% [markdown]
# ## Comments which belong in an issue tracker

# %%
x.clear() # Code crashes here sometimes
class Agent(object):
    pass
    # TODO: Implement pretty-printer method


# %% [markdown]
#
#
#
# BUT comments that reference issues in the tracker can be good.
#
# E.g.
#
#
#

# %%
if x.safe_to_clear(): # Guard added as temporary workaround for #32
    x.clear()

# %% [markdown]
#
#
#
# is OK. And platforms like GitHub will create a link to it when browsing the code.
#

# %% [markdown]
# ## Comments which only make sense to the author today

# %%
agent.turn() # Turtle Power!
agent.move()
agents[:]=[]# Shredder!


# %% [markdown]
# ## Comments which are unpublishable

# %%
# Stupid supervisor made me write this code
# So I did it while very very drunk.

# %% [markdown]
# ## Good commenting: pedagogical comments

# %% [markdown]
#
# Code that *is* good style, but you're not familiar with, or 
# that colleagues might not be familiar with
#
#
#

# %%
# This is how you define a decorator in python
# See https://wiki.python.org/moin/PythonDecorators
def double(decorated_function):
    # Here, the result function forms a closure over 
    # the decorated function
    def result_function(entry):
        return decorated_function(decorated_function(entry))
    # The returned result is a function
    return result_function

@double
def try_me_twice():
    pass


# %% [markdown]
# ## Good commenting: reasons and definitions

# %% [markdown]
#
# Comments which explain coding definitions or reasons for programming choices.
#
#

# %%
def __init__(self):
    self.angle = 0 # clockwise from +ve y-axis
    nonzero_indices = [] # Use sparse model as memory constrained
