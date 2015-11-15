#coding=utf-8
import paramiko
"""
这是实验paramiko的SFTPClient类
"""
username = "ql"
password = "redhat"
hostname = "192.168.1.15"
port = 22
try:
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put("F:\learnpython\hosts","/home/ql/test.txt")
    print sftp.stat("/home/ql/test.txt")
    print sftp.listdir("/home/ql")
    t.close()
except Exception,e:
    print str(e)