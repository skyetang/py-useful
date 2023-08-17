# coding:utf-8
# 匿名函数
f = lambda: print(1)
f()

f1 = lambda x, y=2: x > y
print(f1(1))

f2 = lambda x, y: x+y
print(f2(1, 4))

users = [
    {'name': 'aiya'},
    {'name': 'yige'},
    {'name': 'xiaohua'}
]
users.sort(key=lambda x: x['name'], reverse=True)
print(users)