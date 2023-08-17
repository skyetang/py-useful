# coding:utf-8

# __str__ 如果定义了该函数，当print当前实例化对象的时候，会返回该函数的Return信息，一般用于对类的说明性文字
# __getattr__ 当调用的属性或者方法不存在时，会返该方法定义的信息
# __setattr__ 拦截当前类中不存在的属性和值，会触发该函数，该函数可以进行业务处理
# __call__ 本质是将一个类变成一个函数直接调用

class Test(object):
    two = False
    __three = False

    def __init__(self, one=True):
        self.one = one

    def __str__(self):
        return 'this is a test class'

    def __getattr__(self, item):
        print(f'key:{item}并不存在')

    def get_three(self):
        print('类中可以get私有three:', self.__three)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        print('---', self.__dict__)

    def __call__(self, *args, **kwargs):
        print('call will start')
        print(args, kwargs)


t = Test()
print(t)
t.a
t.get_three()

t.name = 'aiya'
t('yige')


class Test2(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __getattr__(self, key):
        if self.__attr:
            key = f'{self.__attr}.{key}'
        else:
            key = key
        print(key)
        return Test2(key)

    def __call__(self, name='aiya'):
        print(f'key is {name}')
        return Test2()


t2 = Test2()
t2.a.b.cd.e('xxx').f('ffff').g('ggg')