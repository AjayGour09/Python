import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
x = np.linspace(0,5,11)
y = x**2
print(x)
print(y)
print(plt.plot(x,y))

print(plt.title("Graph"))

print(plt.xlabel("X-axis"))
print(plt.ylabel("Y-axis"))
print(plt.show())