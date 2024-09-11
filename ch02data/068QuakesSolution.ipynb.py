# ---
# jupyter:
#   jekyll:
#     display_name: Quakes Solution
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Solution: the biggest earthquake in the UK this century
#
# ## Import modules
#
# We first import the modules we will need to get and plot the data. We will use the `requests` module to query the USGS earthquake catalog, the `math` module to do some coordinate conversion and the `IPython` module to display a map image.

# %% jupyter={"outputs_hidden": false}
import math

# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests
import IPython
from IPython.display import Image

# %% [markdown]
# ## Download the data
#
# We can reuse the code provided in the exercise notebook to query the USGS earthquake catalog API using the `requests` module.

# %%
earthquake_catalog_api_url = "http://earthquake.usgs.gov/fdsnws/event/1/query"
query_parameters = {
    "format": "geojson",
    "starttime": "2001-01-01",
    "maxlatitude": "60.830",
    "minlatitude": "49.877",
    "maxlongitude": "1.767",
    "minlongitude": "-8.182",
    "minmagnitude": "1",
    "orderby": "time-asc"
}
quakes_response = requests.get(earthquake_catalog_api_url, params=query_parameters)

# %% [markdown]
# We can check that the returned object is a `Response` as expected

# %% jupyter={"outputs_hidden": false}
type(quakes_response)

# %% [markdown]
# It is also useful to check whether the status of the returned response corresponds to there not being any client or server errors, with this being indicated by a status code of 200

# %% jupyter={"outputs_hidden": false}
assert quakes_response.status_code == 200

# %% [markdown]
# ## Parse the data as JSON

# %% [markdown]
# We saw in the exercise notebooks that the `Reponse` objects returned by `requests.get` have various attributes that allow accessing the response content in different formats including `Response.content` to get the raw `bytes` content and `Response.text` to get the response as a (Unicode) `str` object. We can print out all of the attributes of an object in Python using the inbuilt `dir` function; typically these will include attributes intended for internal use only which are conventionally indicated by prefixing with an underscore character `_`. We can display all the attributes without an initial underscore character as follows.

# %%
[attribute for attribute in dir(quakes_response) if attribute[0] != '_']

# %% [markdown]
# As well as the `content`, `ok`, `status_code` and `text` attributes we already encountered, we can see there is also a `json` attribute, which seems like it could be  relevant to our task of decoding the response as JSON. We can find out more about this attribute by using a useful feature of Jupyter / IPython - by adding a question mark `?` to the end of a Python object the documentation string (`docstring`) for that object will be displayed.

# %%
# quakes_response.json?

# %% [markdown]
# From this we can see that `quakes.response` is a method (function bound to an object) which returns a Python object corresponding to a JSON encoded response, which is exactly what we need. There are no required arguments so we can call the method by just adding a pair of empty parentheses.

# %% jupyter={"outputs_hidden": false}
quakes_json = quakes_response.json()

# %% [markdown]
# If we had not been aware of the `json` method an alternative would be to use the `json` module directly as we saw previously. For example the following would give an equivalent result to the above.
#
# ```Python
# import json
# quakes_json = json.loads(quakes_response.text)
# ```

# %% [markdown]
# ## Investigate the data to discover how it is structured.
#
# Now that we have queried and decoded the data into a Python object, we need to do some exploration to find out how it is structure. In some cases there may be documentation we can use to help guide our exploration of data - for example [this page on the USGS earthquake catalog website](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) gives a summary of the GeoJSON format. However, in other cases we may not be so lucky and have to work with data with an undocumented format so it is also useful to consider how we might explore that data structure ourselves.  
#
#
# A potentially useful first step is to check what the type of the `quakes_json` object is.

# %% jupyter={"outputs_hidden": false}
type(quakes_json)

# %% [markdown]
# We see that `quakes_json` is a Python `dict` (dictionary) object. We might want to find out what keys are defined in this dictionary - we can do this by calling the `keys` method.

# %% jupyter={"outputs_hidden": false}
quakes_json.keys()

# %% [markdown]
# We see that the dictionary has three keys, all of which are strings. The `features` key in particular here looks potentially promising for our goal of finding the maximum magnitude event in the data (on the rationale that the magnitude is a *feature* of the event). We can check what type the value associated with the `features` key is.

# %% jupyter={"outputs_hidden": false}
type(quakes_json['features'])

# %% [markdown]
# We find out that the `features` key contains a list. We can check the length of this list.

# %% jupyter={"outputs_hidden": false}
len(quakes_json['features'])

# %% [markdown]
# We could also use a set (which we encountered previously in the lesson on dictionaries) to find out what the set of types of all of the elements in the `quakes_json['features']` list is. Similarly to the list comprehensions we encountered in a previous lesson we can use a similar syntax here to succinctly construct the set we required.

# %%
{type(feature) for feature in quakes_json['features']}

# %% [markdown]
# From this we see that all of the elements in the `quakes_json['features']` share the same Python `dict` type. We can use a similar approach to find out what keys all these dictionary objects have.

# %%
{tuple(feature.keys()) for feature in quakes_json['features']}

