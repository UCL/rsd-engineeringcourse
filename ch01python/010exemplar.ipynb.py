# ---
# jupyter:
#   jekyll:
#     display_name: An example program
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## An example Python data analysis notebook

# %% [markdown]
# This page illustrates how to use Python to perform a simple but complete analysis: retrieve data, do some computations based on it, and visualise the results.
#
# **Don't worry if you don't understand everything on this page!** Its purpose is to give you an example of things you can do and how to go about doing them - you are not expected to be able to reproduce an analysis like this in Python at this stage! We will be looking at the concepts and practices introduced on this page as we go along the course.
#
# As we show the code for different parts of the work, we will be touching on various aspects you may want to keep in mind, either related to Python specifically, or to research programming more generally.

# %% [markdown]
# ### Why write software to manage your data and plots? 

# %% [markdown]
# We can use programs for our entire research pipeline. Not just big scientific simulation codes, but also the small scripts which we use to tidy up data and produce plots. This should be code, so that the whole research pipeline
# is recorded for reproducibility. Data manipulation in spreadsheets is much harder to share or 
# check. 

# %% [markdown]
# You can see another similar demonstration on the [software carpentry site](https://swcarpentry.github.io/python-novice-inflammation/02-numpy.html).
# We'll try to give links to other sources of Python training along the way.
# Part of our approach is that we assume you know how to use the internet! If you
# find something confusing out there, please bring it along to the next session. In this course, we'll always try to draw your attention to other sources of information about what we're learning. Paying attention to as many of these as you need to, is just as important as these core notes.

# %% [markdown]
# ### Importing Libraries

# %% [markdown]
# Research programming is all about using libraries: tools other people have provided programs that do many cool things.
# By combining them we can feel really powerful but doing minimum work ourselves. The python syntax to import someone else's library is "import".

# %%
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook

# install geopy if it is not already installed
%pip install geopy

import geopy # A python library for investigating geographic information.
# https://pypi.org/project/geopy/

# %% [markdown]
# Now, if you try to follow along on this example in an Jupyter notebook, you'll probably find that 
# you just got an error message.
#
# You'll need to wait until we've covered installation of additional python libraries later in the course, then come
# back to this and try again. For now, just follow along and try get the feel for how programming for data-focused
# research works.

# %%
# Select geocoding service provided by OpenStreetMap's Nominatim - https://wiki.openstreetmap.org/wiki/Nominatim
geocoder = geopy.geocoders.Nominatim(user_agent="comp0023") 
geocoder.geocode('Cambridge', exactly_one=False)

# %% [markdown]
# The results come out as a **list** inside a list: `[Name, [Latitude, Longitude]]`. 
# Programs represent data in a variety of different **containers** like this.

# %% [markdown]
# ### Comments

# %% [markdown]
# Code after a `#` symbol doesn't get run.

# %%
print("This runs") # print("This doesn't")
# print("This doesn't either")

# %% [markdown]
# ### Functions

# %% [markdown]
# We can wrap code up in a **function**, so that we can repeatedly get just the information we want.
#

# %%
def geolocate(city):
    """Get the latitude and longitude of a specific location."""
    
    full_name, coordinates = geocoder.geocode(city)
    return coordinates


# %% [markdown]
# Defining **functions** which put together code to make a more complex task seem simple from the outside is the most important thing in programming. The output of the function is specified using the `return` keyword. The input to the function is put inside brackets after the function name:
#

# %%
geolocate(city='Cambridge')

# %% [markdown]
# ### Variables

# %% [markdown]
# We can store a result in a variable:

# %%
london_location = geolocate("London")
print(london_location)

# %% [markdown]
# ### More complex functions

# %% [markdown]
# We'll fetch a map of a place from the Google Maps server, given a longitude and latitude.
# The URLs look like: `https://mt0.google.com/vt?x=658&y=340&z=10&lyrs=s`. Since we'll frequently be generating these URLs, we will create two helper functions to make our life easier.
#
# The first is a function to [convert our latitude and longitude into the coordinate tiles system used by Google Maps](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#X_and_Y).
# We will then create a second function to build up a web request from the URL given our parameters.
#

# %%
import os
import math
import requests

def deg2num(lat_deg, lon_deg, zoom):
    """Convert latitude and longitude to XY tiles coordinates."""

    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    x_tiles_coord = int((lon_deg + 180.0) / 360.0 * n)
    y_tiles_coord = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)

    return (x_tiles_coord, y_tiles_coord)

