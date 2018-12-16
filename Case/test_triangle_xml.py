import unittest
# 导入待测三角形类
from testday07UT02.Func.triangle import Triangle
# xml文件解析类
from testday07UT02.ReadData.read_xml import ReadXml


# 自定义测试类
class TestTriangleXML(unittest.TestCase):
    # 自定义测试方法
    def test_triangle_xml(self):
        # 循环遍历,轮换加载用例数据
        for i in range(len(ReadXml().get_len('side'))):
            # 初始化待测函数,并用xml解析类传值
            result = Triangle().triangle(int(ReadXml().read_xml('side', i, 'side1')),
                                         int(ReadXml().read_xml('side', i, 'side2')),
                                         int(ReadXml().read_xml('side', i, 'side3')))
            # 设置断言,判断结果是否符合预期
            # 通过修改数据源文件,配合xml解析方法,动态获取对应数据的预期结果
            self.assertEqual(result, ReadXml().read_xml('side', i, 'result'))

            # 以下的打印以为验证case执行结果,实际单元自动化脚本可不实现以下内容!!!!!!
            print(int(ReadXml().read_xml('side', i, 'side1')),
                  int(ReadXml().read_xml('side', i, 'side2')),
                  int(ReadXml().read_xml('side', i, 'side3')),
                  ReadXml().read_xml('side', i, 'result'), '>>>>>>验证成功！')


if __name__ == '__main__':
    unittest.main()
