# ---
# jupyter:
#   jekyll:
#     display_name: Miscellaneous libraries
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---
#
# %% [markdown]
# # Miscellaneous libraries to improve your code's performance
# 
# Over the course of years, Python ecosystem has developed more and more solutions
# to combat the relatively slow performance of the language. As seen in the previous
# lessons, the speed of computation matters quite a lot while using a technology
# in scientific setting. This lesson introduces a few such popular libraries that have
# been widely adopted in the scientific use of Python.
# 
# ## Compiling Python code
# 
# We know that Python is an interpreted and not a compiled language, but is there a way
# to compile Python code? There are a few libraries/frameworks that lets you
# [*just in time*][wiki-jit] (JIT) or [*ahead of time*][wiki-aot] (AOT) compile Python code. Both the techniques allow
# users to compile their Python code without using any explicit low level langauge's
# bindings, but both the techniques are different from each other.
# 
# [wiki-jit]: https://en.wikipedia.org/wiki/Just-in-time_compilation
# [wiki-aot]: https://en.wikipedia.org/wiki/Ahead-of-time_compilation
#
# Just in time compilers compile functions/methods at runtime whereas ahead of time
# compilers compile the entire code before runtime. AOT can do much more compiler
# optimizations than JIT, but AOT compilers produce huge binaries and that too only
# for specific platforms. JIT compilers have limited optimization routines but they
# produce small and platform independent binaries.
# 
# JIT and AOT compilers for Python include, but are not limited to -
#  - [Numba](http://numba.pydata.org): a Just-In-Time Compiler for Numerical Functions in Python
#  - [mypyc](https://mypyc.readthedocs.io/en/latest/introduction.html): compiles Python modules to C extensions using standard Python type hints
#  - [JAX](https://jax.readthedocs.io/en/latest/jit-compilation.html): a Python library for accelerator-oriented array computation and program transformation
# 
# Although all of them were built to speed-up Python code, each one of them is a bit
# different from each other when it comes to their use-case. We will specifically look into
# Numba in this lesson.
# 
# ### Numba
# 
# Numba is an open source JIT compiler that translates a subset of Python and NumPy code
# into fast machine code. The good thing about Numba is that it works on plain Python
# loops and one doesn't need to configure any compilers manually to JIT compile Python code.
# Another good thing is that it understands NumPy natively, but as detailed in its
# documentation, it only understands a subset of NumPy functionalities.
# 
# Numba provides users with an easy to use function decorator - `jit`. Let's start by
# importing the libraries we will use in this lesson.
#

# %%
import math

from numba import jit, njit
import numpy as np

# %% [markdown]
# We can mark a function to be JIT compiled by decorating it
# with numba's `@jit`. The decorator takes a `nopython` argument that tells Numba to
# enter the compilation mode and not fall back to usual Python execution.
# 
# Here, we are showing a usual python function, and one that's decorated. 
# We don't need to duplicate and change its name when using numba, but we want to keep both of them here to compare their execution times.

# %%
def f(x):
    return np.sqrt(x)

@jit(nopython=True)
def jit_f(x):
    return np.sqrt(x)

# %% [markdown]
# It looks like the `jit` decorator should make our Numba compile our function
# and make it much faster than the non-jit version. Let's test this out.
# 
# Note that the first function call is not included while timing because that
# is where Numba compiles the function. The compilation at runtime is called
# just in time compilation and resultant binaries are cached for the future
# runs. 

# %%
data = np.random.uniform(low=0.0, high=100.0, size=1_000)

# %%
# %%timeit
f(data)

# %%
# %%timeit -n 1 -r 1
_ = jit_f(data)  # compilation and run

# %%
# %%timeit
jit_f(data)  # just run

