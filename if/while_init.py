# coding:utf-8

count = 0
total = 0

while count <= 100:
    total += count
    count += 1
    if count == 10:
        print('count 到10了')
    elif count == 50:
        print('count 到50了')
    elif count == 99:
        print('count 马上到100了')

print(total, count)

users = ['aiya', 'xiaohua', 'xiansan']
index = 0
length = len(users)

while index <= length - 1:
    print(users[index])
    index += 1