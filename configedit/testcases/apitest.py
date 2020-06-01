import os,sys,unittest
from ddt import ddt,data
from lib.readconfig import ReadConfig
from lib.readexcel import ReadExcel
from config import setting
from lib.newreport import NewReport

testdata = ReadExcel(setting.SOURCE_FILE,'Sheet1').read_data()
print(testdata)

@ddt
class Api_Test(unittest.TestCase):

	def setUp(self):
		pass

	@data(*testdata)
	def test_api1(self,data):
		u"""nihao"""

		print("test_api1")
		try:
			print(ReadConfig().get_config('USER','EMAIL_SERVER'))
		except Exception as e:
			print(str(e))

		print(data['url'])

	def test_api2(self):
		try:
			ReadConfig().set_config('USER','nihao','nihao1')
		except Exception as e:
			print(str(e))
		pass


	def test_api3(self):
		try:
			ReadConfig().del_config('USER','nihao')
		except Exception as e:
			print(str(e))
		pass


if __name__ == '__main__':
	unittest.main()
