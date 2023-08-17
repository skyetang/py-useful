# coding:utf-8

# 主线程不需要等待子线程处理完，就会结束
import random
import time
import threading

lists = ['python', 'django', 'flask', 'requests', 'uvloop']

new_lists = []

def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = f'{data}_new'
    new_lists.append(new_data)
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    t_list = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    print('old list:', lists)
    print('new list:', new_lists)
    print('time is %s' % (time.time() - start))

