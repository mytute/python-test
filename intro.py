#  17 Inheritance - Creating Subclasses

# inheritance allow us to inherit attribute and methods from a parent class.  

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

class Developer(Employee):
    pass

dev_1 = Developer('Corey', 'Schafer', 5000)
dev_2 = Developer('Test', 'User', 6000)

print(dev_1.email)
print(dev_2.email)

# show how to find method "resolution order"    
# there are the places that python serarches attributes methods  
print(help(Developer)) # result: Developer > Employee > builtins.object


# in above example when init the "Developer" class it automatically call the it parent "Employee" class and it "init" method. let's see what we can do when we want to add some values to child "Developer" class when we init the "Developer" class.  

class Developer2(Employee):
    raise_amt = 1.10 # this not effect to parent class  

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # following method also same for above "super" method  
        # but following method usually use for when we have multiple inheritance
        # Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang 


dev_1 = Developer2('Corey', 'Schafer', 5000, 'Python')
dev_2 = Developer2('Test', 'User', 6000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

# let's see another exmaple of inheritance of "Employee"  

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else: 
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer2('Corey', 'Schafer', 5000, 'Python')
dev_2 = Developer2('Test', 'User', 6000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1]) # create manager instance with developer instance as employees  

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


# python has these two built in functions called "isinstance" and "issubclass"   
print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer2)) # False


print(issubclass(Manager, Employee)) # True
print(issubclass(Developer2, Employee)) # True
print(issubclass(Manager, Developer2)) # False
