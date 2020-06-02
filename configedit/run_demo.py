#coding=UTF-8
import io,sys,unittest2,xlrd,ConfigParser,time,webbrowser
from config import setting
from package.HTMLTestRunner import HTMLTestRunner


def add_case(test_path=setting.TEST_CASE):
	testunit=unittest2.TestSuite()
	discover = unittest2.loader.TestLoader().discover(test_path,pattern="**test.py",top_level_dir=None)
	return discover


def run_case(all_case,test_report=setting.TEST_REPORT):
	now = time.strftime('%Y-%m-%d %H-%M-%S')
	filename = test_report+'\\'+now+'-'+'report.html'
	fb = io.open(filename,'wb')
	runner = HTMLTestRunner(stream=fb,title="UI界面自动化测试报告",description="this is description")
	runner.run(all_case)
	fb.close()


if __name__ == '__main__':
	cases = add_case()
	run_case(cases)

