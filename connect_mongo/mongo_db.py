# 重新通过配置文件安装mongodb
# mongod --config 'C:\Program Files\MongoDB\Server\4.0\mongo.cnf' --reinstall

# pip install pymongo --target F:\python\venv\lib\site-packages -i https://pypi.tuna.tsinghua.edu.cn/simple
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017, username='admin', password='abc123456', authSource='admin')