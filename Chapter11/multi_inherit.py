class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name of Employee is {self.name} and the company is {self.company}")

class Coder:
    language="python" 
    def printLanguages(self):
        print(f"Out of all languages here is your language:{self.language}")


class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showLanguages(self):
      print(f"The name is {self.company} and the language is {self.language}language")

a=Employee()
b=Programmer()
b.show()
b.printLanguages()
b.showLanguages()

print(a.company,b.company)


