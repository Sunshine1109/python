## 面向对象高级编程

```shell
# 使用__slots__
# 使用@property
# 多重继承
# 定制类
# 使用枚举类
# 使用元类
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


#### 4. 定制类


#### 5. 使用枚举类


#### 6. 使用元类