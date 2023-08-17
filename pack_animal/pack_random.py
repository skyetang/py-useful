# coding:utf-8

# random.random  随机返回0~1之间的浮点数
# random.uniform  产生一个a,b区间的随机浮点数
# random.randint 产生一个a,b区间的随机整数
# random.choice  返回对象中的一个随机元素
# random.sample  随机返回对象中指定的元素，可以返多个
# random.randrange 获取区间内的一个随机数，可传入一个步长来设置返回数的步长

import random

gifts = ['iphone', 'ipad', 'iwatch', 'appletv']


def choice_gifts():
    data = random.choice(gifts)
    print(f'你抽中了{data}')


def choice_gift_new():
    count = random.randrange(0, 100, 1)
    # count =random.choice(range(0,100,1) 和上面这个效果等同
    print(count)
    if 0 <= count <= 50:
        print('你中了一个iphone')
    elif 50 < count <= 70:
        print('你中了一台iwatch')
    elif 70 < count <= 90:
        print('你中了一台appleTv')
    else:
        print('你中了一台appleCar')


if __name__ == '__main__':
    choice_gift_new()