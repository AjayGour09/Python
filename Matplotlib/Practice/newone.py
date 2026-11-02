import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from random import sample

x = np.linspace(0,5,11)
# y = x**2
# plt.plot(x,y)
# plt.title("GRAPH")
# plt.xlabel("X-LAVEL")
# plt.ylabel("Y-lavel")
# plt.subplot(2,2,2)
# plt.hist(x)
# plt.show()


data = sample(range(1,1000),100)
plt.hist(data)
plt.boxplot(x)
plt.savefig("basicplot.png")
plt.show()