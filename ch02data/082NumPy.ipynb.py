# ---
# jupyter:
#   jekyll:
#     display_name: Numerical Python
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # NumPy
#
# ## The scientific Python trilogy
#
# Why is Python so popular for research work?
#
# MATLAB has typically been the most popular "language of technical computing", with strong built-in support for efficient numerical analysis with matrices (the *mat* in MATLAB is for matrix, not maths), and plotting.
#
# Other dynamic languages can be argued to have cleaner, more logical syntax, for example [Ruby](https://www.ruby-lang.org/en/) or [Scheme][scheme].
#
# [scheme]: https://en.wikipedia.org/wiki/Scheme_(programming_language)
# But Python users developed three critical libraries, matching the power of MATLAB for scientific work:
#
# * [Matplotlib](https://matplotlib.org/), a plotting library for creating visualizations in Python.
# * [NumPy](https://numpy.org/), a fast numeric computing library offering a flexible *n*-dimensional array type.
# * [IPython](https://ipython.readthedocs.io/en/stable/overview.html), an interactive Python interpreter that later led to the [Jupyter notebook](https://jupyter.org/) interface.
#
# By combining a plotting library, a fast numeric library, and an easy-to-use interface allowing live plotting commands in a persistent environment, the powerful capabilities of MATLAB were matched by a free and open toolchain.
#
# We've learned about Matplotlib and IPython in this course already. NumPy is the last part of the trilogy.
#
# ## Limitations of Python lists
#
# The standard Python list is inherently one dimensional. To make a matrix (two-dimensional array of numbers), we could create a list of lists:

# %%
x = [[row_index + col_index for col_index in range(5)] for row_index in range(5)]
x

# %% [markdown]
# However, applying an operation to every element is a pain. We would like to be able to use an intuitive syntax like the following

# %%
x + 5

# %% [markdown]
# As the `+` operator is used to perform concatenation for lists we instead have to use something more cumbersome such as the following.

# %%
[[elem + 5 for elem in row] for row in x]

# %% [markdown]
# Common useful operations like transposing a matrix or reshaping a 10 by 10 matrix into a 20 by 5 matrix are not easy to perform with nested Python lists.
#
# ## Importing NumPy
#
# The main NumPy *application programming interface* (API) is exposed via the top-level `numpy` module. This is not part of the Python standard library but instead needs to be separately installed, for example using a package manager such as `pip` or `conda`.
#
# As we will typically need to access the names defined in the `numpy` module a lot when working with NumPy in code, it is common in practice to import `numpy` as the shorthand name `np`. While modern editing environments such as the Jupyter Lab interface have tab-completion functionality which makes the reduction in keystrokes necessary less important, the shorter name can still have value in reducing line length and is a very common convention so we will follow suit here. 

# %%
import numpy as np

# %% [markdown]
# ## The NumPy array
#
# NumPy's `ndarray` type represents a multidimensional grid of values of a shared type. In NumPy nomenclature each dimension is termed an *axes* and the tuple of sizes of all the dimensions of the array is termed the array *shape*. We can construct a `ndarray` using the `np.array` function. The first positional argument to this function should be an *array like* Python object: this can be another array, or more commonly [a (nested) sequence](https://numpy.org/doc/stable/user/basics.creation.html#converting-python-sequences-to-numpy-arrays), with the constraint that sequences at each level must be of the same length. For example to construct a one-dimensional array with 5 integer elements we can pass in a corresponding list of 5 integers.

# %%
my_array = np.array([0, 1, 2, 3, 4])
type(my_array)

# %% [markdown]
# The NumPy array seems at first to be very similar to a list:

# %%
my_array

# %%
my_array[2]

# %%
for element in my_array:
    print("Hello " * element)

# %% [markdown]
# However, we see see there are some differences, for example:

# %%
my_array.append(4)

# %% [markdown]
# NumPy arrays do not provide an `append` method. For NumPy arrays it is generally expected that you will not change the *size* of an array once it has been defined and the way arrays are stored in memory would make such resize operations inefficient. Python lists on the other can be efficiently appended to, joined and split. However, you gain a lot of functionality in return for this limitation.
#
# ## Array creation routines
#
# As well as `np.array`, NumPy has various other routines available for creating arrays. For example [`np.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) provides an array equivalent to the built-in `range` function, with `start`, `stop` and `step` arguments with the same semantics as for `range`. When called with integer arguments `np.arange` will return a NumPy array equivalent to an equivalent call to `range` passed to `np.array`. For example

