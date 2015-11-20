#coding=utf-8
import urllib2
import urllib
import re
class  BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None
    def  getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #调试标题内容是否被匹配到
            return result.group(1).strip()
        else:
            return  None
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)