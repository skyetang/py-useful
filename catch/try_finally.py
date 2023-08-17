# coding:utf-8

# 无论是否发生异常，一定会执行代码块
# 在函数中，即便在try或except中进行了return 也依然会执行finally语法块
# try语法至少要伴随except 或finally中的一个来使用

def test1():
    try:
        1 / 0
    except Exception as e:
        print(e)
    finally:
        return 'finally'


result = test1()
print(result)


def test2():
    try:
        1 / 0
    except Exception as e:
        print(1111)
        return e
    finally:
        print('finally')


print('--02--')
result = test2()
print(result)


def test3():
    try:
        print('1111')
        return 'try'
    except Exception as e:
        print(e)
    finally:
        print('finally test')


print('--03--')
result = test3()
print(result)


def test4():
    try:
        1 / 0
    except Exception as e:
        return e
    # 同时有多个return时，finally的return会覆盖之前的return
    finally:
        return 'finally'


print('--04--')
result = test4()
print(result)


def test5():
    try:
        return 'try'
    except Exception as e:
        print(e)
    finally:
        return 'finally'


print('--05--')
result = test5()
print(result)


def test6():
    try:
        1 / 0
    # 即使出错了，也不会中断执行，会继续执行下去
    # 如果finally里面是return，则连报错也不会出现，会继续执行finaly
    finally:
        print('finally')


print('--06--')
test6()