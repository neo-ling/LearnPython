#coding=utf-8
import urllib2
import urllib
import re
class QSBK: #定义一个糗事百科类
    def __init__(self): #初始化方法，定义一些变量
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []
        self.enable = False #存放程序是否继续运行的变量
    def getPage(self,pageIndex): #传人某一页的索引获得页面代码
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url,headers = self.headers) #构建请求
            response = urllib2.urlopen(request) #获取页面代码
            pageCode = response.read().decode('utf-8') #转化成UTF-8编码
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败，错误原因",e.reason
                return None
    def getPageItems(self,pageIndex): #传入莫一页代码，返回段子列表
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile(r'<div.*?class="author.*?>.*?<a.*?href.*?title="(.*?)">.*?</a>.*?<div.*?class="content">(.*?)<!--.*?</div>.*?<div.*?class="stats.*?<i.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern,pageCode)
        pageStories = [] #存储每页的段子
        for item in items:
            pageStories.append([item[0],item[1],item[2].strip()])
        return pageStories
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1

    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        #遍历一页的段子
        for story in pageStories:
            #等待用户输入
            input = raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page,story[0],story[2],story[1])

    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)


spider = QSBK()
spider.start()


