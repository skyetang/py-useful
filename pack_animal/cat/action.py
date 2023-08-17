# coding:utf-8

cat_name = 'aiya'


def roar():
    return 'cat roar'


def jump():
    return 'cat jump'


def run():
    return 'cat run'


class Cat(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        return f'{self.name}在奔跑'