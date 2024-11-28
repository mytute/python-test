# Wroking with Textual Data.  

textual data in python are represented with "strings"  
Snake case is commonly used to create descriptive variable and method names in Python.  

1. show how to define string variable and print it.    
```python 
message = 'Hello World' 
print(message)
```

for string difference between the single quotes and double quotes it really just depends on what text you have in your string.   

2. if your string have single quote then show how to handle it without getting error.  
```python 
message1 = 'Bobby\'s World' # using escape carector.  
message2 = "Bobby's World" # using double quotes. 
```

3. if your string have double quote then show how to handle it without getting error.  
```python 
message1 = "Bobby \"A\" World" # using escape carector.  
message2 = 'Bobby "A" World' # using single quotes. 
```

4. show how to define multi-line string.  
```python 
message = """Bobby's World was a good 
cartoon in the 1990s"""
```

5. show how to find how many characters are in the string.  
```python 
message = 'Hello World' 
print(len(message)) # 11
```

6. show how to access strings characters individually.  
```python 
message = 'Hello World' 
print(message[0]) # H 
print(message[10]) # d 
print(message[11]) # showing index error 
# showing rage of characters [includ, exclude] 
print(message[0:4]) # Hell 
# by default start from and end to.  
print(message[:4]) # Hell 
print(message[6:]) # World 
```

7. show string method with strings.     
```python 
message = 'Hello World' 

print(message.lower()) #  
print(message.upper()) # 

# how many 'Hello' matches are in 'message' string.  
print(message.count('Hello')) # 1
print(message.count('l')) # 3 

# find located starting index of the string. 
print(message.find("World") # 3 
print(message.find("Universe")) # -1 (not found) 

# replace characters not effected to original string.   
print(message.replace('World', 'Universe')) # Hello Universe  
print(message) # Hello World
message = message.replace('World', 'Universe')
print(message) # Hello Universe
```

8. show string concadination.   
```python 
greeting = 'Hello' 
name = 'Michael' 
# with plus sign operator  
message = greeting + ', ' + name;
print(message) # Hello, Michael  
# with fomatted way   
message = '{}, {}'.format(greeting, name) # Hello, Michael
# with fstring way  
message = f'{greeting}, {name}' # Hello, Michael
```

9.   

```python 
message = 'Hello World'
print(dir(message)) # show all of the attributes and method that can access.  
print(help(str)) # show more details of string (str) class
```


