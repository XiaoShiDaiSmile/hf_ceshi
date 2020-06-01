import os,sys,unittest,time,shutil,webbrowser
sys.path.append(os.path.split(os.path.realpath(__file__))[0])
sys.path.append("abc")
print(sys.path)
print(os.path.join(os.path.split(os.path.realpath(__file__))[0],'config'))
from config import setting
