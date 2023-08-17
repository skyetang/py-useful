# coding:utf-8

a = 'hello aiya'
print(a, type(a))

b = b'hello aiya'
print(b, type(b))

print(b.capitalize())
print(b.replace(b'hello', b'hi'))
print(b[:3])
print(b.find(b'e'))

# dir 返回该变量拥有的所有属性方法
print(dir(b))

# encode 返回一个bytes类型的值，只存在于字符串类型中
# decode 返回一个字符串的值，只存在于bytes类型的数据中
c = 'hello 小哈'
d = c.encode('utf-8')
print(d, type(d))
e = d.decode('utf-8')
print(e, type(e))





