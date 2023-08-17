# coding:utf-8

import os
import os.path

path = os.getcwd()
print(path, type(path))
# 判断是否是绝对路径
print(os.path.isabs(path))
print(os.path.isabs('test'))

make_path = f'{path}/test2'
# 当文件存在时，则无法创建文件了
# if not os.path.exists(make_path):
#     os.makedirs(make_path)
#
new_path = f'{path}/test1'
# if os.path.exists(new_path):
#     os.removedirs(new_path)

data = os.listdir(path)
print(data)

# 通过join组成新路径
new_path2 = os.path.join(path, 'test2', 'abc')
print(new_path2)
# if os.path.exists(new_path2):
#     os.removedirs(new_path2)
#
# if os.path.exists('test3'):
#     os.removedirs('test3')

# removedirs 把整个层级全部删,如果最后一层级的文件夹不为空，则无法删除
os.removedirs('test3/test11')

# os.rename('test3', 'test3_new')
# os.rename('main_new.py', 'main.py')

# 只会删除指定路径的最后一个层级的文件夹, 且如果指定的文件夹不为空，则不能被删除
# os.rmdir(f'{path}/test1/abc')
# os.rmdir('test1')

# split 把最后一层和前面的路径分割
print(os.path.split(path))

print(os.path.isfile('pack_os.py'))
print('--', os.path.isdir(os.path.split(path)[0]))

print(dir(os.path))

