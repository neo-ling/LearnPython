#coding=utf-8
import  urllib2
import urllib
url = "https://member.meizu.com/sso?appuri=https%3A%2F%2Fmember.meizu.com%2Findex.jsp&useruri=&service=&sid="
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
values = {'username':"18683130956","password":'050124qly'}
headers = { 'User-Agent': user_agent }
data = urllib.urlencode(values)
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
page = response.read()
print page
