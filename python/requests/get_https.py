#!/usr/bin/python3

import requests
import IPython
from xml.etree import cElementTree as ET

url = 'https://api.opensuse.org/about'

print('Solution 1 with decode_content=1')
def https_get():
    r = requests.get(url, stream=True)
    IPython.embed()
    r.raw.decode_content=1
    return r.raw

def xml_parse():
    f = https_get()
    root = ET.parse(f).getroot()
    print(root)

xml_parse()
