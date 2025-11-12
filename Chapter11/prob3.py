# # class Employee:
# #     salary=234      #class properity
# #     increment=20

# # e=Employee
# # e.salary=234  #instence attribute
# # e.increment=20








# class Employee:
#     salary=234      
#     _increment=20
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary+self.salary*(self._increment/100))
    
#     @property
#     def increment(self):
#         return self._increment
    
    
#     @increment.setter
#     def increment(self,salary):
#         self._increment = ((salary/self.salary)-1)*100

# e=Employee()
# # print(e.salaryAfterIncrement)


# e.increment=280
# print(e.salaryAfterIncrement)






class Employee:
    salary = 234
    _increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self._increment / 100)

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, new_salary):
        self._increment = ((new_salary / self.salary) - 1) * 100

e = Employee()

print("Initial increment:", e.increment)  # 👉 prints 20

e.increment = 300  # sets new salary, updates increment

print("Updated increment:", e.increment)  # 👉 prints 28.2051...
print("Salary after increment:", e.salaryAfterIncrement)


    