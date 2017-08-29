#/usr/bin/env python

import safewriter
import sys

try:
    import readline
except:
    print('Python without readline support')


sys.stdout = safewriter.SafeWriter(sys.stdout)

while True:
    prompt = 'Your input (q)uit:  '
    in_var = raw_input(prompt)
    if in_var == 'q':
        break
    print(in_var)
