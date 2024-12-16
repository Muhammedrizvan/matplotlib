#color each dot
#you can even set a specific color for each dot by using array of color
#as value for the c argument:
#note:you cannot use the color arguments for this ,only the c arguments.
#set your own color of the markers

import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange",
                   "purple","beige","brown","gray","cyan","maroon"])
plt.scatter(x,y,c=colors)
plt.show()
