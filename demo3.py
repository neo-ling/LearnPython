#coding=utf-8
import urllib2
import urllib
"""
以post方式传递参数
"""
values = {"username":"18683130956@163.com","password":"0501212hq?"}
data = urllib.urlencode(values)
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.code

"""
以get方式传递参数
"""
values = {}
values['username'] = "18683130956@163.com"
values['password'] = "0501212hq?"
data = urllib.urlencode(values)
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.code
