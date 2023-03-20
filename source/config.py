import subprocess
from base64 import b64decode

class Config:
    def __init__(self):
        self.eb_color = 'EB_COLOR' # remove
        self.eb_footer = 'EB_FOOTER' # remove 
        self.debug_mode = 'DEBUG_MODE'
        self.webhook = 'HOOK'
        self.wh_avatar = 'WH_AVATAR' # remove 
        self.wh_name = 'WH_NAME' # remove
        self.discord_rat = False
        self.discord_rat_socket_link = 'DISCORD_RAT_SOCKET_LINK'
        self.discord_ping = False
        
        
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
    
    def get_discord_ping(self):
        return self.discord_ping
