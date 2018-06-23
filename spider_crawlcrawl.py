#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import html
import requests
import schedule
import smtplib
from email.mime.text import MIMEText
import time

mailcount = 0

def gethtml(url):
    return requests.get(url).content.decode('utf-8')

def getcontext(utlhtml, xpaths):
    selector = html.fromstring(utlhtml)
    return selector.xpath(xpaths)

def runjob():
    content = gethtml('http://www.kwh.org.mo')
    context = getcontext(content, '//div[@id="content"]//table//font//br')[0].tail
    print(context)
    if context != '(暫未有貨提供首次注射人士)':
        global mailcount
        if mailcount < 6:
            mailcount += 1
            sendmail('预约状态已经被改变成：'+context)


def sendmail(context):
    msg_from = 'niro-du@outlook.com'
    password = 'Asdfghjkl123'
    msg_to = 'charlene0607@163.com'

    subject = "晓慧同学请注意：可以速去预约啦"
    msg = MIMEText(context)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP('smtp.live.com')
        s.starttls()
        s.login(user=msg_from, password=password)
        s.sendmail(from_addr=msg_from, to_addrs=msg_to,msg=msg.as_string())
        print('发送成功')
        s.quit()
    except Exception as e:
        print('发送失败_'+str(e))


if __name__ == "__main__":
    count = 0
    schedule.every().day.at("8:05").do(runjob) 
    schedule.every(3).minutes.do(runjob)
    while True:
        if mailcount < 6:
            schedule.run_pending()
            time.sleep(1)
        else:
            schedule.cancel_job(runjob)
            break