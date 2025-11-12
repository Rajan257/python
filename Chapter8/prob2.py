# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
# print(sum(4))



# def pattern(n):
#     if(n==0):
#         return 
#     print("*" * n)
#     pattern(n-1)
# pattern(5)




#inches to cm


# def inch_to_cms(inch):
#     return inch * 2.54
# n=int(input("Enter value in inches: "))

# print(f"The corresponding value in cms is {inch_to_cms(n)}")


# def rem(l,word):
#     for item in l:
#          l.remove(word)
#          return l

# l=["Rajan","Shyam","sita","Pyare","Mohan"]
# print(rem(l,"Mohan"))




# def rem(l,word):
#     n=[]
#     for item in l:
#          if not (item == word):
#               n.append(item.strip(word))
#     return n

# l=["Rajan","Shyam","sita","Pyare","an"]

# print(rem(l,"an"))



def multiply(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
multiply(5)