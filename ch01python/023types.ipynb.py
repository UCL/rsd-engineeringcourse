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
# ## Types

# %% [markdown]
# We have seen that Python objects have a 'type':

# %%
type(5)

# %% [markdown]
# ### Floats and integers

# %% [markdown]
# Python has two core numeric types, `int` for integer, and `float` for real number.

# %%
one = 1
ten = 10
one_float = 1.0
ten_float = 10.

# %% [markdown]
# The zero after a decimal point is optional - it is the **Dot** makes it a float. However, it is better to always include the zero to improve readability.

# %%
tenth= one_float / ten_float

# %%
tenth

# %%
type(one)

# %%
type(one_float)

# %% [markdown]
# The meaning of an operator varies depending on the type it is applied to!

# %%
print(1 + 2)  # returns an integer

# %%
print(1.0 + 2.0)  # returns a float

# %% [markdown]
# The division by operator always returns a `float`, whether it's applied to `float`s or `int`s.

# %%
10 / 3

# %%
10.0 / 3

# %%
10 / 3.0

# %% [markdown]
# To perform integer division we need to use the `divmod` function, which returns the quotiant and remainder of the division.

# %%
quotiant, remainder = divmod(10, 3)
print(f"{quotiant=}, {remainder=}")

# %% [markdown]
# Note that if either of the input type are `float`, the returned values will also be `float`s.

# %%
divmod(10, 3.0)

# %% [markdown]
# There is a function for every built-in type, which is used to convert the input to an output of the desired type.

# %%
x = float(5)
type(x)

# %%
divmod(10, float(3))

# %% [markdown]
# I lied when I said that the `float` type was a real number. It's actually a computer representation of a real number
# called a "floating point number". Representing $\sqrt 2$ or $\frac{1}{3}$ perfectly would be impossible in a computer, so we use a finite amount of memory to do it.

# %%
N = 10000.0
sum([1 / N] * int(N))

# %% [markdown]
# *Supplementary material*:
#
# * [Python's documentation about floating point arithmetic](https://docs.python.org/tutorial/floatingpoint.html);
# * [How floating point numbers work](http://floating-point-gui.de/formats/fp/);
# * Advanced: [What Every Computer Scientist Should Know About Floating-Point Arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

# %% [markdown]
# ### Strings

# %% [markdown]
# Python has a built in `string` type, supporting many
# useful methods.

# %%
given = "Terry"
family = "Jones"
full = given + " " + family

# %% [markdown]
# So `+` for strings means "join them together" - *concatenate*.

# %%
print(full.upper())

# %% [markdown]
# As for `float` and `int`, the name of a type can be used as a function to convert between types:

# %%
ten, one

# %%
print(ten + one)

# %%
print(float(str(ten) + str(one)))

# %% [markdown]
# We can remove extraneous material from the start and end of a string:

# %%
"    Hello  ".strip()

# %% [markdown]
# Note that you can write strings in Python using either single (`' ... '`) or double (`" ... "`) quote marks. The two ways are equivalent. However, if your string includes a single quote (e.g. an apostrophe), you should use double quotes to surround it:

# %%
"Terry's animation"

# %% [markdown]
# And vice versa: if your string has a double quote inside it, you should wrap the whole string in single quotes.

# %%
'"Wow!", said John.'

# %% [markdown]
# ### Lists

# %% [markdown]
# Python's basic **container** type is the `list`.

# %% [markdown]
# We can define our own list with square brackets:

# %%
[1, 3, 7]

# %%
type([1, 3, 7])

# %% [markdown]
# Lists *do not* have to contain just one type:

# %%
various_things = [1, 2, "banana", 3.4, [1,2] ]

# %% [markdown]
# We access an **element** of a list with an `int` in square brackets:

# %%
various_things[2]

# %%
index = 0
various_things[index]

# %% [markdown]
# Note that list indices start from zero.

# %% [markdown]
# We can use a string to join together a list of strings:

# %%
name = ["Sir", "Michael", "Edward", "Palin"]
print("==".join(name))

# %% [markdown]
# And we can split up a string into a list:

# %%
"Ernst Stavro Blofeld".split(" ")

# %%
"Ernst Stavro Blofeld".split("o")

# %% [markdown]
# And combine these:

# %%
"->".join("John Ronald Reuel Tolkein".split(" "))

# %% [markdown]
# A matrix can be represented by **nesting** lists -- putting lists inside other lists.

# %%
identity = [[1, 0], [0, 1]]

# %%
identity[0][0]

# %% [markdown]
# ... but later we will learn about a better way of representing matrices.

# %% [markdown]
# ### Ranges

# %% [markdown]
# Another useful type is range, which gives you a sequence of consecutive numbers. In contrast to a list, ranges generate the numbers as you need them, rather than all at once.
#
# If you try to print a range, you'll see something that looks a little strange: 

# %%
range(5)

# %% [markdown]
# We don't see the contents, because *they haven't been generatead yet*. Instead, Python gives us a description of the object - in this case, its type (range) and its lower and upper limits.

# %% [markdown]
# We can quickly make a list with numbers counted up by converting this range:

# %%
count_to_five = range(5)
print(list(count_to_five))

# %% [markdown]
# Ranges in Python can be customised in other ways, such as by specifying the lower limit or the step (that is, the difference between successive elements). You can find more information about them in the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#ranges).

# %% [markdown]
# ### Sequences

# %% [markdown]
# Many other things can be treated like `lists`. Python calls things that can be treated like lists `sequences`.

# %% [markdown]
# A string is one such *sequence type*.

# %% [markdown]
# Sequences support various useful operations, including:
# - Accessing a single element at a particular index: `sequence[index]`
# - Accessing multiple elements (a *slice*): `sequence[start:end_plus_one]`
# - Getting the length of a sequence: `len(sequence)`
# - Checking whether the sequence contains an element: `element in sequence`
#
# The following examples illustrate these operations with lists, strings and ranges.

# %%
print(count_to_five[1])

# %%
print("Palin"[2])

# %%
count_to_five = range(5)

# %%
count_to_five[1:3]

# %%
"Hello World"[4:8]

# %%
len(various_things)

# %%
len("Python")

# %%
name

# %%
"Edward" in name

# %%
3 in count_to_five

# %% [markdown]
# ### Unpacking

# %% [markdown]
# Multiple values can be **unpacked** when assigning from sequences, like dealing out decks of cards.

# %%
mylist = ['Hello', 'World']
a, b = mylist
print(b)

# %%
range(4)

# %%
zero, one, two, three = range(4)

# %%
two

# %% [markdown]
# If there is too much or too little data, an error results:

# %%
zero, one, two, three = range(7)

# %%
zero, one, two, three = range(2)

# %% [markdown]
# Python provides some handy syntax to split a sequence into its first element ("head") and the remaining ones (its "tail"):

# %%
head, *tail = range(4)
print("head is", head)
print("tail is", tail)

# %% [markdown]
# Note the syntax with the \*. The same pattern can be used, for example, to extract the middle segment of a sequence whose length we might not know:

# %%
one, *two, three = range(10)

# %%
print("one is", one)
print("two is", two)
print("three is", three)
