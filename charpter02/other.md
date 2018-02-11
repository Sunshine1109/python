## 函数式编程

```shell
# 高阶函数
# 返回函数
# 匿名函数
# 装饰器
# 偏函数
```
#### 1 高阶函数

##### 1.1 map函数

```py
# map返回的对象是Iterator
def f(x):
    return x * x
r = map(f, [1, 2, 3])
print(list(r))
```

##### 1.2 reduce函数

```py
from functools import reduce
def add(a, b):
    return a + b
print(reduce(add, [1, 2, 3]))
```

##### 1.3 filter函数

```py
def is_odd(n):
    return n % 2 == 0
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))
```

##### 1.4 sorted函数

```py
# 默认排序(小-大)
print(sorted([22, 10, -12, 20]))

# 绝对值排序
print(sorted([22, 10, -12, 20], key=abs))

# 忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
```

#### 2. 返回函数

##### 2.1 函数作为返回值

```py
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f) # <function lazy_sum.<locals>.sum at 0x104168730>
print(f()) # 25

# 每次调用都会返回一个新函数，即使缓入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2) # False
```

##### 2.2 闭包

> 类似`Javascript`中的闭包概念

```py
# 1. 经典的闭包问题
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9
# 返回结果并不是预期中的1 4 9，原因在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 2. 解决经典闭包问题：立即执行

def count():
    def f(j):
        def g():
            return j * j
        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9
```

#### 3. 匿名函数

> `lambda`表示匿名函数。`lambad x:`，冒号前面的`x`表示函数参数

```py
# 1. map函数使用匿名函数
list(map(lambda x: x * x, [1, 2, 3]))
print(list)

# 2. 赋值
f = lambda x: x * x
print(f) # <function <lambda> at 0x1041689d8>

# 3. 作为返回值
def build(x, y):
    return lambda: x * x + y * y
```

#### 4. 装饰器

> 函数也是一个对象，通过变量调用函数

```py
# 1. 通过变量调用函数
def now():
    print('2018-01-11')
f = now;
print(f())

# 2. __name__属性
print(now.__name__)
print(f.__name__)

# 3. 通过装饰器增加now功能
def log(func):
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把log放在now函数定义处，相当于执行了语句 now = log(now)
@log
def now():
    print('2018-01-11')
print(now())

# 4. 嵌套
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('excute')
def now():
    print('2018-01-11')
print(now())

# 5. 上面会出现个问题，经过装饰器函数装饰之后，原来函数的一些属性如：__name__会发生变化
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ', func.__name__)
        return func(*args, **kw)
    return wrapper
```

#### 5. 偏函数

> `functools.partial`的作用是把一个函数的默写参数给固定住(也就是设置默认值)，返回一个新函数，调用这个新函数会更简单

```py
# 1. 基础用法
import functools
int2 = functools.partial(int, base=2)
print(int2('1000001') # 65

# 2. 带参数
max2 = functools.partial(max, 10)
max2(4, 5, 6) # 相当于max2(10, 4, 5, 6)
```