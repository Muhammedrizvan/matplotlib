#set lines prporties for the grid
#you can also set the line prporties of the grid
#like this : grid (color = 'color',linestyle','linewidth' = number).

#set the lines prporties of the grid?

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


plt.title("Sports Watch Data")
plt.xlabel("Average Pilse")
plt.ylabel("Caloris Burnage")

plt.plot(x,y)
plt.grid(color='green',linestyle='--',linewidth=0.5)
plt.show()
