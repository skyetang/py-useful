# coding:utf-8
import copy

list_arr = ['python', 'html', 'javascript']
list_sort = list_arr.sort()

print(list_arr)

A = ['hello', 'hi']
A.clear()
print(A)

B = [1, 2, 3]
C =B.copy()

print(B, C)

# 深拷贝
D = [[1, 3, 4], [4, 5, 6]]
E = copy.deepcopy(D)
print(f'E的值是{E}')
print('E的值是 %s' % E)
print('E的值是{}'.format(E))
D[0].append(5)
print(D)
print(E)

# extend 将其它元素扩展到当前列表中

students = ['xiao', 'hua']
new_students = ['hei']
students.extend(new_students)
print(students)
