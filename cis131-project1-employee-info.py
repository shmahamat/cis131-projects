'''
Souleyman Mahamat
CIS131
04/07/2025

This module provides functionality to manage and display employee data for an
organization. It defines a base class `Person` and a derived class `Employee`,
both of which include validation for fields such as ID number, phone number,
classification, and role. Employee records are read from a file named
'employees.txt', parsed into `Employee` objects, and stored in a list. The
program includes functions to display either employment or contact information
in a formatted table, and a simple text-based menu system allows users to
interact with the data. The expected input file format includes fields such as
name, ID, email, phone, hire date, classification, role, and salary.
'''

from abc import ABC, abstractmethod
from datetime import date
import re

# Abstract base class Person
class Person(ABC):
    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName

        # ID validation: must be a 4-digit integer
        if isinstance(idNumber, int) and 1000 <= idNumber <= 9999:
            self._idNumber = idNumber
        else:
            raise ValueError("ID Number must be a 4-digit integer")

        self.emailAddress = emailAddress

        # Phone number validation: must be a string with 12 characters or fewer
        if isinstance(phoneNumber, str) and len(phoneNumber) <= 12:
            self.phoneNumber = phoneNumber
        else:
            raise ValueError("Phone number must be a string with max 12 characters")

    def __str__(self):
        return f"{self.lastName}, {self.firstName}"

    def __repr__(self):
        return self.__str__()

    @property
    def idNumber(self):
        return self._idNumber

# Employee class inherits from Person
class Employee(Person):
    # Class-level dictionaries for role and classification types
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber, 
                 hireYear, hireMonth, hireDay, classification, role, annualSalary):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)

        # Store hire date as a date object
        self._hireDate = date(hireYear, hireMonth, hireDay)

        # Validate and set classification
        if classification in Employee.classificationDictionary:
            self.classificationPerson = classification
        else:
            raise ValueError("Invalid classification")

        # Validate and set role
        if role in Employee.roleDictionary:
            self.rolePerson = role
        else:
            raise ValueError("Invalid role")

        # Validate salary
        if float(annualSalary) < 0:
            raise ValueError("Salary must not be negative")

        # Store salary rounded to 2 decimal places
        self.annualSalary = round(float(annualSalary), 2)

    @property
    def hireDate(self):
        return self._hireDate

    def __str__(self):
        return f"{super().__str__()} - {self.rolePerson}"

    def __repr__(self):
        return self.__str__()

# Helper function to get dictionary key from value (case-insensitive)
def get_key_from_value(d, val):
    for key, value in d.items():
        if value.lower() == val.lower():
            return key
    return None

# Reads employees from file and returns a list of Employee objects
def getEmployees():
    employeeList = []
    try:
        with open("employees.txt", "r") as f:
            next(f)  # Skip header line
            for line in f:
                # Split line using 2+ spaces or tabs
                parts = re.split(r'\s{2,}|\t+', line.strip())
                if len(parts) < 9:
                    continue  # Skip malformed lines

                # Parse fields from line
                lastName = parts[0].strip()
                firstName = parts[1].strip()
                idNumber = int(parts[2].strip())
                email = parts[3].strip()
                phone = parts[4].strip()
                month, day, year = map(int, parts[5].strip().split("/"))
                classificationValue = parts[6].strip()
                roleValue = parts[7].strip()
                salary = parts[8].strip()

                # Convert human-readable classification/role to code
                classKey = get_key_from_value(Employee.classificationDictionary, classificationValue)
                roleKey = get_key_from_value(Employee.roleDictionary, roleValue)

                if classKey and roleKey:
                    try:
                        # Create Employee object and add to list
                        emp = Employee(firstName, lastName, idNumber, email, phone, 
                                       year, month, day, classKey, roleKey, salary)
                        print(f"Added employee {firstName} {lastName}...")
                        employeeList.append(emp)
                    except ValueError as ve:
                        print(f"Skipping employee {firstName} {lastName} - {ve}")
    except FileNotFoundError:
        print("employees.txt file not found.")
    return employeeList

# Displays employment-related details for each employee
def displayEmployeeEmploymentInformation(employeeList):
    print("\n\t\t\tEmployee Employment Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}{'Phone':<16}{'HireDate':<15}{'Classification':<15}{'Role':<10}{'Salary':<10}")
    for emp in employeeList:
        print(f"{emp.lastName:<15}{emp.firstName:<15}{emp.idNumber:<6}{emp.emailAddress:<30}{emp.phoneNumber:<16}{emp.hireDate.strftime('%-m/%-d/%Y'):<15}{Employee.classificationDictionary[emp.classificationPerson]:<15}{Employee.roleDictionary[emp.rolePerson]:<10}${emp.annualSalary:<10.2f}")

# Displays contact info for each employee
def displayEmployeeContactInformation(employeeList):
    print("\n\t\t\tEmployee Contact Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}{'Phone':<16}")
    for emp in employeeList:
        print(f"{emp.lastName:<15}{emp.firstName:<15}{emp.idNumber:<6}{emp.emailAddress:<30}{emp.phoneNumber:<16}")

# Displays the menu and handles user interaction
def createMenu(employeeList):
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        choice = input(">: ")

        if choice == "1":
            print("\nThank you for using the system.\n\nNow exiting the program…")
            break
        elif choice == "2":
            displayEmployeeEmploymentInformation(employeeList)
        elif choice == "3":
            displayEmployeeContactInformation(employeeList)
        else:
            print(f"\nI am sorry, {choice} is not an option.")

# Main program entry point
if __name__ == "__main__":
    print("Starting application…\n")
    print("Adding employees…\n")
    employeeList = getEmployees()
    createMenu(employeeList)
