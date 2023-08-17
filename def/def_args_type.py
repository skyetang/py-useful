# coding:utf-8

def add(a: int, b: int = 3):
    print(a + b)


add(1, 2)
add('hello', 'aiya')


def test(a: int, b: int = 3, *args:int, **kwargs:str):
    print(a, b, args, kwargs)


test(1, 2, 3, '4', nmae='aiya')