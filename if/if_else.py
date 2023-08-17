# coding:utf-8

url = 'https://www.baidu.com'

if 'www.baidu.com' in url:
    print('你查看的是百度网站')
else:
    print('你的网址有误')

if 'www.baidu.ccom' in url:
    _url = 'www.baidu.com'
else:
    _url = None
print('_url is %s' % _url)