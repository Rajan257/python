import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar ' \
        'coyote crow deer dog donkey duck eagle ferret fox frog goat goose ' \
        'hawk lion lizard llama mole monkey moose mouse mule newt otter ' \
        'owl panda parrot pigeon python rabbit ram rat raven rhino salmon ' \
        'seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # Returns a random word from the passed list
    return random.choice(wordList)

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', missedLetters)
    blanks = ['_' if letter not in correctLetters else letter for letter in secretWord]
    print(' '.join(blanks))

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# --- Main program ---
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        # Check if player has won
        foundAllLetters = True
        for letter in secretWord:
            if letter not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess

        # Check if player has lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'You have run out of guesses!\n'
                  f'After {len(missedLetters)} missed guesses and '
                  f'{len(correctLetters)} correct guesses, '
                  f'the word was "{secretWord}"')
            gameIsDone = True

    # Ask if play again
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
