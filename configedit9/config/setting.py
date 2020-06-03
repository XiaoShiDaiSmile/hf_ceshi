import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEST_CASE = os.path.join(BASE_DIR,'testcases')
TEST_REPORT = os.path.join(BASE_DIR,'report')
TEST_CONFIG = os.path.join(BASE_DIR,'databases','config.ini')
SOURCE_FILE = os.path.join(BASE_DIR,'databases','TestDemo.xlsx')