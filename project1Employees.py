'''
Souleyman Mahamat
CIS131
04/07/2025

This module provides functionality to manage and display employee and
student data for an organization. It defines a base class `Person` and
derived classes `Employee` and `Student`, both of which include validation
and use inheritance. Employee and student records are read from their
respective files ('employees.txt' and 'students.txt'), parsed into object
lists, and displayed through a text-based menu system. The program supports
polymorphic output for contact information.
'''

from abc import ABC
from datetime import date
import re

# Abstract base class Person
class Person(ABC):
    def __init__(self, firstName, lastName, idNumber, emailAddress,
                 phoneNumber):
        self.firstName = firstName
        self.lastName = lastName

        if isinstance(idNumber, int) and 1000 <= idNumber <= 9999:
            self._idNumber = idNumber
        else:
            raise ValueError("ID Number must be a 4-digit integer")

        self.emailAddress = emailAddress

        if isinstance(phoneNumber, str) and len(phoneNumber) <= 12:
            self.phoneNumber = phoneNumber
        else:
            raise ValueError("Phone number must be a string with max 12 "
                             "characters")

    def __str__(self):
        return f"{self.lastName}, {self.firstName}"

    def __repr__(self):
        return self.__str__()

    @property
    def idNumber(self):
        return self._idNumber

# Employee class inherits from Person
class Employee(Person):
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {
        "001": "Full-time",
        "002": "Part-time"
    }

    def __init__(self, firstName, lastName, idNumber, emailAddress,
                 phoneNumber, hireYear, hireMonth, hireDay, classification,
                 role, annualSalary):
        super().__init__(firstName, lastName, idNumber, emailAddress,
                         phoneNumber)

        self._hireDate = date(hireYear, hireMonth, hireDay)

        if classification in Employee.classificationDictionary:
            self.classificationPerson = classification
        else:
            raise ValueError("Invalid classification")

        if role in Employee.roleDictionary:
            self.rolePerson = role
        else:
            raise ValueError("Invalid role")

        if float(annualSalary) < 0:
            raise ValueError("Salary must not be negative")

        self.annualSalary = round(float(annualSalary), 2)

    @property
    def hireDate(self):
        return self._hireDate

    def __str__(self):
        return f"{super().__str__()} - {self.rolePerson}"

    def __repr__(self):
        return self.__str__()

# Student class inherits from Person
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, emailAddress,
                 phoneNumber):
        super().__init__(firstName, lastName, idNumber, emailAddress,
                         phoneNumber)

    def __str__(self):
        return f"{super().__str__()} - Student"

    def __repr__(self):
        return self.__str__()

# Helper function

def get_key_from_value(d, val):
    for key, value in d.items():
        if value.lower().startswith(val.lower()):
            return key
    return None

def getEmployees():
    employeeList = []
    try:
        with open("employees.txt", "r") as f:
            next(f)
            for line in f:
                parts = [p.strip() for p in re.split(r'\t+|\s{2,}',
                                                     line.strip())]
                if len(parts) < 9:
                    continue

                parts = parts[:9]  # Limit to expected fields
                (lastName, firstName, idStr, email, phone, hireDate,
                 classificationValue, roleValue, salary) = parts
                idNumber = int(idStr)
                month, day, year = map(int, hireDate.split("/"))

                classKey = get_key_from_value(
                    Employee.classificationDictionary, classificationValue)
                roleKey = get_key_from_value(Employee.roleDictionary,
                                             roleValue)

                if classKey and roleKey:
                    try:
                        emp = Employee(firstName, lastName, idNumber, email,
                                       phone, year, month, day, classKey,
                                       roleKey, salary)
                        print(f"Added employee {firstName} {lastName}...")
                        employeeList.append(emp)
                    except ValueError as ve:
                        print(f"Skipping employee {firstName} {lastName} - "
                              f"{ve}")
    except FileNotFoundError:
        print("employees.txt file not found.")
    return employeeList

def getStudents():
    studentList = []
    try:
        with open("students.txt", "r") as f:
            next(f)
            for line in f:
                parts = [p.strip() for p in re.split(r'\t+|\s{2,}',
                                                     line.strip())]
                if len(parts) < 5:
                    continue

                lastName, firstName, idStr, email, phone = parts
                idNumber = int(idStr)
                try:
                    student = Student(firstName, lastName, idNumber, email,
                                      phone)
                    print(f"Added student {firstName} {lastName}…")
                    studentList.append(student)
                except ValueError as ve:
                    print(f"Skipping student {firstName} {lastName} - {ve}")
    except FileNotFoundError:
        print("students.txt file not found.")
    return studentList

def displayEmployeeEmploymentInformation(employeeList):
    print("\n\t\t\tEmployee Employment Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}"
          f"{'Phone':<16}{'HireDate':<15}{'Classification':<15}"
          f"{'Role':<10}{'Salary':<10}")
    for emp in employeeList:
        print(f"{emp.lastName:<15}{emp.firstName:<15}{emp.idNumber:<6}"
              f"{emp.emailAddress:<30}{emp.phoneNumber:<16}"
              f"{emp.hireDate.strftime('%m/%d/%Y'):<15}"
              f"{Employee.classificationDictionary[emp.classificationPerson]:<15}"
              f"{Employee.roleDictionary[emp.rolePerson]:<10}"
              f"${emp.annualSalary:<10.2f}")

def displayContactInformation(personList):
    print("\n\t\t\tContact Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}"
          f"{'Phone':<16}")
    for person in personList:
        print(f"{person.lastName:<15}{person.firstName:<15}"
              f"{person.idNumber:<6}{person.emailAddress:<30}"
              f"{person.phoneNumber:<16}")

def createMenu(employeeList, studentList):
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        print("4. Display Student Contact Information")
        print("5. Display All Contact Information (Employees and Students)")
        choice = input(">: ")

        if choice == "1":
            print("\nThank you for using the system.\n\nNow exiting the "
                  "program…")
            break
        elif choice == "2":
            displayEmployeeEmploymentInformation(employeeList)
        elif choice == "3":
            displayContactInformation(employeeList)
        elif choice == "4":
            displayContactInformation(studentList)
        elif choice == "5":
            displayContactInformation(employeeList + studentList)
        else:
            print(f"\nI am sorry, {choice} is not an option.")

if __name__ == "__main__":
    print("Starting application…\n")
    print("Adding employees…\n")
    employeeList = getEmployees()

    print("\nAdding students…\n")
    studentList = getStudents()

    createMenu(employeeList, studentList)
