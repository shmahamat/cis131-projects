'''
Souleyman Mahamat
cis-131
01-21-2025

This script plays a "guess the number" game. The program selects a random number 
between 1 and 1000, and the player must guess it. The script provides feedback 
on whether the guess is too high or too low, guiding the player to the correct answer. 
The number of attempts is counted, and performance feedback is given based on 
the number of guesses. If the player guesses correctly, they can choose to play again.
''' 

from random import randint  # Import randint to generate a random number

number_to_guess = randint(2, 999)  # Generate a random number between 2 and 999
number_of_guessses = 0  # Initialize the number of guesses

def is_guess_right(user_guess):
    """Function to check if the user's guess is correct, too low, or too high."""
    try:
        if user_guess == '':
            return False

        user_guess = int(user_guess)  # Convert input to integer

        if user_guess < number_to_guess:
            return "low"  # Return "low" if guess is less than the number
        elif user_guess > number_to_guess:
            return "high"  # Return "high" if guess is greater than the number
        else:
            return True  # Return True if guess is correct
    except:
        return False  # Return False if input is invalid (not an integer)
    
user_guess = input("Guess my number between 1 and 1000 with the fewest guesses:")

while True:
    check = is_guess_right(user_guess)  # Check the user's guess
    number_of_guessses += 1  # Increment the guess count
            
    if check == True:
        print('\nCongratulations. You guessed the number!')
        
        # Provide feedback based on the number of guesses
        if number_of_guessses <= 10:
            print("Either you know the secret or you got lucky!")
        else:
            print("You should be able to do better!")
        
        # Ask the user if they want to play again
        continue_game = None
        while continue_game != 'y' and continue_game != 'n':
            continue_game = input('Would you like to play again (y or n): ')
        
        if continue_game == 'n':
            break  # Exit the loop if user chooses not to continue
        else:
            number_to_guess = randint(2, 999)  # Generate a new random number
            number_of_guessses = 0  # Reset guess count
            user_guess = input("Guess my number between 1 and 1000 with the fewest guesses:")
    
    elif check == False:
        user_guess = input('Guess my number between 1 and 1000 with the fewest guesses:')
    elif check == 'low':
        user_guess = input('Too low. Try again: ')  # Prompt user to guess higher
    elif check == 'high':
        user_guess = input('Too high. Try again: ') # Prompt user to guess lower
