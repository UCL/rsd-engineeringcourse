import numpy

data=numpy.loadtxt(fname='../data/inflammation-01.csv',
        delimiter=',')

from matplotlib import pyplot as plt
figure = plt.figure(figsize=(7.0, 3.0))
figure.add_axes([0,0,1,1])
figure.axes[0].imshow(data)
figure.savefig('image.png')

range_over_days = plt.figure(figsize=(7.0, 3.0))

subplot_average=range_over_days.add_subplot(1, 2, 1)
subplot_average.set_ylabel('min')
subplot_average.plot(data.min(0))

subplot_max=range_over_days.add_subplot(1, 2, 2)
subplot_max.set_ylabel('max')
subplot_max.plot(data.max(0))

range_over_days.tight_layout()
range_over_days.savefig('dayrange.png')
