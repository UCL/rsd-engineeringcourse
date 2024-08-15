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
# # Structured data
#
# *Comma separated variable* (CSV) files can only store *tabular data* in which all records share the same fields and each field is a simple data type such as a string or number. We often want to store data which has a more complex *hierarchical structure*, for example data in which the fields in each record are themselves structured objects. Structured data formats like [JSON](#JSON), [YAML](#YAML) and [XML](#XML) are designed for this.
#
# ## JSON
#
# A very common structured data format is [*JavaScript Object Notation* (JSON)](https://en.wikipedia.org/wiki/JSON). As the name suggests this a JavaScript based format for storing data objects. JSON allows us to represent hierarchical data with a [tree-like structure](https://en.wikipedia.org/wiki/Tree_(data_structure)) by nesting sequence-like *arrays* (analogous to Python `list` objects) and mapping-like *objects* (analagous to Python `dict` objects), with the 'leaves' of the tree being one of a small set of simple data types: 
#
#   * *number*: a signed decimal number potentially using [E notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation), for example `12`, `0.58`, `6.022e23`. Unlike Python no distinction is made between integer and floating-point values.
#   * *string*: a sequence of [Unicode characters](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) delimited with double quotation marks, for example `"Hello world"`, `""`, `"😀😄😁"`. Unlike Python, single quotation marks cannot be used as the delimiters instead.
#   * *boolean*: one of the literals `true` or `false`. Note the difference in capitalisation from the equivalent Python values.
#   * `null`: an empty value, comparable to `None` in Python.
#   
# JSON *arrays* are ordered sequences of zero or more elements, and like Python lists are delimited with square brackets with comma separated values. Also like Python lists each element in the array can be of a different type, with the allowable types being the any of the four simple types described above, arrays or objects (see following).
#
# JSON *objects* are *key-value* mappings in which the keys are strings and the values may be any of the simple data types above, arrays or objects. As with Python dictionaries, the keys within each object must be unique, and also like Python dictionaries objects are delimited with curly braces, with each key-value pair comma-separated and a colon used to separate the key from the following value.
#
# The `json` module in the Python standard library provides functions for encoding / decoding Python data structures to / from JSON format. 

# %%
import json

# %% [markdown]
# Specifically `json` uses the following translations between types when decoding and encoding
#
# <div style='text-align: center;'>
#     
# <table style='vertical-align: top; display: inline-block'>
#     <tr> <th colspan="2"> Decoding (JSON to Python) </th> </tr>
#     <tr> <th> JSON </th> <th> Python </th> </tr>
#     <tr> <td> object </td> <td> dict </td> </tr>
#     <tr> <td> array </td> <td> list </td> </tr>
#     <tr> <td> string </td> <td> str </td> </tr>
#     <tr> <td> number (integer) </td> <td> int </td> </tr>
#     <tr> <td> number (real) </td> <td> float </td> </tr>
#     <tr> <td> boolean </td> <td> bool </td> </tr>
#     <tr> <td> null </td> <td> None </td> </tr>
# </table>
#
# <table style='vertical-align: top; display: inline-block'>
#     <tr> <th colspan="2"> Encoding (Python to JSON) </th> </tr>
#     <tr> <th> Python </th> <th> JSON </th> </tr>
#     <tr> <td> dict </td> <td> object </td> </tr>
#     <tr> <td> list, tuple </td> <td> array </td> </tr>
#     <tr> <td> str </td> <td> string </td> </tr>
#     <tr> <td> int, float </td> <td> number </td> </tr>
#     <tr> <td> bool </td> <td> boolean </td> </tr>
#     <tr> <td> None </td> <td> null </td> </tr>
# </table>
#
# </div>
#
# Note that mapping of types when encoding from Python to JSON is not one-to-one so sequentially encoding a Python object to JSON and then decoding back to a Python object can result in some changes in types.
#
# As a simple example consider the following Python object consisting of nested dictionaries and lists: 

# %%
my_data =  {'foo': ['value', 1, True], 'bar': {'spam': 3.4, 'eggs': None}}

# %% [markdown]
# We can encode this Python object to a JSON formatted string using the [`json.dumps` function](https://docs.python.org/3/library/json.html#json.dumps) 

# %%
json_string = json.dumps(my_data)
print(json_string)

# %% [markdown]
# The `json.dumps` function has several optional keyword arguments that can be used to produce a more nicely formatted output which can be useful to increase readability when encoding large objects, for instance

# %%
json_string = json.dumps(my_data, indent=4, sort_keys=True)
print(json_string)

# %% [markdown]
# We can then easily save the JSON formatted string to a file using the `open` function we encountered in a previous lesson.

# %%
with open('my_file.json', 'w') as f:
    f.write(json_string)

# %% [markdown]
# As encoding a Python object to JSON format and writing the result to a file is such a common operation, the `json` module also provides the `json.dump` function which can be used to directly write the JSON encoding of a Python object to a file:

# %%
with open('my_file.json', 'w') as f:
    json.dump(my_data, f)

# %% [markdown]
# We can similarly use `open` to read JSON formatted data in to a string

# %%
with open('my_file.json', 'r') as f:
     loaded_json_string = f.read()
print(loaded_json_string)

# %% [markdown]
# We can then use the [`json.loads` function](https://docs.python.org/3/library/json.html#json.loads) to decode this JSON formatted string in to a Python object

# %%
loaded_data = json.loads(loaded_json_string)
print(f"loaded_data = {loaded_data}")
print(f"type(loaded_data) = {type(loaded_data).__name__}")
print(f"type(loaded_data['foo']) = {type(loaded_data['foo']).__name__}")

