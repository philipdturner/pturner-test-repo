#!/usr/local/bin/python3

class MyClass:
    def __init__(self):
        self.l = []
        self.d = []

    def append_l(self,s):
        self.l.append(s)

    def append_d(self,s):
        self.d.append(s)

m = MyClass()
m.append_l(1)
m.append_l(2)
m.append_d('aaa')
m.append_d('bbb')

print(m.l)
print(m.d)
