import random

guessesTaken=0

print("Hello! What is your name?")

myName=input()

number=random.randint(1,20)
 
print("Well,"+myName+", I am thinking of a number between 1 and 20")

guess=input()

guess=int(guess)

for guessesTaken in range(6):
    print("Take a guess.")
    guess=input()
    guess=int(guess)

    if guess<number:
        print("your guess is too low") #8 spaces in front of print

    if guess>number:
        print("Your guess is too high")  

    if guess==number:
            break

if guess==number:
    guessesTaken =str(guessesTaken+1)

    print("Good job,"+myName+"! you guessed my number in"+guessesTaken+"guesses!")

if guess !=number:
    number=str(number)
    print("Nope.The number i was thinking of was"+number+".")



