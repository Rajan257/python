import random

# Word list to choose from
word_list = ['python', 'hangman', 'computer', 'programming', 'developer', 'keyboard']

# Choose a random word
secret_word = random.choice(word_list)
display = ['_'] * len(secret_word)
lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("I have chosen a word. Try to guess it letter by letter.")
print("You have", lives, "lives.")
print(" ".join(display))

# Game loop
while lives > 0 and '_' in display:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong guess!")
        lives -= 1
        print("Lives left:", lives)

    print("Current word:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))

# Result
if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 You ran out of lives. The word was:", secret_word)
