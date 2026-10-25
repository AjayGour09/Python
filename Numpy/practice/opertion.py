import numpy as np;
a1 =np.array([1,2,3,4,5])
a2 = np.array([6,7,8,9,10])
print(a1+a2) 
print(a1-a2) 
print(a1*a2) 
print(a1/a2) 

print(a1+10)

a = np.array([[1,2],[3,5]])
b = np.array([[5,7],[7,8]])
print(a@b) #Matrix multipliction    
print(a.T)  #Transpose (Reverse the metrix)

print(np.hstack((a,b))) #Spalating
print(np.column_stack((a,b)))

