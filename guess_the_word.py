# Kristina McMillion
# CIS-256 Fall 2026
# Programming Assignment 4

import random

WORD_LIST = [
    "Whoville",
    "Grinch",
    "Christmas",
    "Max",
    "Heart",
    "Stole",
    "Sled",
    "Tree",
]

MAX_ATTEMPTS = 6

def choose_word(word=WORD_LIST):
    """Select and return a lowercase word from the provided word list."""
    if not word:
        raise ValueError("Word list must not be empty.")
    return random.choice(word).lower()

def create_display_word(secret_word, guessed_letters):
    """Return the word with guessed letters revealed and ungussed letters as '_',"""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )

def process_guess(secret_word, guessed_letters, remaining_attempts, guess):
   """Process a single-letter guess and return updated state:
   (guessed_letters, remaining_attempts, status, message)""" 
   normalized_guess = guess.strip().lower()

   if len(normalized_guess) != 1 or not normalized_guess.isalpha():
       return (
           guessed_letters,
           remaining_attempts,
           "invalid",
           "Please enter a single alphabetic letter.",
       )

   if normalized_guess in guessed_letters:
       return (
           guessed_letters,
           remaining_attempts,
           "duplicate",
           f"You already guessed '{normalized_guess}'.  Try another letter.",
       )

   updated_guess = guessed_letters | {normalized_guess}

   if normalized_guess in secret_word:
       count = secret_word.count(normalized_guess)
       plural = "s" if count > 1 else ""
       return (
           updated_guess,
           remaining_attempts,
           "correct",
           f"Great job! '{normalized_guess}' appears {count} time{plural}.",
       )

   updated_attempts = remaining_attempts - 1
   return (
       updated_guess,
       updated_attempts,
       "incorrect",
       f"Sorry, '{normalized_guess}' is not in the word. Attempts left: {updated_attempts}",
       )
 
def is_word_guessed(secret_word, guessed_letters):
    """ Return True if every letter in secret_word has been guessed."""
    return all(letter in guessed_letters for letter in secret_word)
 
def play_game(word=WORD_LIST, max_attempts=MAX_ATTEMPTS):
    """Run the interactive word-guessing game loop."""
    secret_word = choose_word(word)
    guessed_letters = set()
    remaining_attempts = max_attempts
 
    print("Let's Play Guess the Word!")
    print(f"You have {remaining_attempts} incorrect guesses allowed.")
 
    while remaining_attempts > 0 and not is_word_guessed(secret_word, guessed_letters):
        print("\nword:", create_display_word(secret_word, guessed_letters))
        if guessed_letters:
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))
 
        user_input = input("Guess a letter: ")
        guessed_letters, remaining_attempts, _, message = process_guess(
            secret_word, guessed_letters, remaining_attempts, user_input
        )
        print(message)
 
    if is_word_guessed(secret_word, guessed_letters):
        print(f"\nCongratulations! You guessed the word '{secret_word}'!")
    else:
        print(f"\nOut of attempts! The word was '{secret_word}'. Please try again!")
 
if __name__ == "__main__":
    play_game()
