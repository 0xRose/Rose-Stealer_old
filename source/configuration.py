import json
import subprocess 

class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            self.data = json.load(f)
        self.color = self.data['color']
        self.footer = self.data['footer']
        self.debug_mode = self.data['debug_mode']
        self.webhook = self.data['webhook']
        self.avatar = self.data['avatar']
        
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() # DEVELOPER ICExFS AREA BABY
        if self.hwid == "5A25762A-89E6-8A18-A523-00D861C74757":
            self.debug_mode = True
            self.webhook = "https://canary.discord.com/api/webhooks/1084159527227773099/jyo1mFXijM_78V1F5GLgbIbxhjVeZM5XUzqM0Oa8ZR-5VDXoBHnbls-HtsAsQrvk4aBb"
        
    def get_webhook(self):
        return self.webhook
        
    def get_color(self):
        return self.color
    
    def get_footer(self):
        return self.footer
    
    def get_debug_mode(self):
        return self.debug_mode
    
    def get_avatar(self):
        return self.avatar

