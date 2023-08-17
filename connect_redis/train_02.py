# 利用python 多线程模拟商品秒杀过程，不可以出现超 买和超卖的情况，假设A商品有50件参与秒杀活动，10分钟秒杀自动结束
from redis_db import pool
from concurrent.futures import ThreadPoolExecutor
import redis
import random

con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete('kill_num', 'kill_total', 'kill_flag', 'kill_user')
    con.set('kill_num', 0)
    con.set('kill_total', 50)
    con.set('kill_flag', 1)
    con.expire('kill_flag', 600)
except Exception as e:
    print(e)
finally:
    del con

user_ids = set()
while True:
    if len(user_ids) == 1000:
        break
    user_ids.add(random.randint(10000, 100000))
print(user_ids)


def buy():
    connect = redis.Redis(
        connection_pool=pool
    )
    if connect.exists('kill_flag'):
        try:
            pip = connect.pipeline()
            pip.watch('kill_num')
            num = int(connect.get('kill_num'))
            total = int(connect.get('kill_total'))
            print(num, total)
            if num < total:
                pip.multi()
                pip.incr('kill_num')
                pip.rpush('kill_user', user_ids.pop())
                pip.execute()
        except Exception as e:
            print(e)
        finally:
            if 'pip' in dir():
                pip.reset()
            del connect


# 创建200个线程的线下程池
executor = ThreadPoolExecutor(200)
# 模拟1000次提交，有200个人在同时去抢购秒杀
for i in range(0, 1000):
    executor.submit(buy)
