#!/usr/local/bin/python3

s1: str = 'a'
s2: int = 1
a1 = ['zzz','yyy','xxx','www','vvv']
t1 = ('zzz','yyy','xxx','www','vvv')
d1 = { "fname" : 'Phil', "lname" : 'Turner' }

print('type(s1)',type(s1))
print('s1', s1)
print('type(s2)',type(s2))
print('s2', s2)
print('type(a1)',type(a1))
print('a1',a1)
print('type(t1)',type(t1))
print('t1', t1)
print('type(d1)',type(d1))
print('d1',d1)

print('a1[1]', a1[1])
print("a1[1] = 'aaa'")
a1[1] = 'aaa'
print('a1', a1)

print('t1[1]',t1[1])
try:
    print("t1[1] = 'aaa'")
    t1[1] = 'aaa'
except:
    print('Cannot assign a tuple')
    print('t1[1] is still', t1[1])

d2 = { "fname" : 'Sven', "lname" : 'Eidissen' }
d3 = { 'fname' : 'Pranjal' , 'lname' : 'Suri' }

# Create empty list
a2 = []
# Append our names to that list
a2.append(d1)
a2.append(d2)
a2.append(d3)
# Append a tuple
a2.append((111,222,333))
# Append a list to the list
a2.append([999,888,777])
a2.append(s1)
print(a2)

# Iterate over the list
for e in a2:
    print('type(e)',type(e),'e is',e)
    if isinstance(e,dict) is True:
        for key in e:
            print(key,e[key])
        for key,value in e.items():
            print(key,value)
    if isinstance(e,list) is True:
        for l in e:
            print(l)
        for i in range(len(e) - 1):
            print(i,e[i])
