Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string handling
>>> name='String handling'
>>> print(name.upper())
STRING HANDLING
>>> print(name.lowe())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(name.lowe())
AttributeError: 'str' object has no attribute 'lowe'. Did you mean: 'lower'?
>>> print(name.lower())
string handling
>>> print(name.strip())
String handling
>>> print(name.replace('S','T'))
Ttring handling
>>> 
>>> #negative indexing and slicing
>>> print(name[-1])
g
>>> print(name[-15])
S
>>> print(name[:-1])
String handlin
print(name[-15:-7])
String h
