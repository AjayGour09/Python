import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(sns.load_dataset('tips'))
df1 = sns.displot(df['total_bill'])
# print(df1)

print(sns.histplot(df['total_bill'],bins=20,kde=True))
print(plt.show())