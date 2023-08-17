# coding:utf-8
# 无法确定是哪种异常的情况下的通用捕获方法，使用except Exception as e:
# 确定是哪种异常的情况下使用具体的捕获方法： except <具体的异常类型> as e:
# 可以通过将多个异常组成一个元组来传递，但是当捕获到第一个后，不会继续往下捕获

def upper(str_data):
    new_str = 'None'
    # 执行完try或except后，程序会继续往下走
    try:
        new_str = str_data.upper()
    except Exception as e:
        print(f'程序出错了！！！{e}')
    return new_str


result = upper(1)
print('---', result)


def test():
    try:
        print('try front')
        # try 当中如果遇到错误后，该错误后面的语句将不会再执行，直接进入到except当中去执行
        1 / 0
        print('try back')
    except Exception as e:
        print(e)


test()


# def test1():
#    try:
#        print('hello')
#        print(name)
# 如果是通过具体的异常名称来捕获异常，当出现的异常与指定的不匹配时，则会报错
#    except ZeroDivisionError as e:
#        print(e)


# test1()

# 捕获多个异常，匹配到哪个输出哪个
def test2():
    try:
        print('heelo')
        print(name)
    except (ZeroDivisionError, NameError) as e:
        print(e)


test2()