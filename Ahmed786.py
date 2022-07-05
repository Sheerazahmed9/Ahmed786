#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Ahmed786.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed786/blob/main/Ahmed.cpython-310.so?raw=true -o Ahmed.so')
        from Ahmed import reg
        reg()
    else:
        from Ahmed import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('Ahmed786.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed786/blob/main/brand.cpython-310.so?raw=true -o brand.so')
        from brand import reg
        reg()
    else:
        from brand import reg
        reg()
