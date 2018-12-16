import unittest
from testday07UT02.Func.triangle import Triangle
from testday07UT02.ReadData.read_csv import ReadCsv


class TestTriangleCsv(unittest.TestCase):
    def test_triangle_csv(self):
        for i in range(len(ReadCsv().read_csv())):
            result = Triangle().triangle(int(ReadCsv().read_csv()[i][0]),
                                         int(ReadCsv().read_csv()[i][1]),
                                         int(ReadCsv().read_csv()[i][2]))

            self.assertEqual(result, ReadCsv().read_csv()[i][3])
            print('打印三角形返回结果：', result)


if __name__ == '__main__':
    unittest.main()
