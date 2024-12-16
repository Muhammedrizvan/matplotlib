#draw 2 plots on top of each other?
import matplotlib.pyplot as plt
import numpy as np
#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)  #(2row ,1column,1st subplot)
plt.plot(x,y)
#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2) #(2row,1column,second subplt)
plt.plot(x,y)

plt.show()
