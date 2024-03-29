# Import words
import random
from words import words


def display_welcome():
    print("Welcome to the thrilling world of online hangman!\n")
    print("Before we proceed, may I take your name?")


def get_player_name():
    name = input("Enter your name: ")
    if name.isalpha():
        print(f"Hi {name}, let's play Hangman!")
    else:
        print("Invalid input. Please enter alphabetic characters only.")


# Select a random word from the 'words' list
def select_random_word():
    word = random.choice(words)
    return word


# Create a string of underscores with the same length as the 'word'
def hide_word(word):
    hidden_word = "_" * len(word)
    return hidden_word


# Various stages of the hangman drawing
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


# Show the game rules
def show_rules():
    print("Hangman Rules:")
    print("1. The computer will randomly select a word for you to guess.")
    print("2. You can guess one letter at a time.")
    print("3. If the letter you guessed is in the word, it will be revealed.")
    print("4. If the guessed letter is not in the word, you will lose a life.")
    print("5. You have a total of 6 lives.")
    print("6. Your goal is to guess the word before you run out of lives.\n")


# Main game loop
def play_game():
    random_word = select_random_word()
    hidden_word = hide_word(random_word)
    print("Guess the word: " + hidden_word)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    # Continue the game until max incorrect guesses or word is fully guessed
    while incorrect_guesses < max_incorrect_guesses and "_" in hidden_word:
        guess = input("Guess a letter:\n ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

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

    # Game over messages and option to replay
    if "_" not in hidden_word:
        print("Congratulations! You've guessed the word correctly.")
        replay = input("Would you like to challenge again? (y/n):\n ").lower()
        while replay not in ["y", "n"]:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            replay = input("Would you like to challenge again? (y/n):\n ").lower()

        if replay == "y":
            play_game()
        else:
            print("Thank you for playing. Have a nice day!")
    else:
        print("You lost! The word was:", random_word)
        retry = input("Would you like to give it another try? (y/n):\n ").lower()
        while retry not in ["y", "n"]:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            retry = input("Would you like to give it another try? (y/n):\n ").lower()

        if retry == "y":
            play_game()
        else:
            print("Thank you for playing. Have a nice day!")


display_welcome()
get_player_name()

show_rules_option = input("Would you like to see the rules? (y/n):\n ").lower()
while show_rules_option not in ["y", "n"]:
    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    show_rules_option = input("Would you like to see the rules? (y/n):\n ").lower()

if show_rules_option == "y":
    show_rules()

play_game()
