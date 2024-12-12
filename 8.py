#fromat string fmt
#you can also use the shortcut string notation parameter
#to specify the marker.

#this paramater is also called fmt ,and is written with this syntax:
#syntax
#marker|line|color

#mark each points with a circle?

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,'o-.r')
plt.show()
