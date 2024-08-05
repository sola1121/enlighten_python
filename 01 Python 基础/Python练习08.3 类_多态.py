# %%
class Mammal():
    """
    哺乳动物类
    行为: 叫唤
    """
    def bark(self):
        print("未定义种类哺乳动物叫声.")


class Dog(Mammal):
    """
    哺乳动物: 狗
    叫唤: 汪
    """
    def bark(self):
        print("狗叫: 汪.")


class Cat(Mammal):
    """
    哺乳动物: 猫
    叫唤: 喵
    """
    def bark(self):
        print("猫叫: 喵.")


# 接收一个哺乳类及其子类的函数, 根据对象传入的不同, 出现多种状态
# 这里不用指定类型也可以, Python没有严格的类型限制, 仅仅作为提示
# 但是指出类型, 是为了提示该处可以接收Mammal类即其派生
def what_mammal_bark(ob: Mammal) -> None:
    ob.bark()


# 调用同样的函数, 根据对象的不同, 得出不同的结果, 即多态

d = Dog()
what_mammal_bark(d)

c = Cat()
what_mammal_bark(c)
# %%
