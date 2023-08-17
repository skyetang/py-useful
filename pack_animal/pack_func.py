# coding:utf-8

class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b

test = Test()
# vars返回实例化的字典信息
result = vars(test)
print(result)

# 判断是否存在某个属性
print(hasattr(test, 'a'))
print(hasattr(test, 'c'))

# setattr 自定义设置属性,内置的类不能通过此自定义属性
setattr(test, 'c', 3)
print(test.c)
print(vars(test))

# getattr 获取某个属性
print(getattr(list, 'append'))

# any 只要列表中有一个为True,就会返回True;;
# all 需要列表中所有为True,返回True,否则返回False

a = ['', 1]
b = [1, 'abc', 'a' in 'abc']
print(any(a))
print(all(b))


# 在命令行中进行参数传递，执行后可以命令行中输入内容，然后会在print中打印出来
food = input('你想吃什么:')
print(food)

help(input)

