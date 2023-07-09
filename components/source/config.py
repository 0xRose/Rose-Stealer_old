import base64
class Config:
    def __init__(self):
        self.webhook = 'WEBHOOK_URL'
        self.vm_detect_webhook = 'VMHOOK'

        self.debug_mode = True

        self.rose_discord_rat = False
        self.rose_discord_rat_socket_link = 'ROSE_DISCORD_RAT_SOCKET_LINK'
        self.knight_discord_rat = False
        self.knight_discord_rat_bot_token = 'KNIGHT_DISCORD_RAT_BOT_TOKEN'
        self.knight_discord_rat_channel_id = 'KNIGHT_DISCORD_RAT_CHANNEL_ID'
        self.knight_discord_rat_listener_user_id = 'KNIGHT_DISCORD_RAT_LISTENER_USER_ID'
        self.knight_discord_rat_prefix = 'KNIGHT_DISCORD_RAT_PREFIX'

        self.discord_ping = False
        self.injection = False
        self.token_stealing = False
        self.cookie_stealing = False
        self.password_stealing = False
        self.malicious_stealing = False
        self.location_stealing = False
        self.roblox_stealing = False
        self.screenshot = False
        self.start_up = False
        self.fake_error = False
        self.nitro_auto_buy = False
        self.defenderfucker = False
        self.vmdetection = False
        
        self.secr_eb_color = 'MTY3MTE2ODA='
        self.secr_eb_footer = 'Um9zZS1JbmplY3RvciB8IE1hZGUgYnkgR3VtYm9icm90LCBJQ0V4RlMsIHN1ZWdkdSBhbmQgeHBpZXJyb3ogfCBodHRwczovL2dpdGh1Yi5jb20vRGFtYWdpbmdSb3NlL1Jvc2UtSW5qZWN0b3I='
        self.secr_wh_avatar = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RhbWFnaW5nUm9zZS9Sb3NlLUluamVjdG9yL21haW4vY29tcG9uZW50cy9yZWFkbWUvUm9zZS5qcGVn=='
        self.secr_wh_name = 'Um9zZS1JbmplY3Rvcg=='
        self.eb_color = int(base64.b64decode(self.secr_eb_color.encode('ascii')).decode('ascii'))
        self.eb_footer = base64.b64decode(self.secr_eb_footer.encode('ascii')).decode('ascii')
        self.wh_avatar = base64.b64decode(self.secr_wh_avatar.encode('ascii')).decode('ascii')
        self.wh_name = base64.b64decode(self.secr_wh_name.encode('ascii')).decode('ascii')

    def get_roblox_stealing(self):
        return self.roblox_stealing

    def get_injection(self):
        return self.injection   

    def get_token_stealing(self):
        return self.token_stealing 

    def get_cookie_stealing(self):
        return self.cookie_stealing

    def get_password_stealing(self):
        return self.password_stealing

    def get_malicious_stealing(self):
        return self.malicious_stealing

    def get_location_stealing(self):
        return self.location_stealing

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

    def get_rose_discord_rat(self):
        return self.rose_discord_rat

    def get_rose_discord_rat_link(self):
        return self.rose_discord_rat_socket_link
    
    def get_knight_discord_rat(self):
        return self.knight_discord_rat
    
    def get_knight_discord_rat_bot_token(self):
        return self.knight_discord_rat_bot_token
    
    def get_knight_discord_rat_channel_id(self):
        return self.knight_discord_rat_channel_id
    
    def get_knight_discord_rat_listener_user_id(self):
        return self.knight_discord_rat_listener_user_id
    
    def get_knight_discord_rat_prefix(self):
        return self.knight_discord_rat_prefix
    
    def get_discord_ping(self):
        return self.discord_ping

    def get_screenshot(self):
        return self.screenshot

    def get_vm_detect_webhook(self):
        return self.vm_detect_webhook
    
    def get_start_up(self):
        return self.start_up
    
    def get_fake_error(self):
        return self.fake_error
    
    def get_nitro_auto_buy(self):
        return self.nitro_auto_buy
    
    def get_defenderfucker(self):
        return self.defenderfucker

    def get_vmdetection(self):
        return self.vmdetection
    
