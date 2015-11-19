#coding=utf-8
import urllib2
import re
url = "http://blog.csdn.net/FansUnion"
#自定义Header，模拟浏览器向服务器发起请求
req = urllib2.Request(url)
req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36")
req.add_header('Host','static.csdn.net')
req.add_header('Referer', 'http://blog.csdn.net')
req.add_header('GET', url)

#下载网页html并打印
html = urllib2.urlopen(req)
content = html.read()
print content
html.close()

