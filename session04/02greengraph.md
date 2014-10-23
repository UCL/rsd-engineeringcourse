---
title: Libraries example
---

##Graph of Green Spaces

###The problem

Let's look at an extended example of using libraries to work with Python to analyse data.

We'd like to know how density of green space varies as we move from city centre to the countryside:

* Find the location of two places by name
* Obtain maps or satellite images of the geography at points between them
    * In this toy example: just evenly divide the range
* Determine the proportion of the images that are parkland
    * In this toy example: bits that are green!
* Plot a graph

###Geolocation

Google provides a service to go from "London" to 51.51N, 0.1275W. Fortunately, there's a very nice library
on PyPI to access it: `pip install geopy`

{{ pyfrag('04','greengraph','geolocation') }}

###Addressing the google maps API

Google maps has a static API to obtain satellite images with URLs like this:

[http://maps.googleapis.com/maps/api/staticmap?style=feature:all|element:labels|visibility:off&size=400x400&sensor=false&zoom=10&center=51.5072,-0.1275](http://maps.googleapis.com/maps/api/staticmap?style=feature:all|element:labels|visibility:off&size=400x400&sensor=false&zoom=10&center=51.5072,-0.1275)

We'll therefore need to use a library to build this URL, and fetch the result

`sudo pip install pypng` will get you this library.

{{ pyfrag('04','greengraph','URL') }}

{% if notebook %}
```python
import IPython
map_png=map_at(*london_location)
IPython.core.display.Image(map_png.content)
```
{% endif %}

###Finding the green bits

We'll need a library to parse `.png` image files and determine which bits are green:

{{ pyfrag('04','greengraph', 'png')}}

###Checking our code

We could write some unit tests, but for something like this, visualisation is the key to
verification. Let's look which bits are green by building a new png.

We could write the new png to disk, but we can use `StringIO` to get a string in memory which
behaves like a file:

{{ pyfrag('04','greengraph', 'visualise') }}

{% if notebook %}
```python
IPython.core.display.Image(show_green_in_png(map_at(*london_location,satellite=True)))
```
{% else %}
![The green bits of London](session04/python/green.png)
{% endif %}

###Points in between

We need all the points equally spaced between two locations.
Numpy has a routine for just this:

{{ pyfrag('04','greengraph','points') }}

###The results

{% if notebook %}
``` python
import matplotlib.pyplot as plt
%matplotlib inline
plt.plot([count_green_in_png(get_map(*location,zoom=10,satellite=True))
            for location in location_sequence(geolocate("London"),geolocate("Birmingham"),10)])
```
{% else %}
{{ pyfrag('04','greengraph', 'save') }}
![The density of green space between London and Birmingham](session04/python/greengraph.png)
{% endif %}


