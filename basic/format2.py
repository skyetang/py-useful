# coding:utf-8

info = 'my name \n is hx'

print(info)

info_2 = 'my name is \'skye\''

print(info_2)

# r 让转义字符无效
info_3 = r'my name is \\skye \\'
print(info_3)

# r无法让格式化字符失效，只对转义字符有用
print(r'my name is %s' % 'skye')