import os,sys
# sys.path.append("\\opt\\tomcat\\apache-tomcat-8.5.55\\webapps\\workspace\\Demo\\configedit\\config")
# print(os.path.split(os.path.realpath(__file__))[0])
# print("setting")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEST_CASE = os.path.join(BASE_DIR,'testcases')
TEST_REPORT = os.path.join(BASE_DIR,'report')
TEST_CONFIG = os.path.join(BASE_DIR,'databases','config.ini')
SOURCE_FILE = os.path.join(BASE_DIR,'databases','TestDemo.xlsx')