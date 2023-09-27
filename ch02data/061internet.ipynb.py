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
# ## Getting data from the Internet

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
# This can be really powerful if we want to, for example, perform an automated meta-analysis across a selection of research papers.

# %% [markdown]
# ### URLs

# %% [markdown]
# All internet resources are defined by a Uniform Resource Locator.

# %%
"https://static-maps.yandex.ru/1.x/?size=400,400&ll=-0.1275,51.51&z=10&l=sat&lang=en_US"

# %% [markdown]
# A url consists of:
#
# * A *scheme* (`http`, `https`, `ssh`, ...)
# * A *host* (`static-maps.yandex.ru`, the name of the remote computer you want to talk to)
# * A *port* (optional, most protocols have a typical port associated with them, e.g. 80 for http, 443 for https)
# * A *path* (Like a file path on the machine, here it is `1.x/`)
# * A *query* part after a `?`, (optional, usually ampersand-separated *parameters* e.g. `size=400x400`, or `z=10`)

# %% [markdown]
# **Supplementary materials**: These can actually be different for different protocols, the above is a simplification.  You can see more, for example, at
#     [the wikipedia article about the URI scheme](https://en.wikipedia.org/wiki/URI_scheme).

# %% [markdown]
# URLs are not allowed to include all characters; we need to, for example, "escape" a space that appears inside the URL,
# replacing it with `%20`, so e.g. a request of `http://some example.com/` would need to be `http://some%20example.com/`
#

# %% [markdown]
# **Supplementary materials**: The code used to replace each character is the [ASCII](http://www.asciitable.com) code for it.

# %% [markdown]
# **Supplementary materials**: The escaping rules are quite subtle. See [the wikipedia article for more detail](https://en.wikipedia.org/wiki/Percent-encoding). The standard library provides the [urlencode](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) function that can take care of this for you. 

# %% [markdown]
# ### Requests

# %% [markdown]
# The python [requests](http://docs.python-requests.org/en/latest/) library can help us manage and manipulate URLs. It is easier to use than the `urllib` library that is part of the standard library, and is included with anaconda and canopy. It sorts out escaping, parameter encoding, and so on for us.

# %% [markdown]
# To request the above URL, for example, we write:

# %%
import requests

# %%
response = requests.get("https://static-maps.yandex.ru/1.x/?size=400,400&ll=-0.1275,51.51&z=10&l=sat&lang=en_US",
                        params={
                            'size': '400,400',
                            'll': '-0.1275,51.51',
                            'zoom': 10,
                            'l': 'sat',
                            'lang': 'en_US'
                        })

# %%
response.content[0:50]

# %% [markdown]
# When we do a request, the result comes back as text. For the png image in the above, this isn't very readable.

# %% [markdown]
# Just as for file access, therefore, we will need to send the text we get to a python module which understands that file format.

# %% [markdown]
# Again, it is important to separate the *transport* model (e.g. a file system, or an "http request" for the web) from the data model of the data that is returned.

# %% [markdown]
# ### Example: Sunspots

# %% [markdown]
# Let's try to get something scientific: the sunspot cycle data from [SILSO](http://sidc.be/silso/home):

# %%
spots = requests.get('http://www.sidc.be/silso/INFO/snmtotcsv.php').text

# %%
spots[0:80]

# %% [markdown]
# This looks like semicolon-separated data, with different records on different lines. (Line separators come out as `\n`)

# %% [markdown]
# There are many many scientific datasets which can now be downloaded like this - integrating the download into your data
# pipeline can help to keep your data flows organised.

# %% [markdown]
# ### Writing our own Parser

# %% [markdown]
# We'll need a python library to handle semicolon-separated data like the sunspot data.

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
#     "something; something"; something; something
#     
# has three fields, the first of which is
#
#     something; something
#     
#  The naive code above would give four fields, of which the first is 
#  
#     "something

# %% [markdown]
# You'll never manage to get all that right; so you'll be better off using a library to do it.

# %% [markdown]
# ### Writing data to the internet

# %% [markdown]
# Note that we're using `requests.get`. `get` is used to receive data from the web.
# You can also use `post` to fill in a web-form programmatically.

# %% [markdown]
# **Supplementary material**: Learn about using `post` with [requests](http://docs.python-requests.org/en/latest/user/quickstart/).

# %% [markdown]
# **Supplementary material**: Learn about the different kinds of [http request](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods): [Get, Post, Put, Delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)...

# %% [markdown]
# This can be used for all kinds of things, for example, to programmatically add data to a web resource. It's all well beyond
# our scope for this course, but it's important to know it's possible, and start to think about the scientific possibilities.
