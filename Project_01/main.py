import random

computer = random.choice([1,-1,0])

youstr = input("Enter Your Choice : ")
youDict = {"s":1,"w":-1,"g":0}
you = youDict[youstr]

print(f'youh choose{you}')

if(computer == you):
    print("Its Draw ")
else:
    if(computer ==-1 and you ==1):
        print("You win!")
    elif(computer ==-1 and you ==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==1 and you==0):
        print("You win! ")
    elif(computer==0 and you==-1):
        print("You win! ")
    elif(computer==0 and you==1):
        print("You Lose")          
    else:
        print("Something Went Wrong !")
