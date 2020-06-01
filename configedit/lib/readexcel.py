import os,sys,xlrd


class ReadExcel:

	def __init__(self,filename,SheetName='Shee1'):
		self.data = xlrd.open_workbook(filename)
		self.table = self.data.sheet_by_name(SheetName)
		self.rows = self.table.nrows
		self.cols = self.table.ncols


	def read_data(self):
		if self.rows>1:
			keys = self.table.row_values(0)
			listApiData = []
			for col in range(1,self.rows):
				values = self.table.row_values(col)
				dict_api = dict(zip(keys,values))
				listApiData.append(dict_api)
			return listApiData
		else:
			print("table is empty")
			return None