import numpy as np

arr1 =np.array([1,2,3])
arr2 =np.array([1,22,1])

new_arr = np.concatenate((arr1,arr2)) #Concatenation..
print(new_arr)
new_del = np.delete(arr2,0) #Deletion....
print(new_del)

arr_2d = np.array([[1,3,4,3],[1,2,3,2]])
new_array = np.delete(arr_2d ,0, axis=0)
print(new_arr)