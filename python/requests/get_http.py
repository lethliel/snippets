#!/usr/bin/python3

import requests
import IPython

url = 'http://api.opensuse.org/about'

r = requests.get(url, stream=True)
#IPython.embed()
raw_obj = r.raw
print(raw_obj.read())
