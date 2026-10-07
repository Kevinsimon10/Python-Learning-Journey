Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set
>>> #unordered collection and values are unindexed
... 
>>> #it stores values based on Hashable
... s={5,7,2,1,4,3}
>>> print(s)
... 
{1, 2, 3, 4, 5, 7}
>>> #set not allow duplicate values
... 
>>> ss={2,3,4,4,5,5,6}
... 
>>> print(ss)
{2, 3, 4, 5, 6}
>>> #pop works as first in first out
>>> s.pop()
... 
1
>>> print(s)
... 
{2, 3, 4, 5, 7}
>>> s.add(0)
... 
print(s)

{0, 2, 3, 4, 5, 7}
d={7,2,8,5,3,9}

print(d)

{2, 3, 5, 7, 8, 9}
z={'h', 'e', 'l', 'o', 'i'}

print(z)

{'l', 'i', 'o', 'h', 'e'}
#Dictionary

d = {"Brand": "Rusteze","Model": "LightningMcqueen","year": 2006,"year": 2016}
print(len(d))
3
#Add new item to Dictionary
d['city'] = 'chennai'
d.update({"year":2011})
print(len(d))
4
#overwrite key's value with maverick
d['Model']='chevrolet corvette c6'
print(d)
{'Brand': 'Rusteze', 'Model': 'chevrolet corvette c6', 'year': 2011, 'city': 'chennai'}
#overwright key year2 with year?
d['year2']=d.pop('year')
print(d)
{'Brand': 'Rusteze', 'Model': 'chevrolet corvette c6', 'city': 'chennai', 'year2': 2011}
