import random

def generate_secret(num_digits=3, unique=True):
    digits = list('0123456789')
    if unique:
        secret = ''.join(random.sample(digits, num_digits))
        # avoid leading zero for nicer UX
        if secret[0] == '0':
            # swap with a non-zero digit
            for i in range(1, len(secret)):
                if secret[i] != '0':
                    lst = list(secret)
                    lst[0], lst[i] = lst[i], lst[0]
                    secret = ''.join(lst)
                    break
    else:
        secret = ''.join(random.choice(digits) for _ in range(num_digits))
    return secret

def get_clues(guess, secret):
    """Return clues string following Bagels rules:
       - 'Fermi' for correct digit in correct place
       - 'Pico' for correct digit wrong place
       - 'Bagels' if no digits are correct
       Clues are returned sorted lexicographically to avoid leaking position info by order.
    """
    if guess == secret:
        return "You got it!"

    clues = []
    for i, ch in enumerate(guess):
        if ch == secret[i]:
            clues.append("Fermi")
        elif ch in secret:
            clues.append("Pico")

    if not clues:
        return "Bagels"
    else:
        # sort to not reveal ordering information
        clues.sort()
        return ' '.join(clues)

def valid_guess(guess, num_digits):
    return guess.isdigit() and len(guess) == num_digits

def play_bagels(num_digits=3, max_guesses=10, unique=True):
    secret = generate_secret(num_digits=num_digits, unique=unique)
    print(f"Welcome to Bagels! Guess the {num_digits}-digit secret number.")
    print("Clues: 'Fermi' = right digit & right place, 'Pico' = right digit wrong place, 'Bagels' = none.")
    print(f"You have {max_guesses} guesses. Good luck!\n")

    for attempt in range(1, max_guesses + 1):
        while True:
            guess = input(f"Guess #{attempt}: ").strip()
            if not valid_guess(guess, num_digits):
                print(f"→ Enter exactly {num_digits} digits (0-9). Try again.")
                continue
            # optionally enforce unique digits if desired
            if unique and len(set(guess)) != len(guess):
                print("→ Use unique digits (no repeats). Try again.")
                continue
            break

        clues = get_clues(guess, secret)
        print(clues)
        if guess == secret:
            print(f"Nice! You cracked it in {attempt} guesses.\n")
            break
    else:
        print(f"Out of guesses — the secret was: {secret}\n")

if __name__ == "__main__":
    # Example: 3-digit Bagels with unique digits and 10 max guesses
    play_bagels(num_digits=3, max_guesses=10, unique=True)
