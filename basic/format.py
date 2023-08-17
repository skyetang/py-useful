# coding:utf-8

info = 'my name is %s, my age is %s'

name_01 = 'hx'
age_01 = 20
name_02 = 'xiaomu'
age_02 = '22'

print(info % (name_01, age_01))
print(info % (name_02, age_02))

language = ['html', 'css', 'js']
print(info % ('skye', language))

info_02 = 'my name is {}, my age is {}'
print(info_02.format(name_01, age_01))

# 变量名一定要先定义才行
info_03 = f'my name is {name_01}, my age is {age_01}'
print(info_03)

print('ar is {:c}'.format(123))