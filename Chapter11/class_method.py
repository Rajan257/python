class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute  is {cls.a}")

e= Employee()
e.a=45
e.show()

#in this programme happens that without calssmethod it will print 45 because of instance 
#after the class method it will work like this the value will print 1
