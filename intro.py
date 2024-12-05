# classmethod and staticmethod    

# regular methods in a class automatically take the instance (self) as the first argument, but in the class methods it take class as first argument.   

class Employee: 
    raise_amount = 1.04
    num_of_emps = 0 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # regular method 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class method  
    # in class method first argument is class. 
    @classmethod
    def set_raise_amt(cls, amount):
       cls.raise_amount = amount 

    # using classmethod we can return new instance within class  
    @classmethod 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method  
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True



emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

# let's see easy way to input employee details  
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# using class method do Employee.raise_amount = amount  in differant way   
Employee.set_raise_amt(1.05)

print(Employee.raise_amount) # result: 1.05
print(emp_1.raise_amount) # result: 1.05
print(emp_2.raise_amount) # result: 1.05


# show we can call class methods using instance and do same thing  

emp_1.set_raise_amt(1.06)

print(Employee.raise_amount) # result: 1.06
print(emp_1.raise_amount) # result: 1.06
print(emp_2.raise_amount) # result: 1.06

# show using classmethod we can create new instance and return inside class  
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)


# static method don't pass anything to the method automatically 
# you should write regularmethod or classmethod only that method has connection with class variables.  
# if you don't access instance or the class anywhere with in the method 

import datetime 
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date)) # result: False  

