# Arithmatic operator
a= 9
b=4

c=a+b

print(c)


#Assignment operator

a=4-2 # Assign 4-2 in a

b =6

b+= 3 # Increment the value of b by 3 and then assign it to b

print(b)

b-= 4
print(b)

# Comperison operator
d=5>=5
print(d)

# read all comperison operator

# logical operatore 

e= True or False


print("A B | OR AND NOT_A NOT_B NOR XOR")
for A in [0, 1]:
    for B in [0, 1]:
        OR = A | B
        AND = A & B
        NOT_A = 1 - A
        NOT_B = 1 - B
        NOR = 1 - (A | B)
        XOR = A ^ B
        print(f"{A} {B} |  {OR}   {AND}    {NOT_A}     {NOT_B}    {NOR}   {XOR}")


# Truth table of "and"

print("True and False or ", True and False)
print("True and False or ", True and False)
print("True and False or ", True and False)
print("True and False or ", True and False)


# Truth table of 'or'
print("True or False is ", True or False)
print("True or False is ", True or  False)
print("True or False is ", True or False)
print("True or False is ", True or  False)

