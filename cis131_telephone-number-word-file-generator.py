"""
Souleyman Mahamat
cis131
02/24/2025

This script prompts the user for a phone number and generates all possible 
letter combinations using the corresponding keypad digits. It then checks 
each generated combination to determine if it forms a valid word or can be 
split into valid words from the nltk words corpus. The script to a the file
<number>-generated-words-<utc timestamp> total number of combinations and the
valid words found.
"""

from datetime import datetime,timezone
import nltk
from nltk.corpus import words

# Download the words corpus from nltk library, suppressing unnecessary output
nltk.download('words', quiet=True)

# Convert the list of words from nltk corpus into a set for faster lookups
word_list = set(words.words())

# Dictionary mapping each digit to corresponding letters as per the phone keypad
keypad = {
    2: ('a', 'b', 'c'),
    3: ('d', 'e', 'f'),
    4: ('g', 'h', 'i'),
    5: ('j', 'k', 'l'),
    6: ('m', 'n', 'o'),
    7: ('p', 'q', 'r', 's'),
    8: ('t', 'u', 'v'),
    9: ('w', 'x', 'y', 'z')
}

# Prompt the user to input a valid phone number without 0, 1, or '-'
phone_number = '0'
while '0' in phone_number or '-' in phone_number or '1' in phone_number or \
        phone_number == '':
    phone_number = input('Enter a phone number (no 0, 1, or "-"): ')
    try:
        int(phone_number)  # Try converting input to an integer
    except:
        phone_number = '0'  # If not a valid number, reset and ask again
    
# Convert the phone number into a list of integers
phone_number_string = phone_number
phone_number = list(phone_number)
phone_number = [int(i) for i in phone_number]


def generate_combinations(phone_number, index=0, prefix=""):
    if index == len(phone_number):
        return [prefix]
    
    digit = phone_number[index]
    letters = keypad[digit]  # Get the letters corresponding to the current digit
    results = []  # List to hold the generated combinations
    
    # For each letter corresponding to the digit, recursively generate 
    # combinations
    for letter in letters:
        results.extend(generate_combinations(phone_number, index + 1, 
                                              prefix + letter))
    
    return results


def is_valid_word(word):
    word_combos = []  # List to store valid word combinations
    if word in word_list:  # Check if the whole word is valid
        word_combos.append(word)
    
    # Check for split word combinations (e.g., 'catdog' -> 'cat' + 'dog')
    for i in range(len(word)):
        if word[0:i] in word_list and word[i:] in word_list:
            word = word[0:i] + '_' + word[i:]  # Split the word and add an 
            # underscore
            word_combos.append(word)
    
    return word_combos


# Generate all possible combinations of letters for the given phone number
combinations = generate_combinations(phone_number)

valid_combos = []  # List to hold the valid words found from the combinations

# Check each combination to see if it's a valid word or can be split into 
# valid words
for word in combinations:
    output = is_valid_word(word)
    if output != []:  # If the word is valid or split into valid words
        valid_combos.extend(output)

# Display the results
print(f"Total number of combinations: {len(combinations)}")
print(f"Total valid words found: {len(valid_combos)}")
print(valid_combos)  # Display the list of valid word combinations
print()

try:
    timestamp = datetime.now(timezone.utc).astimezone()
    timestamp = timestamp.isoformat().replace('+00:00','')
    file = f'{phone_number_string}-generated-words-{timestamp}'
    print(file)
    
    with open(file, "w") as file:
        timestamp = datetime.now(timezone.utc).astimezone()
        timestamp = timestamp.isoformat().replace('+00:00','')
        file.write(f'Phone numebr: {phone_number_string}\n')
        file.write(f'Total number of combinations: {len(combinations)}\n')
        file.write(f'Total valid words found: {len(valid_combos)}\n\n')
        
        for i in range(len(valid_combos)):
            file.write(f'{valid_combos[i]}\n')
except:
    print("File output error, check permissions.")