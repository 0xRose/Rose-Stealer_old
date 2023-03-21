import json
import subprocess
from base64 import b64decode

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
        self.discord_rat = self.data['DISCORD_RAT']
        self.discord_rat_socket_link = self.data['DISCORD_RAT_SOCKET_LINK']
        self.vmdetectwebhook = self.data['VMDETECTHOOK']
        
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
    
    def get_discord_rat(self):
        return self.discord_rat
    
    def get_discord_rat_link(self):
        return self.discord_rat_socket_link

    def get_vmdetectwebhook(self):
        return self.vmdetectwebhook
