#coding=utf-8
import urllib2
import re
class ZZS:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        self.headers = {'User-Agent': self.user_agent}
        self.stories = [] #存放内容的变量，每一个元素是每一页获得的内容
        self.enable = False
    def getPage(self,pageIndex):
        try:
            url = "http://www.zhangzishi.cc/page/" + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接涨姿势失败,错误原因是",e.reason
                return None
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile('<h2><a target=.*?href=(.*?)>(.*?)</a></h2>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = [] #存储每页获得的网址和标题内容
        for item in items:
            pageStories.append([item[0],item[1]])
        return pageStories
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
    def getOnePage(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页，内容是%s\t,网址链接是%s" % (page,story[1],story[0])
    def start(self):
        print u"正在读取涨姿势,按回车查看，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOnePage(pageStories,nowPage)

zzs = ZZS()
zzs.start()