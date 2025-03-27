'''
Abstract classes and methods lab module including Employee base class
and Salaried and Hourly subclasses.

Souleyman Mahamat
CIS-131
3/26/2025
'''

import abc


class Employee(abc.ABC):    
    '''
    Base class for all employees.
    Enforces that all subclasses implement the earnings() method.
    Stores basic employee details like first name, last name, and SSN.
    '''
    
    def __init__(self, first_name, last_name, ssn):
        # Initializing employee attributes
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        
    @property
    def first_name(self):
        # Getter for first name
        return self._first_name
    
    @property
    def last_name(self):
        # Getter for last name
        return self._last_name
    
    @property
    def ssn(self):
        # Getter for SSN
        return self._ssn
    
    def __repr__(self):
        # String representation of an employee
        return f'{self._first_name} {self._last_name} {self._ssn}'
        
    @abc.abstractmethod
    def earnings(self):
        # Abstract method to be implemented by subclasses
        raise NotImplementedError


class SalariedEmployee(Employee):
    '''
    Represents a salaried employee who earns a fixed weekly salary.
    '''
    
    def __init__(self, first_name, last_name, ssn, weekly_salary):
        super().__init__(first_name, last_name, ssn)
        self._weekly_salary = weekly_salary
    
    @property
    def weekly_salary(self):
        # Getter for weekly salary
        return self._weekly_salary
    
    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        # Setter for weekly salary with validation
        if not weekly_salary >= 0:
            raise ValueError('Weekly salary must be non-negative.')
        self._weekly_salary = weekly_salary
    
    def earnings(self):
        # Returns the earnings for a salaried employee
        return self._weekly_salary
    
    def __repr__(self):
        # String representation of a salaried employee
        return (f'Salaried Employee:\n{super().__repr__()}\n'
                f'Weekly Salary: {self._weekly_salary}\n'
                f'Earnings: {self.earnings()}')


class HourlyEmployee(Employee):
    '''
    Represents an hourly employee who earns based on hours worked and an hourly wage.
    '''
    
    def __init__(self, first_name, last_name, ssn, hours, wages):
        super().__init__(first_name, last_name, ssn)
        self._hours = hours
        self._wages = wages
        
    @property
    def hours(self):
        # Getter for hours worked
        return self._hours
    
    @hours.setter
    def hours(self, hours):
        # Setter for hours worked with validation (must be between 0 and 168)
        if not (hours >= 0 and hours <= 168):
            raise ValueError('Hours must be in range 0-168.')
        self._hours = hours
    
    @property
    def wages(self):
        # Getter for hourly wage
        return self._wages
    
    @wages.setter
    def wages(self, wages):
        # Setter for hourly wage with validation
        if not wages >= 0:
            raise ValueError('Wage per hour must be non-negative.')
        self._wages = wages
    
    def earnings(self):
        # Calculates earnings with overtime pay (time-and-a-half for hours above 40)
        if self._hours > 40:
            overtime_hours = self._hours - 40
            return (40 * self._wages) + (overtime_hours * self._wages * 1.5)
        return self._hours * self._wages
    
    def __repr__(self):
        # String representation of an hourly employee
        return (f'Hourly Employee:\n{super().__repr__()}\n'
                f'Wages: {self._wages}\nHours: {self._hours}\n'
                f'Earnings: {self.earnings()}')