#labels
#add labels to the pie chart with the labels parameter.

#the labels parameter must be an array with one labels for each wefge:

#a simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["apples","bananas","cherries","dates"]

plt.pie(y,labels=mylabels)
plt.show()
