import os,sys
from time import sleep
sys.path.append("\\opt\\tomcat\\apache-tomcat-8.5.55\\webapps\\workspace\\Demo\\configedit")
print(os.path.split(os.path.realpath(__file__))[0])
print(sys.path)
from config import setting

