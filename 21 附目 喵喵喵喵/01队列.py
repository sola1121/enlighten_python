# 创建队列
# 在队列中增加一个元素
# 在队列尾部删除一个元素
# 判断队列是不是为空
# 计算队列长度
class QueueObject:
    def __init__(self):
        self.item = list()
    
    # 在列表头位置增加元素
    def enqueue(self, value):
        self.item.insert(0, value)

    # 在列表尾部删除元素
    def dequeue(self):
        return self.item.pop()

    # 判断当前的队列是否为空
    def is_empty(self):
        return self.item == []

    def __len__(self):
        return len(self.item)

    def size(self):
        return self.__len__()


if __name__ == "__main__":

    que = QueueObject()
    print(que.is_empty())
    que.enqueue("hello")
    print(que.is_empty())
    print(que.size())
    print(que.dequeue())
