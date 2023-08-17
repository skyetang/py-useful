# coding:utf-8

fruits = {
    'apple': 30,
    'banana': 50,
    'pear': 100
}

real_fruits = fruits.copy()
print(real_fruits)

real_fruits['orange'] = 50
real_fruits.update({ 'cherry': 100})

print(f'real{real_fruits}')
print(fruits)

real_fruits['apple'] = real_fruits['apple'] - 5
real_fruits['pear'] -= 3
print(real_fruits)

real_fruits.clear()
print('第二天')
real_fruits = fruits.copy()
print(real_fruits)