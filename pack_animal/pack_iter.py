# coding:utf-8

# 迭代器减少对内存的消耗，提升执行效率
iter_obj = iter((1, 2, 3))


def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None

# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

# 返回一个迭代器对象
def make_iter():
    for i in range(10):
        yield i


iter_obj =make_iter()
print(type(iter_obj))
print(next(iter_obj))

# 当读取完一个迭代器对象后，数据就为空了，第二次就拿 不到了
for i in iter_obj:
    print(i)
print('------')
for i in iter_obj:
    print(i)


# 通过这种方式也可以返回一个迭代器对象
iter_obj = (i for i in range(10))

for i in iter_obj:
    print(i)
print('=====')
for i in iter_obj:
    print(i)