import os,sys,configparser
from config import setting


class ReadConfig:

	def __init__(self):
		self.cf = configparser.ConfigParser()
		self.cf.read(setting.TEST_CONFIG)


	def get_config(self,field,key):
		result = self.cf.get(field,key)
		return result


	def set_config(self,field,key,value):
		fb = open(setting.TEST_CONFIG,'w')
		self.cf.set(field,key,value)
		self.cf.write(fb)


	def del_config(self,field,key):
		fb = open(setting.TEST_CONFIG,'w')
		self.cf.remove_option(field,key)
		self.cf.write(fb)



