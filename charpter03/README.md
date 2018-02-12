## 模块

```shell
# 编写一个模块

``` 
#### 1. 编写一个模块

```py
# 注释1：可以让.py文件直接在Unix/Linux/Mac上运行
#!/usr/bin/env

# 注释2：指定字符编码
# -*- coding: utf-8 -*-

# 文档注释，任何模块第一行字符串都被视为文档注释
'a test module' # 

# 模块作者信息
__author__ = 'xiuhong'

# 代码部分

import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('Hello, World')
  elseif len(args) == 2:
    print('Hello, %s!' % args[1])
  else:
    print('Too many arguments!')

if __name__ == '__main__'
  test()
```

#### 2. 命名空间

* 通过下标`_name`来表示`private`；python并没有限制，只是一种命名规范

```py
def _private1(name):
    print('hello %s' % name)

def _private2(name):
    print('hi %s' % name)

def greeting():
    args = sys.argv
    if len(args[1]) > 3:
        _private1(args[1])
    else:
        _private2(args[1])
```