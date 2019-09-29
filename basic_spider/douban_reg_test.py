import requests
import re

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/77.0.3865.90 Safari/537.36'}
content = requests.get('https://book.douban.com/', headers=headers).text
html = '''
<!DOCTYPE html>
<html lang="zh-CN" class="ua-mac ua-webkit book-new-nav">
  <head>
    <meta charset="utf-8">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
  <meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.douban.com/book/">
  <meta name="keywords" content="豆瓣读书,新书速递,畅销书,书评,书单"/>
  <meta name="description" content="记录你读过的、想读和正在读的书，顺便打分，添加标签及个人附注，写评论。根据你的口味，推荐适合的书给你。" />
  <meta name="verify-v1" content="EYARGSAVd5U+06FeTmxO8Mj28Fc/hM/9PqMfrlMo8YA=">
  <meta property="wb:webmaster" content="7c86191e898cd20d">
  <meta property="qc:admins" content="1520412177364752166375">
'''
print(content)
patternTDK = re.compile('keywords".*?content="(.*?)".*?description.*?content="(.*?)"', re.S)
# pattern = re.compile('<div*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)"</span>.*?</div>', re.S)
pattern = re.compile('cover.*?href="(.*?)" title="(.*?)".*?author">\n(.*?)\n.*?year">\n(.*?)\n.*?publisher">\n(.*?)\n', re.S)

resultsTDK = re.findall(patternTDK, content)
results = re.findall(pattern, content)
print(resultsTDK)
print(results)

for result in results:
    url, title, author, year, publisher = result
    title = re.sub('\s', '', title)
    author = re.sub('\s', '', author)
    year = re.sub('\s', '', year)
    publisher = re.sub('\s', '', publisher)
    print(url, title, author, year, publisher)
