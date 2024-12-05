# Classes and Instances  

# why we are use classes  
# They allow us to logicallu group our variables and functions way that easy to reuse also easy to build upon it need be.  
# method : function that assosiate with class.  

# show instance variable contain data that unique to each intance  

class Employee:
    pass 

emp_1 = Employee()
emp_2 = Employee()

print(emp_1) # <__main__.Employee object at 0x7fb0b4133380>
print(emp_2) # <__main__.Employee object at 0x7fb0b37e4b90> 

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'samadhivkcom@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

# input employee details when initialize the class and add method for printing full name of employee.     
class Employee2:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee2('Corey', 'Schafer', 50000)
emp_2 = Employee2('Test', 'User', 60000)

print(emp_1.first)
print(emp_2.first)
print(emp_1.fullname())

# show another way to call "fullname" function.  
print(Employee2.fullname(emp_1))
 
