# coding:utf-8
import time
import os
import multiprocessing

# 通过进程模块执行的函数无法获取返值，即使有返回值也拿不到
# 多个进程同时修改文件可能会出现错误
# 进程数量太多可能会造成资源不足，甚至死机等情况


def work_a():
    for i in range(10):
        # 当前函数的进程号码
        print(i, 'a', os.getpid())


        time.sleep(1)


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()  # 主进程1
    print(start)
    a_p = multiprocessing.Process(target=work_a)  # 子进程1
    # a_p.start()  # 子进程1执行
    b_p = multiprocessing.Process(target=work_b)  # 子进程2
    # b_p.start()  # 子进程2执行

    for p in (a_p, b_p):
        p.start()

    for p in (a_p, b_p):
        p.join()  #  阻塞掉进程，执行完了再执行主进程

    for p in (a_p, b_p):
        print(p.is_alive())

    print('时间消耗是:', time.time()-start)  # 主进程代码2
    print('parent pid is %s' % os.getpid())  # 主进程代码3
