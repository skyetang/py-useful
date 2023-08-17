# coding:utf-8

users = [
    {'username': 'aiya', 'age': 33, 'top': 174, 'sex': '男'},
    {'username': 'xiaohua', 'age': 33, 'top': 174, 'sex': '女'},
    {'username': '李四', 'age': 33, 'top': 174, 'sex': '男'},
    {'username': '张三', 'age': 33, 'top': 174, 'sex': '男'},
]

man = []

for user in users:
    if user.get('sex') == '女':
        continue
    man.append(user)
    print('{}加入了行列'.format(user.get('username')))

print(man)

l = range(100)

for i in l:
    if i == 80:
        print('------')
        print('已经循环80次了，要退出了')
        break
    print(i)
else:
    print('循环正常退出了')
    