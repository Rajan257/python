# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute-force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        try:
            key = int(input())
            if (key >= 1 and key <= MAX_KEY_SIZE):
                return key
        except ValueError:
            print('Please enter a valid integer between 1 and %s.' % (MAX_KEY_SIZE))

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':  # decrypt
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:  # symbol not in SYMBOLS (e.g., punctuation, space)
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated

# --- Main program ---
mode = getMode()
message = getMessage()

if mode[0] != 'b':  # not brute-force
    key = getKey()

print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))


















# import random

# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# MAX_KEY_SIZE = len(SYMBOLS)

# MESSAGES = [
#     "Python is awesome",
#     "Caesar Cipher is fun",
#     "Never give up",
#     "Hello World",
#     "Crack the code",
#     "OpenAI rocks",
#     "Keep learning",
#     "Secret mission",
#     "Game over",
#     "You win this round"
# ]

# def encrypt_message(message, key):
#     translated = ""
#     for symbol in message:
#         if symbol in SYMBOLS:
#             symbolIndex = SYMBOLS.find(symbol)
#             symbolIndex = (symbolIndex + key) % len(SYMBOLS)
#             translated += SYMBOLS[symbolIndex]
#         else:
#             translated += symbol
#     return translated

# def play_round():
#     message = random.choice(MESSAGES)
#     key = random.randint(1, MAX_KEY_SIZE)
#     encrypted = encrypt_message(message, key)

#     print("\n🔐 Encrypted message:", encrypted)
#     print("💡 Hint: Key is between 1 and", MAX_KEY_SIZE)
    
#     for attempt in range(3):
#         guess = input(f"Attempt {attempt+1}: Decrypt the message: ")
#         if guess.strip() == message:
#             print("✅ Correct! The key was", key)
#             return True
#         else:
#             print("❌ Wrong guess.")
#     print("💔 Out of attempts! The message was:", message, "| Key:", key)
#     return False

# def main():
#     print("=== 🕵️ Caesar Cipher Challenge 🕵️ ===")
#     score = 0
#     rounds = 5
    
#     for r in range(1, rounds+1):
#         print(f"\n--- Round {r} ---")
#         if play_round():
#             score += 1
#     print("\n🏆 Final Score:", score, "/", rounds)
#     print("Thanks for playing!")

# if __name__ == "__main__":
#     main()
