# coding:utf-8

# filter(func, list)  对list的每个item进行条件过滤,满足条件的会放到一个新的filter对象中，可通过list进行格式化读取
# map(func, list) 对列表中的每个成员执行函数，将执行后判断的结果放到新的list中，返回map对象
# reduce(func, list) 对列表中的数据进行累加，返回累加后的结果

from functools import reduce

fruits = ['apple', 'orange', 'banana']

result = filter(lambda x: 'e' in x, fruits)
print(list(result))
print(fruits)


def filter_func(item):
    if 'e' in item:
        return True


filter_result = filter(filter_func, fruits)
print(list(filter_result))

map_result = map(filter_func, fruits)
print(list(map_result))

reduce_result = reduce(lambda x, y: x + y, [0, 1, 2, 3, 7])
print(reduce_result)

# 字符串也可以累加
reduce_result_str = reduce(lambda x,y: x + y, fruits)
print(reduce_result_str)