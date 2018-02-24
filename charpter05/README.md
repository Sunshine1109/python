## 面向对象高级编程

```shell
# 使用__slots__
# 使用@property
# 多重继承
# 定制类
# 使用枚举类
```

#### 1. 使用__slots__

> `__slots`来限制`class`实例能添加的属性

* 给实例和class添加属性和方法
```py
class Student(object):
    pass

# 1. 给实例绑定属性
s = Student()
s.name = 'xiuhong'

# 实例方法
def set_age(self, age):
    self.age = age

# 2. 给实例绑定方法
from types import MethodType
s.set_age = MethodType(set_age, s)

# 3. 给一个实例绑定方法对另一个实例是不起作用的
s2 = Student()
hasattr(s2, 'set_age') # False

# 4. 给class绑定方法，对所有实例都起作用
Student.set_age = set_age
```

* 使用__slots__

```py
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

```


#### 2. 使用@property

> @property负责把一个方法变成属性调用

```py
class Student(object):
    
    # getter
    @property
    def score(self):
        return self._score
    
    # setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an iteger')
        if value < 0 or value > 100:
            raise ValueError('score muste between 0 ~ 100')
        self._score = value
    
std = Student()
std.score = 90
print('score', std.score)

# 设置只读属性: 不设置setter即可
```

#### 3. 多重继承

```py
class Mammal(object):
    def mammal(self):
        print('I am mammal')

class Runnable(object):
    def run(self):
        print('I can run')

class Dog(Mammal, Runnable):
    def dog(self):
        print('I am dog')

dog = Dog()
dog = Dog()
print(dog.dog())
print(dog.mammal())
print(dog.run())
```

#### 4. 定制类

```py
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    __repr__ = __str__

std = Student('xiu')
print(std)

print('\n## 2. __iter__ 和 __getitem__ ##\n')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[10])
print(f[0:5])

print('\n## 2. __getattr__ ##\n ')

class Student(object):
    def __init__(self):
        self.name = 'xiu'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

std = Student()
print(std.score)

print('\n## 3. __call__ ##\n')

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('self call')

std = Student('xiu')
print(std())
print(callable(Student('hong')))
```

#### 5. 使用枚举类

```py
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
```