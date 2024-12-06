#  18 Special (Magic/Dunder) Methods  

# method with duble underscore call "Dunder" methods in python ex: __init__  

class Employee: 
    raise_amount = 1.04  # class variable 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
   
    # repr mean unambiguous representation of the object.  
    # Purpose: Provides an official string representation of an object, mainly for developers.
    # Use Case: Useful for debugging; should ideally return a string that can recreate the object if passed to eval().
    def __repr__(self):
       return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    # str for more readable representation of an object  
    # Purpose: Provides an informal or user-friendly string representation of an object.   
    # Use Case: Intended for end-users and used when print() or str() is called.
    def __str__(self):
      return '{} - {}'.format(self.fullname(), self.email)

    # combine two instance  
    def __add__(self, other):
      return self.pay + other.pay

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

# without __repr__ method will print :  <__main__.Employee object at 0x7ff86ebab380>
print(emp_1) # result : Employee('Corey','Schafer','5000')  
# after add __str__ method  
print(emp_1) # result : Corey Schafer - Corey.Schafer@company.com


print(emp_1.__repr__()) # result :Employee('Corey','Schafer','5000')  
print(emp_1.__str__())  # result :Corey Schafer - Corey.Schafer@company.com  

# let's see another Dunder methods  
print(int.__add__(1,2)) # result: 3  
print(str.__add__('a', 'b')) # result: ab  

# use of __add__ in class for combine two instance  
print(emp_1 + emp_2) # result : 11000 
