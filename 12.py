#use both mec and mfc
#arguments to color the entire marker:

#set the color of the edge and the face to red

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker='*',ms='20',mfc='g',mec='r')
plt.show()
