from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete('country', 'city')
    con.mset({'country': '中国', 'city': '成都'})
    res = con.mget('country', 'city')
    for val in res:
        print(val.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con
