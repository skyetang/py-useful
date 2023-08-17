# coding:utf-8
# 安装requests库
# pip install requests -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
import os.path
import time
import urllib.parse
import requests
from bs4 import BeautifulSoup
import json

# 登录信息和目标用户ID
cookie = ''
user_id = ''

form_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': cookie
}
index_res = requests.get(f'https://www.douyin.com/user/{user_id}', headers=form_header)
index_content = index_res.text
index_soup = BeautifulSoup(index_content, 'html.parser')
index_a = index_soup.find_all('a', attrs={'class': 'B3AsdZT9 chmb2GX8'})
index_title = index_soup.find('title').string

for item in index_a:
    print(item['href'])
    video_href = f'https://www.douyin.com{item["href"]}'
    video_res = requests.get(video_href, headers=form_header)
    video_page_content = video_res.text
    video_soup = BeautifulSoup(video_page_content, 'html.parser')

    # 获取视频数据并解密和格式化，拿到原视频地址
    video_data = video_soup.find('script', attrs={'id': 'RENDER_DATA'})
    decode_data = urllib.parse.unquote(video_data.string)
    json_data = json.loads(decode_data)
    video_origin_url = 'https:' + json_data['74931a6b75e09238f154ab1577c994c9']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
    print(video_origin_url)

    # 获取视频标题
    video_title = video_soup.find('title').string + '.mp4'

    # 打开原视频链接，创建文件夹，并将视频保存到相应的位置
    video_content = requests.get(url=video_origin_url, headers=form_header).content
    stor_url = f'G:/DouYin/{index_title}/'
    if not os.path.exists(stor_url):
        os.makedirs(stor_url)
    with open(stor_url + video_title, mode='wb') as f:
        f.write(video_content)
    print(f'{stor_url}{video_title}文件已保存')
    print('== 休息5s ==')
    time.sleep(5)
    print('== 5S时间到，继续工作 ==')
