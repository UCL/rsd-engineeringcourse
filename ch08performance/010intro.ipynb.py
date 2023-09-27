# ---
# jupyter:
#   jekyll:
#     display_name: Two Mandelbrots
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Performance programming

# %% [markdown]
# We've spent most of this course looking at how to make code readable and reliable. For research work, it is often also important that code is efficient: that it does what it needs to do *quickly*.

# %% [markdown]
# It is very hard to work out beforehand whether code will be efficient or not: it is essential to *Profile* code, to measure its performance, to determine what aspects of it are slow.

# %% [markdown]
# When we looked at Functional programming, we claimed that code which is conceptualised in terms of actions on whole data-sets rather than individual elements is more efficient. Let's measure the performance of some different ways of implementing some code and see how they perform.

# %% [markdown]
# ## Two Mandelbrots

# %% [markdown]
# You're probably familiar with a famous fractal called the [Mandelbrot Set](https://www.youtube.com/watch?v=ZDU40eUcTj0).

# %% [markdown]
# For a complex number $c$, $c$ is in the Mandelbrot set if the series $z_{i+1}=z_{i}^2+c$ (With $z_0=c$) stays close to $0$.
# Traditionally, we plot a color showing how many steps are needed for $\left|z_i\right|>2$, whereupon we are sure the series will diverge.

# %% [markdown]
# Here's a trivial python implementation:

# %%
def mandel1(position, limit=50):
    
    value = position
    
    while abs(value) < 2:
        limit -= 1        
        value = value**2 + position
        if limit < 0:
            return 0
        
    return limit


# %%
xmin = -1.5
ymin = -1.0
xmax = 0.5
ymax = 1.0
resolution = 300
xstep = (xmax - xmin) / resolution
ystep = (ymax - ymin) / resolution
xs = [(xmin + (xmax - xmin) * i / resolution) for i in range(resolution)]
ys = [(ymin + (ymax - ymin) * i / resolution) for i in range(resolution)]

# %%
# %%timeit
data = [[mandel1(complex(x, y)) for x in xs] for y in ys]

# %%
data1 = [[mandel1(complex(x, y)) for x in xs] for y in ys]

# %%
# %matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(data1, interpolation='none')

# %% [markdown]
# We will learn this lesson how to make a version of this code which works Ten Times faster:

# %%
import numpy as np
def mandel_numpy(position,limit=50):
    value = position
    diverged_at_count = np.zeros(position.shape)
    while limit > 0:
        limit -= 1
        value = value**2+position
        diverging = value * np.conj(value) > 4
        first_diverged_this_time = np.logical_and(diverging, diverged_at_count == 0)
        diverged_at_count[first_diverged_this_time] = limit
        value[diverging] = 2
        
    return diverged_at_count


# %%
ymatrix, xmatrix = np.mgrid[ymin:ymax:ystep, xmin:xmax:xstep]

# %%
values = xmatrix + 1j * ymatrix

# %%
data_numpy = mandel_numpy(values)

# %%
# %matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(data_numpy, interpolation='none')

# %%
# %%timeit
data_numpy = mandel_numpy(values)

# %% [markdown]
# Note we get the same answer:

# %%
sum(sum(abs(data_numpy - data1)))
