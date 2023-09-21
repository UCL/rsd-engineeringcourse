# ---
# jupyter:
#   jekyll:
#     display_name: Numerical Python
#   jupytext:
#     notebook_metadata_filter: kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## NumPy

# %% [markdown]
# ### The Scientific Python Trilogy

# %% [markdown]
# Why is Python so popular for research work?

# %% [markdown]
# MATLAB has typically been the most popular "language of technical computing", with strong built-in support for efficient numerical analysis with matrices (the *mat* in MATLAB is for Matrix, not Maths), and plotting.

# %% [markdown]
# Other dynamic languages have cleaner, more logical syntax (Ruby, Haskell)

# %% [markdown]
# But Python users developed three critical libraries, matching the power of MATLAB for scientific work:

# %% [markdown]
# * Matplotlib, the plotting library created by [John D. Hunter](https://en.wikipedia.org/wiki/John_D._Hunter)
# * NumPy, a fast matrix maths library created by [Travis Oliphant](https://en.wikipedia.org/wiki/Travis_Oliphant)
# * IPython, the precursor of the notebook, created by [Fernando Perez](https://en.wikipedia.org/wiki/Fernando_P%nC3%A9rez_(software_developer))

# %% [markdown]
# By combining a plotting library, a matrix maths library, and an easy-to-use interface allowing live plotting commands
# in a persistent environment, the powerful capabilities of MATLAB were matched by a free and open toolchain.

# %% [markdown]
# We've learned about Matplotlib and IPython in this course already. NumPy is the last part of the trilogy.

# %% [markdown]
# ### Limitations of Python Lists

# %% [markdown]
# The normal Python list is just one dimensional. To make a matrix, we have to nest Python lists:

# %%
x = [list(range(5)) for N in range(5)]

# %%
x

# %%
x[2][2]

# %% [markdown]
# Applying an operation to every element is a pain:

# %%
x + 5

# %%
[[elem + 5 for elem in row] for row in x]

# %% [markdown]
# Common useful operations like transposing a matrix or reshaping a 10 by 10 matrix into a 20 by 5 matrix are not easy to code in raw Python lists.

# %% [markdown]
# ### The NumPy array

# %% [markdown]
# NumPy's array type represents a multidimensional matrix $M_{i,j,k...n}$

# %% [markdown]
# The NumPy array seems at first to be just like a list. For example, we can index it and iterate over it:

# %%
import numpy as np
my_array = np.array(range(5))

# %%
my_array

# %%
my_array[2]

# %%
for element in my_array:
    print("Hello" * element)

# %% [markdown]
# We can also see our first weakness of NumPy arrays versus Python lists:

# %%
my_array.append(4)

# %% [markdown]
# For NumPy arrays, you typically don't change the data size once you've defined your array,
# whereas for Python lists, you can do this efficiently. However, you get back lots of goodies in return...

# %% [markdown]
# ### Elementwise Operations

# %% [markdown]
# Most operations can be applied element-wise automatically!

# %%
my_array + 2

# %% [markdown]
# These "vectorized" operations are very fast: (the `%%timeit` magic reports how long it takes to run a cell; there is [more information](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) available if interested)

# %%
import numpy as np
big_list = range(10000)
big_array = np.arange(10000)

# %%
# %%timeit
[x**2 for x in big_list]

# %%
# %%timeit
big_array**2

# %% [markdown]
# ### arange and linspace

# %% [markdown]
# NumPy has two methods for quickly defining evenly-spaced arrays of (floating-point) numbers. These can be useful, for example, in plotting.
#
# The first method is `arange`:

# %%
x = np.arange(0, 10, 0.1)  # Start, stop, step size

# %% [markdown]
# This is similar to Python's `range`, although note that we can't use non-integer steps with the latter!

# %%
y = list(range(0, 10, 0.1))

# %% [markdown]
# The second method is `linspace`:

# %%
import math
values = np.linspace(0, math.pi, 100)  # Start, stop, number of steps

# %%
values

# %% [markdown]
# Regardless of the method used, the array of values that we get can be used in the same way.
#
# In fact, NumPy comes with "vectorised" versions of common functions which work element-by-element when applied to arrays:

