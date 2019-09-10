#!/usr/bin/env python
# From https://gist.github.com/fperez/e2bbc0a208e82e450f69
# Note, updated version of 
# https://github.com/ipython/ipython-in-depth/blob/master/tools/nbmerge.py
"""
usage:
python nbmerge.py A.ipynb B.ipynb C.ipynb > merged.ipynb
"""
from __future__ import print_function

import io
import os
import string
import sys

import nbformat

def fix_images_paths(cells, filename):
    # find parent path
    path_filename = filename.split('/')
    full_path = '/'.join(path_filename[:-1]) + "/"

    # fix paths
    for cell in cells:
        if ("![" in cell['source'] and ".svg)" in cell['source']):
            source = cell['source']
            new_source = source
            # where the link starts
            start = source.find("](")
            if source[start+2:start+4] == './':
                new_source = source[:start+2] + full_path + source[start+4:]
            elif source[start+2] in string.ascii_letters:
                new_source = source[:start+2] + full_path + source[start+2:]
            cell['source'] = new_source
    return cells

def merge_notebooks(filenames, outfile):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            nb.cells = fix_images_paths(nb.cells, fname)
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    result=nbformat.writes(merged)
    with io.open(outfile, 'w', encoding='utf-8') as out:
        out.write(result)

if __name__ == '__main__':
    notebooks = sys.argv[1:-1]
    outfile = sys.argv[-1]
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    merge_notebooks(notebooks, outfile)
