# coding:utf-8

import json


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    # loads 将JSON字符串解码成python对象
    return json.loads(data)


def write(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            # 将python对象编码成JSON字符串
            _data = json.dumps(data)
            print('_data', _data, type(_data))
            f.write(_data)
        else:
            raise TypeError('data need dict')
    return True


data = {'name': '小华', 'age': 18, 'top': 176}


if __name__ == '__main__':
    write('test.json', data)
    print(read('test.json'))

    result = read('test.json')
    result['sex'] = 'body'
    write('test.json', result)