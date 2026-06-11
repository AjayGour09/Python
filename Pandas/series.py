import numpy as np
import pandas as pd

labels = ['a','b','c','d']
my_list = [1,2,3,4]
my_arr = np.array([1,2,3])
dic = {1:2,2:3,34:54}

new_list = pd.Series(my_list , index=labels)
print(new_list)

print(pd.Series(my_arr))
print(pd.Series(dic))
