#matplotlib

#creating bars
#with pyplot,you can use the bar() function to draw bar graph:

#draw 4 bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()