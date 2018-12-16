import json


class ReadJson(object):
    def read_json(self):
        with open('../DataPool/triangle.json', 'r', encoding="utf-8") as f:
            # 通过load()方法，获取json文件的内容
            source = json.load(f)
            # print(source)
            # 根据键取出对应值（返回数据类型为list）
            # print(source['data'])
            return source['data']


if __name__ == '__main__':
    print(ReadJson().read_json())
