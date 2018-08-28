#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'a test module' #

# 模块作者信息
__author__ = 'xiuhong'

# 代码部分

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def _private1():
    args = sys.argv
    if len(args[1]) < 3:
        print('hello xxxxx')
    else:
        print('hello %s' % args[1])

def _private2(name):
    print('hi %s' % name)

def greeting():
    args = sys.argv
    if len(args[1]) > 3:
        _private1(args[1])
    else:
        _private2(args[1])


# 只有在命令行下才成立，常用于命令行下测试
if __name__ == '__main__':
    test()
    # greeting()
    # _private1()


