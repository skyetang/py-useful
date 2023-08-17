# pip install requests --target F:\python\venv\lib\site-packages -i https://pypi.tuna.tsinghua.edu.cn/simple
import requests

res = requests.get(url='http://httpbin.org/ip')
print(res.text)


data = {'name': 'skye'}
res = requests.post(url='http://httpbin.org/post', data=data)
print(res.text)

# 设置请求参数
data = {'key1': 'value1', 'key2': 'value2'}
res = requests.get('http://httpbin.org/get', params=data)
print(res.url)
print(res.content)

# 获取图片数据需要用：content
res = requests.get('https://img.alicdn.com/imgextra/i2/O1CN01a69z6z1hJklCkBqOU_!!6000000004257-2-tps-174-106.png')
with open('logo.png', 'wb') as f:
    f.write(res.content)

# 设置header信息
header = {'useragent': 'pythonTest1'}
res = requests.get('http://httpbin.org/ip', timeout=2, headers=header)
print(res.text)
print(res.status_code)
print(res.request.headers)

# 可以查看当前发送cookie的URL，可以进行测试
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'hello skye'}
res = requests.get(url=url, cookies=cookies)
print(res.text)
print(res.request.headers)