# %% [markdown]
# Surprisingly, the JITted function was slower than plain Python and NumPy
# implementation! Why did this happen? Numba does not provide valuable performance
# gains over pure Python or NumPy code for simple operations and small dataset.
# The JITted function turned out to be slower than the non-JIT implementation
# because of the compilation overhead. Note that the result from the compilation
# run could be very noisy and could give a higher than real value, as mentioned
# in the previous lessons. Let's try increasing the size of our
# data and perform a non-NumPy list comprehension on the data.
# 
# The `jit` decorator with `nopython=True` is so widely used there exists an alias
# decorator for the same - `@njit`

# %%
data = np.random.uniform(low=0.0, high=100.0, size=1_000_000)


# %%
def f(x):
    return [math.sqrt(elem) for elem in x]

@njit
def jit_f(x):
    return [math.sqrt(elem) for elem in x]

# %%
# %%timeit
f(data)

# %%
# %%timeit -n 1 -r 1
_ = jit_f(data)  # compilation and run

# %%
# %%timeit
jit_f(data)  # just run

# %% [markdown]
# That was way faster than the non-JIT function! But, the result was still slower
# than the NumPy implementation. NumPy is still good for relatively simple
# computations, but as the complexity increases, Numba functions start
# outperforming NumPy implementations.

# %% [markdown]
# Let's go back to our plain Python mandelbrot code from the previous lessons and
# JIT compile it -

# %%
@njit
def mandel1(position, limit=50):
    
    value = position
    
    while abs(value) < 2:
        limit -= 1        
        value = value**2 + position
        if limit < 0:
            return 0
        
    return limit

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
# %%timeit -n 1 -r 1
data = [[mandel1(complex(x, y)) for x in xs] for y in ys]  # compilation and run

# %%
# %%timeit
data = [[mandel1(complex(x, y)) for x in xs] for y in ys]  # just run

# %% [markdown]
# The compiled code already beats our fastest NumPy implementation! It is not
# necessary the compiled code will perform better than NumPy code, but it usually
# gives performance gains for signifantly large computations. As always, it is
# good to measure the performance to check if there are any gains.

# %% [markdown]
# Let's try JITting our NumPy code.

# %%
@njit
def mandel_numpy(position,limit=50):
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

ymatrix, xmatrix = np.mgrid[ymin:ymax:ystep, xmin:xmax:xstep]
values = xmatrix + 1j * ymatrix

# %%
# %%timeit
mandel_numpy(values)

# %% [markdown]
# That does not work. The error might be solvable or it might just be out of Numba's
# scope. Numba does not distinguish between plain Python
# and NumPy; hence both the implementations are broken down to the same machine
# code. Therefore, for Numba, it makes sense to write complex computations with the ease
# of Python loops and lists than with NumPy functions. Moreover, Numba only understands
# a subset of Python and NumPy so it is possible that a NumPy snippet does not
# work but a simplified Python loop does.

# %% [markdown]
# Let's make minor adjustments to fix the NumPy implementation and measure its
# performance. We flatten the NumPy arrays and consider only the real part
# while performing the comparison.
# %%
@njit
def mandel_numpy(position,limit=50):
    value = position.flatten()
    diverged_at_count = np.zeros(position.shape).flatten()
    while limit > 0:
        limit -= 1
        value = value**2 + position.flatten()
        diverging = (value * np.conj(value)).real > 4
        first_diverged_this_time = (np.logical_and(diverging, diverged_at_count == 0))
        diverged_at_count[first_diverged_this_time] = limit
        value[diverging] = 2

    return diverged_at_count.reshape(position.shape)

ymatrix, xmatrix = np.mgrid[ymin:ymax:ystep, xmin:xmax:xstep]
values = xmatrix + 1j * ymatrix

# %%
# %%timeit -n 1 -r 1
mandel_numpy(values)  # compilation and run

# %%
# %%timeit
mandel_numpy(values)  # just run

# %% [markdown]
# The code performs similar to the plain Python example!

# %% [markdown]
# Numba also has functionalities to vectorize, parallelize, and strictly type check
# the code. All of these functions boost the performance even further or helps
# Numba to avoid falling back to the "object" mode (`nopython=False`). Refer
# to [Numba's documentation](http://numba.pydata.org) for a complete list of features.

