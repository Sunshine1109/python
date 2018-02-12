## 面向对象编程

```shell
# 类和实例
# 访问限制
# 继承和多态
# 获取对象信息
# 实例属性和类属性
```

#### 1. 类和实例

##### 1.1 语法

```py
# 定义类
# 1. 类名大写
# 2. object表示继承类
class Student(object):
    # __init__: 在创建实例的时候，会自动调用
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 实例化
joy = Student('xiuhong', 100)
```

##### 1.2 数据封装

```py
# 1. 在实例上封装
def print_score(std):
    print('%s %s' % (std.name, std.score))

# 2. 在class内部封装
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))
```

#### 2. 访问限制

> 如果让`class`内部属性不被外部访问，可以把属性名的前面加两个下划线`__`，在python中，实例的变量名如果以`__`开头，就变成了一个私有变量(`private`)，只有内部可以访问，外部不能访问

```py
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score
    
    def get_name(self):
        return self.__name
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
        
    def set_name(self, name):
        self.__name = name

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))
```

#### 3. 继承和多态

##### 3.1 继承

```py
# Animal
class Animal(object):
    def run(self):
        print('Animal is running...')

# Dog
class Dog(Animal):
    def run(self):
        print('Dog is running...')

# Cat
class Cat(Animal):
    def run(self):
        print('Cat is running...')
```

#### 3.2 多态

* 子类可以改变父类中的方法

```py
class Anima(objcet):
    def run(self):
        print('Animal is running...')
    
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def runTwice(animal):
    animal.run()
    animal.run()

animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run()
cat.run()
```

#### 4. 获取对象信息

##### 4.1 type()

```py
# 1. 判断对象类型
print(type(123)) # <class 'int'>
print(type('str')) # <class 'str'>
print(type(None)) # <type(None) 'NoneType'>

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

print(type(Student)) # <class 'type'>

std = Student('xiuhong', 77)
print(type(std)) # <class '__main__.Student'>

# 2. 判断对象是否是函数
import types
def fn():
    pass

print(type(fn) == types.FunctionType) # True
print(type(abs) == types.BuildinFunctionType) # True
print(type(lambda x: x) == types.LambdaType) # True
print(type(x for x in range(10)) == types.GeneratorType) # True
```

##### 4.2 isinstance()

```py
# 优先使用isinstance
print(isinstance(123, (int, float)))
print(isinstance(b'a', bytes))
print(isinstance((1, 2, 3), (list, tuple)))
```

##### 4.3 dir()

> 获取一个对象的所有属性和方法

```py
print(dir(str))

# __xxx__这种属性或方法在python内部都是特殊的用途；比如__len__方法返回长度，调用len时，它会自动调用对象内部的__len__方法
print(len('abc')) # 3
print('abc'.__len__()) # 3

class myDog(object):
    def __len__(self):
        return 100 

myDog = myDog()
len(myDog) # 100


# getattr() / setattr() / hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
hasattr(obj, 'x') # True
hasattr(obj, 'y') # False
setattr(obj, 'y', 10)
getattr(obj, 'y')
getattr(obj, 'z', 404) # 设置默认值
```

#### 5. 实例属性和类属性

```py
# 1. 给实例绑定属性
class Student(object):
    def __init__(self, name):
        self.__name = name

std = Student('xiuhong')

# 2. 给类class绑定属性
class Student(object):
    name = 'Student'
    # ...

# 实例属性和类属性切勿使用相同的名字，否则实例属性会覆盖掉类属性
```