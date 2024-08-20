# ---
# jupyter:
#   jekyll:
#     display_name: Plotting
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Plotting with Matplotlib - object-oriented interface
#
# Now that we are familiar with the basics of object-oriented programming, we revisit Matplotlib to illustrate its powerful object-oriented interface, rather than the more restricted `pylab` interface we encountered previously. 

# %%
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# ## *Aside*: Notebook magics
#
# At the beginning of notebooks you will often see the command
#
# ```Python
# %matplotlib inline
# ```
#
# This is an example of a [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html), a special syntax which can only be used when running an [*IPython* (interactive Python)](https://ipython.readthedocs.io/en/stable/overview.html) kernel, for example via a Jupyter notebook or the `IPython` terminal application. These commands are prefixed by one or two percent characters, with a single `%` indicating a [line magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#line-magics) command where only the content on the immediately following line is used by the magic and a double `%%` indicating a [cell magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics) which should be placed at the beginning of a notebook cell and means that all the content in the cell will be interpreted by the magic command. We have already encountered magic commands, for example the `%%writefile` cell magic which writes the cell content to a specified file.
#
# The [`%matplotlib` magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-matplotlib) allows specifying the [backend](https://matplotlib.org/stable/tutorials/introductory/usage.html#backends) used by Matplotlib to display plots, with there various system-dependent [built-in option](https://matplotlib.org/stable/tutorials/introductory/usage.html#the-builtin-backends) as well as additional backends that can be installed as extensions such as [`ipympl`](https://github.com/matplotlib/ipympl) which uses [Jupyter's widget framework](https://ipywidgets.readthedocs.io/en/latest/) to enable interactive features on plots in Jupyter notebooks. A list of the backends current available can be obtained by running

# %%
# %matplotlib --list

# %% [markdown]
# Running `%matplotlib inline` instructs Matplotlib to use a backend which displays plots as static images 'inline' in the cell output area. In recent versions of Matplotlib and Jupyter this backend is automatically set when importing `matplotlib.pyplot` within a Jupyter notebook and so the `%matplotlib inline` command is not strictly necessary in this case, however you will often still see this command in older notebooks. As the command will have no additional effect if `matplotlib.pyplot` has been imported it is safe to include it to for example ensure compatibility with older Jupyter / Matplotlib versions

# %%
# %matplotlib inline

# %% [markdown]
# ## Basic plot elements - figures and axes
#
# As a first example we recreate the basic line plot we constructed previously using the `pylab` interface.

# %%
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
lines = ax.plot([0, 1, 2, 3, 4], [1, 5, 3, 7, -11])

# %% [markdown]
# We have introduced three new functions here and corresponding Python types. The `plt.figure` function instructs Matplotlib to create and return a new [`Figure` object](https://matplotlib.org/stable/tutorials/introductory/usage.html#figure) which holds all of the elements corresponding to a single figure, such as one or more plot axes and other elements such as an overall figure title. The `plt.figure` function takes various optional arguments; here we pass a tuple of the figure dimensions in inches `(width, height)` as the `figsize` keyword argument. Note that the actual displayed size of the plot on screen will also depend on the resolution of your display, this can be adjusted for by also specifying the optional `dpi` (dots per inch) keyword argument to `plt.figure`.
#
# A `Figure` object is itself mainly just a container with its main function to allow adding the [`AxesSubplot` objects](https://matplotlib.org/stable/tutorials/introductory/usage.html#axes) on which we will actually produce plots. A simple way to add an axes to a `Figure` instance is using the `add_subplot` method which returns an `AxesSubplot` object. This optionally takes arguments to specify the number and location of plots when adding multiple axes to a single figure, however here we only require a single axes so we just call `add_subplot` on the `Figure` object `fig` we created in the previous line without any arguments.
#
# The `AxesSubplot` object exposes various methods for actually producing plots. One of the more generally useful methods is `plot`, which is almost identical to the `plt.plot` function we encountered previously. The value returned by `ax.plot` is a list of `Line2D` instances corresponding to the plotted line(s): in this case we plotted only one line so the list has only one element. The `Line2D` object can be used to update or access the properties of the plotted line after the initial `ax.plot` call.
#
# As creating a figure and adding a subplot (axes) to it is such a common operation, Matplotlib provides a function `plt.subplots` which combines the functionality of the `plt.figure` and `fig.add_subplot` functions. The `plt.subplots` function as the name suggests can be used to generate multiple subplots on a single figure (we will demonstrate this in the following section) but with its default arguments will just generate a figure with a single axes. Keyword arguments to `plt.figure` will be passed through from `plt.subplots` so for example we can set the figure size by specifying the `figsize` argument. The `plt.subplots` function returns a pair of objects the first of which is the `Figure` object and the second the one or more `AxesSubplot` instances created. We can therefore recreate the above plot as follows.

