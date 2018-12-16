import unittest

from testday07UT02.Func.calc import Calc


class Test_Calc(unittest.TestCase):
    # 自定义求和函数测试方法
    def test_calc_add(self):
        result = Calc().add(5, 5)
        print('和为：', result)
        # 设置断言判断结果
        self.assertEqual(10, result)

    # 自定义求减函数测试方法
    def test_calc_sub(self):
        result = Calc().sub(10, 5)
        print('差为：', result)
        # 设置断言判断结果
        self.assertEqual(5, result)

        # 注意:如果被测目标不存在准备和结束工作,可以不实现setUp()和tearDown方法
    # def setUp(self):
    #     pass
    # def tearDown(self):
    #     pass


if __name__ == '__main__':
    unittest.main()

# 注意:在UnitTest框架下,所有的自定义测试方法彼此间是独立运行的,
# 如果有某一个测试方法执行后报错,并不会影响其他测试方法的正常执行!
