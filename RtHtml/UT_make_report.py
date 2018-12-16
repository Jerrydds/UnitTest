import unittest

import time

from testday07UT02.Tool.HTMLTestReportCN import HTMLTestRunner

if __name__ == '__main__':
    # 组装Case
    # case存放路径
    case_dir = '../Case/'
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')

    # 报告存放路径
    report_dir = '../Report/'
    # 获取系统时间
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    print(now_time)
    # 设置报告名称
    report_name = report_dir + now_time + 'Report.html'

    # 打开报告写入的文件流
    with open(report_name, 'wb') as f:
        # 初始化执行对象
        # 注意：打印结果表示为'E' 代表错误
        runner = HTMLTestRunner(stream=f, verbosity=2, title='三角形函数单元测试报告',
                                description="平台：WindowsOS，测试执行人：testQA")
        # 调用执行方法
        runner.run(discover)
