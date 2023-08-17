# coding:utf-8

import sys

modules = sys.modules
print(modules)







# sys.exit(1)

path = sys.path
print(path)

code = sys.getdefaultencoding()
print(code)

plate = sys.platform
print(plate)

# 返回python版本
print(sys.version)

# 可以通过外部terminal执行命令时传参，然后在文件当中获取数据
print(sys.argv)
