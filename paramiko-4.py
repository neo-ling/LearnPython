#coding=utf-8
"""
实现堡垒机的远程命令执行
"""
import paramiko
import sys,os,time

blip = "192.168.1.8" #定义堡垒机相关信息
bluser = "root"
blpassword = "redhat"

hostname = "192.168.1.15" #业务服务器相关信息
username = "ql"
password = "redhat"

port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log') #记录日志

ssh = paramiko.SSHClient() #ssh登陆堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpassword)

channel = ssh.invoke_shell() #创建会话，开启命令调用
channel.settimeout(10) #会话命令超时时间，单位是秒

buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n') #执行ssh登陆业务服务器
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception,e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''
channel.send(password+'\n')
buff = ''
while not buff.endswith('$ '):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
#command = raw_input('please input a command: ')
channel.send('ifconfig\n')
buff = ''
try:
    while buff.find('$ ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception,e:
    print 'error info: ' + str(e)
print buff
channel.close()
ssh.close()
