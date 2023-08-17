from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
con.set('country', '中国')
con.set('city', '成都')
country = con.get('country').decode('utf-8')
print(country)

del con
