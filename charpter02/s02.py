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
