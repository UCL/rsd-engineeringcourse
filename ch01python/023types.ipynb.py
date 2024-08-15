# ---
# jupyter:
#   jekyll:
#     display_name: Types
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Types

# %% [markdown]
# We have so far encountered several different 'types' of Python object: 
#
# - integer numbers, for example `42`, 
# - real numbers, for example `3.14`,
# - strings, for example `"abc"`,
# - functions, for example `print`,
# - the special 'null'-value `None`. 
#
# The built-in function `type` when passed a single argument will return the type of the argument object. For example

# %%
type(42)

# %%
type("abc")

# %% [markdown]
# ## Converting between types
#
# The Python type names such as `int` (integer numbers) and `str` (strings) can be used like functions to construct _instances_ of the type, typically by passing an object of another type which can be converted to the type being called. For example we can use `int` to convert a string of digits to an integer

# %%
int("123")

# %%
int("2") + int("2")

# %% [markdown]
# or to convert a decimal number to an integer (in this case by truncating off the decimal part)

# %%
int(2.1)

# %% [markdown]
# Conversely we can use `str` to convert numbers to strings

# %%
str(123)

# %%
str(3.14)

# %% [markdown]
# ## Object attributes and methods
#
# Objects in Python have _attributes_: named values associated with the object and which are referenced to using the dot operator `.` followed by the attribute name, for example `an_object.attribute` would access (if it exists) the attribute named `attribute` of the object `an_object`. Each type has a set of pre-defined attributes. 
#
# Object attributes can reference arbitrary data associated with the object, or special functions termed _methods_ which have access to both any argument passed to them _and_ any other attributes of the object, and which are typically used to implement functionality connected to a particular object type.
#
# For example the `float` type used by Python to represent non-integer numbers (more on this in a bit) has attribute `real` and `imaginary` which can be used to access the real and imaginary components when considering the value as a [complex number](https://en.wikipedia.org/wiki/Complex_number)

# %%
a_number = 12.5
print(a_number.real)
print(a_number.imag)

# %% [markdown]
# Objects of `str` type (strings) have methods `upper` and `lower` which both take no arguments, and respectively return the string in all upper case or all lower case characters

# %%
a_string = "Hello world!"
print(a_string.upper())
print(a_string.lower())

# %% [markdown]
# If you try to access an attribute not defined for a particular type you will get an error

# %%
a_string.real

# %%
a_number.upper()

# %% [markdown]
# We can list all of the attributes of an object by passing the object to the built-in `dir` function, for example

# %%
print(dir(a_string))

# %% [markdown]
# The attributes with names beginning and ending in double underscores `__` are special methods that implement the functionality associated with applying operators (and certain built-in functions) to objects of that type, and are generally not accessed directly.
#
# In Jupyter notebooks we can also view an objects properties using tab-completion by typing the object name followed by a dot `.` then hitting <kbd>tab</kbd>

# %% [markdown]
# ## Operators
#
# Now that we know more about types, functions and methods we should look again at what happens when we write:

# %%
four = 2 + 2

# %% [markdown]
# The addition symbol `+` here is an example of what is termed an _operator_, in particular `+` is a _binary operator_ as it applies to pairs of values.
#
# We can think of the above code as equivalent to something like
#
# ```Python
#     four = add(2, 2)
# ```
#
# where `add` is the name of a function which takes two arguments and returns their sum.
#
# In Python, these functions _do_ exist, but they're actually _methods_ of the first input: they're the mysterious double-underscore `__` surrounded attributes we saw previously. For example the addition operator `+` is associated with a special method `__add__`

# %%
two = 2
two.__add__(two)

# %% [markdown]
# The meaning of an operator varies for different types. For example for strings the addition operator `+` implements string concatenation (joining).

# %%
"Hello" + " " + "world"

# %%
"2" + "2"

# %% [markdown]
# Sometimes we get an error when a type doesn't have an operator:

# %%
"Hello" - "world"

# %% [markdown]
# The word "operand" means "thing that an operator operates on"!

# %% [markdown]
# Or when two types can't work together with an operator:

# %%
"2" + 5

# %% [markdown]
# Just as in mathematics, operators in Python have a built-in precedence, with brackets used to force an order of operations:

# %%
print(2 + 3 * 4)

# %%
print((2 + 3) * 4)

# %% [markdown]
# *Supplementary material*: [Python operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)

# %% [markdown]
# ## Floats and integers

# %% [markdown]
# Python has two core numeric types, `int` for integers, and `float` for real numbers.

# %%
integer_one = 1
integer_ten = 10
float_one = 1.0
float_ten = 10.

# %% [markdown]
# Binary arithmetic operators applied to objects of `float` and `int` types will return a `float`

# %%
integer_one * float_ten

# %%
float_one + integer_one

# %% [markdown]
# In Python there are two division operators `/` and `//` which implement different mathematical operations. The _true division_ (or just _division_) operator `/` implements what we usually think of by division, such that for two `float` values `x` and `y` `z = x / y` is another `float` values such that `y * z` is (to within machine precision) equal to `x`. The _floor division_ operator `//` instead implements the operation of dividing and rounding down to the nearest integer.

# %%
float_one / float_ten

# %%
float_one / integer_ten

# %%
float_one // float_ten

# %%
integer_one // integer_ten

# %%
integer_one // float_ten

# %% [markdown]
# In reality the `float` type does not exactly represent real numbers (as being able to represent all real numbers to arbitrary precision is impossible in a object with uses a finite amount of memory) but instead represents real-numbers as a finite-precision 'floating-point' approximation. This has many important implications for the implementation of numerical algorithms. We will not have time to cover this topic here but the following resources can be used to learn more for those who are interested.
#
# *Supplementary material*:
#
# * [Floating point arithmetic in Python](https://docs.python.org/3/tutorial/floatingpoint.html)
# * [Floating point guide](http://floating-point-gui.de/formats/fp/)
# * Advanced: [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)

# %% [markdown]
# ## Strings

# %% [markdown]
# Python built-in `string` type, supports many useful operators and methods. As we have seen already the addition operator can be used to concatenate strings

# %%
given = "Grace"
family = "Hopper"
full = given + " " + family

# %% [markdown]
# The multiplication operator `*` can be used to repeat strings

# %%
"Badger " * 3

# %% [markdown]
# Methods such as `upper` and `lower` can be used to alter the case of the string characters.

# %%
print(full.lower())
print(full.upper())

# %% [markdown]
# The `replace` method can be used to replace characters

# %%
full.replace("c", "p")

# %% [markdown]
# The `count` method can be used to count the occurences of particular characters in the string

# %%
full.count("p")

# %% [markdown]
# We can use `strip` to remove extraneous whitespace from the start and end of a string:

# %%
"    Hello  ".strip()
