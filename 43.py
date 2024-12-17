#bar color
#the bar() and barh() take the keyword argument
#color to set the color of the bars:

#draw 4 red bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y, color="red")
plt.show()
