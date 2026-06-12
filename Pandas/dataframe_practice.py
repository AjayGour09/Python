import numpy as np
import pandas as pd


data = {
    "A" :[1,2,3,np.nan,2],
    "B" :[np.nan,7,3,np.nan,2],
    "C" :[1,np.nan,3,np.nan,2],
    "D" :[1,2,np.nan,np.nan,2],
}
df =pd.DataFrame(data)
print(df)
print(df.isna())
print(df.isna().sum())
print(df.isna().any())
print(df.dropna())
print(df.dropna(thresh=2))
print(df.fillna(0))
values  ={'A':300,'B':450,"C":322,'D':549}
print(df.fillna(value=values))
print(df.fillna(df.mean()))