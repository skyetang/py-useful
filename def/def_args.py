# coding:utf-8

def add(a, b, c=3):
    return a + b + c


result = add(1, 2)
print(result)

result = add(1, 3, 5)
print(result)

# args 将无参数的值合并成元组
# kwargs 将有参数与默认值的赋值语句合并成字典

def test_args(*args, **kwargs):
    print(args, type(args), 'argstype')
    print(kwargs, type(kwargs))


test_args(1,2,3,4,5,name='aiya', age=3)


def test_args_super(file, *args, **kwargs):
    if len(args) >= 1:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print('----')
    print(file)
    print(args, len(args))
    print(kwargs, len(kwargs))
    print('===')


# test_args_super(1, 2, 3, name='aiya')
a = ('python', 'js')
b = {'name': 'aiya'}
test_args_super(12, 15, a, b, age=12)
test_args_super(*a, **b)


def add(a, b=1):
    print(a + b)


add(1)
add(1, 2)
add(a=1, b=2)
add(b=2, a=1)
#add(b=2)   #会报错


def test(a, b=1, *args):
    print(a, b, args)


s = ('11', '2')
ss = {'name': 'aiya', 'age':1}
test(1, 2, 4, 6666, 7777)

# 参数可以随意更换位置，但在使用传参时需要通过赋值语句对参数赋值调用，所以，**kwargs 不能在乱序参数中使用，
# 因为它是将有参数的都合并成字典，届时将分不清哪些是必须参数，哪些应该合并成字典
def test2(*args, a, b=1):
    print(a, b, args, 'test2')


test2(a=1, *s)


def test3(a, b=1, **kwargs):
    print(a, b, kwargs)


d = {'name':'aiya'}
test3(1, 2, name='aiya')
test3(a=1, b=2, name='aiya')
# 不按顺序传参可以，则需要通过赋值语句的方式传参
test3(name='aiya', age=12, a=1, b=2, sex='man')
test3(**d, a=2, b=4)
