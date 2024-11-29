def hello_func():
    pass

hello_func() # call the function 
print(hello_func) # <function hello_func at 0x7f2975b85c60>
print(hello_func()) # None :because not returning any thing with the function.

# return value from function
def hello1():
    return 'Hello Function'
print(hello1().upper()) # HELLO FUNCTION 

# passing argument and default parameter
def hello2(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print(hello2('HI')) # HI, You
print(hello2('HI', 'Corey')) # HI, Corey
print(hello2('HI', name= 'Corey')) # HI, Corey
# passing unorder argument to the function 
print(hello2(name= 'Corey',greeting='HI')) # HI, Corey

# getting argument into one paramenter in the function.
# args:positional argument, kwargs- keyword values 
def student_info(*args, **kwargs):
    print(args)   # ('Math', 'Art') Tuple
    print(kwargs) # {'name': 'John', 'age': 22} Dictionary
student_info('Math', 'Art', name='John', age=22)

# spread argumemts and add as parameters 
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
def student_details(*args, **kwargs):
    print(args) 
    print(kwargs)
student_details(courses, info) # all set as positional arguments
# result:(['Math', 'Art'], {'name': 'John', 'age': 22})
# result:{}
student_details(*courses, **info)
# result:('Math', 'Art')
# result:{'name': 'John', 'age': 22}

