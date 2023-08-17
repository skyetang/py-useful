# 构造4页连接
# 发送请示，请求4页数据
# 获取response数据
# 写入本地html文件
import requests

header = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

for i in range(1, 5):
    url = 'http://yushu.talelin.com/book/search?q=python&page={}'.format(i)
    res = requests.get(url=url, headers=header)
    html_file_name = 'page_{}.html'.format(i)
    with open(html_file_name, 'w', encoding='utf-8') as f:
        f.write(res.text)
    print('{}文件已下载好'.format(html_file_name))