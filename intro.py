# Namedtuple - When and why should you use namedtuples


# show how to use tuple like dictionary but keeping data format  

# normal way to define tuple  
color = (55,155,255)
print(color[1]) # by indexing not clear what is happening here  

# using dictionary   
color = { 'red': 55, 'green':155, 'blue': 255}
print(color)

# using nametuple
from collections import namedtuple 

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)

print(color[1])
print(color.green)
