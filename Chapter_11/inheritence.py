class Employe:
    company ="ITC"
    name = "Default name"
    sallary = "190000"
    def show(self):
        print(f"The name is {self.name} and The salary is {self.sallary} ")
class programmer:
    company = "ITC Infotech"
    language = "Python"
    def show(self):
        print(f"The name is {self.language} and The salary is {self.sallary}")
    def showLanguage(self):
        print(f"The name is {self.name} and the Salary is {self.language}")

a =Employe
b = programmer
print(a.company , b.company)     