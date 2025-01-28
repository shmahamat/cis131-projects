
'''
Souleyman Mahamat
cis-131
01-27-2025

This is a sentinel-controlled-repetition script that prompts the user to input
the miles driven and gallons used for each tankful. The script calculatesand
displays the miles per gallon obtained for each tankful. After processing all
input information, the script calculates and displays the combined miles
per gallon obtained for all tankfuls.
'''

# initialize variables
miles_driven = 0
gallons_used = 0
mpg = 0
total_miles = 0
total_gallons = 0

# Input validity verification functions, input must be floats > 0 and != 1

def miles_driven_not_valid(miles_driven):

    try:
        miles_driven = float(miles_driven)
        
        if miles_driven <= 0:
            return True
        
        return False
    
    except:
        # Handle the exception
        return True

def gallons_used_not_valid(gallons_used):
            
    try:
        
        gallons_used = float(gallons_used)
        
        if gallons_used == -1:
            return False
            
        elif gallons_used <= 0:
            return True
        
        return False
    
    except:
        # Handle the exception
        return True

#main loop
while gallons_used != -1:
    gallons_used = input('Enter the gallons used (-1 to end): ')
    
    # continue asking for gallons used until valid input received
    while gallons_used_not_valid(gallons_used):
        gallons_used = input('Enter the gallons used (-1 to end): ')
        if gallons_used == -1: # if sentinel entered break loop
            break
    
    gallons_used = float(gallons_used)
    if gallons_used != -1:
        total_gallons += gallons_used
    
    # avoid adding sentinel to total
    if gallons_used == -1:
        break
    
    miles_driven = input('Enter the miles driven: ')
    
    # continue asking for miles driven until valid input received
    while miles_driven_not_valid(miles_driven):
        miles_driven = input('Enter the miles driven: ')
    
    miles_driven = float(miles_driven)
    
    mpg = miles_driven/gallons_used
    
    # avoid adding sentinel to total
    if total_gallons != -1:
        total_miles += miles_driven
    
    # print latest calculated mpg    
    print(f'The miles/gallon for this tank was {mpg:.6f}\n')

if total_gallons > 0: # verify whether anything was added total gallons
    average_mpg = total_miles/total_gallons
    print(f'\nThe overall average miles/gallon was {average_mpg:.6f}')