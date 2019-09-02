# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import cloud_sptheme as csp

# -- Project information -----------------------------------------------------

project = 'Research Software Engineering with Python'
copyright = '2019, JH, DPS, AG'
author = 'JH, DPS, AG'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'cloud'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',
#         'searchbox.html',
#         'donate.html',
#     ]
# }
# html_theme_options = {
#     "fixed_sidebar": True
# }
html_theme_path = [csp.get_theme_dir()]
html_theme_options = { "roottarget": "index" }
# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}
# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True
# The frontpage document.
index_doc = 'index'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}
if csp.is_cloud_theme(html_theme):
    html_theme_options.update(
        roottarget=index_doc,
        borderless_decor=True,
        sidebarwidth="3in",
        hyphenation_language="en",
    )
