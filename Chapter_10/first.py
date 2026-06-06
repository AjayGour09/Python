class Employee:
    name = "Ajay"
    language ="Py"
    Sallary = "120000"

    def getInfo(self):
        print(f"The language is {self.language} and the Sallary is {self.Sallary}")
    def greet(self):
        print("Good Morning")  


ajay = Employee()
print(ajay.name , ajay.language)

ajay.getInfo()
ajay.greet()
rohan = Employee()
print(rohan.language , rohan.Sallary)

rohan.name ="NilKamal"
print(rohan.name)