class Employee:
    name="Harry"
    language="py"                               #this is a class attribute
    salary=12000

harry=Employee()
harry.name="Harry"                               # this is an instance (object)attribute
print(harry.language,harry.salary,harry.name)

rohan=Employee()
rohan.name="Rohan RoRo"
print(rohan.salary,rohan.language,rohan.name)


# here name is object Attribute and slary and language are class attribut as they directly belong to the class


