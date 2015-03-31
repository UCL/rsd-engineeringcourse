---
title: Exercises
---

###Exercises

We previously looked at Greengraph.py, a script that enables us to explore how green space varies as we move from the city to the countryside:

``` python
### "geolocation"
import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

def geolocate(place):
    return geocoder.geocode(place,exactly_one=False)[0][1]

london_location=geolocate("London")
print london_location

...
```

The Greengraph example is only available as a single large [script](https://github.com/UCL/rsd-engineeringcourse/blob/master/session04/python/greengraph.py).

Your task is to transform this into a python package that can be pip installed directly from GitHub. Remember to include:

- an \__init\__.py file
- a setup.py file
- tests
- license and documentation


