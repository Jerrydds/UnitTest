# 1. 通过Python语言编写一个运算的类(Calc)，类中包含两个函数：
#
#     1) add(self,a,b) 返回a+b之和
#     2) sub(self,a,c) 返回a-c之差


# 自定义运算类
class Calc(object):
    # 自定义求和函数
    def add(self, a, b):
        return a + b

    # 自定义求减函数
    def sub(self, a, c):
        return a - c


if __name__ == '__main__':
    print(Calc().add(5, 5))
    print(Calc().sub(10, 5))
