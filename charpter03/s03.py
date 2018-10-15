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

class GoldDog(Dog):
    def __init__(self, name, color, age, favorite):
        Dog.__init__(self, name, color, age)
        self.favorite = favorite;

    def eat(self):
        print('jingmao is eating %s' % self.favorite)

gold1 = GoldDog('jinmao', 'yellow', 3, 'meat')
print('gold1 name is %s' % gold1.getName())
print('gold1', gold1.favorite)


d1 = Dog('dog1', 'red', 2)
d2 = Dog('dog2', 'yellow', 1)
d3 = Dog('dog3', 'black', 4)

print(d1.color)
print(d1.getName())

d1.setName('dog5')
print(d1.getName())
abs(-12)