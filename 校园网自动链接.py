#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import requests
import sys

#####这里是提交的信息#######
#登录地址
post_addr="http://192.168.254.10"

#构造头部信息
post_header={
  'Host':"192.168.254.10",
  'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
  'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  'Accept-Language':"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  'Accept-Encoding':"gzip, deflate",   
  'Referer':"http://192.168.254.10/a70.htm",
  'Content-Type':"application/x-www-form-urlencoded",
  'X-Requested-With':"XMLHttpRequest",
  'Content-Length':"3538",   
  'Connection':"keep-alive"   
}
#提交的信息内容
post_data = {
  #将用户名改成你的账户，默认是学号；
  'DDDDD':'用户名@telecom',
  #将账户密码改成你的密码，默认是身份证号后6位
  'upass':'密码',
  'R1':'0',
  'R2':'',
  'R3':'0',
  'R6':'0',
  'para':'00',
  '0MKKey':'123456',
  'buttonClicked':'',
  'redirect_url':'',
  'err_flag':'',
  'username':'',
  'password':'',
  'user':'',
  'cmd':'',
  'Login':'',
  'v6ip':'',
	}
#执行的代码
#response = requests.post(post_addr, data=post_data, headers=post_header)
########以上为网络认证执行的代码
PING_RESULT = 0
NETWORK_RESULT = 0
 
def DisableNetwork():
    result = os.system(u"netsh interface set interface 以太网 disable")
    if result == 1:
        print("正在认证中，请稍等5分钟！")
    else:
        print("认证成功！")
 
def ping():
    
    
    result = os.system(u"ping www.baidu.com -n 3")
    if result == 0:
        print("网络正常")
    else:
        print("网络故障")
    return result
 
 
if __name__ == '__main__':
    while True:
        PING_RESULT = ping()
 
        if PING_RESULT == 0:
            time.sleep(500) #验证网络正常后的休眠时间，单位为秒
        else:
            print('开始重新认证')
            response = requests.post(post_addr, data=post_data, headers=post_header)
            DisableNetwork()
            time.sleep(180) #验证网络失败后的休眠时间，单位为秒