# %%
np.arange(0, 10)

# %%
np.array(range(0, 10))

# %%
np.arange(1, 5, 2)

# %%
np.array(range(1, 5, 2))

# %% [markdown]
# Unlike `range`, `np.arange` can also be used with non-integer arguments, for example

# %%
np.arange(0.0, 0.5, 0.1)

# %% [markdown]
# Beware however because of the limits of floating point precision, using `np.arange` with non-integer arguments [can sometimes lead to inconsistent seeming outputs](https://stackoverflow.com/questions/62217178/inconsistent-behavior-in-np-arange):

# %%
print(np.arange(14.1, 15.1, 0.1))
print(np.arange(15.1, 16.1, 0.1))

# %% [markdown]
# The `np.linspace` function is an alternative array creation routine which offers a safer approach for constructing arrays of equally spaced non-integer values. The first three arguments to `np.linspace` are `start`, `stop` and `num`, corresponding under the default keyword argument values to respectively the starting value of the returned sequence, the  end value of the sequence and the number of values in the sequence. Unlike the `stop` argument to `np.arange` by default the `stop` value in `np.linspace` is an inclusive upper bound on the sequence values and the `num` argument allows explicitly stating the length of the returned sequence, preventing inconsistencies in the returned lengths for similar inputs encountered above for `np.arange`. For example the following cell constructs an array of 11 evenly spaced floating point values between 15.1 and 16.1 inclusive

# %%
np.linspace(15.1, 16.1, 11)

# %% [markdown]
# `np.linspace` also accepts an optional boolean keyword argument `endpoint` which can be used to specify whether the `stop` argument corresponds to the last sample; if `False` then the first `num` of the `num + 1` evenly spaced samples between `start` and `stop` (inclusive) are returned. For example

# %%
np.linspace(15.1, 16.1, 10, endpoint=False)

# %% [markdown]
# NumPy also provides routines for constructing arrays with all one elements (`np.ones`), all zero elements (`np.zeros`) and all elements equal to a specified value (`np.full`)

# %%
np.ones(shape=5)

# %%
np.zeros(shape=10)

# %%
np.full(shape=100, fill_value=42)

# %% [markdown]
# The `np.empty` function can be used to construct an array in which the array memory is left uninitialised; while this can potentially be slightly cheaper than initialising arrays with a defined value care needs to be taken to not use the uninitialised values as these will depend on whatever was stored in the memory previously (and may not even evaluate to a valid number)

# %%
np.empty(50)

# %% [markdown]
# ## Array data types
#
# A Python `list` can contain data of mixed type:

# %%
x = ['hello', 2, 3.4, True]
for el in x:
    print(type(el))

# %% [markdown]
# In *most cases* all the elements of a NumPy array will be of the same type. The [*data type*](https://numpy.org/doc/stable/user/basics.types.html) of an array can be specified by the `dtype` argument to `np.array` (as well as to other array creation routines such as `np.arange` and `np.linspace`). If omitted the default is to use the 'minimum' (least generic) type required to hold the objects in the (nested) sequence, with all the objects cast to this type. The results of this type conversion can sometimes be non-intuitive. For example, in the following

# %%
for el in np.array(x):
    print(type(el))

# %% [markdown]
# the array data type has been automatically set to the `numpy.str_` string type as the other integer, float and bool objects can all be represented as strings. In contrast if we repeat the same code snippet but exclude the first string entry in the list `x`

# %%
for el in np.array(x[1:]):
    print(type(el))

