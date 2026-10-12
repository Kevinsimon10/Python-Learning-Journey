Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # functions
>>> def functions():
...     print('this is function')
... 
...     
>>> functions()
this is function
>>> # functions with parameter and arguments
>>> def my_function(fname):
...     print(fname + 'son')
... 
...     
>>> my_function("A")
Ason
>>> my_function("B")
Bson
>>> my_function("C")
Cson
>>> # functions with difference between print and return
... # print (simply prints what's inside that)
>>> def add_with_print(a, b):
...     print(a + b)
... 
    
x = add_with_print(10, 20)
30
print(x)  # This will print None because the function does not use 'return'
None
# return (return value to function mean to 'parameter' and
# value come when function called)
def add_with_return(a, b):
    return a + b

y = add_with_return(10, 20)
print(y)  # This will print 30
30

def check_number(n):
        if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
        if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    
SyntaxError: expected an indented block after 'if' statement on line 2
else:
        return "Zero"
    
SyntaxError: invalid syntax

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

    

print(check_number(10))
print(check_number(-5))
print(check_number(0))
SyntaxError: multiple statements found while compiling a single statement
print(check_number(10))
Positive
print(check_number(-5))
Negative
print(check_number(0))
Zero
