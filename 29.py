#drw 6 plots

import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1) #(2rows,3columns,1st subplot)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,3) #(2row,3columns,second subplot)
plt.plot(x,y)

x = np.array([0,1,2,3])
y= np.array([3,8,1,10])
plt.subplot(2,3,4) #third
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4) #forth
plt.plot(x,y)

x = np.array([0,1,2,3])
y= np.array([3,8,1,10])
plt.subplot(2,3,5)
plt.plot(x,y)