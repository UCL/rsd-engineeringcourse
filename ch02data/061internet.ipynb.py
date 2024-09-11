# ---
# jupyter:
#   jekyll:
#     display_name: Internet
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Getting data from the internet

# %% [markdown]
# We've seen about obtaining data from our local file system.

# %% [markdown]
# The other common place today that we might want to obtain data is from the internet.

# %% [markdown]
# It's very common today to treat the web as a source and store of information; we need to be able to programmatically
# download data, and place it in Python objects.

# %% [markdown]
# We may also want to be able to programmatically *upload* data, for example, to automatically fill in forms.

# %% [markdown]
# This can be really powerful if we want to, for example, do automated meta-analysis across a selection of research papers.

# %% [markdown]
# ## Uniform resource locators

# %% [markdown]
# All internet resources are defined by a [_uniform resource locator_ (URL)](https://en.wikipedia.org/wiki/URL) which are a particular type of [_uniform resource identifier_ (URI)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). For example

# %%
"https://mt0.google.com:443/vt?x=658&y=340&z=10&lyrs=s"

# %% [markdown]
# A URL consists of:
#
# * A *scheme* (`http` [_hypertext transfer protocol_](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), `https` [_hypertext transfer protocol secure_ ](https://en.wikipedia.org/wiki/HTTPS), `ssh` [_secure shell_](https://en.wikipedia.org/wiki/Secure_Shell), ...)
# * A *host* (`mt0.google.com`, the name of the remote computer you want to talk to)
# * A *port* (optional, most protocols have a typical port associated with them, e.g. 80 for HTTP, 443 for HTTPS)
# * A *path* (analogous to a file path on the machine, here it is just `vt`)
# * A *query* part after a ?, (optional, usually ampersand `&` separated *parameters* e.g. `x=658` or `z=10`)

# %% [markdown]
# **Supplementary materials**: These can actually be different for different protocols, the above is a simplification, you can see more, for example, at
#     [the Wikipedia article on URIs](https://en.wikipedia.org/wiki/URI_scheme).

# %% [markdown]
# URLs are not allowed to include all characters; we need to, for example, [_escape_](https://en.wikipedia.org/wiki/Escape_character) a space that appears inside the URL, replacing it with `%20`, so e.g. a request of `http://some example.com/` would need to be `http://some%20example.com/`.
#

# %% [markdown]
# **Supplementary materials**: The code used to replace each character is the [ASCII](http://www.asciitable.com) code for it.

# %% [markdown]
# **Supplementary materials**: The escaping rules are quite subtle. See [the Wikipedia article on percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding). The standard library provides the [urlencode](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) function that can take care of this for you.

# %% [markdown]
# ## Requests

# %% [markdown]
# The Python [Requests](http://docs.python-requests.org/en/latest/) library can help us manipulate URLs and requesting the content associated with them. It is easier to use than the `urllib` library that is part of the standard library, and is included with Anaconda and Canopy. It sorts out escaping, parameter encoding, and so on for us.

# %%
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests

# %% [markdown]
# To request the above URL, for example, we write:

# %%
response = requests.get(
    url="https://mt0.google.com:443/vt", 
    params={'x': 658, 'y': 340, 'lyrs': 's', 'z': 10}
)

# %% [markdown]
# The returned object is a instance of the `requests.Response` class

# %%
response

# %%
isinstance(response, requests.Response)

# %% [markdown]
# The `Response` class defines various useful attributes associated with the responses, for example we can check the [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for our request with a value of 200 indicating a successful request

# %%
response.status_code

# %% [markdown]
# We can also more directly check if the response was successful or not with the boolean `Response.ok` attribute

# %%
response.ok

# %% [markdown]
# We can get the URL that was requested using the `Response.url` attribute

# %%
response.url

# %% [markdown]
# When we do a request, the associated response content, accessible at the `Response.content` attribute, is returned as bytes. For the JPEG image in the above, this isn't very readable:

# %%
type(response.content)

# %%
response.content[:10]

# %% [markdown]
# We can also get the content as a string using the `Response.content` attribute, though this is even less readable here as some of the returned bytes do not have corresponding character encodings

# %%
type(response.text)

# %%
response.text[:10]

# %% [markdown]
# To get a more useful representation of the data, we will therefore need to process the content we get using a Python function which understands the byte-encoding of the corresponding file format.

# %% [markdown]
# Again, it is important to separate the *transport* model, (e.g. a file system, or a HTTP request for the web), from the data model of the data that is returned.

# %% [markdown]
# ## Example: sunspots

# %% [markdown]
# Let's try to get something scientific: the sunspot cycle data from the [Sunspot Index and Long-term Solar Observations website](http://sidc.be/silso/home)

# %%
spots = requests.get('http://www.sidc.be/silso/INFO/snmtotcsv.php').text

# %%
spots[-100:]

# %% [markdown]
# This looks like semicolon-separated data, with different records on different lines. Line separators come out as `\n` which is the escape-sequence corresponding a newline character in Python.

# %% [markdown]
# There are many many scientific datasets which can now be downloaded like this - integrating the download into your data
# pipeline can help to keep your data flows organised.

# %% [markdown]
# ## Writing our own parser

# %% [markdown]
# We'll need a Python library to handle semicolon-separated data like the sunspot data.

# %% [markdown]
# You might be thinking: "But I can do that myself!":

# %%
lines = spots.split("\n")
lines[0:5]

# %%
years = [line.split(";")[0] for line in lines]

# %%
years[0:15]

# %% [markdown]
# But **don't**: what if, for example, one of the records contains a separator inside it; most computers will put the content in quotes,
# so that, for example,
#
#     "Something; something"; something; something
#     
# has three fields, the first of which is
#
#     Something; something
#    

# %% [markdown]
# Our naive code above would however not correctly parse this input:

# %%
'"Something; something"; something; something'.split(';')

# %% [markdown]
# You'll never manage to get all that right; so you'll be better off using a library to do it.

# %% [markdown]
# ## Writing data to the internet

# %% [markdown]
# Note that we're using `requests.get`. `get` is used to receive data from the web.
# You can also use `post` to fill in a web-form programmatically.

# %% [markdown]
# **Supplementary material**: Learn about using `post` with [Requests](http://docs.python-requests.org/en/latest/user/quickstart/).

# %% [markdown]
# **Supplementary material**: Learn about the different kinds of [HTTP request](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods): [Get, Post, Put, Delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)...

# %% [markdown]
# This can be used for all kinds of things, for example, to programmatically add data to a web resource. It's all well beyond
# our scope for this course, but it's important to know it's possible, and start to think about the scientific possibilities.
