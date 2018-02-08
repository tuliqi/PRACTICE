# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import unittest
from common.HTMLTestRunner import HTMLTestRunner
from Testcases.testSearchBook import TestSearchBookPage

if __name__ == '__main__':
    TEST_UNIT = unittest.TestSuite()
    # TestLoginPage('test_login'),
    TEST_UNIT.addTest(TestSearchBookPage('test_search_python_book'))
    # testunit.addTest(TestBookSignPage('test_bookSign_nopayBook'))
    # testunit.addTest(TestBookSignPage('test_bookSign_cancelBook'))
    # testunit.addTest(TestBookSignPage('test_bookSign_CheckOut'))
    # 定义报告输出路径
    HTML_PATH = "testReport.html"
    fp = open(HTML_PATH, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"飞雪智慧公寓平台测试", description=u"测试用例结果")
    runner.run(TEST_UNIT)
    fp.close()
