# 三角形判断类
class Triangle(object):
    # 判断方法
    def triangle(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            if a == b and b == c:
                return '等边三角形'
            elif a == b or a == c or b == c:
                return '等腰三角形'
            else:
                return '普通三角形'
        else:
            return '不是三角形'


if __name__ == '__main__':
    print(Triangle().triangle(1, 2, 3))
    print(Triangle().triangle(2, 2, 2))
    print(Triangle().triangle(2, 2, 3))
    print(Triangle().triangle(2, 3, 4))