# %% [markdown]
# As with `json.dumps` and `json.dump`, there is also a [`json.load` function](https://docs.python.org/3/library/json.html#json.load) which can be used to directly load a JSON formatted file in to a Python object:

# %%
with open('my_file.json', 'r') as f:
     loaded_data = json.load(f)
print(f"loaded_data = {loaded_data}")

# %% [markdown]
# JSON is a very useful format for loading and saving Python data structures. It is a common way of transferring data on the internet, and as there is good support in many programming languages, it is a convenient inter-language file interchange format.

# %% [markdown]
# ## YAML

# %% [markdown]
# YAML ([originally short for *Yet Another Markup Language*](https://en.wikipedia.org/wiki/YAML#History_and_name)) is another structured data format with many similarities to JSON; in fact [recent versions of YAML are a superset of JSON](https://en.wikipedia.org/wiki/YAML#Comparison_with_JSON). As well as supporting the same types and syntax as JSON, YAML also several additional features which can allow more readable formatting of data, for example
#
#   * Similar to Python, whitespace indentation can be used to denote nested structures rather than using explicit delimiters. 
#   * Strings do not need to be delimited with quotes in most cases other than when escaping special characters.
#   * Comments can be included by prefixing with the `#` character, with all subsequent characters up to the end of the line ignored when decoding.
#   * Arrays (lists) can be denoted by placing each element on a separate line prefixed with a `-` character.
#   * Objects (dictionaries) can be denoted by placing each key-value pair on a separate line with a `:` character separating the key and value.
#   
# For example, the following text represents an equivalent data object as encountered in the previous JSON section in a YAML compatible format
#
# ```yaml
# foo:
#   # The following is a list
#   - value
#   - 1
#   - true
# bar:
#   # The indentation heres indicates the following lines are a nested object
#   spam: 3.4
#   eggs: null
# ```
#  
# Unlike for JSON, there is no built-in module for encoding / decoding YAML files in the Python standard library. One third-party option is the [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) library. If PyYAML is installed in the active Python environment (it is included in the Anaconda Python distribution for example), then the `yaml` module can then be imported by running the following

# %%
import yaml

# %% [markdown]
# Similarly to the `json.dump` and `json.dumps` functions, `yaml` provides a `dump` function which can be used to encode a Python object to a corresponding YAML formatted string *or* directly write the YAML formatted output to a file. When called without a `stream` keyword argument the `yaml.dump` function returns a YAML formatted string corresponding to the passed object (analogous to `json.dumps`):

# %%
yaml_string = yaml.dump(my_data)
print(yaml_string)

# %% [markdown]
# If we instead pass a stream-like object such as a file as the second argument, the output will instead be written directly to the stream (analogous to `json.dump`):

# %%
with open('my_file.yaml', 'w') as f:
    yaml.dump(my_data, stream=f)

# %% [markdown]
# The `yaml` module also provides a `load` function analogous to the `json.load` function for loading objects from YAML formatted files. Although YAML itself only represents data, it supports language-specific tags which YAML parsers such as PyYAML may use to allow representing arbitrary types. As this means PyYAML can construct Python objects which may execute code on loading, loading YAML files from untrusted sources can be a [security concern](https://pyyaml.org/wiki/PyYAMLDocumentation#loading-yaml). It is therefore recommended to use `yaml.safe_load` to load YAML files when you are unsure about their source as this removes the risk of arbitrary code execution (with the tradeoff of no longer being able to encode any Python object). As the data object we just wrote to file only uses simple types, we can use `yaml.safe_load` here without any issues.

# %%
with open('my_file.yaml', 'r') as f:
    loaded_data = yaml.safe_load(f)
print(f"loaded_data = {loaded_data}")
print(f"type(loaded_data) = {type(loaded_data).__name__}")
print(f"type(loaded_data['foo']) = {type(loaded_data['foo']).__name__}")

# %% [markdown]
# YAML is a very versatile format for ad-hoc data files, however, as YAML encoding / decoding is not part of the Python standard library, JSON is sometimes preferred for its increased ease of use and universality.

# %% [markdown]
# ## XML

# %% [markdown]
# *Supplementary material* 
#
# [*Extensible Markup Language* (XML)](http://www.w3schools.com/xml/) is another popular format for storing hierarchical data structures. XML is very general and flexible, but is also very verbose which can hinder the human readability of XML encoded data and lead to large file sizes. In some scientific fields, XML based formats for data storage are very common. If you want to read and write XML formatted data in Python, a collection of tools for processing XML are available in the standard library within the [XML package](https://docs.python.org/3/library/xml.html).

# %% [markdown]
# ## Exercise: saving and loading a maze

# %% [markdown]
# Use YAML or JSON to save to disk, and to load it again, the maze data structure you designed in the previous *A Maze Model* exercise or the example solution below if you do not have a solution to hand.

# %%
maze = {
    'living' : {
        'exits': {
            'north' : 'kitchen',
            'outside' : 'garden',
            'upstairs' : 'bedroom'
        },
        'people' : ['James'],
        'capacity' : 2
    },
    'kitchen' : {
        'exits': {
            'south' : 'living'
        },
        'people' : [],
        'capacity' : 1
    },
    'garden' : {
        'exits': {
            'inside' : 'living'
        },
        'people' : ['Sue'],
        'capacity' : 3
    },
    'bedroom' : {
        'exits': {
            'downstairs' : 'living',
            'jump' : 'garden'
        },
        'people' : [],
        'capacity' : 1
    }
}
