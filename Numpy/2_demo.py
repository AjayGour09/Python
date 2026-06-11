import numpy as np

filled_arr =np.full((4,4),6) #full
print(filled_arr)

arr = np.arange(2,21,2)
print(arr)
diagonal_metrix  = np.eye(4) #eye
print(diagonal_metrix)

arr_2d = np.array([[1,23,4],[3,4,22]]) # shape 
print(arr_2d.shape)

arra =np.array([[1,2,3],[2,3,21],[2,4,3]])
print(arra.size)

arr_1d = np.array([1])
arr_2d = np.array([[1,2,3],[2,3,1]])
arr_3d = np.array([[[1,2,3],[1,2,3],[2,4,6]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
print(arr.dtype)