# 11 Generators  


1. convert following function in to generator function that function return result for each call.  
```python 
def square_numbers(nums):
    result = [] 
    for i in nums:
        result.append(i*i)
    return result 

my_nums = square_numbers([1,2,3,4,5]) 
print(my_nums) # [1, 4, 9, 16, 25] 
```

converted function   
```python 
def square_numbers_gen(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers_gen([1,2,3,4,5]) 
print(my_nums) # <generator object square_numbers_gen at 0x7fa93a7eaa80> 

# generators don't hold the entire result in memory, it yield one result at a time 
print(next(my_nums))    # result: 1 
print(next(my_nums))    # result: 4
print(next(my_nums))    # result: 9
print(next(my_nums))    # result: 16
print(next(my_nums))    # result: 25
# print(next(my_nums)) error 

# print generator value using for loop   
my_nums_for = square_numbers_gen([1,2,3,4,5]) 
for num in my_nums_for:
    print(num)
```

2. convert above square function in to list comprehension and after convert it in to generator.     
```python
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)
# convert above list comprehension in to generator  
my_nums_list = (x*x for x in [1,2,3,4,5])
for num in my_nums_list:
    print(num)

# show how to printout all of the values of the generator   
my_nums_list = (x*x for x in [1,2,3,4,5])
print(list(my_nums_list)) # [1, 4, 9, 16, 25]
```

