# import words from words files
import random
from words import words

guess_word = random.choices(words) 

print(guess_word)

import random
from words import words

guess_word = random.choices(words) 

print(guess_word)

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
