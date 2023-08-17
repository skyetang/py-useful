# coding:utf-8
# dict.keys() -> 返回一个keys的伪列表

my_dict = {'name' : 'skye', 'id' : '0023', 'price' : '33.9', 'author' : 'NN'}
key_titile = my_dict.keys()
# 返回的伪列表无列表的所有功能
print(key_titile)

# 通过list改变格式后，会有列表的所有功能,因为key 是唯一的，所以该列表的值也都是唯一不重复的
my_keys = list(my_dict.keys())
print(my_keys)
my_keys.append('address')
print(my_keys)
print(my_keys[2:4])

#  get 方法没有找到keys值，不会报错，但有逻辑判断效率比[]低一些
name = my_dict.get('name')
# []方法找不到对应的值会报错，但是效率更高
name2 = my_dict['name']
# 查找不到的情况，会返回后面的默认值
name_def = my_dict.get('idx', '999')
print(name)
print(name2)
print(name_def)