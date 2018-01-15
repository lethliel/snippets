#!/usr/bin/python3

import sys
from urllib.request import pathname2url, install_opener, urlopen


def convert_list(s):
    try:
        return str(s,encoding='utf-8')
    except:
        return s
    return

def modified_readlines():
    fd.readlines=orig_readl
    xlist = fd.readlines() 
    ret = list(map(lambda x: convert_list(x), xlist))
    return ret    

def called():
    global fd
    fd = urlopen('http://localhost')

    global orig_readl
    orig_readl =  fd.readlines
    fd.readlines = modified_readlines

    return fd

def executer():
    fd = called()
    arr = fd.readlines()
    print(arr)

executer()
