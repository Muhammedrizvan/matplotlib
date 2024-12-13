#set font proporties for title and labels
#fontdict parameter in xlabel(),ylabel(),
#and title() to set font proporties fro the title and labels.
#set font prporties for the title and lable?

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("sports watch data",fontdict=font1)
plt.xlabel("average pilse",fontdict=font2)
plt.ylabel("caloris burnage",fontdict=font2)

plt.plot(x,y)
plt.show()
