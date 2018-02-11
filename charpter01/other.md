#### 高级特性

```shell
# 切片
# 迭代
# 列表生成式
# 生成器
# 迭代器
```

#### 1. 切片

> 操作数组list或tuple

```py
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 1. 取前三个元素
print(L[0:3]) # 从索引0开始取，直到索引3为止，但不包括索引3

# 2. 若果第一个索引是0，还可以省略
print(L[:3]) 

# 3. 从索引1开始，取出两个元素
print(L[1:3])

# 4. 支持取倒数第x个元素
print(L[-1]) # ['Jack']
print(L[-2:]) # ['Bob', 'Jack']
print(L[-2:-1]) # ['Bob']

# 5. 数列
L = list.(range(100))

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
```

#### 2. 迭代

> 给定一个list或tuple，可以通过for循环来遍历这个list或tuple，这种遍历成为迭代

```py
# 1. 语法: 通过for...in实现
d = {'a': 1, 'b': 2, 'c': 3}
for key in b:
    print(key)

# 1.1 迭代value
for value in d.values():
    print(value)

# 1.2 迭代key和value
for k, v in d.items:
    print(k, '=', v)

# 1.3 迭代字符串
for ch in 'ABC':
    print(ch)

# 1.4 判断一个对象是否可迭代
from collections import Iterable
isinstance('abc', Iterable) # True
isinstance([1, 2, 3], Iterable) # True
isinstance(123, Iterable) # False

# 1.5 下表循环
for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)

# 1.6 同时引入两个变量
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)
```

#### 3. 列表生成式

> 列表生成，用来创建list

```py
# 1. 生成1-10的list
print(list(range(1, 11)))

# 2. 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.appedn(x * x)
print(L)

# 2.1 简洁方法
print([x * x for x in range(1, 11)])

# 2.2 for循环后面可以加if判断，可以用做筛选
print([x * x for x in range(1, 11) if x % 2 == 0])

# 3. 两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 4. 输出当前目录下文件名
import os
print([d for d in os.listdir('.')])

# 5. 可同时使用两个或更多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in d.items():
    print(key, '=', value)
 
# 5.1 简介写法
print(key + '=' + value for key, value in d.items())

# 5.2 把list中所有字符串变成小写
L = ['Hello', 'World', 'IBM']
print([s.lower() for s in L]) # ['hello', 'world', 'ibm']
```
#### 4. 生成器

> 为节省内存空间，一边循环一遍计算

```py
# 1. 创建生成器: generator


```
