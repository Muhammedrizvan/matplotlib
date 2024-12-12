#marker size

#you can use the keyword argument narkersize
#or the size of the marker to 20?

#set the size of the marker to 20

import matplotlib.pyplot as plt
import numpy as  np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='*',ms=20)
plt.show()