def request_map_at(latitude, longitude, zoom=10, satellite=True):
    """Retrieve a map from Google at a given location."""

    base_url = "https://mt0.google.com/vt?"
    x_coord, y_coord = deg2num(latitude, longitude, zoom)

    params = dict(
        x=x_coord,
        y=y_coord,
        z=zoom,
    )
    if satellite:
        params['lyrs'] = 's'
    
    return requests.get(base_url, params=params)



# %%
london_latitude, london_longitude = london_location
map_response = request_map_at(london_latitude, london_longitude)


# %% [markdown]
# ### Checking our work

# %% [markdown]
# Let's see what URL we ended up with.
#
# Firsty we will define two constants so that we can split the returned URL into the base URL and the part of the URL that corresponds to the location we requested:
#

# %%
url = map_response.url

first_25s = slice(0, 25)
from_25th = slice(25, None)

print(url)
print(url[first_25s])
print(url[from_25th])


# %% [markdown]
# `url` is a string and we can select parts of this string using the `slice`s we defined above. `first_25s` will select characters 0 to 24 of the string and `from_25th` will select all characters from the 25th onwards.
#

# %% [markdown]
# We can write **tests** so that if we change our code later we can check the results are still valid. We will do this here using `assert` statements. If any of those `assert` statements are `False` we will get an error. If we receive an error from our tests we know we need to fix something in our code.

# %%
assert "https://mt0.google.com/vt?" in url
assert "z=10" in url
assert "lyrs=s" in url


# %% [markdown]
# Our previous function comes back with an Object representing the web request. In Python, we can use the `.
# operator` to get access to a particular **attribute** of the object. In this case, the image at the requested URL is stored in the `content` attribute. It's a big file, so let's just get look at first few bytes:
#

# %%
map_response.content[0:20]


# %% [markdown]
# ### Displaying results

# %% [markdown]
# We'll need to do this a lot, so we can wrap up our previous function in another function to save on typing.

# %%
def map_content_at(latitude, longitude, zoom=10, satellite=True):
    """Retrieve a map image from Google at a given location."""

    return request_map_at(latitude, longitude, zoom=10, satellite=True).content



# %% [markdown]
# We can use a library that comes with Jupyter notebook to display the image. This is one of the most powerful things about modern programming languages like Python - being able to work with images, documents, or any other kind of data just as easily as we can with numbers or strings.
#

# %%
import IPython

map_png = map_content_at(london_latitude, london_longitude)


# %%
print("The type of our map result is actually a: ", type(map_png))


# %%
IPython.display.Image(map_png)

# %%
IPython.display.Image(map_content_at(*geolocate("New Delhi")))

# %% [markdown]
# ### Manipulating Numbers

# %% [markdown]
# Now we get to our research project: we want to use satellite imagery to find out how urbanised the world is along a line between two cites. We expect the satellite image to be greener in the countryside.
#

# %% [markdown]
# We'll need to import a few more libraries to count how much green there is in an image.
#

# %%
from io import BytesIO  # A library to convert between files and strings
import numpy as np  # A library to deal with matrices
import imageio.v3 as iio  # A library to deal with images


# %% [markdown]
# Let's define what we count as green:

# %%
def is_green(pixels):
    """Determine if each pixel in an image array is green."""
    
    # RGB indices
    red, green, blue = range(3)

    threshold = 1.1
    greener_than_red = pixels[:, :, green] > threshold * pixels[:, :, red]
    greener_than_blue = pixels[:, :, green] > threshold * pixels[:, :, blue]
    green = np.logical_and(greener_than_red, greener_than_blue) 

    return green



# %% [markdown]
# This code has assumed we have our pixel data for the image as a $256 \times 256 \times 3$ 3-d matrix,
# with each of the three layers being red, green, and blue pixels.
#
# We find out which pixels are green by comparing, element-by-element, the middle (green, number 1) layer to the top (red, zero) and bottom (blue, 2)

# %% [markdown]
# Now we just need to parse in our data, which is a PNG image, and turn it into our matrix format:

# %%
def count_green_in_png(data):
    """Determine the total number of green pixels in an image."""

    f = BytesIO(data)
    pixels = iio.imread(f) # Get our PNG image as a numpy array

    return np.sum(is_green(pixels))



# %%
london_map = map_content_at(london_latitude, london_longitude)
green_count_london = count_green_in_png(london_map)
print(green_count_london)


# %%
iio.imread(BytesIO(london_map)).shape


# %% [markdown]
# We'll also need a function to get an evenly spaced set of places between two endpoints:

