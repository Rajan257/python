# l=[1,2,3,4,5,6,7,8]

# for i, item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)




# n =int(input("Enter the number: "))
# table=[n*i for i in range(1,11)]
# print(table)




# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter b number: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("infinite")



n=int(input("Enter the number: "))
table=[n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"table of {n}: {str(table)}\n")
    