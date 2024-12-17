#matplotlib pie charts

#creating pie charts
#with pyplot,you can use the pie() function to draw pie charts:

#a simple pie charts:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])

plt.pie(y)
plt.show()
