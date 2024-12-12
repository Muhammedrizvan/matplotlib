#matplotlib markers
#markers
#you can use the keyword argument marker
#to emphasize each points with specified narker:

#mark each points with a circle

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker = '*')
plt.show()
