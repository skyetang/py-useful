# coding:utf-8

drivers = ['a', 'b', 'c']
testers = ['b', 'c', 'd']
tec = ['c', 'f', 'g']
cool = ['w', 'u']

driver_set = set(drivers)
test_set = set(testers)
tec_set = set(tec)

# 返回drivers 和testers 对比不同的元素
diff_a = driver_set.difference(test_set)
print(diff_a)

# 返回drivers 和testers,tec 的交集
inter_a = driver_set.intersection(test_set, tec_set)
print(inter_a)

# 返回包含了所有集合的元素，重复的元素只会出现一次

union_a = driver_set.union(test_set, tec_set)
print(union_a)
union_b = driver_set.union(testers, tec)
print(union_b)


# isdisjoint 判断两个集合是否包含相同的元素，如果没有返回True，否则有返False
is_a = driver_set.isdisjoint(cool)
print(is_a)