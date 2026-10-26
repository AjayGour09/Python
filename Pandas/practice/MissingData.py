import numpy as np
import pandas as pd

data = {
    'A':[1,2,np.nan , 4],
    'B':[3,4,5,np.nan],
    'C':[np.nan , 4,5,np.nan],
    'D':[np.nan,np.nan,np.nan, 6]
}

df = pd.DataFrame(data)
print(df)
print(df.isna())
print(df.isna().sum())
print(df.isna().any())
print(df.dropna())
print(df.dropna(thresh=1))
print(df.fillna(0))