# coding:utf-8

str = 'python is a good language'
Nonn = None
str_arr = ['abc', 'cddd', 'aaaa']
list_arr = [13, 'abc', None, ['123', 'cccc']]
list_arr2 = ['fff']

if __name__ == '__main__':
    print(str)
    print(max(str))
    print(Nonn)
    print(max(str_arr))
    print(list_arr[1])
    print(id(list_arr))


list_arr = list_arr + list_arr2

print(list_arr)
print(id(list_arr))

list_arr[4] = ('1', '2')
print(list_arr)
print(id(list_arr))
print(type(list_arr))

list_arr[4] = 'testf'
print(list_arr)
