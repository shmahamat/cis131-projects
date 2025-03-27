class Employee:
    
    '''
    '''
    
    def __init__(self,first_name,last_name,ssn):
        
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.ssn}'

#employee = Employee('John','Deer',123)

print(repr(employee))