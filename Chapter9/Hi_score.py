import random 

def game():
    print("You are playing the game...")
    score=random.randint(1,62)
    #fetch the hiscore
    with open("Hi_score.txt") as f:
        Hi_score = f.read()
        if(Hi_score!=""):
            Hi_score=int(Hi_score)
        else:
            Hi_score = 0

    print(f"Your score: {score}")
    if(score>Hi_score ):
        #write thsi hiscore to the file
        with open("Hi_score.txt","w") as f:
            f.write(str(score))

    return score
    
game()