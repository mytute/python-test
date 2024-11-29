
# show hardcoded if condition with 'True' and 'False'
if True:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print('Conditional was True') 

# Comparisons:
# Equal            ==
# Not Equal        !=
# Greater Than     >
# Less Than        <
# Greater or Equal >=
# Less or Equal    <=
# Object Identity  is

# show if/else conditional check  
language = 'Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# show multiple if/else/elseif conditional check  
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# Boolean operations
# and
# or
# not

user = 'Admin'
logged_in = False

if not logged_in:
    print('please logged in')
elif logged_in and user == 'Admin':
    print('Admin page')
elif logged_in and (user != 'Admin'):
    print('User page')
else:
    print('Welcome page')

# show different between "==" and "is"

a = [1,2,3]
b = [1,2,3]
c = a

print(a == b) # true
print(a is b) # false  because these are two different objects in memory

# show with memory id
print(id(a))
print(id(b))
print(id(a) == id(b)) # False
print(id(a) == id(c)) # True bacause of referance 


# Flase Values:
  # False
  # None
  # Zero of any numeric type
  # Any empty sequence. For exmaple, '', (), []
  # Any empty mapping. For exmaple, {}

condition = False # None, 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')























