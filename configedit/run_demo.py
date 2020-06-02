#coding=UTF-8
import os,sys,unittest,xlrd,ConfigParser
from config import setting
from lib.readconfig import ReadConfig
from package.HTMLTestRunner import HTMLTestRunner


def add_case(test_path=setting.TEST_CASE):
	print(unittest.defaultTestLoader)
	discover = unittest.defaultTestLoader.discover(test_path,pattern="**test.py")
	return discover


def run_case(all_case,test_report=setting.TEST_REPORT):
	now = time.strftime('%Y-%m-%d %H-%M-%S')
	filename = test_report+'\\'+now+'-'+'report.html'
	fb = open(filename,'wb')
	runner = HTMLTestRunner(stream=fb,title="UI界面自动化测试报告",description="this is description")
	runner.run(all_case)
	#webbrowser.open_new_tab(filename)
	fb.close()
	# report = new_report(setting.TEST_REPORT)
	# print(report)
	# send_email(report)


if __name__ == '__main__':
	cases = add_case()
	run_case(cases)

