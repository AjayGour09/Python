# List is the collection of diffrent type of data , it is mutalable ,ordered and allow to duplicate value.
Elements = ["Rahul" ,"Rohan",True ,3.43 , 76 ,"Banana"]

print(Elements[0])

Elements[5] ="Orange"
print(Elements)
print(Elements[1:5])

Elements.append("Apple")
print(Elements)
Elements.insert(1,"Vinod")
print(Elements)
Elements.reverse()
print(Elements)
Elements.pop(7)
print(Elements)
li = [31,2,13,4,51]
li.sort()
print(li)
li.remove(2)
print(li)