f = [1, 2, 3]
g = (1, 2, 3)
h = {1, 2, 3}
print(tuple(f), set(f))
print(type(tuple(f)), type(set(f)))
print(tuple(f) == g)
print(set(f) == h)
# 不是相同的类存地址
print(tuple(f) is g)

print(list(h))

print(str(f), type(str(f))) #'[1, 2, 3]'
print(list(str(f)))