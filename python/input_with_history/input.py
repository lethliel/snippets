#!/usr/bin/python

try:
    import readline
except:
    print('Python without readline support')



while True:
    prompt = 'Your input (q)uit:  '
    in_var = raw_input(prompt)
    if in_var == 'q':
        break
    print(in_var)
