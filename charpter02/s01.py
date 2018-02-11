#!/usr/bin/env python3
import math

print('\n\n################### 调用函数 ###################\n\n')
print('\n## 调用函数 ##\n')
print(abs(-20)) # 20
# 传参不匹配会报错
# print(abs(1, 2)) # 报错

# 数据类型转换
print(int('123')) # 123
print(int(12.23)) # 12.23

print(float('12.24')) # 12.24
print(str(1.23)) # '1.23'
print(bool(1)) # True
print(bool('')) # False

# 函数赋值给变量
callback = abs
print(callback(-1)) # 1

print('\n## 定义函数 ##\n')
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))

# 返回多个值
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y) # 151.96152422706632 70.0

# 返回多个值的情况，其实是tuple
r = move(100, 100, 60, math.pi / 6)
print(r) # (151.96152422706632, 70.0)

print('\n\n#################### 函数的参数 ######################\n\n')
print('\n## 1. 位置参数 ##\n')
# demo 1
def power(x):
    return x * x
print(power(5)) # 25

# demo 2
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 3)) # 125

print('\n## 2. 默认参数 ##\n')
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
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
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())


print('\n## 3. 可变参数 ##\n')
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
    for n in numbers:
        sum = sum + n
    return sum

print(calc(1, 2, 3)) # 6

nums = [1, 2, 3]
print(calc(*nums)) # 6

print('\n## 4. 关键字参数 ##\n')

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30)) # name: Michael age: 30 other: {}
print(person('Michael', 30, city='Beijing', other = {'gender': 'M', 'job': 'Engineer'}))

print('\n## 5. 命名关键字参数 ##\n')

# 1. 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
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



print('\n\n#################### 递归函数 ######################\n\n')
# 需要防止栈溢出，当递归调用的次数过多，会导致栈溢出; 如求 1000!
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5)) # 120

    # 需要防止栈溢出，当递归调用的次数过多，会导致栈溢出; 如求 1000!
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(10)) # 3628800