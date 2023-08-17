# coding:utf-8

projects = {
    'ipad' : { 'name': 'pad', 'price': 2200},
    'iphone': { 'name': 'iphone', 'price': 3300},
    'pc': { 'name' : 'pc', 'price': 4400},
    'mac': { 'name' : 'mac', 'price' : 5500}
}

print(projects.keys())
print('一个中学生买了一台{}，价格是{}'.format(projects['ipad']['name'], projects['ipad']['price']))
print(f'一个大学生，买了一台{projects["mac"]}, 价格是{projects["mac"]["price"]}')
pop_value = projects.pop('pc')

print(f'pop返回的值是{pop_value}')
print(f'pop删除后的字典值是{projects}')

del projects['iphone']
print(projects)

projects.clear()
print(projects)

del projects
# print(projects)  del删除字典后会报错
