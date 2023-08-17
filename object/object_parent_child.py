# coding:utf-8
# object 是一个python内置的通用类，就是继承的写法
class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f'{self.name} are talking'

    def what_sex(self):
        if self.sex == 'girl':
            return f'{self.name} is girl'
        else:
            return f'{self.name} is boy'


class ChildOne(Parent):
    def play_football(self):
        return f'{self.name} are playing football'


class ChildTwo(Parent):
    def play_pingpong(self):
        return f'{self.name} are playing pingpong'


c_one = ChildOne('aiya', 'girl')
res = c_one.what_sex()
print(res)
res = c_one.play_football()
print(res)
c_two = ChildTwo('yige', 'boy')
res = c_two.play_pingpong()
print(res)

p = Parent('father', 'boy')
print(p.what_sex())