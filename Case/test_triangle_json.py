import unittest
# 导入待测三角形类
from testday07UT02.Func.triangle import Triangle
# xml文件解析类
from testday07UT02.ReadData.read_json import ReadJson

# 自定义测试类
class TestTriangleJson(unittest.TestCase):
    # 自定义测试方法
    def test_triangle_json(self):
        # 循环遍历,轮换加载用例数据
        for i in range(len(ReadJson().read_json())):
            # 初始化待测函数,并用json解析类传值
            result = Triangle().triangle(int(ReadJson().read_json()[i]['side1']),
                                         int(ReadJson().read_json()[i]['side2']),
                                         int(ReadJson().read_json()[i]['side3']))
            # 设置断言,判断结果是否符合预期
            # 通过修改数据源文件,配合json解析方法,动态获取对应数据的预期结果
            self.assertEqual(result, ReadJson().read_json()[i]['result'])
            print('返回结果为：', result)

if __name__ == '__main__':
    unittest.main()