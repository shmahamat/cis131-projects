'''
Souleyman Mahamat
CIS131
05/18/2025

Project 5:
This module manages employee and student data, including academic scores.
It also has a few sorting options.
'''

from abc import ABC
from datetime import date
import re

# Abstract base class Person
class Person(ABC):
    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
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
            raise ValueError("Phone number must be a string with max 12 characters")

    def __str__(self):
        return f"{self.lastName}, {self.firstName}"

    def __repr__(self):
        return self.__str__()

    @property
    def idNumber(self):
        return self._idNumber

# Employee class
class Employee(Person):
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full-time", "002": "Part-time"}

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber,
                 hireYear, hireMonth, hireDay, classification, role, annualSalary):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
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

# Student class
class Student(Person):
    courseNameList = ["Art", "Latin", "Greek", "Mathematics", "Science", "Painting", "Sculpting"]

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        self.coursesStudentDict = {}

    def __str__(self):
        return f"{super().__str__()} - Student"

    def getStudentAcademics(self):
        order = ["Art", "Greek", "Latin", "Science", "Mathematics"]
        scores = [str(self.coursesStudentDict.get(course, "")) for course in order]
        return f"{self.lastName:<15}{self.firstName:<15}{self.idNumber:<6}" + ''.join([f"{score:<8}" for score in scores])

    def getStudentAcademicReport(self):
        scores = [self.coursesStudentDict.get(course, 0) for course in ["Art", "Greek", "Latin", "Science", "Mathematics"]]
        high = max(scores)
        low = min(scores)
        avg = round(sum(scores) / len(scores), 1)

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        return {
            'LastName': self.lastName,
            'FirstName': self.firstName,
            'ID': self.idNumber,
            'Scores': scores,
            'High': high,
            'Low': low,
            'Average': avg,
            'Grade': grade
        }

# Utility
def get_key_from_value(d, val):
    for key, value in d.items():
        if value.lower().startswith(val.lower()):
            return key
    return None

# Full report
def displayFullStudentAcademicReport(studentList):
    print("\n\t\t\tFull Academic Report\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'StudentID':<10}{'Art':<6}{'Greek':<6}{'Latin':<6}{'Science':<8}{'Math':<6}\
        {'High':<6}{'Low':<6}{'Average':<8}{'Grade':<6}")
    all_scores = [[], [], [], [], []]  # For Art, Greek, Latin, Science, Math

    for student in studentList:
        report = student.getStudentAcademicReport()
        print(f"{report['LastName']:<12}{report['FirstName']:<12}{report['ID']:<10}" + ''.join([f"{s:<6}"\
             for s in report['Scores']]) + f"{report['High']:<6}{report['Low']:<6}{report['Average']:<8}{report['Grade']:<6}")
        for i in range(5):
            all_scores[i].append(report['Scores'][i])

    # Display column-wise High, Low, Avg
    labels = ['High', 'Low', 'Average']
    funcs = [max, min, lambda lst: round(sum(lst)/len(lst), 1)]

    for label, func in zip(labels, funcs):
        line = f"{label:<34}" + ''.join([f"{func(courseScores):<6}" for courseScores in all_scores])
        print(line)

# Specific student academic record
def lookUpStudentAcademicRecord(studentList):
    while True:
        user_input = input("\nPlease enter the ID of the student (or -1 to quit): ")
        if user_input == "-1":
            return
        try:
            id_lookup = int(user_input)
            found = False
            for student in studentList:
                if student.idNumber == id_lookup:
                    print("\n\t\t\tIndividual Student Report.\n")
                    print(f"{'LastName':<12}{'FirstName':<12}{'StudentID':<10}{'Art':<6}{'Greek':<6}{'Latin':<6}{'Science':<8}{'Math':<6}{'High':<6}{'Low':<6}{'Average':<8}{'Grade':<6}")
                    report = student.getStudentAcademicReport()
                    print(f"{report['LastName']:<12}{report['FirstName']:<12}{report['ID']:<10}" + ''.join([f"{s:<6}" for s in report['Scores']]) + f"{report['High']:<6}{report['Low']:<6}{report['Average']:<8}{report['Grade']:<6}")
                    found = True
                    break
            if not found:
                print("That is not an ID we have on record.")
        except ValueError:
            print("Please enter a valid ID number.")

# honor roll
def getHonorRoll(studentList):
    print("\nHonor Roll Report\n")
    print(f"{'LastName':<12}{'FirstName':<12}{'StudentID':<10}{'Art':<6}{'Greek':<6}{'Latin':<6}{'Science':<8}{'Math':<6}{'High':<6}{'Low':<6}{'Average':<8}{'Grade':<6}")
    for student in studentList:
        report = student.getStudentAcademicReport()
        if report['Grade'] == 'A':
            print(f"{report['LastName']:<12}{report['FirstName']:<12}{report['ID']:<10}" + ''.join([f"{s:<6}" for s in report['Scores']]) + f"{report['High']:<6}{report['Low']:<6}{report['Average']:<8}{report['Grade']:<6}")

