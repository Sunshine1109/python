#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n################# 1. 使用__slots__ #############\n\n')
class Student(object):
    def __init__(self, name):
        self.name = name

std1 = Student('xiuhong')
std1.score = 100
std2 = Student('muqian')
print(hasattr(std1, 'score')) # True
print(hasattr(std2, 'score')) # True
print(std1.score) # 100

from types import MethodType
def set_score(self, score):
    self.score = score

std1.set_score = MethodType(set_score, std1)
std1.set_score(101)
print(std1.score)
# print(std2.score) # AttributeError

# 给class 添加方法
def set_class(self, classname):
    self.classname = classname
Student.set_class = set_class

std1.set_class('a3-7')
std2.set_class('a3-8')

print(std1.classname)
print(std2.classname)


class Student(object):
    __slots__ = ('name', 'age')

std1 = Student()
std1.name = 'xiuhong'
print(std1.name)

# std1.  = 97 # AttributeError
# print(std1.score)

# __slots__对继承类不起作用
class BadStudent(Student):
    def bad():
        print('I\'m bad boy')

std2 = BadStudent()
std2.score = 0
# print(dir(std2))
print(std2.score)


print('\n\n################### 2. property #######################\n\n')

class Student(object):
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an iteger')
        if value < 0 or value > 100:
            raise ValueError('score muste between 0 ~ 100')
        self._score = value
    
std = Student()
std.score = 90
print('score', std.score)


print('\n\n################### 3. 多重继承 ######################\n\n')

