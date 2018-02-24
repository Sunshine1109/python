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

class Mammal(object):
    def mammal(self):
        print('I am mammal')

class Runnable(object):
    def run(self):
        print('I can run')

class Dog(Mammal, Runnable):
    def dog(self):
        print('I am dog')

dog = Dog()
print(dog.dog())
print(dog.mammal())
print(dog.run())

print('\n\n################## 4. 定制类 ######################\n\n')

print('\n## 1. __str__ 和 __repr__ ##\n')
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    __repr__ = __str__

std = Student('xiu')
print(std)

print('\n## 2. __iter__ 和 __getitem__ ##\n')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
for n in Fib():
    print(n)
print(f[10])
print(f[0:5])

print('\n## 2. __getattr__ ##\n ')

class Student(object):
    def __init__(self):
        self.name = 'xiu'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

std = Student()
print(std.score)

print('\n## 3. __call__ ##\n')

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('self call')

std = Student('xiu')
print(std())
print(callable(Student('hong')))

print('\n\n################ 5. 枚举类 ##################\n\n')

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)