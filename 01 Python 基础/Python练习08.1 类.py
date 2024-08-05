# %%
# 定义一个类, 并声明该类的一个实例
class Car:
    """
        车
        属性:
            有发动机
            有油箱
        行为:
            可以行使
            需要加油
    """
    def __init__(self, gass: int, engine: bool) -> None:
        self.gass = gass   # 当前汽车的油量
        self.engine = engine   # 当前汽车的引擎是否完好
    
    def run(self):
        # 当油量小于1的时候, 没法行使
        if self.gass<1:
            raise Exception("缺油, 车辆无法行使.")
        if self.engine != True:
            raise Exception("引擎有故障, 车辆无法行使.")
        print(f"当前油量{self.gass}, 引擎状态{self.engine}, 正常行使.")


# 实例化一个车类的对象
c = Car(10, True)
try:
    c.run()   # 运行
except Exception as err:
    print(err)


# %%
# 实例变量与方法 对比 类变量与方法
# 实例变量是在类实例化后才会被创建, 并绑定在对应的实例对象上
# 类变量是在定义类的时候就有的, 该类的所有实例对象都将共享该类的变量

class Value():
    # 类变量
    cls_v = 99

    # 重写实例对象的构造函数, 其第一个参数self表示所创建的实例
    def __init__(self, v) -> None:
        # 在构造类实例对象时才会创建的实例对象变量
        self.obj_v = v

    # 类方法, 可以操作类, 其第一个参数cls表示该类自身
    @ classmethod
    def set_v(cls, v):
        cls.cls_v = v


o1 = Value(1)
o2 = Value(2)

print(f"实例对象1中的变量为{o1.obj_v}, 对应的类变量为{o1.cls_v}\n\
      实例对象2中的变量为{o2.obj_v}, 对应的类变量为{o2.cls_v}\n\
      类中的变量为{Value.cls_v}, 可见所有的该类的实例对象都共享一个类变量.")


# %%
# 类中函数的重写
class Number(object):
    """
    重新定义个一个Number类
    可以完成加减乘除的算术运算
    """
    def __init__(self, value) -> None:
        self._number = float(value)
    
    def __str__(self) -> str:
        return f"自定义Number类实例, 当前值为{self._number}"

    def __add__(self, other):
        """加"""
        return Number(self._number + other)

    def __sub__(self, other):
        """减"""
        return Number(self._number - other)

    def __mul__(self, other):
        """乘"""
        return Number(self._number * other)

    def __truediv__(self, other):
        """除"""
        if other == 0:
            raise ZeroDivisionError
        return Number(self._number / other)

num = Number(10)
print(num)
print(num*10)


# %%
# 类的私有属性和方法
class One():
    def __init__(self, val=None):
        self.__one = val

    def set_one(self, val):
        self.__one = val
    
    def get_one(self):
        return self.__one
    

class Two(One):
    def __init__(self, val=None):
        super().__init__(val)


t = Two()
t.set_one(321)
print(t.get_one())
