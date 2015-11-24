#coding=utf-8
import requests

url ="http://www.heibanke.com/lesson/crawler_ex01/"
number = 0
while number <= 30:
    params = {'username':'neo','password':str(number)}
    r = requests.post(url,data=params)
    if r.text.find(u"输入的密码错误") > 0:
        print u"输入的密码",number,u"错误"
        number = number + 1
    else:
        print r.text
        break




