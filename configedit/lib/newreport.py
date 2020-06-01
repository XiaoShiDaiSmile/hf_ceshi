import os,sys

def NewReport(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn:os.path.getmtime(testreport+'\\'+fn))
	file_new = os.path.join(testreport,lists[-1])
	return file_new