# %% [markdown] 
# #### Numba support in Scientific Python ecosystem
# 
# Most of the scientific libraries nowadays ship Numba support with them. For example,
# [Awkward Array](https://awkward-array.org) is a library that lets users perfor JIT
# compilable operations on non-uniform data, something that NumPy misses. Similarly,
# [Akimbo](https://akimbo.readthedocs.io) provides JIT compilable processing of nested,
# non-uniform data in dataframes. There are other niche libraries, such as,
# [vector](https://vector.readthedocs.io) that provides Numba support for high energy
# physics vector.
# 
# ## Compiled Python bindings
# 
# Several Python libraries/frameworks are written in a compiled language but provide Python
# bindings for their compiled code. This code does not have to be explicitly marked to be
# compiled by developers. A few Python libraries that have their core written in
# compiled languages but provide Python bindings -
# 
#  - [Cython](https://cython.org): superset of Python that supports calling C functions and declaring C types on variables and class attributes
#  - [Scipy](https://scipy.org): wraps highly-optimized scientific implementations written in low-level languages like Fortran, C, and C++
#  - [Polars](https://docs.pola.rs): dataframes powered by a multithreaded, vectorized query engine, written in Rust
#  - [boost-histogram](https://boost-histogram.readthedocs.io/en/latest/): Python bindings for the C++14 Boost::Histogram library
#  - [Awkward Array](https://awkward-array.org/doc/main/): compiled and fast manipulation of JSON-like data with NumPy-like idioms
#  - [Astropy](https://www.astropy.org): astronomy and astrophysics core library
# 
# JIT or AOT compiling libraries and the libraries providing Python bindings for a compiled
# language are not mutually exclusive. For instance, PyTorch and Tensorflow offer users
# "eager" and "graph" executation. Eager execution builds computational graph at runtime,
# making it slow, easy to debug, and JIT compilable. On the other hand, "graph" execution
# builds the computational graph at the kernel level, making it fast, hard to debug, and
# with no need to JIT compile. Similarly, Awkward Array provides Python bindings for array
# creation, but high-level operations on these arrays can be JIT compiled.
# 
# We will specifically look into Cython in the next lesson.
# 
# ## Distributed and parallel computing with Python
# 
# Along with the speed of execution of a program, scientific computation usually requires
# a large amount of memory because of the massive nature of data produced at scientific
# experiments. This issue can be addressed by employing distributed and parallel
# computing frameworks to spread the computation across multiple machines or multiple
# cores in a single machine. Parallel computing at a smaller level can be achieved by distributing
# a task over multiple threads, but Python's GIL (Global Interpreter Lock) blocks
# the interpretor from doing this for computational tasks. There are ongoing efforts, such
# as the implementation of [PEP 703](https://peps.python.org/pep-0703/) to make GIL
# optional, but Numba allows users to bypass GIL by pass `nogil=True` to `@jit`.
# 
# At a larger scale, Dask can be used to parallelize computation over multiple
# machine or "nodes". Dask can even parallelize the code marked with `@numba.jit(nogil=True)`
# to multiple threads in a machine, but it does not itself bypass the GIL.
# 
# ### Dask
# 
# Dask is a Python library for parallel and distributed computing. Dask supports
# arrays, dataframes, Python objects, as well as tasks on computer clusters and
# nodes. The API of Dask is very similar to that of NumPy, Pandas, and plain Python,
# allowing users to quickly parallelize their implementations. Let's create a dummy
# dataframe using dask.

# %%
import dask

df = dask.datasets.make_people()  # returns a dask "bag"
df = df.to_dataframe()

# %%
df

# %% [markdown]
# The computation gave us a dask object and not the actual answer. Why is that?
# Displaying the dataframe just displays the metadata of the variable, and not any
# data. This is because of the "lazy" nature of dask. Dask has "lazy" execution,
# which means that it will store the operations on the data and
# create a task graph for the same, but will not execute the operations until a
# user explicitly asks for the result. The metadata specifies `npartitions=10`,
# which means that the dataframe is split into 10 parts that will be accessed parallely.
# We can explicitly tell dask to give us the dataframe values using `.compute()`.

