import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("insurance.csv")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

numberic_columns = ['age', 'bmi', 'children', 'charges']
for col in numberic_columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col],kde=True,bins=20)
    plt.show()
    
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()