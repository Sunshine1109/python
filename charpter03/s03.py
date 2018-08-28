#!/usr/bin/env python3

class Dog(object):

    def __init__(self, name, color, age):
        self.__name = name
        self.color = color
        self.age = age

    def bat(self):
        print('%s %s %s' % (self.__name__, self.color, self.age))

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

d1 = Dog('dog1', 'red', 2)
d2 = Dog('dog2', 'yellow', 1)
d3 = Dog('dog3', 'black', 4)

print(d1.color)
print(d1.getName())

d1.setName('dog5')
print(d1.getName())
