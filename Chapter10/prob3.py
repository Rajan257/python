class Demo:
    a=5
o=Demo()
print(o.a) # print class attribute beacuse instance attribute not present

o.a=0     #Instance attribute is set
print(o.a)   # prints the instance attribute because instance
print(Demo().a) # prints the class attribute