# %%
# %matplotlib inline

from matplotlib import pyplot as plt
plt.plot(values, np.sin(values))

# %% [markdown]
# So we don't have to use awkward list comprehensions when using these.

# %% [markdown]
# ### Multi-Dimensional Arrays

# %% [markdown]
# NumPy's true power comes from multi-dimensional arrays:

# %%
np.zeros([3, 4, 2])  # 3 arrays with 4 rows and 2 columns each

# %% [markdown]
# Unlike a list-of-lists in Python, we can reshape arrays:

# %%
x = np.array(range(40))
x

# %%
y = x.reshape([4, 5, 2])
y

# %% [markdown]
# And index multiple columns at once:

# %%
y[3, 2, 1]

# %% [markdown]
# Including selecting on inner axes while taking all from the outermost:

# %%
y[:, 2, 1]

# %% [markdown]
# And subselecting ranges:

# %%
y[2:, :1, :]  # Last 2 axes, 1st row, all columns

# %% [markdown]
# And [transpose](https://en.wikipedia.org/wiki/Transpose) arrays:

# %%
y.transpose()

# %% [markdown]
# You can get the dimensions of an array with `shape`:

# %%
y.shape

# %%
y.transpose().shape

# %% [markdown]
# Some numpy functions apply by default to the whole array, but can be chosen to act only on certain axes:

# %%
x = np.arange(12).reshape(4,3)
x

# %%
x.mean(1)  # Mean along the second axis, leaving the first.

# %%
x.mean(0)  # Mean along the first axis, leaving the second.

# %%
x.mean()  # mean of all axes

# %% [markdown]
# ### Array Datatypes

# %% [markdown]
# A Python `list` can contain data of mixed type:

# %%
x = ['hello', 2, 3.4]

# %%
type(x[2])

# %%
type(x[1])

# %% [markdown]
# A NumPy array always contains just one datatype:

# %%
np.array(x)

# %% [markdown]
# NumPy will choose the least-generic-possible datatype that can contain the data:

# %%
y = np.array([2, 3.4])

# %%
y

# %% [markdown]
# You can access the array's `dtype`, or check the type of individual elements:

# %%
y.dtype

# %%
type(y[0])

# %%
z = np.array([3, 4, 5])
z

# %%
type(z[0])

# %% [markdown]
# The results are, when you get to know them, fairly obvious string codes for datatypes: 
#     NumPy supports all kinds of datatypes beyond the python basics.

# %% [markdown]
# NumPy will convert python type names to dtypes:

# %%
x = [2, 3.4, 7.2, 0]

# %%
int_array = np.array(x, dtype=int)

# %%
float_array = np.array(x, dtype=float)

# %%
int_array

# %%
float_array

# %%
int_array.dtype

# %%
float_array.dtype

# %% [markdown]
# ### Broadcasting

# %% [markdown]
# This is another really powerful feature of NumPy.

# %% [markdown]
# By default, array operations are element-by-element:

# %%
np.arange(5) * np.arange(5)

# %% [markdown]
# If we multiply arrays with non-matching shapes we get an error:

# %%
np.arange(5) * np.arange(6)

# %%
np.zeros([2,3]) * np.zeros([2,4])

# %%
m1 = np.arange(100).reshape([10, 10])

# %%
m2 = np.arange(100).reshape([10, 5, 2])

# %%
m1 + m2

# %% [markdown]
# Arrays must match in all dimensions in order to be compatible:

# %%
np.ones([3, 3]) * np.ones([3, 3]) # Note elementwise multiply, *not* matrix multiply.

# %% [markdown]
# **Except**, that if one array has any Dimension 1, then the data is **REPEATED** to match the other.

# %%
col = np.arange(10).reshape([10, 1])
col

# %%
row = col.transpose()
row

# %%
col.shape # "Column Vector"

# %%
row.shape # "Row Vector"

# %%
row + col

# %%
10 * row + col

# %% [markdown]
# This works for arrays with more than one unit dimension. 

# %% [markdown]
# ### Newaxis

# %% [markdown]
# Broadcasting is very powerful, and numpy allows indexing with `np.newaxis` to temporarily create new one-long dimensions on the fly.

