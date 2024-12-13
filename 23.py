#position the title
#you can use the loc parameter in title(),xlabel(),ylabel() to position the them
#legal values for title and label: 'left','right' and 'center'.default value is 'center'.
#legal values for ylabel : 'top','center','bottom'
#position the title and xlabel to the left?

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


plt.title("sports watch data",loc='left')
plt.xlabel("average pilse",loc='left')  #horizontal = left,right
plt.ylabel("caloris burnage",loc='top') #vertical = top,center,bottom

plt.plot(x,y)
plt.show()
