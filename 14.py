#shorter syntax
#linestyle ca be written as ls
#dotted can be written as:
#dashed can be written as --

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,ls='--')
plt.show()
