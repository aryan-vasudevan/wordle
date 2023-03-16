import random
from termcolor import colored

# Get the words
words = open("words.txt", "r")
word_list = list((words.read()).split("\n"))
library = {}
for word in word_list:
    library[word] = 1

word_list_len = len(word_list)

def word():
    word_num = random.randint(1, word_list_len - 1)
    word = word_list[word_num]
    return word

def new_guess():
    guess = input(colored("Type a valid 5 letter word: ", "blue"))

    # Make sure it is a valid guess
    while guess not in library or len(guess) != 5:
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
        print(colored(guess, "green"), "\n Correct! The word was ", colored(guess, "green"))   
    else:
        for c in range(5):
            if guess[c] == ans[c]:
                print(colored(guess[c], "green"))
            elif guess[c] in ans:
                print(colored(guess[c], "yellow"))
            else:
                print(colored(guess[c], "dark_grey"))
        
# Loss if the player does not guess it in 6 attempts
print(colored("Sorry, the word was", "blue"), colored(ans, "red"))