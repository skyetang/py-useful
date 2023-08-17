# coding:utf-8

import hashlib
import time

base_sign = 'maoku'


def custom():
    a_timestamp = int(time.time())
    _token = f'{base_sign}{a_timestamp}'
    # 参数token要为比特类型
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    print(hashobj)
    a_token = hashobj.hexdigest()
    print('a_token', a_token, type(a_token))
    return a_token,a_timestamp


def b_service_check(token, timestamp):
    _token = f'{base_sign}{timestamp}'
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False


if __name__ == '__main__':
    a_token, a_timestamp = custom()
    result = b_service_check(a_token, a_timestamp)
    if result:
        print('a合法，b可进行服务')
    else:
        print('a不合法，b不可进行服务')