# %% [markdown]
# we see that all the array elements are now `numpy.float64` double-precision floating point values, as both integer and bool values can be represented as floats. The main takeaway here is that when construct NumPy arrays with `np.array` it generally is advisable to either always use (nested) sequences containing objects of a uniform type *or* to explicitly specify the data type using the `dtype` argument to ensure the constructed array has the data type you expect!
#
# An important exception to the rule-of-thumb that all elements in NumPy arrays are of the same type is the NumPy array with an `object` datatype. This is the 'catch-all' data type used when no other type can represent all the objects in the nested sequence passed to `np.array` or if this data type is explicitly specified via the `dtype` argument. In this case the array stores only references to the objects and when the array elements are accessed the original objects are recovered:

# %%
for el in np.array(x, dtype=object):
    print(type(el))

# %% [markdown]
# While this flexibility allows arrays to hold objects of any type, as we will see most of NumPy's performance gains arise from using arrays with specific data types that allow using efficient compiled code to implement computations.
#
# Arrays have a `dtype` attrinute which specifies their data type:

# %%
x = np.array([2., 3.4, 7.2, 0.])
x.dtype

# %% [markdown]
# NumPy supports a wide range of numeric data types of varying precision levels. The type code in the data type string representation typically consists of the combination of [a primitive type and integer specifying the bit width of the value](https://numpy.org/devdocs/reference/arrays.scalars.html#sized-aliases).
#
# NumPy will also convert Python type names to corresponding data types:

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
# ## Elementwise operations and scalar broadcasting
#
# Most arithmetic operations can be applied directly to NumPy arrays, with the elementwise interpretation of the operations corresponding to what we would intutively expect from the corresponding mathematical notation.

# %%
my_array = np.arange(5)
my_array + my_array

# %%
my_array * my_array

# %% [markdown]
# We can also use unary operations, for example

# %%
-my_array

# %% [markdown]
# As well as binary operations between arrays of the same shape as above, we can also apply binary operations to mixes of arrays and scalars, with binary operations involving a scalar and an array being [*broadcast*](https://numpy.org/doc/stable/user/basics.broadcasting.html) such that the scalar is treated as if it was an array of equal shape to the array operand and the operation then performed elementwise. This again gives compact expressions which correspond with how we would typically intepret such expressions in mathematical notation

# %%
my_array * 2

# %%
my_array + 1

# %%
2 ** my_array

# %% [markdown]
# These *vectorised* operations are very fast. For example, we can use the [`%timeit` magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) to compare the time taken to use a list comprehension to compute the squares of the first 10&thinsp;000 integers:

# %%
# %timeit [x**2 for x in range(10_000)]

# %% [markdown]
# with the time taken to compute the corresponding array of squared integers using NumPy:

# %%
# %timeit np.arange(10_000)**2

# %% [markdown]
# Note that this speed-up is a consequence of all of the array elements being known in advance to be of a specific data type enabling the use of efficient compiled loop in NumPy's backend when computing the operation. The performance advantage is lost when using arrays with the catch-all `object` data type, as in this case NumPy has to revert to looping over the array elements in Python:

# %%
# %timeit np.arange(10_000, dtype=object)**2

# %% [markdown]
# ## Numpy mathematical functions
#
# NumPy comes with vectorised versions of [common mathematical functions](https://numpy.org/doc/stable/reference/routines.math.html) which work elementwise when applied to arrays.
#
# Compared to the list comprehensions used previously these signficantly simplify the process of plotting functions using Matplotlib:

# %%
from matplotlib import pyplot as plt
x = np.linspace(-3, 3, 100)
for func in (np.sin, np.cos, np.tanh, np.arctan, np.absolute):
    plt.plot(x, func(x), label=func.__name__)
plt.legend()

# %% [markdown]
# ## Multi-dimensional arrays
#
# A particularly powerful feature of NumPy is its ability to handle arrays of (almost) arbitrary dimension. For example to create a three dimensional array of zeros we can use the following

# %%
np.zeros(shape=(3, 4, 2))  # or equivalently np.zeros((3, 4, 2))

# %% [markdown]
# Unlike nested lists in Python, we can change the shape of NumPy arrays using the `np.reshape` function (or `ndarray.reshape` method) providing the new total number of elements in the new shape matches the old shape. For example

# %%
x = np.arange(12).reshape((3, 4))
x

# %% [markdown]
# We can also reorder the dimensions of arrays using the `np.transpose` function or corresponding `ndarray.transpose` method. By default this reverses the order of the axes (dimensions)

