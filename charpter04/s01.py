#!/usr/bin/env python3

# -*- coding: utf-8 -*-

print('\n\n###################### 1. 类和实例 #####################\n\n')
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

std = Student('xiuhong', 99)
std.print_score()

print('\n\n###################### 2. 访问限制 ###################\n\n')

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))

std = Student('xiuhonglee', 88)
std.print_score()


print('\n\n###################  3. 继承和多态 ####################\n\n')

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def runTwice(animal):
    animal.run()
    animal.run()

animal = Animal()
dog = Dog()
cat = Cat()

runTwice(animal)
runTwice(dog)
runTwice(cat)

print('\n\n################# 判断对象类型 ###################\n\n')
# 1.判断对象类型
print(type(123)) # <class 'int'>
print(type('str')) # <class 'str'>
print(type(None)) # <type(None) 'NoneType'>

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

print(type(Student)) # <class 'type'>

std = Student('xiuhong', 77)
print(type(std)) # <class '__main__.Student'>

import types
def fn():
    pass

# 2. 判断对象是否是函数
print(type(fn) == types.FunctionType) # True
print(type(abs) == types.BuiltinFunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print(type(x for x in range(10)) == types.GeneratorType) # True

# getattr() / setattr() / hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # True
print(hasattr(obj, 'y')) # False

setattr(obj, 'y', 10)
print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404)) # 如果没有z，返回默认值404
