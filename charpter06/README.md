## IO编程

```shell
# 文件读写
# StringIO和BytesIO
# 操作文件和目录
# 序列化
```

#### 1. 文件读写

* **读文件**

```py
############## 第一种写法 ##############

# 1. 打开文件
f = open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r')

# 2. 读取文件内容
f.read()

# 3. 关闭文件
f.close()

############## 第二种写法 ##############
try:
    f = open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close

############## 第三种写法 ##############
with open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r') as f:
    print(f.read())

############## 按行读 ##############
with open('/Users/xiuhong/workspace/python/charpter06/read01.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

############## 读取二进制文件 ##############
with open('/Users/xiuhong/workspace/python/charpter06/read02.png', 'rb') as f:
    print(f.read())
```

#### 2. StringIO和BytesIO

> 在内存中读写文件

```py
# 1. StringIO 操作str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# 2. BytesIO 操作二进制

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 初始化
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
```

#### 3. 操作文件和目录

```py
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
os.rename('rename01.txt', 'read01.txt')
os.remove('rename01.txt')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
```

#### 4. 序列化

```py

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
```