# %%
x.transpose()

# %% [markdown]
# The shorthand `ndarray.T` property can also be used access the result corresponding to calling the `transpose` method with its default arguments

# %%
x.T

# %% [markdown]
# We can also pass in a specific permutation of the axes indices to `transpose` to get different reorderings, for example

# %%
y = np.arange(24).reshape((3, 4, 2))
y.transpose((0, 2, 1))

# %% [markdown]
# The shape of a particular array can always be accessed using the `ndarray.shape` attribute

# %%
y.shape

# %%
y.transpose((0, 2, 1)).shape

# %% [markdown]
# The total number of dimensions (axes) of an array can be accessed using the `ndarray.ndim` attribute

# %%
y.ndim

# %% [markdown]
# ## Array indexing and slicing
#
# A multidimensional array accepts a comma-delimited sequence of integer indices or index ranges enclosed in square brackets, of up to the number of array dimensions. For an array with *n* dimensions if *n* integer indices are specified then the result is a scalar value of the array's data type

# %%
x = np.arange(40).reshape([4, 5, 2])
x[2, 1, 0]

# %% [markdown]
# If we pass *m < n* indices, then the indices are used to select a [*slice*](https://docs.python.org/3/glossary.html#term-slice) of the array corresponding to using the specified indices to select the first *m* dimensions and selecting all of the remaining *n - m* dimensions

# %%
x[2, 1]

# %%
x[2]

# %% [markdown]
# Similar to lists, NumPy arrays also support [an extended indexing syntax](https://numpy.org/devdocs/user/basics.indexing.html#slicing-and-striding) to support selecting portions of a particular dimension; somewhat confusingly the term *slice* is used to refer both to the outcome of selecting a portion of a sequence *and* the object and associated [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) used to select such portions. Passing a colon separated range `start:stop:step` as the index for an array dimension, will select the elements for which this dimension's index is in the corresponding range object `range(start, stop, step)` for example

# %%
np.arange(10)[1:10:2]

# %% [markdown]
# As for lists the `step` component of the range can be omitted; in this case the second colon can also be left out. 

# %%
np.arange(10)[1:3]

# %% [markdown]
# If the `start` argument is omitted it is implicitly assumed to be zero - that is to start from the beginning of the dimension. If the `end` argument is omitted it is implicitly assumed to be equal to the length of that dimension, that is to stop at the final index along that dimension. Combining these rules together means that for example a plain colon `:` will be interpreted as referring to all indices in that dimension

# %%
np.arange(10)[:]

# %% [markdown]
# For multiple dimensional arrays we can slice along multiple dimensions simultaneously

# %%
x[2:, :1, 0]

# %% [markdown]
# As for lists, the [inbuilt `slice` object](https://docs.python.org/3/library/functions.html#slice) can be used to programatically define slices, for example the following is equivalent to the slicing in the above cell

# %%
x[slice(2, None), slice(None, 1), 0]

# %% [markdown]
# ## Reduction operations
#
# NumPy provides various functions and associate `ndarray` methods which apply an operation along one or more array axes, resulting in an output of reduced dimension. The *reduction* operations include
#
#   * `sum`, `prod`: compute the sum or product along one or more dimensions,
#   * `min`, `max`: compute the minimum or maximum along one or more dimensions,
#   * `argmin`, `argmax`: compute the indices corresponding to the minimum or maximum along one or more dimensions,
#   * `mean`, `std`: compute the empirical mean or standard deviation along one or dimensions.
#   
# All of these operations include both a functional form available in the `numpy` module namespace, and a corresponding `ndarray` method. The interface to the `ndarray` methods match the function other than the first array positional argument being set to array the method is being called on; for example `np.sum(x)` and `x.sum()` will give equivalent results.

# %%
x = np.arange(12).reshape(2, 2, 3)
x

# %%
np.sum(x)  # Sums along all axes

# %%
x.sum() # Also sums along all axes

# %% [markdown]
# All the reduction operations accept an optional `axis` argument which specifies the array axis (dimension) or axes to apply the reduction along. This defaults to `None` corresponding to applying along all axes, with the returned output then a scalar.

# %%
x.sum(axis=None)  # Also sums along all axes

