from selenium import webdriver
# driver = webdriver.Chrome('/Users/xmly/Downloads/chromedriver')
driver = webdriver.Chrome()
driver.get('https://www.tutorabc.com')
print(driver.page_source)