# 用Python程序模拟300位观众，为5位嘉宾随机投票，最后按照降序排列
from redis_db import pool
import redis
import random

con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete('ballot')
    con.zadd('ballot', {'马云': 0, '马化腾': 0, '张朝阳': 0, '丁磊': 0, '李彦宏': 0})
    names = ['马云', '马化腾', '张朝阳', '丁磊', '李彦宏']
    for i in range(0, 300):
        number = random.randint(0, 4)
        name = names[number]
        con.zincrby('ballot', 1, name)
    res = con.zrevrange('ballot', 0, -1, 'WITHSCORES')
    for val in res:
        print(val[0].decode('utf-8'), int(val[1]))
except Exception as e:
    print(e)
finally:
    del con
