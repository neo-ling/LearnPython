#coding=utf-8
import urllib
import re

#获取网页html信息
url = "http://tieba.baidu.com/p/4162342552"
html = urllib.urlopen(url)
content = html.read()
html.close()

#正则匹配图片特征，并获取图片链接
img_tag = re.compile(r'class="BDE_Image" src="(.+?\.jpg)"')
img_links = re.findall(img_tag,content)

#下载图片
img_counter = 0
for img_link in img_links:
    img_name = '%s.jpg' % img_counter
    urllib.urlretrieve(img_link,"E:\LearnPython\pictures\%s" % img_name)
    img_counter += 1

