# Class Variables  

# class variables works like 'static' keyword in java  

class Employee: 
    raise_amount = 1.04  # class variable 
    num_of_emps = 0 # class variable that increment for each instance created  

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # another way to access class variables 
        # self.pay = int(self.pay * Employee.raise_amount)
        # if you use Employee then surely it same for all instance

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# show raise_amount value of class and each instance

print(Employee.raise_amount) # result: 1.04
print(emp_1.raise_amount) # result: 1.04
print(emp_2.raise_amount) # result: 1.04

# show attributes of instance and class for find where class variable is located   
# print namespaces for instance and class  
print(emp_1.__dict__) # not contain 'raise_amount' 
print(emp_2.__dict__) # not contain 'raise_amount'
print(Employee.__dict__) # contain 'raise_amount'
        
# change the raise_amount value in the class from outside and show all instance change value it self  
Employee.raise_amount = 1.05
print(Employee.raise_amount) # result: 1.05
print(emp_1.raise_amount) # result: 1.05
print(emp_2.raise_amount) # result: 1.05

# insert raise_amount value in to instance and show after that instance use only it's value.  
# first program look 'raise_amount' inside instance if there not contain the see the class   
emp_1.raise_amount = 1.06
print(Employee.raise_amount) # result: 1.05 
print(emp_1.raise_amount) # result: 1.06
print(emp_2.raise_amount) # result: 1.05

# check increment count of instance  
print(Employee.num_of_emps) # result: 2

