import numpy as np
import pandas as pd

data = {
    'Category':['A','B','A','B','A','B','A','B'],
    'Store':['S1','S2','S1','S2','S1','S2','S1','S2'],
    'Sales': [100,200,432,643,322,554,655,900],
    'Quantity':[2,3,7,9,8,6,5,4],
    'Date':pd.date_range('23-10-2004', periods=8)
}
df = pd.DataFrame(data)
# print(df)

cat = df.groupby('Category')
for i , v in cat:
    print(i)
    print(v)
    
    
    
    
cat= df.groupby('Category')['Sales'].sum()
print(cat)
cat= df.groupby('Store')['Sales'].sum()
print(cat)
cat= df.groupby(['Category','Store'])['Sales'].sum()
print(cat)

print(df['Sales'].mean)
print(df['Sales'].median)
print(df['Sales'].sum)
print(df['Sales'].sub)
print(df['Sales'].min)
print(df['Sales'].max)
print(df['Sales'].count)
print(df['Sales'].std)
print(df['Sales'].agg(['mean','sum'])) # multiple function use