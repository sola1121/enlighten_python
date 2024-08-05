# %%
# 类的继承关系
class A:
    pass
class B(A):
    pass
print(B.__base__)  # B的超类为A
print(A.__base__)  # A的超类为object
print(object.__base__)   # object的超类为None, 表明其就是最底层的超类


# %%
# 类的继承
# 单继承, 继承父类的属性与方法
class Master():
    """
    师傅类
    """
    def __init__(self, name=None) -> None:
        self.name = name   # 名字        
        self.skill = ["射击", "剑术"]   # 技能

    def show_skill(self):
        print(f"{self.name}具有能力 {self.skill}")


class Pretice1(Master):
    """
    徒弟1类, 从师傅那里继承其技能
    """
    pass


man = Pretice1("小敏")
man.show_skill()


class Pretice2(Master):
    """
    徒弟2类, 从师傅那里继承其技能, 但右发展出了新的能力
    """
    def __init__(self, name=None, *newskills):
        super().__init__(name)
        for nk in newskills:
            self.skill.append(nk)

    def show_skill(self):   # 重写能力展示
        print(f"{self.name}具有能力 {self.skill}")

        # 显式的再初始化父类, 以便再展示父类
        Master.__init__(self, "师傅")
        Master.show_skill(self)


man = Pretice2("小王", "拳击", "擒拿")
man.show_skill()


# %%
# 类的继承
# 多继承, 通过子类调用父类的方法
class Color():
    """
    颜色类
    """
    def __init__(self, c=None):
        self.color = c

    def set_color(self, c):
        self.color = c


class Glass():
    """
    玻璃类
    """
    def __init__(self, k=None):
        self.kind = k

    def set_kind(self, k):
        self.kind = k


class ColoredGlass(Color, Glass):
    """
    有色玻璃类
    """
    # def __init__(self, c=None, k=None):   # 显式的初始化父类中的属性
    #     Color.__init__(self, c)
    #     Glass.__init__(self, k)

    def show(self):
        print("玻璃颜色为:", self.color, "玻璃的种类为:", self.kind)


# 使用mro查看继承顺序, 返回一个元组, 按序为继承顺序, 越靠前的将优先
print(ColoredGlass.__mro__)

cgl = ColoredGlass()
cgl.set_color("透明")
cgl.set_kind("夹层玻璃")
cgl.show()
