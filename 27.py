#matplotlib subplot
#display mulitiple plots
#with the subplot() function you can draw multiple plots in one figure
#draw 2 plots?

import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1) #(1row,2columns,1stsubplot)

plt.title("Sports Watch Data")
plt.xlabel("Average Pilse")
plt.ylabel("Caloris Burnage")
plt.plot(x,y)

#plt 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2) #(1row,2columns,2nd subplot)

plt.plot(x,y)
plt.show()
