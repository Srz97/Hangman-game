# import words from words files
import random
from words import words

guess_word = random.choices(words) 

print(guess_word)