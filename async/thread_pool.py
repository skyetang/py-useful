# coding:utf-8
import time
from concurrent.futures import ThreadPoolExecutor
import threading
import os


lock = threading.Lock()

def work(i):
    lock.acquire()
    print(i, os.getpid())
    time.sleep(1)
    lock.release()
    return os.getpid()


if __name__ == '__main__':
    t = ThreadPoolExecutor(2)
    res_list = []
    for i in range(20):
       result = t.submit(work, (i, ))
       res_list.append(result)
    for res in res_list:
        print(res.result())

