# ---
# jupyter:
#   jekyll:
#     display_name: Faster Mandelbrots?
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

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
def mandel1(position, limit=50):
    value = position    
    while abs(value) < 2:
        limit -= 1        
        value = value**2 + position        
        if limit < 0:
            return 0        
    return limit


# %%
data1 = [[mandel1(complex(x, y)) for x in xs] for y in ys]

# %% [markdown]
# ## Many Mandelbrots

# %% [markdown]
# Let's compare our naive python implementation which used a list comprehension, taking 662ms, with the following:

# %%
# %%timeit
data2 = []
for y in ys:
    row = []
    for x in xs:
        row.append(mandel1(complex(x, y)))
    data2.append(row)

# %%
data2 = []
for y in ys:
    row = []
    for x in xs:
        row.append(mandel1(complex(x, y)))
    data2.append(row)

# %% [markdown]
# Interestingly, not much difference. I would have expected this to be slower, due to the normally high cost of **appending** to data.

# %%
from matplotlib import pyplot as plt
# %matplotlib inline
plt.imshow(data2, interpolation='none')

# %% [markdown]
# We ought to be checking if these results are the same by comparing the values in a test, rather than re-plotting. This is cumbersome in pure Python, but easy with NumPy, so we'll do this later.

# %% [markdown]
# Let's try a pre-allocated data structure:

# %%
data3 = [[0 for i in range(resolution)] for j in range(resolution)]

# %%
# %%timeit
for j, y in enumerate(ys):
    for i, x in enumerate(xs):
        data3[j][i] = mandel1(complex(x, y))

# %%
for j, y in enumerate(ys):
    for i, x in enumerate(xs):
        data3[j][i] = mandel1(complex(x, y))

# %%
plt.imshow(data3, interpolation='none')

# %% [markdown]
# Nope, no gain there. 

# %% [markdown]
# Let's try using functional programming approaches:

# %%
# %%timeit
data4 = []
for y in ys:
    bind_mandel = lambda x: mandel1(complex(x, y))
    data4.append(list(map(bind_mandel, xs)))

# %%
data4 = []
for y in ys:
    bind_mandel = lambda x: mandel1(complex(x, y))
    data4.append(list(map(bind_mandel, xs)))

# %%
plt.imshow(data4, interpolation='none')

# %% [markdown]
# That was a tiny bit slower.

# %% [markdown]
# So, what do we learn from this? Our mental image of what code should be faster or slower is often wrong, or doesn't make much difference. The only way to really improve code performance is empirically, through measurements.
