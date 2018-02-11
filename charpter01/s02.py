#!/usr/bin/env python3

print('\n\n################ 1. 切片 ###################\n\n')
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('初始数组：', L, '\n')
print('\n## 1. 取前三个元素 ## \n')
print(L[0:3]) # 从索引0开始取，直到索引3为止，但不包括索引3

print('\n## 若果第一个索引是0，还可以省略 ##\n')
print(L[:3]) 

print('\n## 从索引1开始，取出两个元素 ##\n')
print(L[1:3])

print('\n## 支持取倒数第x个元素 ##\n')
print(L[-1]) # ['Jack']
print(L[-2:]) # ['Bob', 'Jack']
print(L[-2:-1]) # ['Bob']

print('\n## 数列 ##\n')
L = list(range(100))

# 5.1 取出前10个
print(L[:10])

# 5.2 取出后10个
print(L[-10:])

# 5.3 取出前11 - 20个
print(L[10:20])

# 5.4 前10个，每两个取一个
print(L[:10:2])

# 5.5 全部数，每5个取一个
print(L[::5])

# 5.6 复制一个list
print(L[:])

# tuple操作的结果仍为tuple
print((1, 2, 3, 4, 5)[:3]) # (0, 1, 2)

# 字符串也可以看成是一种list，每个元素就是一个字符
print('ABCDEFG'[:3]) # ABC
print('ABCDEFG'[::2]) # ACEG


print('\n\n################ 2. 迭代 ###################\n\n')
d = {'a': 1, 'b': 2, 'c': 3}
print('## 迭代key ##\n')
for key in d:
    print(key)

print('\n## 1.1 迭代value ##\n')
for value in d.values():
    print(value)

print('\n## 1.2 迭代key和value ##\n')
for k, v in d.items():
    print(k, '=', v)

print('\n## 1. 3迭代字符串 ##\n')
for ch in 'ABC':
    print(ch)

print('\n## 判断一个对象是否可迭代 ##\n')
from collections import Iterable
print(isinstance('abc', Iterable)) # True
print(isinstance([1, 2, 3], Iterable)) # True
print(isinstance(123, Iterable)) # False

print('\n## 1.5 下表循环 ##\n')
for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)

print('\n## 1.6 同时引入两个变量 ##\n')
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)


print('\n\n################ 3. 列表生成式 ###################\n\n')

print('\n## 1. 生成1-10的list ##\n')
print(list(range(1, 11)))

print('\n## 2. 生成[1x1, 2x2, 3x3, ..., 10x10] ##\n')
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print('\n# 2.1 简洁方法 ##\n')
print([x * x for x in range(1, 11)])

print('\n# 2.2 添加过滤筛选 #\n')
print([x * x for x in range(1, 11) if x % 2 == 0])

print('\n# 3. 两层循环 #\n')
print([m + n for m in 'ABC' for n in 'XYZ'])

print('\n# 4. 输出当前目录下文件名 #\n')
import os
print([d for d in os.listdir('.')])

print('\n# 5. 可同时使用两个或更多个变量 #\n')
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    print(key, '=', value)
 
print('\n# 5.1 简洁写法 #\n')
print([key + '=' + value for key, value in d.items()])

print('\n# 5.2 把list中所有字符串变成小写 #\n')
L = ['Hello', 'World', 'IBM']
print([s.lower() for s in L]) # ['hello', 'world', 'ibm']