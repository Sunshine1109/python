#!/usr/bin/env python3

# -*- coding: utf-8 -*-

print('\n\n################### 1. 读文件 ###################\n\n')

print('\n ## 1. 第一种写法 ##\n')
# 1. 打开文件
f = open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r')

# 2. 读取文件内容
print(f.read())

# 3. 关闭文件
f.close()

print('\n ## 2. 第二种写法 ##\n')

try:
    f = open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close

print('\n ## 3. 第三种写法(推荐) ##\n')

with open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r') as f:
    print(f.read())

print('\n ## 4. 按行读 ## \n')

with open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

print('\n ## 5. 读取二进制文件 ##\n')

with open('/Users/xiuhong/workspace/python/charpter06/read02.png', 'rb') as f:
    print(f.read())


print('\n\n ################### 2. 写文件 ####################### \n\n')

print('\n ## 1. 不存在的文件，新建 \n')
with open('/Users/xiuhong/workspace/python/charpter06/newfile.txt', 'w') as f:
    f.write('hello jingjing')

print('\n ## 2. 已存在的文件，覆盖 \n')
with open('/Users/xiuhong/workspace/python/charpter06/newfile.txt', 'w') as f:
    f.write('hello jingjing2')

print('\n ## 3. append 添加 ##\n')
with open('/Users/xiuhong/workspace/python/charpter06/newfile.txt', 'a') as f:
    f.write('\n#########append new content #########')

print('\n\n############ 3. StringIO 和 BytesIO ###############\n\n')

from io import StringIO, BytesIO

print('\n ## 1. StringIO ##\n')

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('Hello\nWorld\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('\n ## 2. BytesIO ## \n')

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 初始化
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()


print('\n\n ################### 4. 操作文件和目录 ################## \n\n')

import os

# 系统名称
print(os.name)

# 详情信息(依赖平台提供接口)
# print(os.uname())

# 环境变量
# print('\n>>>>>>>>>>>> 环境变量 <<<<<<<<<<<<<<<\n', os.environ)
# print('\n>>>>>>>>>>>> PATH 环境变量 <<<<<<<<<<<<<<<\n', os.environ.get('PATH'))

# 查看当前目录
print(os.path.abspath('.'))

# 创建/删除 目录
currentPath = os.path.abspath('.')

testdir = os.path.join(currentPath, 'testdir')
# os.mkdir(testdir)
# os.rmdir(testdir)

# 文件路径 + 文件名
print(os.path.split('/Users/xiuhong/workspace/python/charpter06.read01.txt'))

# 文件扩展名
print(os.path.splitext('/Users/xiuhong/workspace/python/charpter06.read01.txt'))

# 文件重命名
# os.rename('rename01.txt', 'read01.txt')
# os.remove('rename01.txt')

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


print('\n\n ################### 5. 序列化 ################## \n\n')
import json
d = dict(name = 'job', age = 20, score = 80)
print(json.dumps(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('xiuhong', '28', 90)
# print(json.dumps(s, default=student2dict))
print(json.dumps(s, default = lambda obj: obj.__dict__))

# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))