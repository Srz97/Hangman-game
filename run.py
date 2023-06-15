

def display_welcome():
    print("Welcome to the thrilling world of online hangman!")
    print("Alright, before we proceed, Could you please grace me with your name")

def get_player_name():
    name = input("Enter your name: ")
    if name.isalpha():
            print(f"Hi {name} let's play Hangman and see if you can crack the code!")
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

# Hide the Random Number 
def hide_word(word):
    hidden_word = "_" * len(word)
    print("Guess the word: " + hidden_word)

random_word = select_random_word()
hidden_word = hide_word(random_word)
print(hidden_word)