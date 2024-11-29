# Loops and Iterations - For/While Loops  

```python 
nums = [1, 2, 3, 4, 5]

# "break" statement break out of the loop

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
# result:  1 2 Found!

# "continue" statement skip the next iteration.  

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
# result:  1 2 Found! 4 5


# loop with in the loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range keyword in loop
for i in range(10): # default range for 10 is 0 to 9
    print(i) 
# result:  0 1 2 3 4 5 6 7 8 9

for i in range(1,10): # set start value of range as 1
    print(i) 
# result: 1 2 3 4 5 6 7 8 9


# "while" loop just keep going until certain condition is met or until we hit break
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
# result 0 1 2 3 4
```
