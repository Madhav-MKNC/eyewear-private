#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system as run

# installing dependencies
try:
    print('[+] installing required modules...')
    run('pip install -r requirements.txt')
except Exception as err:
    print("[error]", str(err))






