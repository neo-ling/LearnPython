#coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import lxml
class Spider:
    def __init__(self):
        self.siteURL = "https://mm.taobao.com/json/request_top_list.htm"
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        #print  url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return  response.read().decode('gbk')
    def getContent(self,pageIndex):
        page  = self.getPage(pageIndex)
        soup = BeautifulSoup(page,'lxml')
        for a  in soup.find_all('a'):
            print a




spider = Spider()
spider.getPage(1)
spider.getContent(1)
