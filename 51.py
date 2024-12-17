#pull the "apple" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["apples","bananas","cherries","dates"]
myexplode = [0.2,0,0,0]

plt.pie(y,labels=mylabels, explode=myexplode)
plt.show()
