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
# ## Classroom exercise: the biggest earthquake in the UK this century

# %% [markdown]
# ### The Problem

# %% [markdown]
# GeoJSON is a JSON-based file format for sharing geographic data. One example dataset is the USGS earthquake data:

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

# %%
quakes.text[0:100]

# %% [markdown]
# Your exercise: determine the location of the largest magnitude earthquake in the UK this century.

# %% [markdown]
# You'll need to:
# * Get the text of the web result
# * Parse the data as JSON
# * Understand how the data is structured into dictionaries and lists
#    * Where is the magnitude?
#    * Where is the place description or coordinates?
# * Program a search through all the quakes to find the biggest quake
# * Find the place of the biggest quake
# * Form a URL for an online map service at that latitude and longitude: look back at the introductory example
# * Display that image
