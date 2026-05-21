# Set is a collection of non-repetitive elements.sets are unordered , it is unIndexed , there are no way to change item in sets , set can not contain duplicate values 
s=set(); #This is a empty set
s.add(1)
s.add(3);
s.add(6)
# s.clear()
# print(s)

s1 = {1,3,2,4,32}
s2 = {90,54,32}

print(s1.union(s2))
print(s1.intersection(s2))