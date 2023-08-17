# coding:utf-8

a = 'abc'
print(a.split())

b = 'a,b,c'
print(b.split(','))
print(b.split(',', 1))

test = ['a', 'b', 'c']
test_str = '|'.join(test)
print(test_str)

test2 = ['1.2', '2', '3']
print('|'.join(test2))

# 列表里面只能是字符串，不能是数字，字典，元组，None
# test3 = [{'name': 'age'}, {'name': 'sex'}]
# print('.'.join(test3))
# 报错

str = 'a b d c g f e w'
split_str = str.split()
print(split_str)
split_str.sort()
new_str = ' '.join(split_str)
print(new_str)

sort_str_new = 'aidqpcsfsd'
res = sorted(sort_str_new)
print(''.join(res))