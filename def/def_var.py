# coding:utf-8
# 局部变量，无法在函数外，也就是全局当中读取使用
# 全局变量，只能在函数内读取，却不能改变全局变量的值
# global 可以在局部体内，改变全局变量的值(实际使用中不建议）
name = 'aiya'


def test():
    print(name)


test()


def test1():
    name='张三'
    print('函数体内', name)

test1()
print('函数体外', name)


def test2():
    global name
    name = 'lisi'


test2()
print(name)


_dict = {'a': 1, 'b': 2, 'c': 3}


def test3():
    _dict['d'] = 4
    del _dict['a']
    _dict.pop('b')

test3()
print(_dict)
