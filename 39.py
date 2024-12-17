#alpha
#you can adjust the transparency of the dots with the alpha argument
#just like colors , make sure the array for sizes has the same length as the arrays for the x- and y- axis

#set ur own brightness for the markers


import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors=np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
sizes=np.array([20,50,100,200,500,600,60,90,10,300,450,800,75])

plt.scatter(x,y ,s=sizes, c=colors, cmap='viridis' , alpha=0.5)
plt.colorbar()
plt.show()