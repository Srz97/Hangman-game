def display_welcome():
    print("Welcome to the thrilling world of online hangman!")
    print("Alright, before we proceed, could you please grace me with your name?")

def get_player_name():
    name = input("Enter your name: ")
    if name.isalpha():
        print(f"Hi {name}, let's play Hangman and see if you can crack the code!")
    else:
        print("Invalid input. Please enter alphabetic characters only.")

display_welcome()
get_player_name()

# Import words from words files
import random
from words import words

def select_random_word():
    word = random.choice(words)
    return word

# Hide the random word
def hide_word(word):
    hidden_word = "_" * len(word)
    return hidden_word

def draw_hangman(incorrect_guesses):
    stages = [
        """
           _______
          |       |
          |       
          |       
          |       
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |       
          |       
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |       |
          |       
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |       
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |       
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      /
          |      
          -
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          |      
          -
        """
    ]

    print(stages[incorrect_guesses])

random_word = select_random_word()
hidden_word = hide_word(random_word)
print("Guess the word: " + hidden_word)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

# Main game loop
while incorrect_guesses < max_incorrect_guesses and "_" in hidden_word:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in random_word:
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        incorrect_guesses += 1
        draw_hangman(incorrect_guesses)

    hidden_word = ""
    for letter in random_word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"

    print("Guess the word: " + hidden_word)

# Check if the player won or lost
if "_" not in hidden_word:
    print("Congratulations! You've guessed the word correctly.")
else:
    print("You lost! The word was:", random_word)
