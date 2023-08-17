# coding:utf-8

books = []
print(id(books))
# append添加的元素都是从后面添加
books.append('python')
print(books)
print(id(books))

true_test = True
books.append(true_test)
print(books)

books.insert(2, 'js')

# 当insert 指定的位置超过原列表的长度时，只会添加在最后，并不会添加到指定位置
books.insert(5, 'html')
print(books)

animals = ['cat', 'dog']

# 计算列表中的元素有多少个
cat = animals.count('cat')
print(cat)
print('小猫有 {}只'.format(cat))
print(f'小猫有 {cat} 只')
print('小猫有 %s 只\n' % (cat))

animals_dic = [
    {'name': 'dog'},
    {'name': 'dog'},
    {'name': 'dog'},
]

print(animals_dic.count({'name':'dog'}))



