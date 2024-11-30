# basic way to import module 
import my_module

# import with alias
import my_module as mm

# import with direct multiple items 
from my_module import find_index, test as t

# import everything
from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index) # result:1
index = mm.find_index(courses, 'Math')
print(index) # result:1
index = find_index(courses, 'Math')
print(index) # result:1

# use of random module 
import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course1 = random.choice(courses)
random_course2 = random.choice(courses)
print(random_course1)
print(random_course2)

# use of math module  
import math
rads = math.radians(90) # 90 degree convert to radian
print(rads)
print(math.sin(rads)) # result:1

# use of datetime module  
import datetime
import calendar
today = datetime.date.today() # get today date
print(today)
print(calendar.isleap(2020)) # result:True check is leap year

# use of os module  
import os
import calendar
print(os.getcwd()) # get current path
print(os.__file__) # see location of any module file
