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
# ## Solution to the earthquake exercise
#
# **NOTE:** This is intended as a reference for **after** you have attempted [the problem](./066QuakeExercise.html) [(notebook version)](./066QuakeExercise.ipynb) yourself!

# %% [markdown]
# ### Download the data

# %%
import requests
quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

# %% [markdown]
# ### Parse the data as JSON

# %%
import json

# %%
requests_json = json.loads(quakes.text)

# %% [markdown]
# ### Investigate the data to discover how it is structured

# %% [markdown]
# There is no foolproof way of doing this. A good first step is to see the type of our data!

# %%
type(requests_json)

# %% [markdown]
# Now we can navigate through this dictionary to see how the information is stored in the nested dictionaries and lists. The `keys` method can indicate what kind of information each dictionary holds, and the `len` function tells us how many entries are contained in a list. How you explore is up to you!

# %%
requests_json.keys()

# %%
len(requests_json['features'])

# %%
requests_json['features'][0].keys()

# %%
requests_json['features'][0]['properties'].keys()

# %%
requests_json['features'][0]['properties']['mag']

# %%
requests_json['features'][0]['geometry']

# %% [markdown]
# Also note that some IDEs display JSON in a way that makes its structure easier to understand. Try saving this data in a text file and opening it in an IDE or a browser.

# %% [markdown]
# ### Find the largest quake

# %%
quakes = requests_json['features']

# %%
largest_so_far = quakes[0]
for quake in quakes:
    if quake['properties']['mag'] > largest_so_far['properties']['mag']:
        largest_so_far = quake
largest_so_far['properties']['mag']

# %%
lat = largest_so_far['geometry']['coordinates'][1]
long = largest_so_far['geometry']['coordinates'][0]
print("Latitude: {} Longitude: {}".format(lat, long))

# %% [markdown]
# ### Get a map at the point of the quake

# %% [markdown]
# We saw something similar in the [Greengraph example](../ch01python/010exemplar.html#More-complex-functions) [(notebook version)](../ch01python/010exemplar.ipynb#More-complex-functions) of the previous chapter.

# %%
import requests


def request_map_at(lat, long, satellite=True,
                   zoom=10, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"

    params = dict(
        z=zoom,
        size="{},{}".format(size[0], size[1]),
        ll="{},{}".format(long, lat),
        l="sat" if satellite else "map",
        lang="en_US"
    )

    return requests.get(base, params=params)


# %%
map_png = request_map_at(lat, long, zoom=10, satellite=False)

# %% [markdown]
# ### Display the map

# %%
from IPython.display import Image
Image(map_png.content)
