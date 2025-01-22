

'''
Souleyman Mahamat
cis-131
01-21-2025

According to the American Heart Association (AHA) 
(http://bit.ly/AHATargetHeartRates), the formula for calculating your maximum
heart rate in beats per minute is 220 minus your age in years. Your target heart
rate is 50–85% of your maximum heart rate.

This script prompts for and inputs the user’s age and calculates and displays
the user’s maximum heart rate and the range of the user’s target heart rate.

*These formulas are estimates provided by the AHA; maximum and target heart
rates may vary based on the health, fitness, and gender of the individual.
Always consult a physician or qualified healthcare professional before beginning
or modifying an exercise program.
'''

age = input("What is your age? : ") # initializing prompt

# age validation
while True:
    
    # test if given age is an integer > 0
    try:
        age = int(age)
    
        if age <= 0:
            age = input("What is your age? (whole number > 0): ")
            continue
        
        else:
            break
    
    except:
        # Handle the exception
        age = input("What is your age? (whole number > 0): ")
    
    
maximum_heartrate = 220 - age
target_heartrate_range = [maximum_heartrate * 0.5, maximum_heartrate * 0.85]

print(f'''
According to the American Heart Association (AHA)

    Your maximum heart rate is : {maximum_heartrate:.0f} bpm
    Your target heart rate range is : {target_heartrate_range[0]:.0f}-\
{target_heartrate_range[1]:.0f} bpm
''')