# %%
def location_sequence(start, end, steps):
    """Generate a sequence of evenly spaced locations between two sets of coordinates."""

    start_latitude, start_longitude = start
    end_latitude, end_longitude = end
    
    latitudes = np.linspace(start_latitude, end_latitude, steps)
    longitudes = np.linspace(start_longitude, end_longitude, steps)

    path = np.vstack([latitudes, longitudes]).transpose()
    
    return path



# %%
london_to_cambridge = location_sequence(
    start=geolocate("London"),
    end=geolocate("Cambridge"),
    steps=5,
)
print(london_to_cambridge)


# %% [markdown]
# ### Creating Images

# %% [markdown]
# We should display the green content to check our work:

# %%
def show_green_in_png(data):
    """Convert all non-green pixels in an RGB image to black.

    Red and blue channel are set to 0 for all pixels.
    Pixels that are green will have the green channel set to its max value.
    Pixels that are non-green will have the green channel set to 0.
    """

    f = BytesIO(data)
    pixels = iio.imread(f) # Get our PNG image as a numpy array
    green_pixels = is_green(pixels)

    green_channel = 1
    binary_pixels = np.zeros_like(pixels, dtype=np.uint8)
    max_possible_value =  np.iinfo(binary_pixels.dtype).max
    binary_pixels[green_pixels, green_channel] = max_possible_value

    buffer = BytesIO()
    binary_image = iio.imwrite(buffer, binary_pixels, extension='.png')

    return buffer.getvalue()



# %%
london_location

# %%
IPython.display.Image(
    map_content_at(london_latitude, london_longitude, satellite=True)
)

# %%
IPython.display.Image(
    show_green_in_png(
        map_content_at(
            london_latitude,
            london_longitude,
            satellite=True,
        )
    )
)


# %% [markdown]
# ### Looping

# %% [markdown]
# We can loop over each element in out list of coordinates and get a map for that place:

# %%
london_to_birmingham = location_sequence(
    start=geolocate("London"),
    end=geolocate("Birmingham"),
    steps=10,
)

london_to_birmingham_maps = []

for latitude, longitude in london_to_birmingham:

    current_map = map_content_at(latitude, longitude)
    london_to_birmingham_maps.append(current_map)
    
    IPython.display.display(
        IPython.display.Image(
            current_map,
        )
    )


# %% [markdown]
# So now we can count the green from London to Birmingham!

# %%
green_at_each_location = [count_green_in_png(current_map) for current_map in london_to_birmingham_maps]
print(green_at_each_location)


# %% [markdown]
# ### Plotting graphs

# %% [markdown]
# Let's plot a graph.

# %%
import matplotlib.pyplot as plt
# %matplotlib inline

# %%
plt.plot(green_at_each_location)

plt.xticks(range(10))
plt.xlabel("Sequence step")
plt.ylabel(r"$N_{green}$")


# %% [markdown]
# From a research perspective, of course, this code needs a lot of work. But I hope the power of using programming is clear.
#

# %% [markdown]
# ### Composing Program Elements

# %% [markdown]
# We built little pieces of useful code, to:
#
# * Find latitude and longitude of a place
# * Get a map at a given latitude and longitude
# * Decide whether a (red,green,blue) triple is mainly green
# * Decide whether each pixel is mainly green
# * Plot a new image showing the green places
# * Find evenly spaced points between two places

# %% [markdown]
# By putting these together, we can make a function which can plot this graph automatically for any two places:

# %%
def green_between(start, end, steps):
    """Count the amount of green space along a linear path between two locations."""

    sequence = location_sequence(
        start=geolocate(start),
        end=geolocate(end),
        steps=steps,
    )
    maps = [map_content_at(latitude, longitude) for latitude, longitude in sequence]
    green_at_each_location = [count_green_in_png(current_map) for current_map in maps]
    
    return green_at_each_location



# %%
plt.plot(green_between('New York', 'Chicago', 20))


# %% [markdown]
# We can also put the plotting command into a function, to make it more general:
#

# %%
def plot_green_between(start, end, steps):
    """ount the amount of green space along a linear path between two locations"""
    green_between_locations = green_between(start, end, steps)
    plt.plot(green_between_locations)
    xticks_steps = 5 if steps > 10 else 1
    plt.xticks(range(0, steps, xticks_steps))
    plt.xlabel("Sequence step")
    plt.ylabel(r"$N_{green}$")
    plt.title(f"{start} -- {end}")



# %%
plot_green_between('New York', 'Chicago', 20)

# %% [markdown]
# And that's it! We've covered - very very quickly - a lot of the Python language, and have introduced some of the most important concepts in modern software engineering.

# %% [markdown]
# Now we'll go back, carefully, through all the concepts we touched on, and learn how to use them properly ourselves.
