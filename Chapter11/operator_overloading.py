class Number:
  def __init__(self,n):
      self.n=n

  def __add__(self,num):        #it is a function
     return self.n+num.n
  
n=Number(1)
m=Number(2)

print(n + m)
    