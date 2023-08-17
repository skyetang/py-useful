# coding:utf-8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers) - 1)
print(numbers[9])

# 获取后的新列表数据，和原来的列表不同，是一个新的列表
# -1 是指最后一位元素
# 切片，左含右不含
print('获取列表完整数据：', numbers[:])
print('另一种获取完整列表的方法', numbers[0:])
print('第三种获取列表的方法', numbers[0: -1])
print('列表的反序', numbers[::-1])
print('列表的反向获取', numbers[-3:-1])
print('步长获取切片，跳跃获取', numbers[0:8:2])
print('切片生成空列表', numbers[0:0])

# 通过切片进行修改
numbers[2:5] = ['a', 'b', 'c']
print(numbers)
print(numbers.index('c'))

# 字符串可以通过find index 获取索引，但是不能更值

info = 'my name is skye'

# 查找不存在的值会返回-1
str_index = info.find('skye')

# index 如果查找的值不存在会报错
str_index2 = info.index('skye')
print(str_index)
print(str_index2)

# 当字符串被用于列表的Extend时，会被打散成数组
new_info = []
new_info.extend(info)
new_info2 = info[::-1]
print(new_info)
print(new_info2)