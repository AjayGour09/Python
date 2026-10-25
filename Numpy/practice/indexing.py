import numpy as np;
# arr = np.arange(11,21)
# print(arr)

# print(arr[7]) #Indexing

# print(arr[1:5]) # Slicing
# print(arr[3:])
# print(arr[3::2])


# arr = np.arange(1,31).reshape(6,5)
# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[0,1])

# print(arr[0:2,1:3])
# print(arr[3:6,3:5])
# print(arr[:,2])

arr = np.arange(11,21)
print(arr)
bool_index = arr % 2 == 0;
print(bool_index) 

arr = arr[bool_index]
print(arr)