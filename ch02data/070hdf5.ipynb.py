# ---
# jupyter:
#   jekyll:
#     display_name: Scientific File Formats
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Scientific File Formats
#
# CSV, JSON and YAML are very common formats for representing general-purpose data, but their simplicity sometimes makes then inconvenient for scientific applications. A common drawback, for example, is that reading very large amounts of data from a CSV or JSON file can be inefficient. This has led to to the use of more targeted file formats which better address scientists' requirements for storing, accessing or manipulating data.
#
# In this section, we will see an example of such a file format, and how to interact with files written in it programmatically.

# %% [markdown]
# ### HDF5 
#
# HDF5 is the current version of the [Hierachical Data Format](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) (HDF), and is commonly used to store large volumes of scientific data, such as experimental results or measurements. An HDF5 file contains two kinds of entities organised in a hierarchy, similar to a filesystem.
#
# - **Datasets** contain scalar or array values. Each dataset has a type, such as integer, floating-point or string.
#
# - **Groups** contain datasets or other groups, much like directories contain files and directories.
#
# Both datasets and groups can have **attributes** associated with them, which provide metadata about the contents.
#
# For example, let's imagine we are trying to store some measurements of sea level at different locations and dates. One way to organise it is shown in the image below:

# %% [markdown]
# ![Structure of an example HDF5 file, including a dataset called locations and a group called measurements, which in turns contains another dataset](hdf5_example.svg)

# %% [markdown]
# We will store the locations of our sampling points in a dataset called `locations`, and the actual results in a group called `measurements`. Within that group, we will have a dataset for each date we took samples on, which will contain results for all locations on that date. For instance, if we are collecting data from $N$ locations at $T$ times per day, each dataset will be a $N \times T$ array of numerical values (integer or floating-point, depending on how we want to record it).
#
# One of the strengths of the HDF5 format is that a file can contain disparate kinds of data, of arbitrary size and types. The attributes provide additional information about the meaning or provenance of the data, and can even link to other datasets and groups within the file.

# %% [markdown]
# #### Working with HDF5 files
#
# Unlike CSV or JSON files, which contain plain text, HDF5 is a **binary file** format. This means that the information stored there is encoded in a more complex way, and cannot be shown or edited using a simple text editor. Instead, to inspect the contents of an HDF5 file, we must use a more specialised application which "knows" how to to read the encoded information. One such application is [HDFView](https://www.hdfgroup.org/downloads/hdfview/).
#
# An alternative is to interact with files **programmatically** - that is, use some code to read or write HDF5 files. Doing this from scratch would be tricky, but there are various libraries that let you interact with an HDF5 file from within your program. You can see [examples of basic tasks](https://portal.hdfgroup.org/display/HDF5/Examples+from+Learning+the+Basics) in various programming languages, including Python, in the documentation pages of the HDF5 standard.

# %% [markdown]
# #### Accessing HDF5 files with Python
#
# Let's now see an example of creating and reading an HDF5 file with Python. In line with the above, we will use the [`h5py` library](http://docs.h5py.org/en/stable/) that gives us all the functionality we need.
#
# We'll be creating a file that follows the structure of the climate example mentioned earlier.

# %% [markdown]
# The first thing we need to do is install the library. This can be done from the terminal, with the command
# ```
# pip install h5py
# ```
# Some distributions (like Anaconda) already include this library by default, in which case this command will not do anything except report that the library is already installed.
#
# Once installed, we must import it in our file like any other library:

# %%
import h5py

# %% [markdown]
# Let's create a new HDF5 file that mirrors the structure of the above example. We start by creating an object that will represent this file in our program.

# %%
new_file = h5py.File('my_file.hdf5', 'w')

# %% [markdown]
# In the example, the file contains a dataset named `locations` and a group called `measurements` at the root level.  We can add these to our empty file using some of the methods that the file object provides.

# %%
new_file.create_dataset('locations', data=[[55.9548, -3.11], [38.045, 23.999]])

# %%
new_file.create_group('measurements')

# %% [markdown]
# Note that the library lets us create empty datasets, which can be populated later. In this case, however, we initialise the dataset with some values at creation using the `data` argument.

# %% [markdown]
# The HDF5 file objects behave somewhat like Python dictionaries: we can access the new group with the usual indexing syntax (`[...`]). This next section shows how to do that and how to add a dataset to the group. Here, we add 4 measurements for each location for that day.

# %%
group = new_file['measurements']
group.create_dataset("sea_level_20191012", data=[[10, 12, 7, 9], [20, 18, 23, 22]])

# %% [markdown]
# When we are done with writing to the file, we must make sure to close it, so that all the changes are written to it (if they have not been already) and any used memory is released:

# %%
new_file.close()

# %% [markdown]
# There is a different style for reading and writing files, which is safer and saves you the need to close the file after you are finished. We can use this to read a file and iterate over its contents:

# %%
with h5py.File('my_file.hdf5', 'r') as hdf_file:
    # Print out contents of root group
    print("/ contains...")
    for name in hdf_file:
        print(name)
    # Now print out the contents of the measurements group:
    print("/measurements contains...")
    for name in hdf_file['/measurements']:
        print(name)

# %% [markdown]
# This is similar to the `with open(...)` syntax we use to work with text files - it is another example of a context manager.

# %% [markdown]
# There are many more ways you can access a file with `h5py`. If you are interested, you can look at [the quick-start guide](http://docs.h5py.org/en/stable/quick.html) from its documentation for an overview.

# %% [markdown]
# ### Other formats
#
# HDF5 is used across various scientific fields to store data, but some disciplines tend to use other file formats. Examples of such formats (and the python libraries) that are popular in particular disciplines are [DICOM](https://en.wikipedia.org/wiki/DICOM) ([`pydicom`](https://pydicom.github.io/pydicom/stable/)) for medical imaging, [FITS](https://en.wikipedia.org/wiki/FITS) ([`astropy.io.fits`](http://docs.astropy.org/en/stable/io/fits/)) in astronomy, and [NetCDF](https://en.wikipedia.org/wiki/NetCDF) ([`netCDF4`](https://unidata.github.io/netcdf4-python/netCDF4/index.html)) in the geosciences.
#
# The overall points that we have made about HDF5 generally apply to these formats as well. They are binary files which require specific applications, but you can also use various libraries to interact with them programmatically. Some libraries even offer support for multiple related types of files, such as different image formats.
#
# If you often need to work with a particular type of files, try finding a relevant library in your chosen language. If you have not used it before, are you able to read or write a file using it?
