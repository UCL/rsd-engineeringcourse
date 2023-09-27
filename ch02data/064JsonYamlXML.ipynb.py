# ---
# jupyter:
#   jekyll:
#     display_name: Structured data files
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# ## Structured Data

# %% [markdown]
# ### Structured data

# %% [markdown]
# CSV files can only model data where each record has several fields, and each field is a simple datatype,
# a string or number.

# %% [markdown]
# We often want to store data which is more complicated than this, with nested structures of lists and dictionaries.
# Structured data formats like JSON, YAML, and XML are designed for this.

# %% [markdown]
# ### JSON

# %% [markdown]
# [JSON](https://en.wikipedia.org/wiki/JSON) is a very common open-standard data format that is used to store structured data in a human-readable way.

# %% [markdown]
# This allows us to represent data which is combinations of lists and dictionaries as a text file which
# looks a bit like a Javascript (or Python) data literal.

# %%
import json

# %% [markdown]
# Any nested group of dictionaries and lists can be saved:

# %%
mydata = {'key': ['value1', 'value2'], 
          'key2': {'key4':'value3'}}

# %%
json.dumps(mydata)

# %% [markdown]
# If you would like a more readable output, you can use the `indent` argument.

# %%
print(json.dumps(mydata, indent=4))

# %% [markdown]
# Loading data is also really easy:

# %%
# %%writefile myfile.json
{
    "somekey": ["a list", "with values"]
}

# %%
with open('myfile.json', 'r') as json_file:
    my_data_as_string = json_file.read()

# %%
my_data_as_string

# %%
mydata = json.loads(my_data_as_string)

# %%
mydata['somekey']

# %% [markdown]
# This is a very nice solution for loading and saving Python data structures.

# %% [markdown]
# It's a very common way of transferring data on the internet, and of saving datasets to disk.

# %% [markdown]
# There's good support in most languages, so it's a nice inter-language file interchange format.

# %% [markdown]
# ### YAML

# %% [markdown]
# [YAML](https://en.wikipedia.org/wiki/YAML) is a very similar data format to JSON, with some nice additions:

# %% [markdown]
# * You don't need to quote strings if they don't have funny characters in
# * You can have comment lines, beginning with a `#`
# * You can write dictionaries without the curly brackets: it just notices the colons.
# * You can write lists like this:

# %%
# %%writefile myfile.yaml
somekey:
    - a list # Look, this is a list
    - with values

# %%
import yaml  # This may need installed as pyyaml

# %%
with open('myfile.yaml') as yaml_file:
    my_data = yaml.safe_load(yaml_file)
print(mydata)

# %% [markdown]
# YAML is a popular format for ad-hoc data files, but the library doesn't ship with default Python (though it is part
# of Anaconda and Canopy), so some people still prefer JSON for its universality.

# %% [markdown]
# Because YAML gives the option of serialising a list either as newlines with dashes or with square brackets,
# you can control this choice:

# %%
print(yaml.safe_dump(mydata))

# %%
print(yaml.safe_dump(mydata, default_flow_style=True))

# %% [markdown]
# `default_flow_style=False` (the default) uses a "block style" (rather than an "inline" or "flow style") to delineate data structures. See [the YAML docs](http://yaml.org/spec/1.2/spec.html) for more details.

# %% [markdown]
# ### XML

# %% [markdown]
# *Supplementary material*: [XML](http://www.w3schools.com/xml/) is another popular choice when saving nested data structures. 
# It's very careful, but verbose. If your field uses XML data, you'll need to learn a [python XML parser](https://docs.python.org/3/library/xml.etree.elementtree.html)
# (there are a few), and about how XML works.

# %% [markdown]
# ### Exercise: Saving and loading data

# %% [markdown]
# Use YAML or JSON to save your maze data structure to disk and load it again.
