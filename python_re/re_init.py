# coding:utf-8

import re


def had_number(data):
    result = re.findall('\d', data)
    print(result)
    if len(result) != 0:
        return True
    return False


def remove_number(data):
    result = re.findall('\D', data)
    print(result)
    new_result = ''.join(result)
    return new_result


if __name__ == '__main__':
    str = 'i am aiya, i am 22'
    result = had_number(str)
    print(result)
    res = remove_number(str)
    print(res)