# 不导包

class ReadTxt(object):
    def read_txt(self):
        with open('../DataPool/triangle.txt', 'r', encoding='utf-8') as f:
            # f.readlines() 一次读取多行
            # f.readline() 一次读取一行
            # f.read() 读取全部内容

            # 获取文件内容
            data = f.readlines()
            # print(data)
            """
                1.strip() 去除换行符
                2.split（','） 根据逗号分隔字符串，并返回列表类型数据
            """

            # 初始化空列表
            data_list = []
            # 遍历
            for i in data:
                # print(i.strip().split(','))
                data_list.append(i.strip().split(','))
            # print(data_list)
            return data_list

if __name__ == '__main__':
    print(ReadTxt().read_txt())