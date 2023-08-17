# coding:utf-8
import os
import time
import multiprocessing


def work(count, lock):
    # 关门，销让我们的工作只能在让一个进程进行工作
    lock.acquire()
    print(count, os.getpid())
    time.sleep(5)
    # 开门
    lock.release()
    return 'result is %s, pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    # 创建5个进程的进程池
    pool = multiprocessing.Pool(5)
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    results = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i, lock))
        results.append(result)

    for res in results:
        # get函数可以获取到异步函数的返回值
        print(res.get())
    # 主进程关闭，会将子进程都同步关闭
    # time.sleep(10)
    # pool.close()
    # pool.join()
