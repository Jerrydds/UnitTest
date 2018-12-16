import unittest
from testday07UT02.Func.triangle import Triangle
from testday07UT02.ReadData.read_txt import ReadTxt


class TestTriangleTxt(unittest.TestCase):
    def test_triangle_txt(self):
        for i in range(len(ReadTxt().read_txt())):
            result = Triangle().triangle(int(ReadTxt().read_txt()[i][0]),
                                         int(ReadTxt().read_txt()[i][1]),
                                         int(ReadTxt().read_txt()[i][2]))

            self.assertEqual(result, ReadTxt().read_txt()[i][3])
            print('打印三角形返回结果：', result)


if __name__ == '__main__':
    unittest.main()
