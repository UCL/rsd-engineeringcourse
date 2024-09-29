# ---
# jupyter:
#   jekyll:
#     display_name: Mocks
#   jupytext:
#     notebook_metadata_filter: -kernelspec,jupytext,jekyll
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
# ---

# %% [markdown]
# # Mocking

# %% [markdown]
# ## Definition
#
# **Mock**: *verb*,
#
# 1. to tease or laugh at in a scornful or contemptuous manner
# 2. to make a replica or imitation of something
#
#

# %% [markdown]
# **Mocking**
#
# - Replace a real object with a pretend object, which records how it is called, and can assert if it is called wrong

# %% [markdown]
# ## Mocking frameworks
#
# * C: [CMocka](http://www.cmocka.org/)
# * C++: [googletest](https://github.com/google/googletest)
# * Python: [unittest.mock](http://docs.python.org/3/library/unittest.mock)

# %% [markdown]
# ## Recording calls with mock
#
# Mock objects record the calls made to them:

# %%
from unittest.mock import Mock
function = Mock(name="myroutine", return_value=2)

# %%
function(1)

# %%
function(5, "hello", a=True)

# %% attributes={"classes": [" python"], "id": ""}
function.mock_calls

# %% [markdown]
# The arguments of each call can be recovered

# %% attributes={"classes": [" python"], "id": ""}
name, args, kwargs = function.mock_calls[1]
args, kwargs

# %% [markdown]
# Mock objects can return different values for each call

# %%
function = Mock(name="myroutine", side_effect=[2, "xyz"])

# %%
function(1)

# %%
function(1, "hello", {'a': True})

# %% [markdown]
# We expect an error if there are no return values left in the list:

# %%
function()

# %% [markdown]
# ## Using mocks to model test resources

# %% [markdown]
# Often we want to write tests for code which interacts with remote resources. (E.g. databases, the internet, or data files.)

# %% [markdown]
# We don't want to have our tests *actually* interact with the remote resource, as this would mean our tests failed
# due to lost internet connections, for example.

# %% [markdown]
# Instead, we can use mocks to assert that our code does the right thing in terms of the *messages it sends*: the parameters of the
# function calls it makes to the remote resource.

# %% [markdown]
# For example, consider the following code that downloads a map from the internet:

# %%
# sending requests to the web is not fully supported on jupyterlite yet, and the
# cells below might error out on the browser (jupyterlite) version of this notebook
import requests

def map_at(lat, long, satellite=False, zoom=12, 
           size=(400, 400)):

    base = "https://static-maps.yandex.ru/1.x/?"
    
    params = dict(
        z = zoom,
        size = ",".join(map(str,size)),
        ll = ",".join(map(str,(long,lat))),
        lang = "en_US")
    
    if satellite:
        params["l"] = "sat"
    else:
        params["l"] = "map"
        
    return requests.get(base, params=params)


# %%
london_map = map_at(51.5073509, -0.1277583)
from IPython.display import Image

# %%
# %matplotlib inline
Image(london_map.content)

# %% [markdown]
# We would like to test that it is building the parameters correctly. We can do this by **mocking** the requests object. We need to temporarily replace a method in the library with a mock. We can use "patch" to do this:

# %%
from unittest.mock import patch
with patch.object(requests,'get') as mock_get:
    london_map = map_at(51.5073509, -0.1277583)
    print(mock_get.mock_calls)


# %% [markdown]
# Our tests then look like:

# %%
def test_build_default_params():
    with patch.object(requests,'get') as mock_get:
        default_map = map_at(51.0, 0.0)
        mock_get.assert_called_with(
        "https://static-maps.yandex.ru/1.x/?",
        params={
            'z':12,
            'size':'400,400',
            'll':'0.0,51.0',
            'lang':'en_US',
            'l': 'map'
        }
    )
test_build_default_params()


# %% [markdown]
# That was quiet, so it passed. When I'm writing tests, I usually modify one of the expectations, to something 'wrong', just to check it's not
# passing "by accident", run the tests, then change it back!

# %% [markdown]
# ## Testing functions that call other functions
#
# <div align="left">

# %% attributes={"classes": [" python"], "id": ""}
def partial_derivative(function, at, direction, delta=1.0):
    f_x = function(at)
    x_plus_delta = at[:]
    x_plus_delta[direction] += delta
    f_x_plus_delta = function(x_plus_delta)
    return (f_x_plus_delta - f_x) / delta


# %% [markdown]
# We want to test that the above function does the right thing. It is supposed to compute the derivative of a function
# of a vector in a particular direction.

# %% [markdown]
# E.g.:

# %%
partial_derivative(sum, [0,0,0], 1)

# %% [markdown]
# How do we assert that it is doing the right thing? With tests like this:

# %%
from unittest.mock import MagicMock

def test_derivative_2d_y_direction():
    func = MagicMock()
    partial_derivative(func, [0,0], 1)
    func.assert_any_call([0, 1.0])
    func.assert_any_call([0, 0])
    

test_derivative_2d_y_direction()

# %% [markdown]
# We made our mock a "Magic Mock" because otherwise, the mock results `f_x_plus_delta` and `f_x` can't be subtracted:

# %%
MagicMock() - MagicMock()

# %%
Mock() - Mock()