# %%
df.compute()

# %% [markdown] 
# We can now perform pandas like operation on our dataframe and let dask create a
# task graph for the same.

# %%
new_df = df.groupby("occupation").age.max()
new_df

# %% [markdown] 
# Instead of computing, let's visualize the task graph.

# %%
dask.visualize(new_df, filename="visualization.png")

# %% [markdown] 
# We can see that the task graph starts with 10 independent branches because our dataframe
# was split into 10 partitions at the start. Let's compute the answer.

# %%
new_df.compute()

# %% [markdown] 
# Similarly, one can peform such computations on arrays and selected Python data structures.
# 

# #### Dask support in Scientific Python ecosystem
# 
# Similar to the adoption of Numba in the scientific Python ecosystem, dask is being
# adopted at an increasing rate. Some examples include
# [dask-awkward](https://dask-awkward.readthedocs.io) for ragged data
# computation, [dask-histogram](https://dask-histogram.readthedocs.io) for
# parallel filling of histograms dask support in [cuDF](https://docs.rapids.ai/api/cudf),
# for parallelizing CUDA dataframes, and
# [dask-sql](https://dask-sql.readthedocs.io), a distributed SQL Engine.
# 
# ## GPU accelerated computing in Python
# 
# The last method for speeding up Python that we will look at is running your code
# on GPUs instead of CPUs. GPUs are specifically built to speed up computational tasks
# such as doing linear algebra or experimenting with computer graphics. Support for
# GPUs can be provided by writing custom kernels or by using Pythonic GPU libraris
# such as CuPy.
# 
# ### CuPy
# 
# [CuPy](https://cupy.dev) is an array-based library enabling Python code to be scaled to GPUs. CuPy's
# API is very similar to NumPy and SciPy, and it was built as their extension to
# GPUs. There are a few differences in the API, and even a few missing functions,
# but it is actively developed and in a stable state. CuPy requires CUDA or
# AMD ROCm to be installed on your machine. After the installation, majority of
# the NumPy and SciPy scripts can be converted to CuPy by just replacing `numpy`
# and `scipy` with `cupy`.
# 
# ```python
# import cupy as cp
# 
# print(cp.cuda.runtime.getDeviceCount())  # check if CuPy identifies the CUDA GPU
# 
# x = cp.arange(6).reshape(2, 3).astype('f')
# y = cp.arange(6).reshape(2, 3).astype('f')
# 
# result = x + y
# ```
# 
# The code is not executed in this lesson as the service where these lessons are built
# do not posses a GPU.
# 
# #### CuPy support in Scientific Python ecosystem
# 
# Similar to Numba and Dask, CuPy is being adopted in multiple scientific libraries to
# provide GPU capabilities to the users. [Dask](https://docs.dask.org/en/stable/gpu.html)
# along with its exosystem libraries, such as [dask-image](https://image.dask.org/en/latest/index.html)
# provide CuPy and GPU support. Similarly, packages like
# [Awkward Array](https://awkward-array.org/doc/main/),
# [cupy-xarray](https://cupy-xarray.readthedocs.io), and
# [pyxem](https://pyxem.readthedocs.io/en/latest/) use CuPy internally to offer GPU support.
#
# ## Writing custom GPU kernels and binding them to Python
# 
# Some Python libraries write their own custom kernels to provide GPU support to the users.
# For instance, [cuDF](https://docs.rapids.ai/api/cudf) uses libcudf, a C++/CUDA dataframe
# library to provide GPU support for dataframes in Python. Similarly, Tensorflow and
# PyTorch have their own GPU kernels and they do not depend on CuPy to run their code
# on GPUs. One can even write custom GPU kernels in CuPy, and libraries like
# [Awkward Array](https://awkward-array.org/doc/main/) leverage that for ragged data
# computation.
# 

