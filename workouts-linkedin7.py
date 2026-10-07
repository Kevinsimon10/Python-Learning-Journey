Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#table excercise
for i in range(1,11):
     print("6 *",i,"=",i*6)

6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
>>> for i in range(2,11,2):
...     print('6 *',i,'=',i*6)
... 
...     
6 * 2 = 12
6 * 4 = 24
6 * 6 = 36
6 * 8 = 48
6 * 10 = 60
>>> #TUPLE
>>> l=tuple('kevin')
>>> print(l)
('k', 'e', 'v', 'i', 'n')
>>> print(l.count('a'))
0
>>> print(len(l))
5
>>> #print(l.pop(1))
>>> #here we change tuple to list for pop method
>>> t=list(l)
>>> print(t)
['k', 'e', 'v', 'i', 'n']
t.pop()
'n'
print(t)
['k', 'e', 'v', 'i']
l=tuple(t)
print(l)
('k', 'e', 'v', 'i')
#methods of tuple
#there are only two methods available for tuple
print(l.count('k'))
1
print(l.index('k'))
0
