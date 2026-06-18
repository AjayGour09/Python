import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arr = np.array([1,2,3,4,5,6,7,8,30])
meadian = 5
q1 = np.percentile(arr , 25)
q3 = np.percentile(arr,75)
Iqr = q3 - q1

lower = q1 - (1.5 * Iqr)
uper = q3 + (1.5 * Iqr)

l = []
for i in arr:
    if i >= lower and i <= uper:
        l.append(i)
arr2 = np.array(l)
print(arr2)

print(f"The Q1 is {q1} and Q3 is {q3} and Median is {meadian} and IQR is {Iqr} and lower value is {lower} and upper value is {uper} and the outlier is 30")
print(sns.boxplot( x = arr))
print(sns.boxplot( x = arr2))
print(plt.show())