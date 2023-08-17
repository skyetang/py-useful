from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    con.hset('9527', 'name', 'scott')
    con.hset('9527', 'age', 22)
    con.hset('9527', 'city', '中国')
    con.hdel('9527', 'age')
    res = con.hexists('9527', 'name')
    print(res)
    res = con.hgetall('9527')
    for val in res:
        print(val.decode('utf-8'), res[val].decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con