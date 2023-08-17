from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.sadd('employee', 8001, 8002, 8003)
    con.srem('employee', 8001)
    res = con.smembers('employee')
    for val in res:
        print(val.decode('utf-8'))
    con.zadd('keywords', {'张三': 0, '李四': 0, '王五': 0})
    con.zincrby('keyword', 20, '李四')
    res = con.zrevrange('keywords', 0, -1)
    for val in res:
        print(val.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con