# 导包
from xml.dom import minidom


class ReadXml(object):
    def read_xml(self, node, num, childNode):
        # 1. 获取xml文件 注意：传入文件路径及文件名要带后缀
        dom = minidom.parse('../DataPool/triangle.xml')
        print(dom)
        # 2.获取根元素
        root = dom.documentElement
        # print(root)
        # 3、获取第1层元素（第一组数据）
        # 注意:
        #   1.xml解析从这里开始代码没有智能提示
        #   2.getElementsByTagName()返回的是一个列表类型的数据!
        # elements = root.getElementsByTagName('side')
        # 以下方法需自己填写
        # element = root.getElementsByTagName('side')[0]
        element = root.getElementsByTagName(node)[int(num)]

        print(element)
        # 4、获取第2层元素（第一条边的数值）
        # child_element = element.getElementsByTagName('side3')[0].firstChild.data
        # child_element = element.getElementsByTagName(childNode)[0].firstChild.data
        # print(child_element)
        return element.getElementsByTagName(childNode)[0].firstChild.data

    # 获取列表长度
    def get_len(self, node):
        # 1. 获取xml文件 注意：传入文件路径及文件名要带后缀
        dom = minidom.parse('../DataPool/triangle.xml')
        print(dom)
        # 2.获取根元素
        root = dom.documentElement
        # print(root)
        # 3、获取第1层元素（第一组数据）
        # 注意:
        #   1.xml解析从这里开始代码没有智能提示
        #   2.getElementsByTagName()返回的是一个列表类型的数据!
        # elements = root.getElementsByTagName('side')
        # 以下方法需自己填写
        # element = root.getElementsByTagName('side')[0]
        element = root.getElementsByTagName(node)
        return element


if __name__ == '__main__':
    print(ReadXml().read_xml('side', 3, 'side3'))
    print(ReadXml().get_len('side'))

    print(len(ReadXml().get_len('side')))
