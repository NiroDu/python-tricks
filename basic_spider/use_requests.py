import osimport requestsheaders = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '                         'Chrome/77.0.3865.90 Safari/537.36'}response = requests.get('https://www.baidu.com', headers=headers)# print(response.text)# print(response.headers)# print(response.status_code)# print(response.content)# response = requests.get("http://www.baidu.com")# # print(response.cookies)# for key, value in response.cookies.items():#     print(key + '=' + value)imgData = requests.get('https://www.baidu.com/img/xinshouyedong_4f93b2577f07c164ae8efa0412dd6808.gif', headers=headers)print(imgData.content)path = "./tmp"os.mkdir(path, 0o755)print("目录已创建")with open('./tmp/test.gif', 'wb') as file:    file.write(imgData.content)    file.close()