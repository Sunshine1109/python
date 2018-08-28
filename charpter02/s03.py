#!/usr/bin/env python3

import datetime
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        print(datetime.datetime.now())
        return func(*args, **kw);
    return wrapper

@log
def add(a, b):
    return a + b

r = add(10, 2)
print(r)
print('function name %s' % add.__name__)

print('\n===================\n')

# def log2
def log2(author):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('author is %s' %  author)
            return func(*args, **kw)
        return wrapper;
    return decorator;


@log2('xiuhong')
def double(x):
    return x * 2;

#s = log2('xiuhong')(double)(5)

s = double(5)
print('function double\'s name is %s' % double.__name__)
print(s)
