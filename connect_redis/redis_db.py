import redis

try:
    pool = redis.ConnectionPool(
        host='localhost',
        port=6379,
        db=0
    )
except Exception as e:
    print(e)
