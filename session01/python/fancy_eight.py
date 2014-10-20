### Make plot
import numpy as np
import math
import matplotlib.pyplot as plt

theta=np.arange(0,4*math.pi,0.1)
eight=plt.figure()
axes=eight.add_axes([0,0,1,1])
axes.plot(0.5*np.sin(theta),np.cos(theta/2))

### Save plot
eight.savefig('eight.png')
