# coding:utf-8

import base64

replace_one = '%'
replace_two = '$'


def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
        print(data, type(data))
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')
    # base64 是谁都可以加密解密的，所以在加密后的字符串再处理一次，则就不是所有人都能够再解密了，需要找到对应的替换方法才行
    _data = base64.encodebytes(data).decode('utf-8')
    # base64.encodebytes(data) 返回一个byte类型，然后通过decode 解析成字符串类型
    _data = _data.replace('a', replace_one).replace('3', replace_two)
    return _data


def decode(data):
    if not isinstance(data, bytes):
        raise TypeError('data need bytes')
    # 在b类型中的替换，都得转换成byte类型才可以
    b_replace_one = replace_one.encode('utf-8')
    b_replace_two = replace_two.encode('utf-8')
    _data = data.replace(b_replace_one, b'a').replace(b_replace_two, b'3')
    return base64.decodebytes(_data).decode('utf-8')


if __name__ == '__main__':
    result = encode('hello xiaoya')
    print(result, type(result))
    new_res = decode(result.encode('utf-8'))
    print(new_res)

