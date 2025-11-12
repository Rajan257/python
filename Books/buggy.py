import random
number1 = random.randint(1,10)
number2 = random.randint(1,10)

print("What is "+str(number1)+"+"+str(number2)+"?")
answer = input()                                     #because of this this is a debug  the program will not but not work correctly
if answer ==number1+number2:                         #answer=int(input()) is right
    print("Correct!")
else:
    print("Nope! The answer is "+str(number1+number2))