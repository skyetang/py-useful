# coding:utf-8

import os


def create_package(path):
    if os.path.exists(path):
        raise Exception(f'已经存在{path}，不可创建')
    os.makedirs(path)
    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write('# coding:utf-8\n')
    f.close()


class Open(object):
    def __init__(self, path, mode='w', is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode)
        if self.is_return:
            message = f'{message}\n'
        f.write(message)
        f.close()

    def read(self, is_strip=False):
        result = []
        # with 代码块执行后，会自动关闭文件
        with open(self.path, self.mode, encoding='utf-8') as f:
            data = f.readlines()
        for line in data:
            if is_strip:
                temp = line.strip()
                if temp != '':
                    result.append(temp)
            elif line != '':
                result.append(line)
        print(result)

if __name__ == '__main__':
    current_path = os.getcwd()
    path = os.path.join(current_path, 'test1')
    # create_package(path)


    open_path = os.path.join(current_path, 'b.txt')
    o = Open(open_path, mode='r')
    #o.write('hello aiya')
    o.read()
