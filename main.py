import random
import sys
from termcolor import colored

# Get the answer words
possible_words = open("data/possible_words.txt", "r")
possible_word_list = list((possible_words.read()).split("\n"))

# Get the guess words
allowed_words = open("data/allowed_words.txt", "r")
allowed_word_list = list((allowed_words.read()).split("\n"))

pos_list_len = len(possible_word_list)

def word():
    word_num = random.randint(1, pos_list_len - 1)
    word = possible_word_list[word_num]
    return word

def new_guess():
    guess = input(colored("Type a valid 5 letter word: ", "blue"))

    # To quit the game
    if guess == "quit":
        sys.exit()
        
    # Check if it is a valid guess
    elif guess not in allowed_word_list or len(guess) != 5:
        print(colored("Sorry, that's invalid; Word must be valid and 5 characters", "red"))
        new_guess()

    return guess

guess = ""
guess_number = 0
ans = word()

# Wordle
while guess != ans and guess_number < 6:
    # Make a guess and increase the guess number
    guess = new_guess()
    guess_number += 1

    # Validate the guess and make it a win if it is correct
    if guess == ans:
        print(colored(guess, "green"), "\nCorrect! The word was", colored(guess, "green"))
        sys.exit()   
    else:
        for c in range(5):
            if guess[c] == ans[c]:
                color = "green"
            elif guess[c] in ans:
                color = "yellow"
            else:
                color = "dark_grey"

            # Printing each character on the same line
            if c == 4:
                ending = "\n"
            else:
                ending = ""

            print(colored(guess[c], color), end = ending)
            
# Loss if the player does not guess it in 6 attempts
print(colored("Sorry, the word was", "blue"), colored(ans, "red"))