# %% [markdown]
# This tells us that as well as all the elements being dictionaries, all of the dictionaries have the same keys. This suggests the list corresponds to a representation of a sequence of objects of the same type, with each dictionary containing the 'features' for a particular object, with in in this case the objects in questions being particular earthquake events.
#
# To check this idea, we can look at the value of a particular element in the `features` list - as we know all elements are dictionaries with the same keys, its reasonable to assume the first element `quakes_json['features'][0]` will be representative of the all the other elements in the list. We can start by summarising the keys and types of the values in this dictionary.

# %%
for key, value in quakes_json['features'][0].items():
    print(key, type(value).__name__)       

# %% [markdown]
# We can also view the dictionary directly

# %%
quakes_json['features'][0]

# %% [markdown]
# From this we can see the `properties` and `geometry` keys both themselves map to `dict` objects. Within these inner dictionaries are several keys which look relevant to our task of identifying the highest magnitude earthquake event and displaying its location on a map. Specifically the `mag` key in the `properties` dictionary seems likely to represent the magnitude of the event 

# %%
quakes_json['features'][0]['properties']['mag']

# %% [markdown]
# while the `coordinates` key in the `geometry` dictionary seems to represent the location of the event. 

# %%
quakes_json['features'][0]['geometry']['coordinates']

# %% [markdown]
# If go to the URL listed as the value for the `url` key in the `properties` dictionary, 

# %%
quakes_json['features'][0]['properties']['url']

# %% [markdown]
# we can confirm that this is indeed a correct interpretation of the data as the listed magnitude corresponds to the value for the `mag` key while the longitude (East-West axis) and latitude (North-South axis) coordinates (in degrees) of the event location correspond to the first two elements respectively in the list associated with the `coordinates` key (with the third coordinate corresponding to the depth of the event).

# %% [markdown]
# ## Find the largest quake(s)
#
# Now that we have a handle on the structure of the data, we are ready to search through the data to identify the largest magnitude earthquake event(s). We are interested in finding the element (or elements) in a sequence which maximises some property - this operation is termed the [$\arg\max$ in mathematics and computer science](https://en.wikipedia.org/wiki/Arg_max). While there is built-in `max` function in Python there is no corresponding `argmax` function, though several external libraries including the NumPy library which we encounter in a subsequent lesson do include an `argmax` function.
#
# As a first approach, we will set the first eartquake to be the largest and as we iterate over the others we will replace the first one with whatever is larger.

# %%
quakes = quakes_json['features']

largest_so_far = quakes[0]
for quake in quakes:
    if quake['properties']['mag'] > largest_so_far['properties']['mag']:
        largest_so_far = quake
largest_so_far['properties']['mag']

# %% [markdown]
# Great, this gives us the largest earthquake... but, what if there were multiple earthquakes with the same magnitude? 
# Can we know it from the above result?
# We will therefore loop over all of the event details in the `features` list and construct a list of the event or events for which the magnitude is currently the largest, creating a new list if the magnitude of the current event is larger than the previous largest or adding the event to the previous list if it has an equal magnitude. After iterating through all the events this list should contain the details of the event(s) with the largest magnitude. An example implementation of this approach is as follows.

# %% jupyter={"outputs_hidden": false}
largest_magnitude_events = [quakes[0]]

for quake in quakes:
    if quake['properties']['mag'] > largest_magnitude_events[0]['properties']['mag']:
        largest_magnitude_events = [quake]
    elif quake['properties']['mag'] == largest_magnitude_events[0]['properties']['mag']:
        largest_magnitude_events += [quake]

# %% [markdown]
# We can now check if there was a single event with the maximum magnitude or multiple

# %%
len(largest_magnitude_events)

# %% [markdown]
# It turns out there are two events with the same maximal magnitude. As a sanity check we can print the magnitude of both events to check that they match

# %% jupyter={"outputs_hidden": false}
print([quake['properties']['mag'] for quake in largest_magnitude_events])


# %% [markdown]
# ## Get a map at the point of the quake

# %% [markdown]
# We saw something similar in the [Greengraph example](../ch01python/010exemplar.html#More-complex-functions) [(notebook version)](../ch01python/010exemplar.ipynb#More-complex-functions) of the previous chapter.

# %%
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

# %% [markdown]
# As a test we can check the map displayed for the coordinates of the [Prime meridian at the Royal Observatory Greenwich](https://geohack.toolforge.org/geohack.php?pagename=Prime_meridian_(Greenwich)&params=51_28_40.1_N_0_0_5.3_W_type:landmark_globe:earth_region:GB_scale:1000)

# %%
map_response = request_map_at(51.477806, -0.001472, zoom=14)
Image(map_response.content)

# %% [markdown]
# ## Display the maps
#
# We can now finally show the maps for the locations of the maximum magnitude earthquake events. As additional check we also print the description under the `title` key in the `properties` dictionary for the event to check it tallies with the location shown in the displayed map.

# %%
for quake in largest_magnitude_events:
    longitude = quake['geometry']['coordinates'][0]
    latitude = quake['geometry']['coordinates'][1]
    print(quake['properties']['title'])
    display(Image(request_map_at(latitude, longitude, 12).content))
