# ---
# jupyter:
#   jekyll:
#     display_name: Understanding the Exemplar
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Recap: Understanding the "Greengraph" Example

# %% [markdown]
# We now know enough to understand everything we did in [the initial example chapter on the "Greengraph"](../ch01python/010exemplar.html) ([notebook](../ch01python/010exemplar.ipynb)). Go back to that part of the notes, and re-read the code. 

# %% [markdown]
# Now, we can even write it up into a class, and save it as a module. Remember that it is generally a better idea to create files in an editor or integrated development environment (IDE) rather than through the notebook!

# %% [markdown]
# ### Classes for Greengraph
#
# The original example was written as a collection of functions. Alternatively, we can rewrite it in an object-oriented style, using classes to group related functionality.

# %% language="bash"
# mkdir -p greengraph  # Create the folder for the module (on mac or linux)

# %%
# %%writefile greengraph/graph.py

# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook

# install geopy if it is not already installed
%pip install -q geopy

import numpy as np
import geopy
from matplotlib import pyplot as plt

from .map import Map


class Greengraph(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.Nominatim(user_agent="comp0023")

    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]

    def location_sequence(self, start, end, steps):
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1], end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        """Count the amount of green space along a linear path between two locations."""
        self.steps = steps

        sequence = self.location_sequence(
            start=self.geolocate(self.start),
            end=self.geolocate(self.end),
            steps=steps,
        )
        maps = [Map(*location) for location in sequence]
        self.green_at_each_location = [current_map.count_green() for current_map in maps]

        return self.green_at_each_location

    def plot_green_between(self, steps):
        """ount the amount of green space along a linear path between two locations"""
        if not hasattr(self, 'green_at_each_location') or steps != self.steps:
            green_between_locations = self.green_between(steps)
        else:
            green_between_locations = self.green_at_each_location
        plt.plot(green_between_locations)
        xticks_steps = 5 if steps > 10 else 1
        plt.xticks(range(0, steps, xticks_steps))
        plt.xlabel("Sequence step")
        plt.ylabel(r"$N_{green}$")
        plt.title(f"{self.start} -- {self.end}")



# %%
# %%writefile greengraph/map.py
import math
from io import BytesIO

import numpy as np
import imageio.v3 as iio

# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests

class Map(object):
    def __init__(self, latitude, longitude, satellite=True, zoom=10,
                 sensor=False):
        base = "https://mt0.google.com/vt?"
        x_coord, y_coord = self.deg2num(latitude, longitude, zoom)

        params = dict(
            x=x_coord,
            y=y_coord,
            z=zoom,
        )
        if satellite:
            params['lyrs'] = 's'

        self.image = requests.get(
            base, params=params).content  # Fetch our PNG image data
        content = BytesIO(self.image)
        self.pixels = iio.imread(content) # Parse our PNG image as a numpy array

    def deg2num(self, latitude, longitude, zoom):
        """Convert latitude and longitude to XY tiles coordinates."""

        lat_rad = math.radians(latitude)
        n = 2.0 ** zoom
        x_tiles_coord = int((longitude + 180.0) / 360.0 * n)
        y_tiles_coord = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)

        return (x_tiles_coord, y_tiles_coord)

    def green(self, threshold):
        """Determine if each pixel in an image array is green."""

        # RGB indices
        red, green, blue = range(3)

        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:, :, green] > threshold * self.pixels[:, :, red]
        greener_than_blue = self.pixels[:, :, green] > threshold * self.pixels[:, :, blue]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold=1.1):
        return np.sum(self.green(threshold))

    def show_green(data, threshold=1.1):
        green = self.green(threshold)
        out = green[:, :, np.newaxis] * array([0, 1, 0])[np.newaxis, np.newaxis, :]
        buffer = BytesIO()
        result = iio.imwrite(buffer, out, extension='.png')
        return buffer.getvalue()


# %%
# %%writefile greengraph/__init__.py
from .graph import Greengraph

# %% [markdown]
# ### Invoking our code and making a plot

# %%
from matplotlib import pyplot as plt
from greengraph import Greengraph
# %matplotlib inline

mygraph = Greengraph('New York', 'Chicago')
data = mygraph.green_between(20)
mygraph.plot_green_between(20)
