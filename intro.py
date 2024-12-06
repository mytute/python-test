#  19 Property Decorators - Getters, Setters, and Deleters     


class Employee: 

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self._email = first + '.' + last + '@company.com'


    def _fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first , last = name.split(' ')
        self.first = first
        self.last = last

    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None

emp_1 = Employee('Corey', 'Schafer')

# show after changing name it not changed the email address name  
emp_1.first = 'Jim'  
print(emp_1.first) # result: Jim 
print(emp_1._email) # result: Corey.Schafer@company.com
print(emp_1._fullname()) # Jim Schafer   

# using property decorator allow us to define method but we can access it like attribute.  
# to define getter you have to use @Property decorator  
print(emp_1.email) # result: Jim.Schafer@email.com 


# update value using setter(for this you need to add getter first)   
# for update we have to use function name dot setter as decorator name   
emp_1.fullname = 'Samadhi Laksahan' # call setter
print(emp_1.fullname)
print(emp_1.email)

# delete value using deleter  
del emp_1.fullname # call deleter
print(emp_1.fullname)
print(emp_1.email)




