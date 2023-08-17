# coding:utf-8
# 私有变量，与私有方法
class Cat(object):
    __cat_type = 'cat'

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def run(self):
        result = self.__run()
        print(result)

    # 私有函数
    def __run(self):
        return f'{self.__cat_type}小猫{self.name}是一个{self.__sex}在奔跑'

    def jump(self):
        # pass 对函数体进行占位
        result = self.__jump()
        print(result)

    def __jump(self):
        return f'小猫{self.name}在跳跃'


class Test(object):
    # 类或者函数代码块的占位符
    pass


cat = Cat('米米儿', 'boy')
cat.run()
cat.jump()
print(cat.name)
print(dir(cat))

