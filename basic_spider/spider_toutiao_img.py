from json.decoder import JSONDecodeError
from urllib.parse import urlencode
from hashlib import md5
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from multiprocessing import Pool

import os
import requests
import json
import re
import pymongo as pymongo


# import ast
# from config.py import *
MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'

GROUP_START = 1
GROUP_END = 20
KEYWORD = '李知恩'

# 初始化MongoDB
client = pymongo.MongoClient(MONGO_URL, connect=False)
# 创建db对象
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    try:
        data = {
            'aid': '24',
            'app_name': 'web_search',
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'en_qc': '1',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis',
            'timestamp': '1569912626721'
        }
        base = 'https://www.toutiao.com/api/search/content/'
        params = urlencode(data)
        url = base + '?' + params
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/77.0.3865.90 Safari/537.36',
                   'cookie': 'tt_webid=6742291602004723214; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6742291602004723214; csrftoken=4fd3030793fe719a500591f6a482cd56; s_v_web_id=cfba6b89e0095c73ba3fbcd003c889cd; __tasessionId=163fn3ih21569927485862; RT="z=1&dm=toutiao.com&si=5q3sjj4ns2m&ss=k17rd911&sl=a&tt=ayz&obo=3&ld=3a7r&r=4d707aab8209c38c1dfc5a11a3ddf8e5&ul=3a80&hd=3aaq"'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求检索页出错')
        return None
    except ReadTimeout:
        print('Timeout')
        return None
    except ConnectionError:
        print('Connection error')
        return None


def parse_page_index(html):
    try:
        # 将已编码的 JSON 字符串解码为 Python 对象
        data = json.loads(html)
        # 判断存在data对象的键值中存在'data'
        if data and 'data' in data.keys():
            if data['data'] is None:
                print('数据为空' + '!' * 100)
            if data['data']:
                for item in data['data']:
                    if 'article_url' in item.keys():
                        # 若获取不到article_url的值，会返回None，所以只取有article_url的值
                        # 使用yield，返回一个可迭代的生成器
                        yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'cookie': 'tt_webid=6742291602004723214; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6742291602004723214; csrftoken=4fd3030793fe719a500591f6a482cd56; s_v_web_id=cfba6b89e0095c73ba3fbcd003c889cd; __tasessionId=163fn3ih21569927485862; RT="z=1&dm=toutiao.com&si=5q3sjj4ns2m&ss=k17rd911&sl=a&tt=ayz&obo=3&ld=3a7r&r=4d707aab8209c38c1dfc5a11a3ddf8e5&ul=3a80"'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None
    except ReadTimeout:
        print('Timeout')
        return None
    except ConnectionError:
        print('Connection error')
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('title')[0].get_text()
    print(title)
    image_pattern = re.compile('gallery: JSON.parse\((.*?)\),.*?siblingList', re.S)
    result = re.search(image_pattern, html)
    if result:
        # 解析json，相当于js里的json.parse
        data = json.loads(result.group(1))
        # str类型转化到dic类型
        data = json.loads(data)
        # 将data从字符串类型转化为字典类型，方便使用keys()检查存在的key
        # http://funhacks.net/2016/04/24/python_%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E4%B8%BA%E5%AD%97%E5%85%B8/
        # data = ast.literal_eval(data)
        if 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            # 获取到了图片链接，所以要下载图片
            for image in images:
                download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert_one(result):
        print('成功保存到数据库')
        return True
    return False


def save_image(content):
    # 本地路径，md5使得同样的文件同名，jpg后缀
    # os.getcwd()是当前目录
    # file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    # os.mkdir('./tmp/images/', 0o755)
    file_path = '{0}/{1}.{2}'.format('./tmp/images/', md5(content).hexdigest(), 'jpg')
    # 假如文件不存在，就存下来
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            file.write(content)
            file.close()


def download_image(url):
    print('正在下载: ', url)
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'cookie': 'tt_webid=6742291602004723214; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6742291602004723214; csrftoken=4fd3030793fe719a500591f6a482cd56; s_v_web_id=cfba6b89e0095c73ba3fbcd003c889cd; __tasessionId=ctvy5v2h31569915827594',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # response.content 返回的是二进制格式
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错')
        return None
    except ReadTimeout:
        print('Timeout')
        return None
    except ConnectionError:
        print('Connection error')
        return None


def main(offset):
    html = get_page_index(offset, KEYWORD)
    # 在这里接收yield返回的'article_url'内容
    for url in parse_page_index(html):
        html_detail = get_page_detail(url)
        if html_detail:
            result = parse_page_detail(html_detail, url)
            # if result is None:
            #     # 不对空对象进行任何处理
            #     pass
            # else:
            #     save_to_mongo(result)
            if result:
                save_to_mongo(result)


if __name__ == '__main__':
    # # 单进程下载
    # for i in range(1, 20):
    #     main(i*20)

    # 多进程下载
    # 开启限制 https://www.codetd.com/en/article/6433023
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
