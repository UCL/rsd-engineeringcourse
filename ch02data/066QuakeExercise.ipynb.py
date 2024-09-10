# ---
# jupyter:
#   jekyll:
#     display_name: Earthquakes Exercise
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Classroom exercise: the biggest earthquake in the UK this century
#
# ## USGS earthquake catalog
#
# [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) is a JSON-based file format for sharing geographic data. One example dataset available in the GeoJSON format is the [<abbr title="United States Geological Survey">USGS</abbr> earthquake catalog](https://www.usgs.gov/natural-hazards/earthquake-hazards/earthquakes). A [web service *application programming interface* (API)](https://earthquake.usgs.gov/fdsnws/event/1/) is provided for programatically accessing events in the earthquake catalog. Specifically the `query` method allows querying the catalog for events with the [query parameters](https://earthquake.usgs.gov/fdsnws/event/1/#parameters) passed as `key=value` pairs.
#
# We can use the [`requests` Python library](https://docs.python-requests.org/en/latest/) to simplify constructing the appropriate query string to add to the <abbr title="Uniform Resource Locator">URL</abbr> and to deal with sending the <abbr title="Hypertext Transfer Protocol">HTTP</abbr> request.

# %% jupyter={"outputs_hidden": false}
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests

# %% [markdown]
# We first define a variable <abbr title="Uniform Resource Locator">URL</abbr> for the earthquake catalog web service <abbr title="application programming interface">API</abbr>.

# %% jupyter={"outputs_hidden": false}
earthquake_catalog_api_url = "http://earthquake.usgs.gov/fdsnws/event/1/query"

# %% [markdown]
# We now need to define the parameters of our query. We want to get the data in GeoJSON format for all events in the earthquake catalog with date on or after 1st January 2000 and with location within [a bounding box covering the UK](http://bboxfinder.com/#49.877000,-8.182000,60.830000,1.767000). We will filter the events to only request those with magnitude greater or equal to 1 to avoid downloading responses for more frequent small magnitude events. Finally we want the results to be returned in order of ascending time.

# %% jupyter={"outputs_hidden": false}
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

# %% [markdown]
# We now can execute the API query using the [`requests.get` function](https://docs.python-requests.org/en/latest/api/#requests.get). This takes as arguments the <abbr title="Uniform Resource Locator">URL</abbr> to make the request from and, optionally, a dictionary argument `params` containing the parameters to send in the query string for the request. A [`requests.Response` object](https://docs.python-requests.org/en/latest/api/#requests.Response) is returned, which represents the server's response to the HTTP request made.

# %% jupyter={"outputs_hidden": false}
quakes_response = requests.get(earthquake_catalog_api_url, params=query_parameters)

# %% [markdown]
# The response object has various attributes and methods. A useful attribute to check is the `ok` attribute which will be `False` if the status code for the response to the request corresponds to a client or server error and `True` otherwise.

# %%
quakes_response.ok

# %% [markdown]
# We can also check specifically that the status code corresponds to [the expected `200 OK`](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_success) using the `status_code` attribute

# %%
quakes_response.status_code == 200

# %% [markdown]
# The actual content of the response can be accessed in various formats. The `content` attribute gives the content of the response as [bytes](https://docs.python.org/3/library/stdtypes.html#bytes). As here we expect the response content to be Unicode-encoded text, the `text` attribute is more relevant as it gives the response content as a Python string. We can display the first 100 characters of the response content as follows

# %%
print(quakes_response.text[:100])

# %% [markdown]
# ## Task
#
# The task for this exercie is to determine the location of the largest magnitude earthquake in the UK this century, using the data from the <abbr title="United States Geological Survey">USGS</abbr> earthquake catalog.
#
# You will need to:
#
#   * Query the <abbr title="United States Geological Survey">USGS</abbr> earthquake catalog for the relevant event data (see above).
#   * Parse the data as <abbr title="JavaScript Object Notation">JSON</abbr>.
#   * Understand how the data is structured into dictionaries and lists
#      * Where is the magnitude?
#      * Where is the place description or coordinates?
#   * Program a search through all the quakes to find the biggest quake.
#   * Find the place of the biggest quake.
#   * Form a <abbr title="Uniform Resource Locator">URL</abbr> for a map tile centered at that latitude and longitude (look back at the introductory example).
#   * Display that map tile image.
#
# A couple of suggestions on how to tackle this exercise:
# - make a smaller query (for example setting up the `endtime` parameter to only query a year), and
# - open the result url `quakes_response.url` with the Firefox browser to easily understand the file structure.
