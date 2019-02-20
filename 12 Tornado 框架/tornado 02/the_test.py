import abc

class A:   # 假设是一个框架
    # 在框架中, 定义了完整的流程步骤, 其中留出了相应的方法用于用户自定义需求
    def prepare(self):
        print("A的prepare方法")

    def init(self):
        print("A的init方法")

    @abc.abstractmethod
    def get(self):
        # 钩子方法(hook/handler)
        pass

    def finish(self):
        print("A的finish方法")

    def do_something(self):
        # 完整的业务逻辑
        self.prepare()
        self.init()
        self.get()
        self.finish()


class B(A):
    def get(self):
        print("B rewrite function from father class A")


class The_Test:
    def __init__(self, fun):
        obj = fun()
        obj.do_something()


The_Test(B)
