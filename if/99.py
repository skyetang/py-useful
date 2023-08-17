# coding:utf-8

l = range(1, 10)

for i in l:
   for j in l:
       print('{} * {} = {}'.format(j, i, j*i), end='  ')
       if i == j:
           print('')
           break


print('for 乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(j, i, j*1), end=' ')
    print('')


print('while 乘法表')
i = 1
j = 1
while i <= 9:
    while j <= i:
        print('{} * {} = {}'.format(j, i, j*i), end=' ')
        j +=1
    print('')
    j = 1
    i += 1