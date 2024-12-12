#you can use the keyword argument markerfacecolor
#or the shorter mfc to set the color inside
#the edge of the marker:

#set the face color to red?

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='*',ms='20',mfc='r')
plt.show()
