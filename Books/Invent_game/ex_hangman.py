import random

# Extended ASCII art stages (more guesses)
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
# Extra stages with ears
'''
  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''']

wordSets = {
    'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    'colors': 'red orange yellow green blue indigo violet white black brown'.split(),
    'fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split()
}

def getRandomWord(wordList):
    return random.choice(wordList)

def chooseDifficulty():
    while True:
        print("Choose difficulty: (E)asy, (M)edium, (H)ard")
        choice = input().strip().lower()
        if choice in ('e','m','h'):
            return choice

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print("Missed letters:", " ".join(missedLetters))
    blanks = ['_' if l not in correctLetters else l for l in secretWord]
    print("Word:", " ".join(blanks))

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter:")
        guess = input().lower().strip()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You've already guessed that letter.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else:
            return guess

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

def main():
    print("H A N G M A N")
    playing = True
    while playing:
        # select word set
        print("Pick a word set:", ", ".join(wordSets.keys()))
        setName = input().strip().lower()
        if setName not in wordSets:
            setName = random.choice(list(wordSets.keys()))
        # choose difficulty
        diff = chooseDifficulty()
        if diff == 'e':
            maxMissed = 8
        elif diff == 'm':
            maxMissed = 6
        else:
            maxMissed = 4

        secretWord = getRandomWord(wordSets[setName])
        missedLetters = []
        correctLetters = []
        gameOver = False

        while not gameOver:
            displayBoard(missedLetters, correctLetters, secretWord)

            guess = getGuess(missedLetters + correctLetters)

            if guess in secretWord:
                correctLetters.append(guess)
                # check win
                foundAll = all(l in correctLetters for l in secretWord)
                if foundAll:
                    print(f"\nYes! The secret word is \"{secretWord}\"! You win!")
                    gameOver = True
            else:
                missedLetters.append(guess)
                if len(missedLetters) >= maxMissed:
                    displayBoard(missedLetters, correctLetters, secretWord)
                    print(f"\nYou've run out of guesses!\nThe word was \"{secretWord}\".")
                    gameOver = True

        playing = playAgain()

if __name__ == '__main__':
    main()
