# %%
# 空调的抽象类AC, 要求有 制冷cool_wind, 制热hot_wind, 换气swing_1_r
# 根据不同品牌, 有 XiaoMi_AC, Midea_AC

import random

def switch_state(rate) -> bool:
    num = random.randint(1, 1000)
    if num<1000*rate:
        return True
    else:
        return False


class AC():
    """
    空调抽象类
    """
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_1_r(self):
        pass


class XiaoMi_AC(AC):
    def cool_wind(self):
        if switch_state(0.95):
            print("XiaoMi, 开启冷风.")
        else:
            print("XiaoMi, 冷风开启失败.")

    def hot_wind(self):
        if switch_state(0.96):
            print("XiaoMi, 开启热风.")
        else:
            print("XiaoMi, 热风开启失败.")

    def swing_1_r(self):
        if switch_state(1):
            print("XiaoMi, 开启换气")
        else:
            print("XiaoMi, 换气开启失败.")
            

    
class Midea_AC(AC):
    def cool_wind(self):
        if switch_state(0.97):
            print("Midea, 开启冷风.")
        else:
            print("Midea, 冷风开启失败.")
    
    def hot_wind(self):
        if switch_state(0.94):
            print("Midea, 开启热风.")
        else:
            print("Midea, 热风开启失败.")

    def swing_1_r(self):
        if switch_state(0.99):
            print("Midea, 开启换气.")
        else:
            print("Midea, 换气开启失败.")
            


# 测试空调是否可以正常运行, 这里使用多态
def test_work(ac: AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_1_r()

xiaomi_ac = XiaoMi_AC()
test_work(xiaomi_ac)

midea_ac = Midea_AC()
test_work(midea_ac)


# %%
# 使用标准库ABC实现抽象类

from abc import ABC, abstractmethod

# 定义一个抽象类
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    # 非抽象方法
    def get_brand(self):
        return self.brand


# 定义一个继承自抽象类的具体类
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} car engine started.")

    def stop_engine(self):
        print(f"{self.brand} car engine stopped.")


# 使用具体类
my_car = Car("Volvo")
my_car.start_engine()  # 输出: Volvo car engine started.
my_car.stop_engine()   # 输出: Volvo car engine stopped.
print(my_car.get_brand())  # 输出: Volvo

# %%
