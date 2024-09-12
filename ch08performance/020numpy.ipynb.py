# ---
# jupyter:
#   jekyll:
#     display_name: NumPy
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # NumPy for Performance

# %% [markdown]
# ## NumPy constructors

# %% [markdown]
# We saw previously that NumPy's core type is the `ndarray`, or N-Dimensional Array:

# %%
import numpy as np
np.zeros([3, 4, 2, 5])[2, :, :, 1]

# %% [markdown]
# The real magic of numpy arrays is that most python operations are applied, quickly, on an elementwise basis:

# %%
x = np.arange(0, 256, 4).reshape(8, 8)

# %%
y = np.zeros((8, 8))

# %%
# %%timeit
for i in range(8):
    for j in range(8):
        y[i][j] = x[i][j] + 10

# %%
x + 10

# %% [markdown]
# Numpy's mathematical functions also happen this way, and are said to be "vectorized" functions.

# %%
np.sqrt(x)

# %% [markdown]
# Numpy contains many useful functions for creating matrices. In our earlier lectures we've seen `linspace` and `arange` for evenly spaced numbers.

# %%
np.linspace(0, 10, 21)

# %%
np.arange(0, 10, 0.5)

# %% [markdown]
#  Here's one for creating matrices like coordinates in a grid:

# %%
xmin = -1.5
ymin = -1.0
xmax = 0.5
ymax = 1.0
resolution = 300
xstep = (xmax - xmin) / resolution
ystep = (ymax - ymin) / resolution

ymatrix, xmatrix = np.mgrid[ymin:ymax:ystep, xmin:xmax:xstep]

# %%
print(ymatrix)

# %% [markdown]
# We can add these together to make a grid containing the complex numbers we want to test for membership in the Mandelbrot set.

# %%
values = xmatrix + 1j * ymatrix

# %%
print(values)

# %% [markdown]
# ## Arraywise Algorithms

# %% [markdown]
# We can use this to apply the mandelbrot algorithm to whole *ARRAYS*

# %%
z0 = values
z1 = z0 * z0 + values
z2 = z1 * z1 + values
z3 = z2 * z2 + values

# %%
print(z3)


# %% [markdown]
# So can we just apply our `mandel1` function to the whole matrix?

# %%
def mandel1(position,limit=50):
    value = position
    while abs(value) < 2:
        limit -= 1
        value = value**2 + position
        if limit < 0:
            return 0
    return limit


# %%
mandel1(values)

# %% [markdown]
# No. The *logic* of our current routine would require stopping for some elements and not for others. 

# %% [markdown]
# We can ask numpy to **vectorise** our method for us:

# %%
mandel2 = np.vectorize(mandel1)

# %%
data5 = mandel2(values)

# %%
from matplotlib import pyplot as plt
# %matplotlib inline
plt.imshow(data5, interpolation='none')

# %% [markdown]
# Is that any faster?

# %%
# %%timeit
data5 = mandel2(values)


# %% [markdown]
# This is not significantly faster. When we use *vectorize* it's just hiding an plain old python for loop under the hood. We want to make the loop over matrix elements take place in the "**C Layer**".

# %% [markdown]
# What if we just apply the Mandelbrot algorithm without checking for divergence until the end:

# %%
def mandel_numpy_explode(position, limit=50):
    value = position
    while limit > 0:
        limit -= 1
        value = value**2 + position
        diverging = abs(value) > 2

        
    return abs(value) < 2

# %%
data6 = mandel_numpy_explode(values)


# %% [markdown]
# OK, we need to prevent it from running off to $\infty$

# %%
def mandel_numpy(position, limit=50):
    value = position
    while limit > 0:
        limit -= 1
        value = value**2 + position
        diverging = abs(value) > 2
        # Avoid overflow
        value[diverging] = 2
        
    return abs(value) < 2


# %%
data6 = mandel_numpy(values)

# %%
# %%timeit

data6 = mandel_numpy(values)

# %%
from matplotlib import pyplot as plt
# %matplotlib inline
plt.imshow(data6, interpolation='none')

# %% [markdown]
# Wow, that was TEN TIMES faster.

# %% [markdown]
# There's quite a few NumPy tricks there, let's remind ourselves of how they work:

