# coding:utf-8
class Foo(object):
    """"""
    def __init__(self):

        pass

    def __getattr__(self, item):
        # item
        print(item)
        return self
    # 无穷无尽的递归
    # def __getattribute__(self, item):
    #       return self.item
    #   相当于  self.__getattribute__(item) 不停的调用自身
    #     pass


print(Foo().think.different.itcast)


#打印结果
# think
# different
# itcast
# <__main__.Foo object at 0x000001FF9DC50BE0>