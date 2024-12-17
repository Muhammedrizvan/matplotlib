#bar height
#the barh() takes the keyword argument height
#to set the height of the bars:

#draw 4 very thin bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.barh(x,y, height=0.1)
plt.show()
