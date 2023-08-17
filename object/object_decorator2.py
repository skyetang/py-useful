# coding:utf-8

class Test(object):
    def __init__(self, a):
        self.a = a

    def run(self):
        print('run')
        self.jump()
        self.sleep()

    # 将类函数可以不经过实便化而直接被调用，要传递一个cls必要参数
    @classmethod
    def jump(cls):
        print('jump')

    # 被该装饰器调用的函数，不许传递self,cls，且无法在该函数内调用其它类函数或变量
    @staticmethod
    def sleep():
        print('sleep')

    # 将类函数的执行免去括弧，类似于调用属性
    # 设置方法，则需要用到@xxx.setter
    @property
    def go(self):
        print('go')


t = Test('a')
t.run()
Test.jump()
Test.sleep()
t.sleep()
t.jump()
t.go


class Test1(object):
    def __init__(self, name):
        self.__n = name

    @property
    def name(self):
        return self.__n

    @name.setter
    def name(self, value):
        self.__n = value

t1 = Test1('aiya')
print(t1.name)

t1.name = '艾雅'
print(t1.name)