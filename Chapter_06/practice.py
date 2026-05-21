# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))
# c = int(input("Enter Third Number : "))
# d = int(input("Enter Fourth Number : "))


# if(a>b and a>c and a>d):
#     print("The Greater number is A = ",a)
# elif(b>a and b>c and b>d):
#     print("The Greater number is B = ",b)
# elif(c>a and c>b and c>d):
#     print("The Greater number is C = ",c)   
# elif(a==b and b==c and c ==a):
#     print("all number are eqaul")    
# else:
#     print("The Greater number is D = ",d) 


# Sub1 = int (input ("Enter first Subject marks :"))
# Sub2 = int (input("Enter second Subject marks :"))
# Sub3 = int(input("Enter Third Subject marks :"))
# percentage = ((Sub1+Sub2+Sub3)*100)/300
# if(percentage >= 40 and Sub1 >= 33 and Sub2>= 33 and Sub3 >= 33):
#     print("Student is Pass The Total Percentage is ",percentage,"%")
# else:
#      print("Student is fail The Total Percentage is ",percentage,"%")

# Message1 = "Make a lot of Money"
# Message2 = "buy Now"
# Message3 = "Subscribe This"
# Message4 = "click This"

# Message = input("Enter Your Message :")

# if(Message1 in Message or Message2 in Message or Message3 in Message or Message4 in Message):
#     print("This is a Spam Please Safe")
# else:
#     print("Not a Spam You are Safe")



# Username = input("Enter your name : ")
# if(len(Username)>=10):
#     print("name is Long ")
# else:
#     print("Basic name")

name_List = ["Ajay","Rohan","Sohan" , "Priya"]
name = input("Enter Your Name ")
if(name in name_List):
    print("Your name is in the list " , name)
else:
    print("Your name is not in the list " , name)