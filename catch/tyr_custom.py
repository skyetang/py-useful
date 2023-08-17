# coding:utf-8

# raise:将信息以报错的形式抛出

def test(number):
    if number == 100:
        raise ValueError('number不可以是100')
    return number

# result = test(100)
# print(result)


def test2(number):
    try:
        return test(number) 
    except Exception as e:
        return e


result = test2(100)
print(result)


def test3():
    raise '错误了的测试'

# test3()


class NumberLimitError(Exception):
    def __init__(self, message):
        self.message = message


class NameLimitError(Exception):
    def __init__(self, message):
        self.message = message


# 自定义错误类型
def test4(name):
    if name == 'aiya':
        raise NameLimitError('aiya不支持填写')
    return name


def test5(number):
    if number > 100:
        raise NumberLimitError('数字不能大于100')
    return number


print('-------')
try:
    test4('aiya')
except NameLimitError as e:
    print(e)


try:
    test5(20)
except NumberLimitError as e:
    print(e)
