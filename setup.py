#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system as run

run('pipreqs . --force')
run('pip install -r requirements.txt')







# start the web app
from app import app

try:
    host = input("[+] Enter the Host Address: ")
    port = input("[+] Enter the port for the program: ")
    debug = False if input("[+] Debug [y/n]: ").lower() in ['no', 'n'] else True
    app.start(host=host, port=port, debug=debug)

except Exception as err:
    host = "localhost"
    port = 80
    print("[error]", str(err))
    print("[*] Using defaults")
    print(f"[=] host: {host}")
    print(f"[=] port: {port}")
    app.start(host=host, port=port, debug=debug)
