from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    con.rpush('dname', '销售部', '产品部', '电商部', '财务部')
    con.lpop('dname')
    res = con.lrange('dname', 0, -1)
    for val in res:
        print(val.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con