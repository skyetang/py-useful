# coding:utf-8

class Tool(object):
    def __init__(self, tool):
        self.tool = tool
        print('tool', tool)

    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'


class Food(object):
    def __init__(self, food):
        self.food = food
        print('food', food)

    def work(self):
        return 'food work'

    def cake(self):
        return 'i like cake'


class Person(Food, Tool):
    pass


if __name__ == '__main__':
    p = Person('xxx')
    print(p.car())
    print(p.cake())
    print(p.work())
    # 可以展现出该类是如何继承别的父类的
    print(Person.__mro__)