#plotting without line

#to plot only the marketers,
#you can use shortcut string notation parameter 'o'
#which means 'rings'.

#draw two points in the diagram,
#one at posiotion (1,3) and one in position (8,10)

import matplotlib.pyplot as plt
import numpy as np

xponits = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xponits,ypoints,'o')
plt.show()
