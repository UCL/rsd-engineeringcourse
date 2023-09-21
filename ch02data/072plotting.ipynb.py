# ---
# jupyter:
#   jekyll:
#     display_name: Plotting
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Plotting with Matplotlib
#
# Plotting data is very common and useful in scientific work. Python does not include any plotting functionality in the language itself, but there are various frameworks available for producing plots and visualisations.
#
# In this section, we will look at Matplotlib, one of those frameworks. As the name indicates, it was conceived to provide an interface similar to the MATLAB programming language, but no knowledge of MATLAB is required!

# %% [markdown]
# ### Importing Matplotlib

# %% [markdown]
# We import the `pyplot` object from Matplotlib, which provides us with an interface for making figures. We usually abbreviate it.

# %%
from matplotlib import pyplot as plt

# %% [markdown]
# ### Notebook magics

# %% [markdown]
# When we write:

# %%
# %matplotlib inline

# %% [markdown]
# We tell the Jupyter notebook to show figures we generate alongside the code that created it, rather than in a
# separate window. Lines beginning with a single percent are not python code: they control how the notebook deals with python code.

# %% [markdown]
# Lines beginning with two percents are "cell magics", that tell Jupyter notebook how to interpret the particular cell;
# we've seen `%%writefile`, for example.

# %% [markdown]
# ### A basic plot

# %% [markdown]
# When we write:

# %%
from math import sin, cos, pi
my_fig = plt.plot([sin(pi * x / 100.0) for x in range(100)])

# %% [markdown]
# The plot command *returns* a figure, just like the return value of any function. The notebook then displays this.

# %% [markdown]
# To add a title, axis labels etc, we need to get that figure object, and manipulate it. 
# For convenience, matplotlib allows us to do this just by issuing commands to change the "current figure":

# %%
plt.plot([sin(pi * x / 100.0) for x in range(100)])
plt.title("Hello")

# %% [markdown]
# But this requires us to keep all our commands together in a single cell, and makes use of a "global" single "current plot",
# which, while convenient for quick exploratory sketches, is a bit cumbersome. To produce from our notebook proper plots
# to use in papers, the library defines some types we can use to treat individual figures as variables,
# and manipulate these.

# %% [markdown]
# ### Figures and Axes

# %% [markdown]
# We often want multiple graphs in a single figure (e.g. for figures which display a matrix of graphs of different variables for comparison).

# %% [markdown]
# So Matplotlib divides a `figure` object up into axes: each pair of axes is one 'subplot'. 
# To make a boring figure with just one pair of axes, however, we can just ask for a default new figure, with
# brand new axes. The relevant function returns a (figure, axis) pair, which we can deal out with parallel assignment (unpacking). 

# %%
sine_graph, sine_graph_axes = plt.subplots()

# %% [markdown]
# Once we have some axes, we can plot a graph on them:

# %%
sine_graph_axes.plot([sin(pi * x / 100.0) for x in range(100)], label='sin(x)')

# %% [markdown]
# We can add a title to a pair of axes:

# %%
sine_graph_axes.set_title("My graph")

# %%
sine_graph_axes.set_ylabel("f(x)")

# %%
sine_graph_axes.set_xlabel("100 x")

# %% [markdown]
# Now we need to actually display the figure. As always with the notebook, if we make a variable be returned by the last
# line of a code cell, it gets displayed:

# %%
sine_graph

# %% [markdown]
# We can add another curve:

# %%
sine_graph_axes.plot([cos(pi * x / 100.0) for x in range(100)], label='cos(x)')

# %%
sine_graph

# %% [markdown]
# A legend will help us distinguish the curves:

# %%
sine_graph_axes.legend()

# %%
sine_graph

# %% [markdown]
# ### Saving figures

# %% [markdown]
# We must be able to save figures to disk, in order to use them in papers. This is really easy:

# %%
sine_graph.savefig('my_graph.png')

# %% [markdown]
# In order to be able to check that it worked, we need to know how to display an arbitrary image in the notebook.

# %% [markdown]
# The programmatic way is like this:

# %%
from IPython.display import Image # Get the notebook's own library for manipulating itself.
Image(filename='my_graph.png')

# %% [markdown]
# ### Subplots

# %% [markdown]
# We might have wanted the $\sin$ and $\cos$ graphs on separate axes:

# %%
double_graph = plt.figure()

# %%
sin_axes = double_graph.add_subplot(2, 1, 1) # 2 rows, 1 column, 1st subplot

# %%
cos_axes = double_graph.add_subplot(2, 1, 2) # 2 rows, 1 column, 2nd subplot

# %%
double_graph

# %%
sin_axes.plot([sin(pi * x / 100.0) for x in range(100)])

# %%
sin_axes.set_ylabel("sin(x)")

# %%
cos_axes.plot([cos(pi * x / 100.0) for x in range(100)])

# %%
cos_axes.set_ylabel("cos(x)")

# %%
cos_axes.set_xlabel("100 x")

# %%
double_graph

# %% [markdown]
# ### Versus plots

# %% [markdown]
# When we specify a single `list` to `plot`, the x-values are just the array index number. We usually want to plot something
# more meaningful:

# %%
double_graph = plt.figure()
sin_axes = double_graph.add_subplot(2, 1, 1)
cos_axes = double_graph.add_subplot(2, 1, 2)
cos_axes.set_ylabel("cos(x)")
sin_axes.set_ylabel("sin(x)")
cos_axes.set_xlabel("x")

# %%
sin_axes.plot([x / 100.0 for x in range(100)], [sin(pi * x / 100.0) for x in range(100)])
cos_axes.plot([x / 100.0 for x in range(100)], [cos(pi * x / 100.0) for x in range(100)])

# %%
double_graph

# %% [markdown]
# ### Learning More

# %% [markdown]
# There's so much more to learn about matplotlib: pie charts, bar charts, heat maps, 3-d plotting, animated plots, and so on. You can learn all this via the [Matplotlib Website](http://matplotlib.org/).
# You should try to get comfortable with all this, so please use some time in class, or at home, to work your way through a bunch of the [examples](https://matplotlib.org/stable/gallery/index).
