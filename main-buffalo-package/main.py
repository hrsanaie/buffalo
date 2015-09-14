#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Buffalo infosec corp'
import requests;
print(0b1001);
try:
    class splash:
        def splashBeginning():
                print('\x42\x75\x66\x66\x61\x6c\x6f'+ ' ' +'\x69\x6e\x66\x6f\x73\x65\x63' +' ' +'\x63\x6f\x72\x70');
    splash.splashBeginning();
    req = requests.get('http://bernopa.com/');
    print ('Response Code: ' + str(req.status_code));
    print ('\nResponse:\n' + req.text);
    print("\n\n");
    print(req.cookies);

except exception as e:
 print (e)