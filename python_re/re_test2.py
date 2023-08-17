# coding:utf-8

import re

url = 'https://www.baidu.com/'


def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+', url)
    print(result)
    if len(result) != 0:
        return True
    else:
        return False


def get_url(data):
    result = re.findall('http\w*://(\w*\.*\w+\.\w+)', url)
    print(result)
    if len(result) != 0:
        return result[0]
    else:
        return False


email = 'forb@yeah.net'


def get_email(data):
    result = re.findall('.+@.+\.[a-zA-Z]+', data)
    return result


html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')


def get_html_data(data):
    result = re.findall('style="(.*?)"', data)
    return result

def get_all_data_html(data):
    result = re.findall('="(.+?)"', data)
    return result


if __name__ == '__main__':
    result = check_url(url)
    print(result)
    print(get_url(url))
    print(get_email(email))
    print(get_html_data(html))
    print(get_all_data_html(html))