"""
THIS IS A TEMP FILE THATS GONNA BE DELETED IN 10 MINUTES    
"""

import time
from colorama import init, Fore
import colorama
import requests
import subprocess
import os
os.system('cls')


init(convert=True)


def program():
    print("Hello Word!")


def connect():
    URL = "Your Pastebin RAW URL here"
    hwid = subprocess.check_output(
        'wmic csproduct get uuid').decode().split('\n')[1].strip()

    rq = requests.get(url)

    if rq.status_code == 404:
        print(f'{Fore.LIGHTRED_EX}The URL provided is invalid')
        return
    if hwid in rq.text:
        program()
    else:
        print(f'{Fore.LIGHTRED_EX}Your HWID isn\'t in the database')
        print(f'{Fore.LIGHTRED_EX}Your HWID: {Fore.LIGHTYELLOW_EX}{hwid}')


connect()
input(Fore.BLACK)
