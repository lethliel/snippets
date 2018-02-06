#!/usr/bin/python3
 
byt_test = 'test1'.encode('utf-8')
list = [byt_test, 'test2', 123]

for entry in list:
    print(type(entry))
