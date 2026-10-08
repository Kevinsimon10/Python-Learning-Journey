Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#for loop
for i in range(11):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
for i in range(11, 0, -1):
    print(i)

    
11
10
9
8
7
6
5
4
3
2
1
#use "ends with" for this end=" "

for i in range (0,11):
    print(i, end = ' ')

0 1 2 3 4 5 6 7 8 9 10 
#while

i = 1
while i < 9:
    print(i)
    i += 1

    
1
2
3
4
5
6
7
8
>>> i = 1
>>> while i < 9:
...     print(i)
...     i += 1
... 
...     
1
2
3
4
5
6
7
8
>>> else:
...     
SyntaxError: invalid syntax
>>> print("i is no longer less than 9")
i is no longer less than 9
