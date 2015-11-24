#!coding=utf-8
__author__ = 'QL'
import urllib2
import re
"""
获取豆瓣电影前250名的电影名称
"""
baseurl = "http://movie.douban.com/top250?start=" #基本的url前缀
top_urls = [] #存放url地址
top_content = [] #存放提取出来的电影名称
top_tag = re.compile('<span class="title">(.+?)</span>')
top_num = 1
#确定url地址池
for num in range(10):
    top_urls.append(baseurl + str(num * 25 ))
#print top_urls 测试生成的url正确

#提取电影名称
for url in top_urls:
    content = urllib2.urlopen(url).read()
    pre_content = re.findall(top_tag,content)
    #对匹配出来的电影名称再次进行处理
    for item in  pre_content:
        if item.find('&nbsp') == -1:
            top_content.append(item)
#输出
for item in top_content:
    print 'Top' + str(top_num) + ' ' + item
    top_num += 1