# %% [markdown]
# If `axis` is set to an integer (corresponding to a valid axis index for the array) then the reduction will be applied only along that axis, resulting in a returned output of dimension one less than the original array.

# %%
x.sum(axis=0)  # Sums along the first axis

# %%
x.sum(axis=1)  # Sums along the second axis

# %%
x.sum(axis=2)  # Sums along the third axis

# %% [markdown]
# If axis is set a *tuple* of integer axis indices, the reduction is applied along all the corresponding axes, with the returned output then of dimension equal to the original array dimension minus the length of the axis index tuple.

# %%
x.sum(axis=(0, 1)) # Sums along the first and second axes

# %%
x.sum(axis=(0, 1, 2))  # Also sums along all axes

# %% [markdown]
# ## Advanced broadcasting
#
# We earlier encountered the concept of *broadcasting* in the context of binary operations on mixes of scalars and arrays. A very powerful feature of NumPy is that broadcasting is also extended to apply to operations involving arrays with differing but *compatible* shapes. This allows us to broadcast a smaller array across a larger array without needlessly repeating the data in the smaller array. It also
#
# NumPy's binary operations are usually applied elementwise on pairs of arrays, with the simplest case being when the arrays have exactly matching shapes

# %%
np.arange(0, 5) * np.arange(5, 10)

# %%
np.ones((3, 2)) + np.zeros((3, 2))

# %% [markdown]
# If we apply binary operations to arrays with non-matching shapes we will typically get an error

# %%
np.arange(5) * np.arange(6)

# %%
np.ones((2, 3)) * np.zeros((2, 4))

# %% [markdown]
# However, the condition that array shapes exactly match is relaxed to allow operations to be peformed on pairs of arrays for which the shapes are *compatible* under certain rules. The shape of two arguments to a binary operation are considered compatible if: working from the rightmost dimension leftwards all dimensions which are defined for both arrays are either equal or one of them is equal to one. Any dimensions for which one array only has size one, that array is treated as if the array element was repeated a number of times equal to the size of the corresponding dimension of the other array.
#
# This provides a convenient way for example to perform an outer product operation on vectors (one dimensional arrays)

# %%
np.arange(5).reshape(5, 1) * np.arange(5, 10).reshape(1, 5)

# %% [markdown]
# Importantly arrays do not need to have the same number of dimensions to have compatible shapes, providing the rightmost dimensions of the array with a larger dimension are compatible with the shape of the smaller array, with the missing leftmost dimensions of the smaller array treated as if they were of size one. For example

# %%
np.arange(6).reshape(3, 2) + np.arange(2)

# %% [markdown]
# For a more complete description of NumPy's broadcasting rules including some helpful visualisation [see this article in the official documentation](https://numpy.org/devdocs/user/basics.broadcasting.html).
#
# ## Adding new axes
#
# Broadcasting is very powerful, and NumPy allows indexing with `np.newaxis` to temporarily create new length one dimensions on the fly, rather than explicitly calling `reshape`.

# %%
x = np.arange(10).reshape(2, 5)
y = np.arange(8).reshape(2, 2, 2)

# %%
x.reshape(2, 5, 1, 1).shape

# %%
x[:, :, np.newaxis, np.newaxis].shape

# %%
y[:, np.newaxis, :, :].shape

# %%
res = x[:, :, np.newaxis, np.newaxis] * y[:, np.newaxis, :, :]
res.shape

# %% [markdown]
# This is particularly useful when performing outer product type operations

# %%
x = np.arange(5)
y = np.arange(5, 10)
x[:, np.newaxis] * y[np.newaxis, :]

# %% [markdown]
# Note that `newaxis` works because an array with extra length one dimensions has the same overall size (and so can be a view to the same underlying data) just with a different shape. In other words, a $3 \times 1 \times 3$ and a $3 \times 3$ array contain the same data, differently shaped:

# %%
three_by_three = np.arange(9).reshape(3, 3)
three_by_three

# %%
three_by_three[:, np.newaxis, :]

# %% [markdown]
# ## Matrix multiplications
#
# NumPy interprets the standard `*` operator as elementwise multiplication

