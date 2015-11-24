#coding=utf-8
import urllib
import re


url = "http://www.heibanke.com/lesson/crawler_ex00/"
url1 = "http://www.heibanke.com/lesson/crawler_ex00/"
while True:
    html = urllib.urlopen(url1)
    content = html.read()
    html.close()
    num = re.compile(r'<h3>[^\d<]*?(\d+)[^\d<]*?</h3')
    nums = re.findall(num,content)
    for nu in nums:
        url1=url+nu
        print nu
        print url1




