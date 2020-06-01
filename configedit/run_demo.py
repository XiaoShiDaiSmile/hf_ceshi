import os,sys
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0],'config'))
sys.path.append("/opt/tomcat/apache-tomcat-8.5.55/webapps/workspace/Demo/configedit/config")
print(__file__)
print(sys.path)
from config import setting

