import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

# print(plt.plot(x,y))
print(plt.title("Grpah"))
print(plt.xlabel("X-axis"))
print(plt.ylabel("Y-axis"))


print(plt.subplot(2,2,1))
print(plt.subplot(2,2,2))
print(plt.plot(y,x))
print(plt.subplot(2,2,3))
print(plt.plot(x,y))
print(plt.subplot(2,2,4))
# print(plt.show())
print(plt.plot(x**2,x**2))
print(plt.show())