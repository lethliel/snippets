#!/usr/bin/python3

from io import StringIO, BytesIO
from urllib.request import urlopen 


print('Got file locally with StringIO:')
print('-------------------------------\n')
f = StringIO(open('missingfiles').read())
print(f.read())

print('\nGot file from localhost webserver with urlopen:')
print('-----------------------------------------------\n')
f = urlopen('http://localhost/missingfiles')
print(f.read())

print('\nGot file locally with just open():')
print('------------------------------------\n')
f = open('missingfiles', 'rb')
print(f.read())
