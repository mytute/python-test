
#  Closure is a combination of a function and the lexical environment within which that function was declared.


# first class functions allow us to treat functions like any other object. like asign function to variable and return a function.  
# closures allow us to take advantage of first-class function, that return a function and remembers and has access to variables local to the scope in whicj they were created. 


def outer_function():
    message = 'HI'

    def inner_function():
        print(message)
    return inner_function() # execute inner function here.  

outer_function() # result : "HI"

# instead of excute innert function let's return inner function to excute later.   
def outer_function1():
    message = 'HI'

    def inner_function():
        print(message)
    return inner_function # not execute inner function but just returning.  

my_func = outer_function1() 
my_func() # result : "HI"

# let's pass the argument instead of hard code "message" variable  
def outer_function2(msg):
    message = msg 

    def inner_function():
        print(message)
    return inner_function # not execute inner function but just returning.  

hi_func = outer_function2('Hi') 
bye_func = outer_function2('Bye') 
hi_func() # result : 'Hi'
bye_func() # result : 'Bye'

# Decorators are very similar to above. Decorators are is a function that get another function as a argument add some kind of functionality and return function.  

# write basic example of decorator function.  
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

# just convert above example to working example   
def decorator_function1(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function1(display)
decorated_display()

# here without modifying our original display function, can some inside of our wrapper and add any kind of code that you want.  
def decorator_function2(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display1():
    print('display function ran')

decorated_display = decorator_function2(display1)
decorated_display()

# use decorator symbol to do same function above.  
def decorator_function3(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function3 # add decorator here instead of pass "display2" function in to "decorator_function3".  
def display2():
    print('display function ran')

display2()

# let's write docorator funtion that can use for multiple methods when they have different type and count of arguments.  

def decorator_function4(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function4 
def display4():
    print('display function ran')


@decorator_function4 
def display_info(name, age):
    print('infor function ran')


display4()
display_info('John', 30)

# let use classes as decorators instead of using functions.  
# do that you need to add __init__ and __call__ functions in the decorator class   
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call method execute this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class 
def display5():
    print('display function ran')


@decorator_class 
def display_info5(name, age):
    print('infor function ran {}, {}'.format(name, age))


display5()
display_info5('John', 30)

# let's write practical example for decorators(logger function call )  
# after run following code it will create file name "display_info6.log" file and this way you can create log file for any function in easy way.  
def my_logger(orig_func):
    import logging 

    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info6(name, age):
    print('info function ran {}, {}'.format(name, age))
    
display_info6('Mika', 35)

# let's see another practical example for decorators (timeing how long to function to run)    
def my_timer(orig_func):
    import time 

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__ , t2))
        return result
    return wrapper

import time 

@my_timer
def display_info7(name, age):
    time.sleep(1)
    print('info function ran {}, {}'.format(name, age))

display_info7('Lak', 40)

# let's see how to add multiple decorators to the one function.  

''' 
if we put decorators in following way > 
@my_timer
@my_logger
def display_info7(name, age):
    time.sleep(1)
    print('info function ran {}, {}'.format(name, age))
 
it mean >
result = my_timer(my_logger(display_info7))
my_logger function return 'wrapper' function so getting wrong result or not working properly 
so for that we can use "functools" to wrap "wrapper" function for each decorator function.  
'''

from functools import wraps 

def my_logger1(orig_func):
    import logging 

    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

    

def my_timer1(orig_func):
    import time 

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__ , t2))
        return result
    return wrapper

@my_logger
@my_timer
def display_info8(name, age):
    time.sleep(1)
    print('info function ran {}, {}'.format(name, age))

display_info8('Lak', 45)

# let's see how to create decorators that accept arguments 
# for that you need to wrap decorator function with prefix function   

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Execute Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Execute After', original_function.__name__)
            return result
        return wrapper_function 
    return decorator_function 

@prefix_decorator('LOG:')
def display_info9(name, age):
    print('display info 9 ran with arguments {} {}'.format(name, age))
            
display_info9('Sam', 10)
display_info9('Dhi', 20)
