# 导包
import csv


class ReadCsv(object):
    def read_csv(self):
        # 打开文件
        """
        1.文件路径及文件名带后缀
        2.读取方式 ‘r’
        3.防止获取的文件内容乱码，需要设置编码格式
        """
        with open('../DataPool/triangle.csv', 'r', encoding='UTF-8') as f:
            # 2.获取文件内容
            data = csv.reader(f)
            # print(data)
            # 3.初始化空列表
            data_list = []
            # 4.遍历
            for i in data:
                # prin(i)
                data_list.append(i)
            # print(data_list)
            return data_list


if __name__ == '__main__':
    print(ReadCsv().read_csv())