# %%
fig, ax = plt.subplots(figsize=(6, 4))
lines = ax.plot([0, 1, 2, 3, 4], [1, 5, 3, 7, -11])

# %% [markdown]
# ## Creating multiple axes on a figure
#
# As mentioned above the `plt.subplots` function can also be used to create figures with multiple subplots, specifically a rectlinear grid of axes. There first two positional arguments to `plt.subplots` are respectively `nrows`, which specifies the number of rows in the grid of axes, and `ncol` which specifies the number of columns in the axes grid. For example the following cell will create a figure with 2&times;3 grid of (empty) axes.

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

# %% [markdown]
# When called with arguments that create multiple subplots, the second argument returned by `plt.subplots` is a NumPy array of `AxesSubplot` objects. For example we can inspect the `axes` object just created by displaying its string representation.

# %%
axes

# %% [markdown]
# We can therefore use NumPy's convenient array indexing syntax for accessing invidual axes, with the first index corresponding to the row (vertical) dimension and the second to the column (horizontal) direction. For example the following cell plots a grid of simple polynomial functions on the domain [-1, 1] with varying exponents and coefficients, with a different function being plotted on each axis. 

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
x = np.linspace(-1, 1, 100)
axes[0, 0].plot(x, -x)
axes[0, 1].plot(x, -x**2)
axes[0, 2].plot(x, -x**3)
axes[1, 0].plot(x, x)
axes[1, 1].plot(x, x**2)
axes[1, 2].plot(x, x**3)

# %% [markdown]
# ## Using loops to avoid repetition
#
# While individually accessing axes like this can be useful, in cases such as this where there is a lot of commonality between the plots we can often avoid the repetition in our code by instead using loops to iterate over the axes objects. When we iterate over a NumPy array we return the array *slices* corresponding to indexing only the first dimension. As the first dimension for the `axes` object returned by `plt.subplots` corresponds to the row, a for loops of the form `for axes_row in axes:` will loop over each row of axes. In our case as each row contains three columns, the `axes_row` object will itself be another (one dimensional) NumPy array, with the leading (and only) array dimension now corresponding to the column index. To access the individual axes in each row we can *nest* a further loop which iterates over the elements in `axes_row`. For example, the following cell plots the identity function on all axes.

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
x = np.linspace(-1, 1, 100)
for axes_row in axes:
    for ax in axes_row:
        ax.plot(x, x)

# %% [markdown]
# Plotting the same six times is not very interesting or useful. A common pattern is that we wish to loop over one or more sequences and create a subplot using for each of the items (or combinations of items) in the sequence(s). A handy inbuilt Python function for iterating over several iterable objects in unison is [`zip`](https://docs.python.org/3.3/library/functions.html#zip) - it accepts as argument one or more iterable objects and returns an object which iterates over *tuples* with the *i*th tuple containing the items at the *i*th position in each passed iterable, in the order the iterables are passed to `zip`. 
#
# For example the following cell iterates over pairs of character and integers from respectively a string and `range` object.

# %%
for c, i in zip('abc', range(3)):
    print(c, i)

# %% [markdown]
# We can use `zip` to combine the nested iteration over the axes with iterating over different coefficients and exponents to plot on each row and column of the axes grid. For example, the following cell plots the same set of polynomial functions plotted previously but avoids the repetitive calls to `plot` by using nested loops.

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
x = np.linspace(-1, 1, 100)
for axes_row, coefficient in zip(axes, (-1, 1)):
    for ax, exponent in zip(axes_row, (1, 2, 3)):
        ax.plot(x, coefficient * x**exponent)

# %% [markdown]
# ## Setting axes properties
#
# As well as allowing plotting using the `AxesSubplot.plot` method, `AxesSubplot` objects also expose other methods which can used to customise the appearance of the plot. Previously we encountered the `plt.xlabel`, `plt.ylabel` and `plt.title` functions in the Matplotlib `pylab` interface, for setting respectively the *x*-axis label, *y*-axis label and title of the current axis. The `AxesSubplot` object has methods `AxesSubplot.set_xlabel`, `AxesSubplot.set_ylabel` and `AxesSubplot.set_title` which perform the same roles for the corresponding to a particular `AxesSubplot` object. If we wish to set multiple properties of an axis, we can also use the `AxesSubplot.set` batch property setter method, which takes keyword arguments corresponding to properties that can be set by the `AxesSubplot.set_*` methods. For example the following cell adds labels to the *x*- and *y*-axis for each plot and a title describing the plotted function.

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
x = np.linspace(-1, 1, 100)
for axes_row, coefficient in zip(axes, (-1, 1)):
    for ax, exponent in zip(axes_row, (1, 2, 3)):
        ax.plot(x, coefficient * x**exponent)
        ax.set(xlabel='$x$', ylabel='$y$', title=f'$y = {coefficient} x^{exponent}$')

