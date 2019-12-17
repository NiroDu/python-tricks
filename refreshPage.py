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

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)


def refresh():
    try:
        # browser.get('http://xdcs.ximalaya.com/')
        time.sleep(100)
        # 刷新
        browser.refresh()
        refresh()
    except TimeoutException:
        return refresh()

def get():
    try:
        browser.get('http://xdcs.ximalaya.com/')
        refresh()
    except TimeoutException:
        return get()


def main():
    try:
        get()
    except Exception:
        print('出错啦')
    finally:
        browser.close()


if __name__ == '__main__':
    main()
