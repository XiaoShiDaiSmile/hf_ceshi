import os,sys
sys.append(os.path.join(os.path.split(os.path.realpath(__file__))[0],'config'))
sys.append("/opt/tomcat/apache-tomcat-8.5.55/webapps/workspace/Demo/configedit/config")
print(__file__)
print(sys.path)
from config import setting

