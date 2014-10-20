#!/usr/bin/env python
### "analyze"
import numpy as np
from matplotlib import pyplot as plt
def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    figure = plt.figure(figsize=(10.0, 3.0))

    subplot_average=figure.add_subplot(1, 3, 1)
    subplot_average.set_ylabel('average')
    subplot_average.plot(data.mean(0))

    subplot_max=figure.add_subplot(1, 3, 2)
    subplot_max.set_ylabel('max')
    subplot_max.plot(data.max(0))

    subplot_min=figure.add_subplot(1, 3, 3)
    subplot_min.set_ylabel('min')
    subplot_min.plot(data.min(0))

    figure.tight_layout()
    return figure

### "generate"
import os
def generate(filename, output=False):
    if not output:
        output = os.path.splitext(filename)[0] + '.png'
    analyze(filename).savefig(output)

### "bulk_generate"
def bulk_generate(sources):
    for source in sources:
       generate(source)

### "main"
import sys
if __name__ == "__main__":
    bulk_generate(sys.argv[1:])
