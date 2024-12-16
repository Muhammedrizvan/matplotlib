#task

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17])
y = np.array([99,86,87,88,111,86])
plt.scatter(x, y, color = 'hotpink')


x = np.array([2,2,8,1,15,8])
y = np.array([100,105,84,105,90,99])
plt.scatter(x, y, color = '#88c999')


x = np.array([1,3,5,7,10,4])
y = np.array([82,94,95,80,98,77])
plt.scatter(x, y, color = 'red')

x = np.array([8,5,3,9,12,16])
y = np.array([56,67,89,78,45,23])
plt.scatter(x, y, color = 'green')

x = np.array([11,12,13,14,15,16])
y = np.array([90,91,92,93,94,95])
plt.scatter(x, y, color = 'yellow')

x = np.array([4,5,6,7,8,9])
y = np.array([100,101,102,103,104,105])
plt.scatter(x, y, color = 'indigo')

plt.xlabel("fitness (years)")
plt.ylabel("Speed")
plt.suptitle("Car speed")
plt.show()