# %%
diverging = abs(z3) > 2
z3[diverging] = 2

# %% [markdown]
# When we apply a logical condition to a NumPy array, we get a logical array.

# %%
x = np.arange(10)
y = np.ones([10]) * 5
z = x > y

# %%
x

# %%
y

# %%
print(z)

# %% [markdown]
# Logical arrays can be used to index into arrays:

# %%
x[x>3]

# %%
x[np.logical_not(z)]

# %% [markdown]
# And you can use such an index as the target of an assignment:

# %%
x[z] = 5
x


# %% [markdown]
# Note that we didn't compare two arrays to get our logical array, but an array to a scalar integer -- this was broadcasting again.

# %% [markdown]
# ## More Mandelbrot

# %% [markdown]
# Of course, we didn't calculate the number-of-iterations-to-diverge, just whether the point was in the set.

# %% [markdown]
# Let's correct our code to do that:
#

# %%
def mandel4(position,limit=50):
    value = position
    diverged_at_count = np.zeros(position.shape)
    while limit > 0:
        limit -= 1
        value = value**2 + position
        diverging = abs(value) > 2
        first_diverged_this_time = np.logical_and(diverging, 
                                                  diverged_at_count == 0)
        diverged_at_count[first_diverged_this_time] = limit
        value[diverging] = 2
        
    return diverged_at_count


# %%
data7 = mandel4(values)

# %%
plt.imshow(data7, interpolation='none')

# %%
# %%timeit

data7 = mandel4(values)


# %% [markdown]
# Note that here, all the looping over mandelbrot steps was in Python, but everything below the loop-over-positions happened in C. The code was amazingly quick compared to pure Python.

# %% [markdown]
# Can we do better by avoiding a square root?

# %%
def mandel5(position, limit=50):
    value = position
    diverged_at_count = np.zeros(position.shape)
    while limit > 0:
        limit -= 1
        value = value**2 + position
        diverging = value * np.conj(value) > 4
        first_diverged_this_time = np.logical_and(diverging, diverged_at_count == 0)
        diverged_at_count[first_diverged_this_time] = limit
        value[diverging] = 2
        
    return diverged_at_count


# %%
# %%timeit

data8 = mandel5(values)

# %% [markdown]
# Probably not worth the time I spent thinking about it!

# %% [markdown]
# ## NumPy Testing

# %% [markdown]
# Now, let's look at calculating those residuals, the differences between the different datasets.

# %%
data8 = mandel5(values)
data5 = mandel2(values)

# %%
np.sum((data8 - data5)**2)

# %% [markdown]
# For our non-numpy datasets, numpy knows to turn them into arrays:

# %%
xmin = -1.5
ymin = -1.0
xmax = 0.5
ymax = 1.0
resolution = 300
xstep = (xmax-xmin)/resolution
ystep = (ymax-ymin)/resolution
xs = [(xmin + (xmax - xmin) * i / resolution) for i in range(resolution)]
ys = [(ymin + (ymax - ymin) * i / resolution) for i in range(resolution)]
data1 = [[mandel1(complex(x, y)) for x in xs] for y in ys]
sum(sum((data1 - data7)**2))

# %% [markdown]
# But this doesn't work for pure non-numpy arrays

# %%
data2 = []
for y in ys:
    row = []
    for x in xs:
        row.append(mandel1(complex(x, y)))
    data2.append(row)

# %%
data2 - data1

# %% [markdown]
# So we have to convert to NumPy arrays explicitly:

# %%
sum(sum((np.array(data2) - np.array(data1))**2))

# %% [markdown]
# NumPy provides some convenient assertions to help us write unit tests with NumPy arrays:

# %%
x = [1e-5, 1e-3, 1e-1]
y = np.arccos(np.cos(x))
y

# %%
np.testing.assert_allclose(x, y, rtol=1e-6, atol=1e-20)

# %%
np.testing.assert_allclose(data7, data1)


# %% [markdown]
# ## Arraywise operations are fast

# %% [markdown]
# Note that we might worry that we carry on calculating the mandelbrot values for points that have already diverged.