# %%
import numpy as np
x = np.arange(10).reshape(2, 5)
y = np.arange(8).reshape(2, 2, 2)

# %%
x

# %%
y

# %%
x[:, :, np.newaxis, np.newaxis].shape

# %%
y[:, np.newaxis, :, :].shape

# %%
res = x[:, :, np.newaxis, np.newaxis] * y[:, np.newaxis, :, :]

# %%
res.shape

# %%
np.sum(res)

# %% [markdown]
# Note that `newaxis` works because a $3 \times 1 \times 3$ array and a $3 \times 3$ array contain the same data,
# differently shaped:

# %%
threebythree = np.arange(9).reshape(3, 3)
threebythree

# %%
threebythree[:, np.newaxis, :]

# %% [markdown]
# ### Dot Products

# %% [markdown]
# NumPy multiply is element-by-element, not a dot-product:

# %%
a = np.arange(9).reshape(3, 3)
a

# %%
b = np.arange(3, 12).reshape(3, 3)
b

# %%
a * b

# %% [markdown]
# To get a dot-product, (matrix inner product) we can use a built in function:

# %%
np.dot(a, b)

# %% [markdown]
# Though it is possible to represent this in the algebra of broadcasting and newaxis:

# %%
a[:, :, np.newaxis].shape

# %%
b[np.newaxis, :, :].shape

# %%
a[:, :, np.newaxis] * b[np.newaxis, :, :]

# %%
(a[:, :, np.newaxis] * b[np.newaxis, :, :]).sum(1)

# %% [markdown]
# Or if you prefer:

# %%
(a.reshape(3, 3, 1) * b.reshape(1, 3, 3)).sum(1)

# %% [markdown]
# We use broadcasting to generate $A_{ij}B_{jk}$ as a 3-d matrix:

# %%
a.reshape(3, 3, 1) * b.reshape(1, 3, 3)

# %% [markdown]
# Then we sum over the middle, $j$ axis, [which is the 1-axis of three axes numbered (0,1,2)] of this 3-d matrix. Thus we generate $\Sigma_j A_{ij}B_{jk}$.
#
# We can see that the broadcasting concept gives us a powerful and efficient way to express many linear algebra operations computationally.

# %% [markdown]
# ### Record Arrays

# %% [markdown]
# These are a special array structure designed to match the CSV "Record and Field" model. It's a very different structure
# from the normal NumPy array, and different fields *can* contain different datatypes. We saw this when we looked at CSV files:

# %%
x = np.arange(50).reshape([10, 5])

# %%
record_x = x.view(dtype={'names': ["col1", "col2", "another", "more", "last"], 
                         'formats': [int]*5 })

# %%
record_x

# %% [markdown]
# Record arrays can be addressed with field names like they were a dictionary:

# %%
record_x['col1']

# %% [markdown]
# We've seen these already when we used NumPy's CSV parser.

# %% [markdown]
# ### Logical arrays, masking, and selection

# %% [markdown]
# Numpy defines operators like == and < to apply to arrays *element by element*:

# %%
x = np.zeros([3, 4])
x

# %%
y = np.arange(-1, 2)[:, np.newaxis] * np.arange(-2, 2)[np.newaxis, :]
y

# %%
iszero = x == y
iszero

# %% [markdown]
# A logical array can be used to select elements from an array:

# %%
y[np.logical_not(iszero)]

# %% [markdown]
# Although when printed, this comes out as a flat list, if assigned to, the *selected elements of the array are changed!*

# %%
y[iszero] = 5

# %%
y

# %% [markdown]
# ### Numpy memory

# %% [markdown]
# Numpy memory management can be tricksy:

# %%
x = np.arange(5)
y = x[:]

# %%
y[2] = 0
x

# %% [markdown]
# It does **not** behave like lists!

# %%
x = list(range(5))
y = x[:]

# %%
y[2] = 0
x

# %% [markdown]
# We must use `np.copy` to force separate memory. Otherwise NumPy tries its hardest to make slices be *views* on data.

# %% [markdown]
# Now, this has all been very theoretical, but let's go through a practical example, and see how powerful NumPy can be.