# %%
a = np.arange(9).reshape(3, 3)
b = np.arange(3, 12).reshape(3, 3)
a * b

# %% [markdown]
# To perform matrix multiplication we use the `@` operator instead

# %%
a @ b

# %% [markdown]
# As well as matrix-matrix products (that is products of pairs of two dimensional arrays) this can also be used for matrix-vector products (products of a two dimensional array and one dimensional array) and vector-vector products (products of pairs of one dimensional arrays)

# %%
v = np.arange(3)
a @ v

# %%
v @ v

# %% [markdown]
# ## Structured arrays
#
# So far we have encountered arrays with 'simple' data types corresponding to a single type. NumPy also offers arrays with [*structured data types*](https://numpy.org/devdocs/user/basics.rec.html#structured-datatypes), sometimes termed *record arrays*, for which each array element is composed of several fields, with each field having the same data type across all array elements. These are a special array structure designed to match the *comma separated variable* (CSV) *record and field* model. We saw this when we looked at CSV files:

# %%
x = np.arange(50).reshape((10, 5))

# %%
record_x = x.view(
    dtype={
        'names': ["col1", "col2", "another", "more", "last"], 
        'formats': [int] * 5 
    } 
)

# %%
record_x

# %% [markdown]
# Record arrays can be addressed with field names like they were a dictionary:

# %%
record_x['col1']

# %% [markdown]
# ## Comparison operators and boolean indexing
#
# Numpy defines comparison operators like `==` and `<` to apply to arrays elementwise and also to broadcast similar to arithmetic operations

# %%
x = np.arange(-1, 2)[:, np.newaxis] * np.arange(-2, 2)[np.newaxis, :]
x

# %%
is_zero = (x == 0)
is_zero

# %% [markdown]
# Boolean arrays can also be used to filter the elements of an array matching some condition. For example

# %%
x[is_zero]

# %% [markdown]
# We can use the unary negation operator `~` to negate conditions

# %%
x[~is_zero]

# %% [markdown]
# Although when used to get items from an array, boolean indexing results in a new one dimensional array, if the boolean indexing is instead part of an assignment statement the *selected elements of the array are changed in place*

# %%
x[is_zero] = 5

# %%
x

# %% [markdown]
# For more details about boolean array indexing [see the official documentation](https://numpy.org/devdocs/user/basics.indexing.html#boolean-array-indexing).
#
# ## Copies and views
#
# Care needs to be taken when assigning to slices of a NumPy array

# %%
x = np.arange(6).reshape((3, 2))
x

# %%
y = x[0, :]
y[1] = -99
x

# %% [markdown]
# In general NumPy will try to return *views* to the same underlying array data buffer when performing indexing and slicing operations, where possible. These views share the same underlying data in memory with the original array, and so make such indexing operations cheap in both memory usage and computational cost (by avoiding unnececssary copies). As we saw above however, if we assign to a slice we will therefore also update the original array. We can use the `np.copy` function or corresponding `ndarray.copy` method to force creation of an array referencing a new copy of the underlying data

# %%
x = np.arange(6).reshape((3, 2))
y = x[0, :].copy()
y[1] = -99
x

# %% [markdown]
# More details are given [in the official documentation](https://numpy.org/devdocs/user/basics.copies.html).
#
# ## Further reading
#
# As well as the links to external resource throughout these notes, some suggestions for further reading for those who wish to learn more about NumPy are 
#
#   * The [NumPy quickstart guide](https://numpy.org/devdocs/user/quickstart.html) in the official documentation.
#   * If you have previous experience with MATLAB, [this guide to NumPy for MATLAB users](https://numpy.org/devdocs/user/numpy-for-matlab-users.html) in the official documentation may also be helpful. 
#   * [This *Software Carpenty* lesson](https://swcarpentry.github.io/python-novice-inflammation/02-numpy/index.html) also introduces the basics of using NumPy in an applied example.
#   * The [NumPy section of this Python tutorial for the Stanford CS231n course](https://cs231n.github.io/python-numpy-tutorial/#numpy) covers a lot of the same topics as we have here.
#
# We will also see some practical usage of NumPy arrays in one of the subsequent notebooks on simulating flocking dynamics.
