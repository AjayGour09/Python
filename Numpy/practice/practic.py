import numpy as np 

arr = np.array([1,2,2,3])
arrr = np.array([[1,2,3,4],[5,6,7,8],[88,9,8,7]])
# print(arr)
# print(arrr)

# arrr = np.arange(30)
# ar = np.arange(1,30)
# print(arrr)

# print(np.zeros())
# print(np.ones())
# print(np.zeros((7,6)))
# print(np.ones(3,4))

# a = np.linspace(1,10,20)
# a= np.random.rand(10)
# a = np.random.randint(10)

# print(arrr.shape)
# print(arrr.size)
# print(arr.dtype)

print(arr.min())
print(arr.max())
print(arr.sum())
print(arr.sum())
print(arrr.sum(axis=0))
print(arr.mean())
print(arr.std())
print(arr.argmax())
print(arr.argmin())
print(arr.reshape(2,2))
