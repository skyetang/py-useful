# coding:utf-8
# super 在子类当中，调用父类的方法
# self 指当前的实例化对象
class Parent(object):
    def __init__(self, p):
        print('i am parent %s' % p)

    def talk(self):
        print('parent talk')


class ChildOne(Parent):
    pass


class Child(Parent):
    def __init__(self, p, c):
        super().__init__(p)
        print('i am child %s' % c)

    def all_talk(self):
        super().talk()
        print('child talk')


if __name__ == '__main__':
    c = Child('parent', 'child')
    c.all_talk()