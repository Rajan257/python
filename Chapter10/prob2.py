class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def pow_four(self):
        print(f"The pow_four is {self.n*self.n*self.n*self.n}")

    def pow_five(self):
        print(f"The pow_five is {self.n*self.n*self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square_root is {self.n**1/2}")

a=Calculator(4)
a.square()
a.cube()
a.pow_four()
a.pow_five()
a.square_root()
