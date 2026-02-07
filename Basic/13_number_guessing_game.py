# This program is a simple number guessing game
# The computer selects a number and the user tries to guess it

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Check whether the guess is correct
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong guess!")
    print("The correct number was:", secret_number)


"""
---------------- OUTPUT ----------------

Guess a number between 1 and 10: 5
Wrong guess!
The correct number was: 8

---------------------------------------
"""