# Data loading
def getEmployees():
    employeeList = []
    try:
        with open("employees.txt", "r") as f:
            next(f)
            for line in f:
                parts = [p.strip() for p in re.split(r'\t+|\s{2,}', line.strip())]
                if len(parts) < 9:
                    continue
                parts = parts[:9]
                lastName, firstName, idStr, email, phone, hireDate, classification, role, salary = parts
                idNumber = int(idStr)
                month, day, year = map(int, hireDate.split("/"))
                classKey = get_key_from_value(Employee.classificationDictionary, classification)
                roleKey = get_key_from_value(Employee.roleDictionary, role)
                if classKey and roleKey:
                    try:
                        emp = Employee(firstName, lastName, idNumber, email, phone,
                                       year, month, day, classKey, roleKey, salary)
                        print(f"Added employee {firstName} {lastName}...")
                        employeeList.append(emp)
                    except ValueError as ve:
                        print(f"Skipping employee {firstName} {lastName} - {ve}")
    except FileNotFoundError:
        print("employees.txt file not found.")
    return employeeList

def getStudents():
    studentList = []
    try:
        with open("students.txt", "r") as f:
            next(f)
            for line in f:
                parts = [p.strip() for p in re.split(r'\t+|\s{2,}', line.strip())]
                if len(parts) < 5:
                    continue
                lastName, firstName, idStr, email, phone = parts
                idNumber = int(idStr)
                try:
                    student = Student(firstName, lastName, idNumber, email, phone)
                    print(f"Added student {firstName} {lastName}…")
                    studentList.append(student)
                except ValueError as ve:
                    print(f"Skipping student {firstName} {lastName} - {ve}")
    except FileNotFoundError:
        print("students.txt file not found.")
    return studentList

def getStudentScores(studentList):
    try:
        with open("scores.txt", "r") as f:
            next(f)
            for line in f:
                parts = line.strip().split()
                if len(parts) != 6:
                    continue
                idNum = int(parts[0])
                scores = list(map(int, parts[1:]))
                for student in studentList:
                    if student.idNumber == idNum:
                        for i, course in enumerate(["Art", "Greek", "Latin", "Science", "Mathematics"]):
                            if course in Student.courseNameList:
                                student.coursesStudentDict[course] = scores[i]
                        print(f"Added scores for {student.firstName} {student.lastName}…")
                        break
    except FileNotFoundError:
        print("scores.txt file not found.")

# Display
def displayEmployeeEmploymentInformation(employeeList):
    print("\n\t\t\tEmployee Employment Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}{'Phone':<16}{'HireDate':<15}{'Classification':<15}{'Role':<10}{'Salary':<10}")
    for emp in employeeList:
        print(f"{emp.lastName:<15}{emp.firstName:<15}{emp.idNumber:<6}{emp.emailAddress:<30}{emp.phoneNumber:<16}{emp.hireDate.strftime('%m/%d/%Y'):<15}{Employee.classificationDictionary[emp.classificationPerson]:<15}{Employee.roleDictionary[emp.rolePerson]:<10}${emp.annualSalary:<10.2f}")

def displayContactInformation(personList):
    print("\n\t\t\tContact Information\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Email':<30}{'Phone':<16}")
    for person in personList:
        print(f"{person.lastName:<15}{person.firstName:<15}{person.idNumber:<6}{person.emailAddress:<30}{person.phoneNumber:<16}")

def displayStudentScores(studentList):
    print("\n\t\t\tStudent Academic Report\n")
    print(f"{'LastName':<15}{'FirstName':<15}{'ID':<6}{'Art':<8}{'Greek':<8}{'Latin':<8}{'Science':<8}{'Mathematics':<8}")
    for student in studentList:
        print(student.getStudentAcademics())

# Sorting Helpers
def sortStudentListByLastName(studentList):
    studentList.sort(key=lambda s: (s.lastName.lower(), s.firstName.lower()))

def sortStudentListByStudentID(studentList):
    studentList.sort(key=lambda s: s.idNumber)

def displayFullAcademicReportSortedByLastName(studentList):
    sortStudentListByLastName(studentList)
    displayFullStudentAcademicReport(studentList)

def displayFullAcademicReportSortedByStudentID(studentList):
    sortStudentListByStudentID(studentList)
    displayFullStudentAcademicReport(studentList)

# Menu system
def createMenu(employeeList, studentList):
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        print("4. Display Student Contact Information")
        print("5. Display All Contact Information (Employees and Students)")
        print("6. Display Full Academic Report")
        print("7. Display Academic Report for one Student")
        print("8. Display Honor Roll")
        print("9. Display Full Academic Report Sorted By Last Name")
        print("10. Display Full Academic Report Sorted By Student ID")
        choice = input(">: ")

        if choice == "1":
            print("\nThank you for using the system.\n\nNow exiting the program…")
            break
        elif choice == "2":
            displayEmployeeEmploymentInformation(employeeList)
        elif choice == "3":
            displayContactInformation(employeeList)
        elif choice == "4":
            displayContactInformation(studentList)
        elif choice == "5":
            displayContactInformation(employeeList + studentList)
        elif choice == "6":
            displayFullStudentAcademicReport(studentList)
        elif choice == "7":
            lookUpStudentAcademicRecord(studentList)
        elif choice == "8":
            getHonorRoll(studentList)
        elif choice == "9":
            displayFullAcademicReportSortedByLastName(studentList)
        elif choice == "10":
            displayFullAcademicReportSortedByStudentID(studentList)
        else:
            print(f"\nI am sorry, {choice} is not an option.")


# Main driver
if __name__ == "__main__":
    print("Starting application…\n")
    print("Adding employees…\n")
    employeeList = getEmployees()

    print("\nAdding students…\n")
    studentList = getStudents()

    print("\nLoading student scores…\n")
    getStudentScores(studentList)

    createMenu(employeeList, studentList)
