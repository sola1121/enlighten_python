class Common:

    def the_print(self, n):
        for x in range(n):
            print(x, end=" ")
        print()


class A(Common):

    def test1(self, n):
        self.the_print(n)

    def test2(self, n):
        self.the_print(n)


class B(Common):

    def test3(self, n):
        self.the_print(n)

    def test4(self, n):
        self.the_print(n)

a = B()
a.test3(4)

# 具有相同功能, 可以使用面向对象的继承, 让类继承一拥有相同功能
# 或者新建一个模块, 将共有功能加入到新的模块中, 通过import, 所有类可直接调用
