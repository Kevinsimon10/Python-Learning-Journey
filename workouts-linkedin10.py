Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #patten program
... #square
... for i in range(4):
...     for j in range(4):
...         print('*',end=' ')
...     print()
... 
...     
* * * * 
* * * * 
* * * * 
* * * * 
>>> #RAT
... for i in range(0,6):
...     for j in range(i):
...         print("*",end=" ")
...     print()
... 
...     

* 
* * 
* * * 
* * * * 
* * * * * 
#LAT
for i in range(0,6):
    for j in range (5-i):
        print(" ",end=" ")
    for k in range (i):
        print("*",end=" ")
    print()

    
          
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
#pryamid
for i in range(0,6):
    for j in range (5-i):
        print(" ",end="")
    for k in range (i):
        print("*",end=" ")
    print()

    
     
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
