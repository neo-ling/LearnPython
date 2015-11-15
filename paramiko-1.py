#coding=utf-8
"""
这是实验paramiko的SSHClient类
"""
import paramiko
import sys,os
#host = sys.argv[1]
#host = "192.168.1.15"
user = "ql"
password = "redhat"
#cmd = sys.argv[2]
cmd = "free -m "
file = open("./hosts")
for lines in file.readlines():
    host = lines.strip() #剔除windows的换行符
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,22,user,password)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    print "this is %s:" % host
    print stdout.read()
    ssh.close()
file.close()
