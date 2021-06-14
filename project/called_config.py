import os

# 获取脚本所在文件夹的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'wM9UG@uPS1Rq`1=jiex.7l#$z(^}2o'

# 定义数据库的全路径
DATABASE_PATH = os.path.join(basedir, DATABASE)

