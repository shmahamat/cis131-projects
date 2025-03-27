"""Souleyman Mahamat cis131
This Script collects grades from user and saves them to a file."""

grades = []  # List to store grades

# Loop to collect grades until -1 is entered
while (grade := int(input('Enter grade, -1 to end: '))) != -1:
    grades.append(grade) # Add grades to list 

if grades:  # Check if any grades were entered
    try:
        with open("grades.txt", "w") as file:  # Open file in write mode
            file.writelines(f"{grade}\n" for grade in grades)  # Write grades
    except:
        print("File output error, check permissions.")  # Handle file errors
else:
    print('No grades were entered')  # Inform user if no grades were input