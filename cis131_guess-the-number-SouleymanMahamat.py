'''
Souleyman Mahamat
cis-131
01-21-2025


'''

from random import randint

number_to_guess = randint(2,999)

number_of_guessses = 0

print(number_to_guess)


def is_guess_right(user_guess):
    
    try:
        user_guess = int(user_guess)
        
        if user_guess < number_to_guess:
            return "low"
        
        elif user_guess > number_to_guess:
            return "high"
        
        else:
            return True
    except:
        return False
    
    return False
    
user_guess = input("Guess my number between 1 and 1000 with the fewest guesses:")

while True:
    
    check = is_guess_right(user_guess)
    number_of_guessses += 1
    
    #if number_of_guessses < 10:
    #    print("Either you know the secret or you got lucky!")
    #elif number_of_guessses > 10:
    #    print("You should be able to do better!")
            
    if check == True:
        
        print('\nCongratulations. You guessed the number!')
        
        
            
        continue_game = None
        while continue_game != 'y' and continue_game != 'n':
            continue_game = input('Either you know the secret or you got lucky!\nWould you like to play again(y or n): ')
        
        if continue_game == 'n':
            break
        else:
            number_to_guess = randint(2,999)
            user_guess = input("Guess my number between 1 and 1000 with the fewest guesses:")
    
    elif check == 'low':
        user_guess = input('Too low. Try again: ')
    else:
        user_guess = input('Too high. Try again: ')
