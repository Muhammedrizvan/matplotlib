#color hex
#or you can use hexadesimal color values:

#draw 4 bars with a beatiful green color?

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y, color="#4CAF50")
plt.show()
