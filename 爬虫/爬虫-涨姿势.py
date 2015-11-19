#coding=utf-8
import urllib2
import re
import urllib


url ="http://www.zhangzishi.cc/20151004mt.html"
#定义Header，模拟浏览器向服务器发起请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Host": "cdn.zhangzishi.cc",
    'Referer': 'http://www.zhangzishi.cc/20151004mt.html',
    "GET": url
    }
request = urllib2.Request(url,None,headers)
#获取网页html信息
response = urllib2.urlopen(request)
#正则匹配图片特征，并获取图片链接
img_tag = re.compile(r'src="(.+?\.jpg)"')
img_links = re.findall(img_tag,response.read())

#下载图片
img_counter = 0
for img_link in img_links:
    img_name = '%s.jpg' % img_counter
    urllib.urlretrieve(img_link,"E:\LearnPython\pictures\%s" % img_name)
    img_counter += 1