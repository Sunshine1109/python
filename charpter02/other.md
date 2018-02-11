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