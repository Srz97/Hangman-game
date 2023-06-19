import random
from words import words


def display_welcome():
    print("Welcome to the thrilling world of online hangman!")
    print("Alright, before we proceed, could you please grace me with your name?")

def get_player_name():
    name = input("Enter your name: ")
    if name.isalpha():
        print(f"Hi {name}, let's play Hangman and see if you can crack the code!")
    else:
        print("Invalid input. Please enter alphabetic characters only.")

def select_random_word():
    word = random.choice(words)
    return word

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

def play_game():
    random_word = select_random_word()
    hidden_word = hide_word(random_word)
    print("Guess the word: " + hidden_word)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

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

    if "_" not in hidden_word:
        print("Congratulations! You've guessed the word correctly.")
        replay = input("Would you like to challenge again? (y/n): ").lower()
        while replay not in ["y", "n"]:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            replay = input("Would you like to challenge again? (y/n): ").lower()

        if replay == "y":
            play_game()
        else:
            print("Thank you for playing. Have a nice day!")
    else:
        print("You lost! The word was:", random_word)
        retry = input("Would you like to give it another try? (y/n): ").lower()
        while retry not in ["y", "n"]:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            retry = input("Would you like to give it another try? (y/n): ").lower()

        if retry == "y":
            play_game()
        else:
            print("Thank you for playing. Have a nice day!")

display_welcome()
get_player_name()
play_game()
