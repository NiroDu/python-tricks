from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

import time
import pymongo
import re

KEYWORD = '皮卡丘'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def search():
    try:
        print('正在搜索...')
        browser.get('https://www.taobao.com')
        login_button = wait.until(
            (EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h')))
        )
        # 按住Command点击登陆按钮
        actions = ActionChains(browser)
        actions.key_down(Keys.COMMAND).click(login_button).key_up(Keys.COMMAND)
        actions.perform()
        # 切换到新窗口扫描二维码
        browser.switch_to.window(browser.window_handles[1])
        # 趁这10秒，赶紧登陆验证。。
        time.sleep(10)
        # 刷新
        browser.refresh()
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        input.send_keys(KEYWORD)
        submit = wait.until(
            (EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        )
        submit.click()
        # 获取总页数
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        print(total.text)
        get_products()
        return total.text
    except TimeoutException:
        return search()


def get_products():
    # 滑到浏览器底部
    js_code = '''
    var distance = 500;
    var timer = setInterval(function(){
        window.scrollTo(0, distance)
        distance = distance + 500
    }, 500)
    
    if(document.documentElement.scrollTop > 3000) {
        clearInterval(timer)
    }
    '''
    # browser.execute_script(js_code)
    # time.sleep(1)
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def next_page(page_number):
    print('正在翻页...', page_number)
    try:
        # 页数输入框
        input_page = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        # 页数输入框确定按钮
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input_page.clear()
        input_page.send_keys(page_number)
        submit.click()
        # 对比当前页和输入页是同一页
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert_one(result):
            print('存储到数据库成功', result)
    except Exception:
        print('存储到数据库失败', result)


def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        print(total)
        # 从第二页开始
        for i in range(2, total + 1):
            next_page(i)
    except Exception:
        print('出错啦')
    finally:
        browser.close()


if __name__ == '__main__':
    main()