# %%
def mandel6(position, limit=50):
    value = np.zeros(position.shape) + position
    calculating = np.ones(position.shape, dtype='bool')
    diverged_at_count = np.zeros(position.shape)
    while limit > 0:
        limit -= 1
        value[calculating] = value[calculating]**2 + position[calculating]
        diverging_now = np.zeros(position.shape, dtype='bool')
        diverging_now[calculating] = value[calculating] * \
                                     np.conj(value[calculating])>4
        calculating = np.logical_and(calculating,
                                     np.logical_not(diverging_now))
        diverged_at_count[diverging_now] = limit
        
    return diverged_at_count


# %%
data8 = mandel6(values)

# %%
# %%timeit

data8 = mandel6(values)

# %%
plt.imshow(data8, interpolation='none')

# %% [markdown]
# This was **not faster** even though it was **doing less work**

# %% [markdown]
# This often happens: on modern computers, **branches** (if statements, function calls) and **memory access** is usually the rate-determining step, not maths.

# %% [markdown]
# Complicating your logic to avoid calculations sometimes therefore slows you down. The only way to know is to **measure**

# %% [markdown]
# ## Indexing with arrays

# %% [markdown]
# We've been using Boolean arrays a lot to get access to some elements of an array. We can also do this with integers:

# %%
x = np.arange(64)
y = x.reshape([8,8])
y

# %%
y[[2, 5]]

# %%
y[[0, 2, 5], [1, 2, 7]]

# %% [markdown]
# We can use a : to indicate we want all the values from a particular axis:

# %%
y[0:4:2, [0, 2]]

# %% [markdown]
# We can mix array selectors, boolean selectors, :s and ordinary array seqeuencers:

# %%
z = x.reshape([4, 4, 4])
z

# %%
z[:, [1, 3], 0:3]

# %% [markdown]
# We can manipulate shapes by adding new indices in selectors with np.newaxis:

# %%
z[:, np.newaxis, [1, 3], 0].shape

# %% [markdown]
# When we use basic indexing with integers and : expressions, we get a **view** on the matrix so a copy is avoided:

# %%
a = z[:, :, 2]
a[0, 0] = -500
z

# %% [markdown]
# We can also use ... to specify ": for as many as possible intervening axes":

# %%
z[1]

# %%
z[...,2]


# %% [markdown]
# However, boolean mask indexing and array filter indexing always causes a copy.

# %% [markdown]
# Let's try again at avoiding doing unnecessary work by using new arrays containing the reduced data instead of a mask:

# %%
def mandel7(position, limit=50):
    positions = np.zeros(position.shape) + position
    value = np.zeros(position.shape) + position
    indices = np.mgrid[0:values.shape[0], 0:values.shape[1]]
    diverged_at_count = np.zeros(position.shape)
    while limit > 0:
        limit -= 1
        value = value**2 + positions
        diverging_now = value * np.conj(value) > 4
        diverging_now_indices = indices[:, diverging_now]
        carry_on = np.logical_not(diverging_now)

        value = value[carry_on]
        indices = indices[:, carry_on]
        positions = positions[carry_on]
        diverged_at_count[diverging_now_indices[0,:],
                          diverging_now_indices[1,:]] = limit

    return diverged_at_count


# %%
data9 = mandel7(values)

# %%
plt.imshow(data9, interpolation='none')

# %%
# %%timeit

data9 = mandel7(values)

# %% [markdown]
# Still slower. Probably due to lots of copies -- the point here is that you need to *experiment* to see which optimisations will work. Performance programming needs to be empirical.

# %% [markdown]
# ## Profiling

# %% [markdown]
# We've seen how to compare different functions by the time they take to run. However, we haven't obtained much information about where the code is spending more time. For that we need to use a profiler. IPython offers a profiler through the `%prun` magic. Let's use it to see how it works:

# %%
# %prun mandel7(values)

# %% [markdown]
# `%prun` shows a line per each function call ordered by the total time spent on each of these. However, sometimes a line-by-line output may be more helpful. For that we can use the `line_profiler` package (you need to install it using `pip`). Once installed you can activate it in any notebook by running:

# %%
# %load_ext line_profiler

# %% [markdown]
# And the `%lprun` magic should be now available:

# %%
# %lprun -f mandel7 mandel7(values)

# %% [markdown]
# Here, it is clearer to see which operations are keeping the code busy.
