#!/usr/bin/env python3

import functools
print('\n====== 偏函数=====\n')

# 1. int

print(int('0x10', base=0)) # 16
print(int('101', base=2)) # 5
print(int('101', base=3)) # 10
print(int('0o101', 8)) # 65
# print(int('9', base=8)) # err: ValueError: invalid literal for int() with base 8

# int 传入小数将报错
# print(int('12.22'))
# Error: ValueError: invalid literal for int() with base 10

def int2(x, base=2):
    return int(x, base)

_int2 = functools.partial(int, base=2)

print(int2('101'))
print(_int2('101'))

# 2. float
