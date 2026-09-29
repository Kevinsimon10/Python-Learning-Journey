Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string handling
>>> #concatenation
>>> f_name="lionel"
>>> l_name="messi"
>>> number=10
>>> full_name=(f_name + l_name)
>>> print(f_name + l_name)
lionelmessi
>>> 
>>> #we can change data types for our need
>>> print(f_name + str(number))
lionel10
>>> 
>>> #repeting string
>>> print(full_name*10)
lionelmessilionelmessilionelmessilionelmessilionelmessilionelmessilionelmessilionelmessilionelmessilionelmessi
>>> full_namel="lionel messi"
>>> print(full_namel*10)
lionel messilionel messilionel messilionel messilionel messilionel messilionel messilionel messilionel messilionel messi
>>> print((full_namel.split(" "))*10)
['lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi', 'lionel', 'messi']
