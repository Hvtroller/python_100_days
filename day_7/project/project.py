import random

# This is Hang man game
# Random word is selected from the list of words
# User has to guess the word by entering the letters
# User has 6 chances to guess the word
# After each guess, the word is displayed with the correct letters guessed by the user
# If user is able to guess the word then user wins
# If user is not able to guess the word then user loses

# Constants
WORDS = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
CHANCES = 6

HANGMAN_STATES = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

def select_random_word(words):
    return random.choice(words)

def display_current_progress(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def get_user_guess():
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

def hangman_game():
    word = select_random_word(WORDS)
    guessed_letters = []
    chances = CHANCES

    print("Welcome to Hangman!")
    print(f"You have {chances} chances to guess the word.")

    while chances > 0:
        display_word = display_current_progress(word, guessed_letters)
        print(display_word)
        print(HANGMAN_STATES[chances])

        guess = get_user_guess()

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            chances -= 1
            print(f"You have {chances} chances left.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word correctly: {word}")
            break

    if chances == 0:
        print(HANGMAN_STATES[chances])
        print(f"Sorry, you ran out of chances. The word was: {word}")

if __name__ == "__main__":
    hangman_game()