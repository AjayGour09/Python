import numpy as np 
arr = np.array([1,2,3,4,5])
print(arr)

a =[1,2,3,4,"Hello"]
print(np.array(a))

l = [[1,2,3,4],[5,56,6,7],[9,5,4,1]]
print(np.array(l))
print(np.arange(1,11))
print(np.zeros(6))
print(np.zeros((6,6)))
print(np.ones(3))
print(np.ones((2,3)))
print(np.linspace(1,5,100))
print(np.random.rand(10))
print(np.random.randn(10))

print(np.random.randint(4))
print(np.random.randint(4,16))
m =np.array([[1,2,3],[1,2,3],[1,2,3]])
print(m.shape)
print(m.size)
print(m.dtype)
print(m.min())
print(m.max())
print(m.sum())
print(np.sum(m,axis=0))
print(np.sum(m,axis=1))
print(m.mean())
print(m.std())
print(m.argmax())
print(m.argmin())

a = np.arange(30)
print(a)
print(a.reshape(5,6))