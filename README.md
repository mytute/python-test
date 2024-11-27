# Install and Setup   

1. to check is python already installed for your operating system in the terminal.  
```bash 
$ python --version
```

2. If your computer has both Python 2 and Python 3 installed, the command python typically runs Python 2 by default. To make python point to Python 3 instead of using python3, you can set an alias in your shell configuration file.  
```
$ nvim ~/.bash_profile
```
> /.bash_profile  
```bash 
alias python="python3"
```

3. to open interactive prompt in python.   
```bash 
$ python  

>>> print('Hello World')
Hello World
>>> x = 10
>>> print(x)
10
>>> exit()
```
and above allow write one line of python at a time. and this good only for testing python commands.  

4. we want to have a python file where we can write multiple lines and run an entire scripts.   
for that install "IDLE3" for fedora.  
in the "IDLE3" go to "File"> "New File" to create file that insert multiple lines of python code.  

4.1 in the new file, type the following Python code:
```python
print('Hello World')
```
4.2 Save the File  
Save the file by going to File > Save As.  
Name the file intro.py and choose a directory to save it. Make sure to add the .py extension.  

4.3 Run the Script  
Press F5 (or go to Run > Run Module) to execute the script.  
The output (Hello, World!) will appear in the IDLE3 shell.  

and save as "intro.py" and press the "F5"(Run Module) to run the file.   

