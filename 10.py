#marker color
#you can use the keyword argument markredcolor
#or the shorter mec to set the color of the edge of the markers:

#set the EDG color to red?

import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([3,8,1,10])

plt.plot(ypoint,marker='*',ms=20,mec='r')
plt.show()