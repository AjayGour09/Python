import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,5])
clered_all = np.nan_to_num(arr,nan=100)
print(clered_all)