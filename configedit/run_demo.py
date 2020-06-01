import os,sys,unittest,time,shutil,webbrowser
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0],'config'))
from config import setting
from package.HTMLTestRunner import HTMLTestRunner
from lib.newreport import NewReport
from lib.sendemail import SendMail

def add_case(test_path=setting.TEST_CASE):
	discover = unittest.defaultTestLoader.discover(test_path,pattern="**test.py")
	return discover


def run_case(all_case,test_report=setting.TEST_REPORT):
	shutil.rmtree(test_report)
	os.mkdir(test_report)
	now = time.strftime('%Y-%m-%d %H-%M-%S')
	filename=test_report+'\\'+now+'-'+'report.html'
	fb = open(filename,'wb')
	runner = HTMLTestRunner(stream=fb,
							title="this is test report",
							description="this is description",
							tester="json"
						   )
	runner.run(all_case)
	report = NewReport(setting.TEST_REPORT)
	webbrowser.open_new_tab(filename)
	SendMail(report)
	fb.close()


if __name__ == '__main__':
	cases = add_case()
	run_case(cases)
