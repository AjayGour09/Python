import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('tips')

arr  = df['size'].unique()
# sns.displot(df['total_bill'], bins = 1 ,kde=True) #histplot 
# sns.jointplot(x='total_bill',y="tip",data = df , kind='scatter')
# sns.jointplot(x='total_bill',y="tip",data = df , kind='hex') # reg , kde hist
# sns.pairplot(df,hue="sex",palette='rainbow')
sns.rugplot(df)
plt.show()
