#!/usr/bin/env python3

class Animal(object):

    # 允许绑定的属性名称 
    __slots__ = ("name", "age", "color")

    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
cat = Animal("cat", 2)
print(cat.age)

cat.color = "red"
print(cat.color)

# def set_age(self, age):
#     self.age = age

# # 增加方法
# from types import MethodType
# cat.set_age = MethodType(set_age, cat)

# cat.set_age(3)
# print(cat.age)

# # 给class添加方法
# Animal.set_age = set_age
# cat3 = Animal("cat3", 1)
# cat3.set_age(4)
# print(cat3.age)