# %% [markdown]
# ## Improving the plot layout
#
# Once we start adding labels and titles to multiple axes it is common for plot elements to start overlapping as in the plot produced by the previous cell. Matplotlib `Figure` objects have a useful `Figure.tight_layout` method which will automatically adjust the padding around subplots to try to avoid any overlapping elements. This method should be called after all plots, labels and titles have been added so that all of the displayed elements are taken into account when adjusting the layout. For example the following cell replots the same plot as the previous cell but adds a `fig.tight_layout()` call at the end, with this producing a much better plot layout.

# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
x = np.linspace(-1, 1, 100)
for axes_row, coefficient in zip(axes, (-1, 1)):
    for ax, exponent in zip(axes_row, (1, 2, 3)):
        ax.plot(x, coefficient * x**exponent)
        ax.set(xlabel='$x$', ylabel='$y$', title=f'$y = {coefficient} x^{exponent}$')
fig.tight_layout()

# %% [markdown]
# ## Plotting multiple lines on each plot
#
# Creating a new subplot for each plotted line can sometimes be overkill. For example if rather than wanting plot polynomial functions for two different coefficients, we wished to plot for six different coefficients (and three exponents), we would need a 6&times;3 grid of plots which would make for either a very large or very cramped figure, while also making it difficult to compare the relationships between the plots for different coefficients. In this case we might to decide to plot multiple lines corresponding to different coefficient values on a single subplot. We can add multiple lines to a subplot by making multiple calls to the `AxesSubplot.plot` method. By default each successive plot [will cycle through a sequence of ten colours](https://matplotlib.org/stable/gallery/color/color_cycle_default.html). For example, the following cell plots a single row of three axes, each corresponding to a different exponent and with a series of lines corresponding to polynomials with six different coefficients linearly spaced in [-1, 1] plotted on each axis.

# %%
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
x = np.linspace(-1, 1, 100)
for ax, exponent in zip(axes, [1, 2, 3]):
    for coefficient in np.linspace(-1, 1, 6):
        ax.plot(x, coefficient * (x ** exponent))
fig.tight_layout()

# %% [markdown]
# When plotting multiple lines on an axis as here, it is good practice to include a legend to allow uniquely identifying each different plotted line. The `AxesSubplot.legend` method allows adding a legend to an axis; as with the `plt.legend` function encountered previously there are [multiple ways of associating labels with each plot element](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html). The simplest is often to add a `label` keyword argument to each `AxesSubplot.plot` call with the required string label describing what is being plotted. For example the following cell recreates the plot from the previous cell but with the addition of axis labels, a title and a legend on each subplot. As demonstrated here, the `AxesSubplot.legend` method takes various keyword arguments which can be used to customise the styling and layout of the generated legend.

# %%
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
x = np.linspace(-1, 1, 100)
for ax, exponent in zip(axes, [1, 2, 3]):
    for coefficient in np.linspace(-1, 1, 6):
        ax.plot(x, coefficient * (x ** exponent), label=f'$\\alpha = {coefficient:.2g}$')
    ax.set(xlabel='$x$', ylabel='$y$', title=f'$y = \\alpha x^{exponent}$')
    ax.legend(ncol=2, frameon=False, handlelength=1, columnspacing=1, labelspacing=0)
fig.tight_layout()

# %% [markdown]
# ## Saving figures

# %% [markdown]
# We need to be able to save figures to disk, in order to use them externally, for example in articles. Matplotlib `Figure` objects provide [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) method for this purpose. This accepts one positional argument corresponding to the file path to save the generated figure image file to; this should include an extension which specifies the file format to use. For example the following cell saves the figure produced in the previous cell into a new [*scalable vector graphics* (SVG)](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) file `polynomials.svg` in the current directory.

# %%
fig.savefig('polynomials.svg')

# %% [markdown]
# If you are running this notebook interactively in Jupyter Lab, you should be able to see the generated image file in the file browser pane accessible from the left toolbar (and you can preview the file in a new tab within Jupyter Lab by double clicking on it in the file browser).
#
# As well as SVG output, Matplotlib also supports saving figures in various other formats. A dictionary mapping from file extensions to the names of file formats supported by the backend being used locally can be accessed using the code in the following cell.

# %%
fig.canvas.get_supported_filetypes()

# %% [markdown]
# ## Learning more

# %% [markdown]
# We have only explored a small number of the features and plot types offered by Matplotlib here, with there so much more to learn about Matplotlib: pie charts, bar charts, heat maps, three-dimensional plotting, animated plots, and so on. You can learn all this via the excellent documentation on the [Matplotlib Website](http://matplotlib.org/#). You should try to get comfortable with Matplotlib, so please use some time in class, or at home, to work your way through a bunch of the [examples](http://matplotlib.org/examples/index.html).
