#!/usr/local/bin/python3

c = ['c1', 'c2', 'c3', 'c4']

# my target is
# c1=values(c1),c2=values(c2),c3=values(x3)

t = list(map(lambda x: "%s=values(%s)" % (x,x),c))
print(t)
