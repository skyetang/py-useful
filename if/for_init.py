# coding:utf-8

l = ['chengdu', 'wuhan', 'shanhai', 'guangzhou']

for i in l:
    print(i)

print('finished')

for i in 'python':
    print(i)

users = ('chengdu', 'wuhan', 'beijing')

for name in users:
    if name == 'beijing':
        print('你好，北京')
    else:
        print('hello,欢迎来到%s'% name)
    print('-----------')

users = {'name': 'aiya', 'age': 33}

for i in users:
    print(i, users[i], '字典')

items = users.items()
print(items, 'items')

for key, value in users.items():
    print(key, value)

user_list=[
    {'username': 'aiya'},
    {'username': 'yige'}
]

for uses in user_list:
    print(uses.get('username'), uses.get('age'))

l = range(6)
print(l, type(l))

for i in l:
    print(i)
else:
    print('for循环结束了')

p = ['js', 'hmtl', 'java']
for index, item in enumerate(p):
    print(index, item)


