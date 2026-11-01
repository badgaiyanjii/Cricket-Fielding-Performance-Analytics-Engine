"""
Task 2: Interactive Hangman Game Engine
ShadowFox Python Development Internship
Author: Aanya Badgaiyan
"""

import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        === """,
    """
     +---+
     O   |
         |
         |
        === """,
    """
     +---+
     O   |
     |   |
         |
        === """,
    """
     +---+
     O   |
    /|   |
         |
        === """,
    """
     +---+
     O   |
    /|\\  |
         |
        === """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        === """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        === """
]

WORDS = ["PYTHON", "ANALYTICS", "SHADOWFOX", "CRICKET", "PANDAS", "DATAFRAME"]

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(HANGMAN_PICS) - 1

    print("========================================")
    print("      WELCOME TO HANGMAN CLI GAME       ")
    print("========================================")

    while mistakes < max_mistakes:
        print(HANGMAN_PICS[mistakes])
        
        # Display current word progress
        display_word = [char if char in guessed_letters else "_" for char in secret_word]
        print("Word: " + " ".join(display_word))
        print(f"Remaining Lives: {max_mistakes - mistakes}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        if "_" not in display_word:
            print("\n Congratulations! You solved the word correctly!")
            return

        guess = input("Enter a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f" Good job! '{guess}' is in the word.")
        else:
            print(f" Incorrect! '{guess}' is not in the word.")
            mistakes += 1

    print(HANGMAN_PICS[mistakes])
    print(f"\n Game Over! The correct word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()