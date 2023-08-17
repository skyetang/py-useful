# coding:utf-8

number = 10

if number > 10:
    print('number的值大于10')
elif 5 < number <= 10:
    print('number的值在5和10之间')
elif 0 < number <= 5:
    print('number的值是1~5')
else:
    print('number的值是0或者负数')

print('finish')

users = [
    ('aiya', 33, 90),
    ('xiaomu', 10, 99),
    ('xiaohua', 20, 87)
]

xiaohua = ['xiaohuas', 19, 100]

if users[0][0] == xiaohua[0]:
    xiaohua[0] = '%s_001'% xiaohua[0]
    users.append(xiaohua)
elif users[1][0] == xiaohua[0]:
    xiaohua[0] = '%s_001' % xiaohua[0]
    users.append(xiaohua)
elif users[2][0] == xiaohua[0]:
    xiaohua[0] = '%s_001' % xiaohua[0]
    users.append(xiaohua)
else:
    users.append(xiaohua)
print(users)