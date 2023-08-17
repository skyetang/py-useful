# coding: utf-8
import time
import os.path
import requests
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


# 目标ID和条数
user_id = ''
num = 90


# 以下开始不用修改
form_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'cookie': ''
}

driver = webdriver.Chrome()
driver.get(f'https://www.douyin.com/user/{user_id}')
main_window = driver.current_window_handle
time.sleep(10)
print('-----等待主页加载完毕----')
index_title = driver.title

def drop_down():
    for x in range(1, math.ceil(num/18), 1):
        print(x)
        time.sleep(3)
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
        driver.execute_script(js)
drop_down()

# 定位到视频列表，获取链接数据
ul = driver.find_element(By.CLASS_NAME, 'EZC0YBrG')
ul_a = ul.find_elements(By.TAG_NAME, 'a')

# 给视频添加序列号
index = 0
for a in ul_a:
    index += 1
    try:
        video_href = a.get_attribute('href')
        driver.execute_script(f"window.open('{video_href}', 'new_window')")
        driver.switch_to.window(driver.window_handles[-1])
        print('切换到新页面，准备开始工作')
        time.sleep(5)
        video_origin_url = driver.find_element(By.TAG_NAME, 'source').get_attribute('src')
        print(video_origin_url)
        video_title = f'{index}-{driver.title}.mp4'
        # 打开原视频链接，创建文件夹，并将视频保存到相应的位置
        video_content = requests.get(url=video_origin_url, headers=form_header).content
        # 设置视频保存位置
        stor_url = f'G:/DouYin/{index_title}/'
        if not os.path.exists(stor_url):
            os.makedirs(stor_url)
        with open(stor_url + video_title, mode='wb') as f:
            f.write(video_content)
        print(f'{stor_url}{video_title}文件已保存')
    except Exception as e:
        print(e)
    print('切回主页面')
    driver.switch_to.window(main_window)
    print('== 休息3s ==')
    time.sleep(3)

