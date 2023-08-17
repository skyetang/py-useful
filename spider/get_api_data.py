# coding: utf-8

import requests
import json


# 登录信息和目标用户ID
cookie = ''
user_id = ''

form_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': cookie
}

data = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAvbazhADpx4mn9lXlzy_J1m_HDntUB_O3JjY-MCnEdQIQu8nwcZ8jB3g8uN3ax0yB&max_cursor=1679899627000&locate_item_id=7223271801277648187&locate_query=false&show_live_replay_strategy=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=114.0.0.0&browser_online=true&engine_name=Blink&engine_version=114.0.0.0&os_name=Windows&os_version=10&cpu_core_num=24&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7249698753672857149&msToken=7CR9wUTSs6h9rMeuBtWtqu2Img2ZJuq-xo8ocKgeNC23VGFuw5a8okuRTjkLzh95MLwxYf_bg5dDETnIUs8vGW-p46iJmLBpNiqcnSyfZKoLLgqH3eBXtThtMjexV2o=&X-Bogus=DFSzswVYh4hANx/PtJ5mKVXAIQ-B', headers=form_header)
print(data.content.decode('utf-8'))
