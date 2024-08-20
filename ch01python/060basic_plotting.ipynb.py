# ---
# jupyter:
#   jekyll:
#     display_name: Basic plotting
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Plotting with Matplotlib - the `pyplot` interface
#
# [Matplotlib](https://matplotlib.org/) is a Python library which can be used to produce plots to visualise data. It has support for a wide range of [different plot types](https://matplotlib.org/stable/gallery/index.html), and as well as supporting static outputs it also allows producing [animations](https://matplotlib.org/stable/api/animation_api.html) and [interactive plots](https://matplotlib.org/stable/gallery/index.html#event-handling). As an intial introduction, we will demonstrate how to use Matplotlib's [`pyplot` interface](https://matplotlib.org/stable/api/index.html#the-pyplot-api) (modelled on the plotting functions in MATLAB), to create a simple line plot. Later, we will then illustrate Matplotlib's [object-oriented interface](https://matplotlib.org/stable/api/index.html#id3) which allows more flexibility in creating complex plots and greater control over the appearance of plot elements.
#
# ## Importing Matplotlib
#
# We import the `pyplot` object from Matplotlib, which provides us with an interface for making figures. A common convention is to use the `import ... as ...` syntax to alias `matplotlib.pyplot` to the shorthand name `plt`.

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# ## A basic plot
#
# As a first example we create a basic line plot.

# %%
plt.plot([2, 4, 6, 8, 10], [1, 5, 3, 7, -11])

# %% [markdown]
# The `plt.plot` function allows producing line and scatter plots which visualize the relationship between pairs of variables. Here we pass `plt.plot` two lists of five numbers corresponding to respectively the coordinates of the points to plot on the horizontal (*x*) axis and the coordinates of the points to plot on the vertical (*y*) axis. When passed no other arguments by default `plt.plot` will produce a line plot passing through the specified points. The value returned by `plt.plot` is a list of objects corresponding to the plotted line(s): in this case we plotted only one line so the list has only one element. We will for now ignore these return values, we will return to explain Matplotlib's object-oriented interface in a later episode.
#
# If passed a single list of numbers, the `plt.plot` function will interpret these as the coordinates of the points to plot on the vertical (*y*) axis, with the horizontal (*x*) axis points in this case implicitly assumed to be the indices of the values in the list. For example, if we plot with just the second list from the previous `plt.plot` call

# %%
plt.plot([1, 5, 3, 7, -11])

# %% [markdown]
# We get a very similar looking plot other than the change in the scale on the horizontal axis.

# %% [markdown]
# ## Plotting a function
#
# To make things a little more visually interesting, we will illustrate plotting the trigonometric functions *sine* ($\sin$) and *cosine* ($\cos$). We first import implementations of these functions from the in-built `math` module as well as the constant numerical constant `pi` ($\pi$).

# %%
from math import sin, cos, pi

# %% [markdown]
# The `sin` and `cos` functions both take a single argument corresponding to an angular quantity in [radians](https://en.wikipedia.org/wiki/Radian) and are [periodic](https://en.wikipedia.org/wiki/Periodic_function) with period $2\pi$. We therefore create a list of equally spaced angles in the interval $[0, 2\pi)$ and assign it to a variable `theta`.

# %%
number_of_points = 100
theta = [2 * pi * n / number_of_points for n in range(number_of_points)]

# %% [markdown]
# Using a list comprehension we can now compute the value of the sine function for each value in `theta` and graph this as the vertical coordinates of a line plot.

# %%
plt.plot(theta, [sin(t) for t in theta])

# %% [markdown]
# ## Plotting multiple lines
#
# We can plot multiple different lines on the same plot by making mutiple calls to `plt.plot` within the same cell. For example in the cell below we compute both the sine and cosine functions.

# %%
plt.plot(theta, [sin(t) for t in theta])
plt.plot(theta, [cos(t) for t in theta])

# %% [markdown]
# By default Matplotlib will cycle through a [sequence of colours](https://matplotlib.org/stable/gallery/color/color_cycle_default.html) as each new plot is added to help distinguish between the different plotted lines.
#
# ## Changing the line styles
#
# The `plt.plot` function offers various optional keyword arguments that can be used to further customise the plot. One useful argument is `linestyle` which allows the style of the line used to join the plotted points to be specified - for example this can useful to allow plotted lines to be distinguished even when they are printed in monochrome. Matplotlib as [a variety of built-in linestyles with simple string names](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html) as well as options for performing further customisation. Here we specify for the cosine curve to be plotted with a dotted line.

# %%
plt.plot(theta, [sin(t) for t in theta])
plt.plot(theta, [cos(t) for t in theta], linestyle="dotted")

# %% [markdown]
# ## Adding a legend
#
# Although we can visually distinguish between the two plotted lines, ideally we would have labels to indicate which corresponds to which function. We can add a legend to the plot with the `plt.legend` function. If we pass a list of strings to `plt.legend` these will be interpreted as the labels for each of the lines plotted so far in the order plotted. Matplotlib has [in-built support](https://matplotlib.org/stable/tutorials/text/mathtext.html) for using [TeX markup](https://en.wikibooks.org/wiki/LaTeX/Mathematics) to write mathematical expressions by putting the TeX markup within a pair of dollar signs (`$`). As TeX's use of the backslash character `\` to prefix commands conflicts with Python's interpretation of `\` as an escape character, you should typically use raw-strings by prefixing the string literal with `r` to simplify writing TeX commands.

# %%
plt.plot(theta, [sin(t) for t in theta])
plt.plot(theta, [cos(t) for t in theta], linestyle="dotted")
plt.legend([r"$\sin\theta$", r"$\cos\theta$"])

# %% [markdown]
# Matplotlib also allows the legend label for a plot to be specified in the `plt.plot` call using the `label` keyword arugment. When plotting many lines this can be more readable than having to create a separate list of labels to pass to a subsequent `plt.legend` call. If we specify the `label` keyword arguments we can call `plt.legend` without any arguments.

# %%
plt.plot(theta, [sin(t) for t in theta], label=r"$f(\theta) = \sin\theta$")
plt.plot(theta, [cos(t) for t in theta], linestyle="dotted", label=r"$f(\theta) = \cos\theta$")
plt.legend()

# %% [markdown]
# ## Adding axis labels and a title
#
# The `pyplot` interface also provides functions for adding axis labels and a title to our plot. Specifically `plt.xlabel` and `plt.ylabel` are functions which set the labels on respectively the horizontal (*x*) axis and vertical (*y*) axis, both accepting a string argument corresponding to the axis label. The `plt.title` function, as the name suggests, allows setting an overall title for the plot. As for the legend labels, the axis labels and title may all optionally use TeX mathematical notation delimited by dollar `$` signs.

# %%
plt.plot(theta, [sin(t) for t in theta], label=r"$f(\theta) = \sin\theta$")
plt.plot(theta, [cos(t) for t in theta], linestyle="dotted", label=r"$f(\theta) = \cos\theta$")
plt.legend()
plt.xlabel(r"Angle in radians $\theta$")
plt.ylabel(r"$f(\theta)$")
plt.title("Trigonometric functions")
