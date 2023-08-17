from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)
try:
    # 建立通道，向Redis服务器传递批处理命令和执行事务
    pipline = con.pipeline()
    # 建立观察
    pipline.watch('9527')
    # 开启事务
    pipline.multi()
    pipline.hset('9527', 'age', 22)
    pipline.hset('9527', 'city', '成都')
    # 批处理命令
    pipline.execute()
except Exception as e:
    print(e)
finally:
    if 'pipline' in dir():
        # 把事务的通道关闭，后才可以释放连接
        pipline.reset()
    del con