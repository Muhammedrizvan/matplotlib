#combine color size and alpha
#you can combine a colormap with different sizes of the dots
#this is best visualised if the dots are transparent

#create random arrays with 100 values for x-points ,y-points
#colors and sizes

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=100)
colors=np.random.randint(100,size=(100))
sizes=np.random.randint(100,size=(100))

plt.scatter(x,y ,c=colors , s=sizes , alpha=0.6, cmap="nipy_spectral")

plt.colorbar()
plt.show()