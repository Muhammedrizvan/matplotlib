#horizontal bars
#if you want the bars to be displayed horizontally instead of vertically,
#use the barh() function:

#draw 4 horizontal bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.barh(x,y)
plt.show()