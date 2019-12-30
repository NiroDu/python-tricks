# 前置知识点
# dumps是将dict转化成str格式，loads是将str转化成dict格式。
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool


def get_one_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/77.0.3865.90 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name">.*?>(.*?)</a>.*?star">('
                         '.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        # 对获取到的图片进行下处理：掉@后的内容
        # 'https://p0.meituan.net/movie/76fc92cfa6c8f2959431b8aa604ef7ae126414.jpg@160w_220h_1e_1c'
        new_image = re.sub('(@.*)', '', item[1])
        # 返回生成器
        yield {
            'index': item[0],
            'image': new_image,
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as file:
        # TypeError: the JSON object must be str, not 'dict'
        # https://docs.python.org/zh-cn/3/library/json.html
        # 不允许ensure_ascii编码，使用utf-8
        file.write(json.dumps(content, ensure_ascii=False) + '\n')
        file.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    # 接收生成器的对象
    for item in parse_one_page(html):
        # print(item)
        write_to_file(item)


if __name__ == '__main__':
    # 单进程模式
    # for i in range(10):
    #     main(i*10)

    # 多进程模式，但是这样写入的index不是顺序的
    # https://docs.python.org/zh-cn/3/library/multiprocessing.html
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
    pool.close()
    pool.join()
