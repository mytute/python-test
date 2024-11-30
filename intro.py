
# if you write try to open file which does not exist it will break your code.
#f = open(textfile.txt)

# if you wrap the above line with try/except the it will not break the code and just show error message.
try:
    f = open('textfile.txt')
except Exception:
    print('Error happend!')
    
# "Exception" is catch all error. But we can specify the error
# using "FileNotFoundError" only catch if file not found. so catch other error we can put "Exception" too. put 
try:
    f = open('textfile.txt') # error 1
    #var = bad_var          # error 2
except FileNotFoundError:
    print('Sorry, This file does not exist!')
except Exception:
    print('Something went wrong')

# we cant print Exception instead of custom error message
try:
    f = open('textfile.txt') # error 1
    var = bad_var          # error 2
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

# instead read file inside try block, we can read it inside "else" block too.
try:
    f = open('text_file.txt') # correct file name
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

#  "finally" block execute always whether is there exception or not 
try:
    f = open('text_file.txt') # correct file name
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")


# make custom exceptions
try:
    f = open('text_file.txt') # correct file name
    raise Exception('test error..')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")





