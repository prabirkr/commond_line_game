#  Creating a commond line game with the help of copilot

import random

def play_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the number of guesses
    num_guesses = 0
    
    while True:
        # Get user input
        guess = input("Guess a number between 1 and 10: ")
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if int(guess) == secret_number:
            print("Congratulations! You guessed the correct number in", num_guesses, "guesses.")
            break
        else:
            print("Wrong guess. Try again.")

# Start the game
play_game()