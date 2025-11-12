class Employee:
    name = "Harry"
    language = "python"
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
harry.language = "javascript"

# You can call it like this:
harry.getInfo()
harry.greet()

# Or like this (both work):
# Employee.getInfo(harry)