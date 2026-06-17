import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

print(plt.plot(x,y))

print(plt.xlabel("X-Axix"))
print(plt.ylabel("Y-Axix"))
print(plt.title("Graph"))

print(plt.scatter(x,y))
print(plt.bar(x,y))
print(plt.barh(x,y))
print(plt.hist(x,y))
print(plt.pie(x,y))
print(plt.boxplot(y))
print(plt.fill_between(x,y))
print(plt.show())
