#!/usr/bin/env python3

print('################## 输入输出 #########################\n\n')
# 输出
# print('hello world')

# 1. 可以接受多个字符串，用逗号","隔开
# 2. 遇到逗号会输出一个空格
print('The quick brown fox', 'jump over', 'the lazy dog')

# 输入
# Python提供了input()

# name = input()
# name = input('please input your name: ')
# print('hello', name)


print('\n\n################# 数据类型和变量 ################\n\n')

# 1. 整数
print('\n## 整数 ##\n')
print(0, 100, -100, 0)

# 十六进制
print(0xff00)

# 2. 浮点数
print('\n## 浮点数 ##\n')
print(1.23, -9.01)

# 科学计数法 1.29 x 10的9次方和0.000012
print(1.29e9, 1.2e-5)

# 3. 字符
# '' 和 ""都可以
print('\n## 字符 ##\n')
print('单引号')
print("双引号")

# 转义字符\
print('hello \"xiuhong\"')

# 转义其它字符\n、\t等
print('hello\nworld')

# 不转义 r'内容'
print(r'hello \n world')

# 多行字符，Python允许使用'''...'''的格式表示
print('''line1
... line2 ...
... line3 ...
''')

# 另外，多行字符可以和r''混用
print(r'''hello\nworld
line2\t
''')

# 4. 布尔值

print('\n## 布尔值 ##\n')
print(True)
print(False)

# True
print(3 > 2)

# False
print(3 > 5)

# 布尔值也可以用and\or\not运算
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 >1)

print(True or True)
print(True or False)
print(5 > 3 or 1 > 3)

print(not True)
print(not False)
print(not 1 > 2)

# 5. 空值
print('\n## 空值 ##\n')
print(None)

# 6. 变量
print('\n## 变量 ##\n')
# 命名
a = 1
t_007 = 'T007'
Answer = True

# Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123
print(a)
a = 'ABC'
print(a)

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 7. 常量
print('\n## 常量 ##\n')
PI = 3.14159265359
print(PI)
# 一种是/;计算结果为浮点数，即使是两个证书恰好整除，结果也是浮点数
print(10 / 3) # 3.3333333333333335
print(9 / 3) # 3.0

# 另一种是地板除法 // 类似JavaScript中的Math.floor()，向下取整
print(10 // 3)

# 余数运算
print(10 % 3) # 1


print('ABC'.encode('ascii'))

#### 3. 字符串和编码

print('\n\n################# 字符串和编码 ########################')
print('\n## 字符串和编码 ##\n')

# 字符串是已Unicode编码，支持多语言
print('包含中文str')

# 对于单个字符编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示
# 从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes中包含无法解码的字节，decode()方法会报错; 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 计算bytes包含多少个字符，可以用len()函数; len()函数计算的是字符数，如果换成bytes, len函数就计算字节数
print(len('ABC')) # 3
print(len('中文')) # 2

print(len(b'ABC')) # 3
print(len('中文'.encode('utf-8'))) # 6

print('Hello, %s' % 'world') # Hello, world
print('Hi, %s, you have $%d.' % ('xiuhong', 10000000)) # Hi, xiuhong, you have $10000000

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.14159265359)


print('\n\n##################### 使用list和tuple #####################')

# 1. list
print('\n## list ##\n')
classmates = ['Michael', 'Bob', 'leifeng']
print(classmates)

# len获取长度
print(len(classmates))

# 用索引访问list中每一个位置的元素, 从0开始
# 超出所以呢，Python会报一个IndexError错误
print(classmates[0]) # 'Michael'
# print(classmates[3]) # 报错，越界
print(len(classmates) - 1) # 数组最后一位, leifeng

# 除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1]) # leifeng
# print(classmates[-4]) # 报错，越界


# 插入
classmates.insert(1, 'Jack') # 索引为1
print(classmates) # Michael Jack Bob leifeng 

# append list末尾添加元素
classmates.append('Adam') # 加入到最后一个位置
print(classmates) # Michael Jack Bob leifeng Adam

# pop 删除list末尾元素
classmates.pop()
print(classmates) # Michael Jack Bob leifeng

# pop 删除指定位置元素
classmates.pop(1)
print(classmates) # Michael Bob leifeng

# 替换list中元素
classmates[1] = 'Sarah'
print(classmates) # Michael Sarah leifeng

# list 里面元素类型也可以不同
L = ['Apple', 123, True]
s = ['python', 'java', ['javascript', 'css'], 'schema']
print(len(s)) # 4

# 2. tuple
print('\n## tuple ##\n')
classmates = ('Michael', 'Bob', 'Tracy')

# 使用tuple的意义在于：静态更安全；在定义一个tuple时，tuple的元素就必须被确定下来
t = (1, 2)
# t = (4, 5) # 仍然可以覆盖
print(t)

b = ()
print(b)

# 可变的tuple
d = ('a', 'b', ['A', 'B'])
d[2][0] = 'X'
d[2][1] = 'Y'
print(d) # '不变'是指指向不变

c = ('a', 'b')
# c[1] = 'd' # error
print(c)