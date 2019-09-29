from selenium import webdriver
# driver = webdriver.Chrome('/Users/xmly/Downloads/chromedriver')
driver = webdriver.Chrome()
driver.get('https://www.taobao.com')
print(driver.page_source)
