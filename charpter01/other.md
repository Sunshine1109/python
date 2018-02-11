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
# 1. 创建生成器: generator; 创建list和generator的区别仅在于最外层的[]和()
g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x104133fc0> 

# 1.1 通过next()打印generator
print(next(g)) # 0
print(next(g)) # 1

# 1.2 通过迭代输出
for x in g:
    print(x)

# 2. 打印斐波拉契数列（函数的方法）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))

# 3. 打印斐波拉契梳理（generator）
# 定义generator的另一种方法: 如果函数定义中有yield关键字，该函数就是一个generator函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 3.1 通过循环输出
for n in fib(10):
    print(n)

# 3.2 获取generator返回值

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
```

#### 5. 迭代器

##### 5.1 Iterable对象

> 可用于`for`循环的数据类型分为两类：
* 集合数据类型： `list tuple dict set str`等
* generator类型，包括生成器好和带`yield`的`generator function`

**这些可直接作用域`for`循环的对象成为可迭代对象：`Iterable`，可以通过`isinstance()`判断一个对象是否是`Iterable`对象***

```py
from collections import Iterable
print(isinstance([], Iterable)) # True
print(isinstance('abc', Iterable)) # True
```

##### 5.2 Itertor对象

> 可以被`next()`函数调用并不断返回下一个的对象成为迭代器: `Iterator`

```py
isinstance((x for x in range(10)), Iterator) # True
isinstance([], Iterator) # False

# * 生成器对象既是`Iterable`对象，又是`Itertor`对象
print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))
```

##### 5.3 iter转换

```py
isinstance(iter([]), Iterator) # True
isinstance(iter('abc'), Iterator) # True
```

## `Iterator`优势: 它可以表示一个无限大的数据流