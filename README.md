# Dictionaries - Working with Key-Value Pairs  

```python 
student = { 1:'index', 'name': 'Jhone', 'age': 25, 'courses':['Math', 'CompSci']}
print(student)
print(student['name']) # Jhone access by key(string)
print(student['courses']) # ['Math', 'CompSci'] access by key
print(student[1]) # 'index' access by key(number)

# use get method to not to return error when key is not existed
print(student.get('name')) # Jhone
print(student.get('return none')) # None
# set default value if value not exited
print(student.get('return none', 'not found')) # not found

# add new key value
student['phone'] = '555-5555'
print(student.get('phone', 'Not found')) # 555-5555

# add and edit multiple values in the dictionary using update method
student.update({'name': 'Mosh', 'age': 26, 'phone': '123456'})
print(student) # {1: 'index', 'name': 'Mosh', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '123456'}

# delete key and value using del method
del student[1]
print(student)

# delete key value using pop method
age = student.pop('age')
print(age) # 26
print(student) # {'name': 'Mosh', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '123456'}

# loop key-value in the dictionary
student = {'name': 'Jhone', 'age': 25, 'courses':['Math', 'CompSci']}

print(len(student)) # 3 get size of dictionary
print(student.keys()) # dict_keys(['name', 'age', 'courses'])
print(student.values()) # ict_values(['Jhone', 25, ['Math', 'CompSci']])
# show keys and values 
print(student.items()) # dict_items([('name', 'Jhone'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# loop keys
for key in student:
    print(key) #  'name', 'age', 'courses'

# loop values and kyes 
for key, value in student.items():
    print(key, value) name Jhone, age 25, courses ['Math', 'CompSci']
```
