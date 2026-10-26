import numpy as np
import pandas as pd 

# labels = ['a','b','c']
# my_list = [1,2,3]
# arr = np.array([1,2,3])
# d={1:10,2:20,3:30}
# print(pd.Series(my_list))

data = {
    "Name": ["john", "Alice", "Pritam", "Pyare"],
    "Age": [23, 43, 54, 32],
    "City": ["Uganda", "Canada", "Pakistan", "India"],
    "Sallery": [45000, 85000, 2000, 998000]
}

df = pd.DataFrame(data)

print(df)
print(df["Name"])

df2 = df[["Name", "City"]]
print(df2)
df2["Designation"] = ["Doctor", "Lawer","Helper", "Engineer"]
print(df2)
print(df.drop("City",axis=1))
print(df.loc[[0]])
print(df.loc[[0,1]][["City","Sallery"]])

print(df[df["Age"]>30])