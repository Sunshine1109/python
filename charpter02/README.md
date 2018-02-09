## 函数

```shell
# 调用函数
# 定义函数
# 函数的参数
# 递归函数
```

#### 1. 调用函数

> python内置了很多函数，[官网](http://docs.python.org/3/library/functions.html#abs)

```py
abs(-20) # 20
# 传参不匹配会报错
abs(1, 2) # 报错

# 数据类型转换
int('123') # 123
int(12.23) # 12.23

float('12.24') # 12.24
str(1.23) # '1.23'
bool(1) # True
bool('') # False

# 函数赋值给变量
callback = abs
print(callback(-1)) # 1
```

#### 2. 定义函数

> 在python中，定义一个函数使用def语句

```py
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))
# 如果函数没有return语句，函数也会返回结果None。return None 可以简写为return

# 空函数: 可以作为占位符，现在还没想好怎么写函数的代码，先让程序运行起来
def nop():
    pass

# 参数检查 isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 返回多个值
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y) # 151.96152422706632 70.0

# 返回多个值的情况，其实是tuple
r = move(100, 100, 60, math.pi / 6)
print(r) # (151.96152422706632, 70.0)
```

#### 3. 函数的参数

##### 3.1 位置参数

```py
# demo 1
def power(x):
    return x * x
print(power(5)) # 25

# demo 2
def power(x, n):
    s = 1
    while n > 0
        n = n - 1
        s = s * x
    return s
print(power(5, 3)) # 125
```

##### 3.2 默认参数

```py
# demo 1
def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
    return s

print(power(5)) # 25
print(power(5, 2)) # 25

# demo 2
def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)

# !!! 定义默认参数要牢记一点：默认参数必须制定不变对象 !!!
def add_end(L = None):
    if L is None
        L = []
    L.append('END')
    return L
```

#### 3.3 可变参数

> 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

```py
# 1. 可以传入list或tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(calc([1, 2, 3])) # 6
print(calc((1, 2, 3))) # 6

# 2. 可变参数; 类似ES6中的解构
def calc(*numbers):
    sum = 0
    for n in numbers
        sum = sum + n
    return sum

print(calc(1, 2, 3)) # 6

nums = [1, 2, 3]
print(calc(*nums)) # 6
```

#### 3.4 关键字参数

> 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个dict

```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30)) # name: Michael age: 30 other: {}
print(person('Michael', 30, city='Beijing', {'gender': 'M', 'job': 'Engineer'}))
```

#### 3.5 命名关键字参数

* 对于关键字参数，函数调用者可以传入任意不受限制的关键字参数。茱萸到底传入了哪些，需要在函数内部铜鼓kw检查

```py
# 1. 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw
        pass
    print('name:', name, 'age:', age, 'other', kw)
print(person('Jack', 24, city='Beijing', addr='Chaoyang', sex='M'))

# 2. 命名关键字参数; 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符 *, * 后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
print(person('Jack', 24, city='Beijing', job='Engineer'))

# 3. 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字，就不在需要一个特殊分隔符 * 了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
print(person('Jack', 24, city='Beijing', job='Engineer'))

# 4. 命名关键字参数接受缺省值
def person (name, age, *, city='Beijing', job):
    print(name, age, city, job)
print(person('Jack', 24, job = 'Engineer'))
```

#### 4. 递归函数




