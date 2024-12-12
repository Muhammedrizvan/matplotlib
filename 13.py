#matplotlib line
#use dotted line?

# 'solid' (default)	'-'
# 'dotted'	':'
# 'dashed'	'--'
# 'dashdot'	'-.'
# 'None'	'' or ' '

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,linestyle = '--')
plt.show()
