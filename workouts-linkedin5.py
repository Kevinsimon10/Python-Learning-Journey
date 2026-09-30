Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string formatting
>>> #manual formatting
>>> name='leo'
>>> age=38
>>> age=38
>>> print ("name is {0} and age is {l}".format (name,age))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print ("name is {0} and age is {l}".format (name,age))
KeyError: 'l'
>>> print ("name is {0} and age is {1}".format (name,age))
name is leo and age is 38
>>> #automated formatting
>>> print("name is %s and age is %s"%(name,age))
name is leo and age is 38
>>> print("name is",name,"age is",age)
name is leo age is 38
