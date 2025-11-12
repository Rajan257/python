# def divisble5(n):
#     if(n%5==0):
#         return True
#     return False

# a=[1,332,44,3,98,5,3,875,3,4,5,979,98,3,3,5,56,87]
# f=list(filter(divisble5,a))
# print(f)


from functools import reduce

l=[2,442,2,424,24,24,24,25,5,25,235,35,353,5,353,53,2]
def greater(a,b):
    if(a>b):
        return a
    return b
print (reduce(greater,l))
