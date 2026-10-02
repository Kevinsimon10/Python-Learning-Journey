Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #LIST
>>> players=['messi','lewandowski','kane','foden']
>>> print(players)
['messi', 'lewandowski', 'kane', 'foden']
>>> print(type(players))
<class 'list'>
>>> 
>>> #INDEXING LIST
>>> print(players[2])
kane
>>> print(players[-4])
messi
>>> 
>>> #CHANGING LIST
>>> players[1]='busquets'
>>> print(players)
['messi', 'busquets', 'kane', 'foden']
>>> players[1:3]='messi','syarez','xavi'
>>> print(players)
['messi', 'messi', 'syarez', 'xavi', 'foden']
>>> players.insert(3,'xavi')
>>> print(players)
['messi', 'messi', 'syarez', 'xavi', 'xavi', 'foden']
players.append('iniesta')
print(players)
['messi', 'messi', 'syarez', 'xavi', 'xavi', 'foden', 'iniesta']
players.remove('xavi')
print(players)
['messi', 'messi', 'syarez', 'xavi', 'foden', 'iniesta']
players.pop()
'iniesta'
print(players)
['messi', 'messi', 'syarez', 'xavi', 'foden']
players.sort()
print(players)
['foden', 'messi', 'messi', 'syarez', 'xavi']
