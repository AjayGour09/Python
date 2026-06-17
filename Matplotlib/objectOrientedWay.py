import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

# print(plt.plot())
# print(plt.title("Graph"))
# print(plt.xlabel("X-axis"))
# print(plt.ylabel("Y-axis"))
fig = plt.figure()
axis1 = fig.add_axes([0.1,0.3,0.6,0.8])
print(axis1.plot(x,y))
axis2 = fig.add_axes([0.3,0.4,.3,.3])
print(axis2.plot(x,y))
print(plt.show())