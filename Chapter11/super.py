class Employee:
    def __init__(self):
        print("Constructor of Employee")
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name of Employee is {self.name} and the company is {self.company}")


class Programmer(Employee):
    company = "ITC Infotech"
    def __init__(self):
        print("Constructor of Programmer")
    salary = 12000

    def showLanguages(self):
        print(f"The company name is {self.company} and the programmer salary is {self.salary} rupees")


class Manager(Programmer):
    sector = "coding"
    def __init__(self):
        super().__init__()
        
        print("Constructor of Manager")

    def printSector(self):
        print(f"Manager works in the sector of: {self.sector}")


# ✅ Object Creation and Usage (moved OUTSIDE the class)
project = Employee()
print(project.company)  # From Employee

project = Programmer()
print(project.name, project.salary)  # Inherited from Employee and Programmer

project = Manager()
print(project.name, project.salary, project.sector)  # Inherited from all

# ✅ Calling methods
a = Employee()
b = Programmer()
c = Manager()

b.show()             # Inherited show() from Employee
c.printSector()      # From Manager
b.showLanguages()    # From Programmer

# ✅ Comparing class-level company values
print(a.company, b.company)
