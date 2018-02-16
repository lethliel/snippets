#!/usr/bin/env python

import sys
import struct

try:
    filen = sys.argv[1]
except IndexError as i:
    if len(sys.argv) <= 1:
        print('Please provide file to work on')
        sys.exit(1)

f = open(filen, 'rb')
magic = f.read(7)
print(magic)
print(magic[:4])
if magic[:4] == b'\xed\xab\xee\xdb':
    print('It is a rpm. Let us continue')

f.seek(8)
data = f.read()
val = ''
for c in data:
    c = bytes([c])
    c, = struct.unpack('!c', c)
    if c == '\0':
        break
    else:
        val += c.decode('utf-8')
        print(val)

print(val)
       
 
