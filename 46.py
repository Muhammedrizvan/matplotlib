#bar width
#the bar() takes the keyword argument width to set the width of the bars:

#draw 4 very thin bars?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y, width=0.1)
plt.show()

#the default width value 0.8
#note: for horizontal bars ,use height insted of width.

