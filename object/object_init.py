# coding:utf-8

# 类，构造函数，变量，对象
# 类的self 指实例化对象，需要实例化后才能使用
def sleep(name):
    return name


class Person(object):
    # 构造函数
    sex = 'girl'

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}{self.sex}在奔跑')

    def jump(self):
        print(f'{self.name}在跳跃')

    def work(self):
        self.run()
        self.jump()
        result = sleep(self.name)
        print('sleep result', result)


aiya = Person('aiya')
aiya.name = 'Aiya'
aiya.jump()

yige = Person(name='yige')
yige.jump()
yige.top = 174
print(yige.top)
print(yige.age)

aiya.work()
print(dir(yige))
