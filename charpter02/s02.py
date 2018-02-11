#!/usr/bin/env python3

print('\n\n ####################### 函数式编程 #########################\n\n')

print('\n## 1. 高阶函数 ##\n')
print('\n1. map \n')

def f(x):
    return x * x
r = map(f, [1, 2, 3])
print(list(r))
# map返回的对象是Iterator

print('\n## 2. reduce ##\n')
from functools import reduce
def add(a, b):
    return a + b
    
print(reduce(add, [1, 2, 3]))

print('\n## 3. filter ##\n')
def is_odd(n):
    return n % 2 == 0
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

print('\n## 4. sorted ##\n')
# 默认排序(小-大)
print(sorted([22, 10, -12, 20]))

# 绝对值排序
print(sorted([22, 10, -12, 20], key=abs))

# 忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))