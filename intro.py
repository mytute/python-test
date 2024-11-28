
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# check length of list
print(len(courses)) # 4

# access values individually (index start at 0)
print((courses[1])) # 'Math'
print((courses[-1])) # 'CompSci' last item

# access rage of values  
print((courses[0:2])) # ['History', 'Math']
print((courses[:2])) # ['History', 'Math'] from start to 2nd item  
print((courses[2:])) # ['Physics', 'CompSci'] from 2nd to end item

# ** list methods for modify lists **

# add item to end of list
courses.append('Art')
print(courses) # ['History', 'Math', 'Physics', 'CompSci', 'Art']

# add item to specific location of list
courses.insert(0,'Art') # add to index 0
print(courses) # ['Art', 'History', 'Math', 'Physics', 'CompSci', 'Art']

# add item with extend method (work like spread operators to concad list)
courses_1 = ['History', 'Math']
courses_2 = ['Physics']
courses_1.extend(courses_2) # add to index 0
print(courses_1) # ['History', 'Math', 'Physics']

# remove item from list
courses.remove('Math')
print(courses) # ['Art', 'History', 'Physics', 'CompSci', 'Art']

# remove list item from list
popped = courses.pop() # return a value that removed
print(courses) # ['Art', 'History', 'Physics', 'CompSci']

# change order
courses.reverse()
print(courses) # ['CompSci', 'Physics', 'History', 'Art']
courses.sort() # alphabetical order
print(courses) # ['Art', 'CompSci', 'History', 'Physics']

nums = [1,5,2,4,3]
nums.sort() # sorting ascending order
print(nums)
nums.sort(reverse=True) # sorting descending order
print(nums)
sorted = sorted(nums) # sort without altering the original list

# min max and sum
print(min(nums)) # 1
print(max(nums)) # 5
print(sum(nums)) # 15

# find values in the list
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('Math')) # return index of the list value. 
# print(courses.index('Art')) # if not in the list show error
print('Art' in courses) # check whether value included or not

# loops with list
courses = ['History', 'Math', 'Physics', 'CompSci']

for course in courses:
    print('loop ' + course)
    
# loop with index
for index, course in enumerate(courses):
    print(index, course)

# convert list in to string
courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ', '.join(courses)
print(course_str) # History, Math, Physics, CompSci

# convert seperated string in to list
seperated_str = 'History, Math, Physics, CompSci'
new_list = seperated_str.split(',')
print(new_list) # ['History', ' Math', ' Physics', ' CompSci']



list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art' # this change 'list_2' value too.
print(list_2) # ['Art', 'Math', 'Physics', 'CompSci']

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
# tuple_1[0] = 'Art' # show error !!!! because of Immutability 
print(tuple_1)
new_tuple = ('Art',)
tuple_1 = tuple_1 + new_tuple # not changing tuple_2
print(tuple_1)
print(tuple_2)



# Sets

courses = {'History', 'Math', 'Physics', 'CompSci'}
print(courses) # {'Math', 'CompSci', 'Physics', 'History'} order can change each execution. 

courses = {'History', 'Math', 'Physics', 'CompSci',  'Math'}
print(courses) # {'Math', 'History', 'CompSci', 'Physics'}

# set are optimize for finding valaues
print('Math' in courses)

# set with another set
set_1 = {'History', 'Math', 'Physics', 'CompSci'}
set_2 = {'Art', 'Math', 'CompSci'}

print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))












