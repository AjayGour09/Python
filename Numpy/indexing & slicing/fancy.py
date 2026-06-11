import numpy as np 

arr=np.array([10,20,30,40])
print(arr[arr>12])
print(arr[arr<13])

arr_2d=np.array([[10,20,30,40],[4,3,2,4]])
print(arr_2d.ravel())
print(arr_2d.flatten())