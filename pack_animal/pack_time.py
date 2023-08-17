# coding:utf-8

import time

# 返回一个时间戳，是相对于1970年1月1日0点0分0秒中间的秒数
now = time.time()
print(now)
time.sleep(1)

now_local = time.localtime()
print(now_local, type(now_local))


before = now - 1000
print(before, type(before))
before_obj = time.localtime(before)
print(before_obj, type(before_obj))


now_local_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(now_local_str, type(now_local_str))

now_local_obj = time.strptime(now_local_str, '%Y-%m-%d %H:%M:%S')
print(now_local_obj, type(now_local_obj))