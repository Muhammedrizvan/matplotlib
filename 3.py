#matplotlib plotting

#draw a line in a diagram from position (1,3)
#to position (8,10)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints)
plt.show()

#the x-axis is the horizontal axis.
#the y-axis is the vertical axis
