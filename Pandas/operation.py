import numpy as np 
import pandas as pd


df1 = pd.DataFrame({
    'A':[1,2,3,4,5],
    'B':[10,20,30,40,50],
    'C':[100,200,300,400,500]
})
print(df1)
print(df1.shape)
print(df1.columns)
print(df1.info())
print(df1.describe())
print(df1['A']+10)

def square(x):
    return x**2

df2 = df1['B'].apply(square)
print(df2)