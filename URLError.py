#coding=utf-8
import urllib2
request = urllib2.Request('http://www.xxxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.reason

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
    print e.reason

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason
else:
    print "OK"